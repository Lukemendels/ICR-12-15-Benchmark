(function(root,factory){
  'use strict';
  const api=factory();
  if(typeof module==='object'&&module&&module.exports) module.exports=api;
  if(root) root.PaperclipAnvilAuthoring=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';

  const enc=new TextEncoder();
  const dec=new TextDecoder('utf-8',{fatal:true});
  const ID=/^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  const VERSION=/^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/;
  const HEX=/^[0-9a-f]{64}$/;
  const MAX_OPS=12;
  const MAX_CREATE_FILES=64;
  const MAX_PROPOSAL_BYTES=512*1024;
  const REQUIRED_CREATE_ROOTS=['paperclip.tool.json','ARCHITECTURE.md','SKILL.md'];

  function fail(message){throw new Error(message)}
  function plain(v){return !!v&&typeof v==='object'&&!Array.isArray(v)}
  function stable(v){
    if(Array.isArray(v)) return '['+v.map(stable).join(',')+']';
    if(plain(v)) return '{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+stable(v[k])).join(',')+'}';
    return JSON.stringify(v);
  }
  async function sha(value){
    const bytes=typeof value==='string'?enc.encode(value):value;
    const digest=await crypto.subtle.digest('SHA-256',bytes);
    return [...new Uint8Array(digest)].map(x=>x.toString(16).padStart(2,'0')).join('');
  }
  function safePath(value){
    return typeof value==='string'&&value.length>0&&value.length<=240&&!value.startsWith('/')&&!/^[A-Za-z]:/.test(value)&&!value.includes('\\')&&!value.split('/').includes('..')&&value.split('/').every(part=>/^[A-Za-z0-9._-]+$/.test(part));
  }
  function editablePath(path){
    return safePath(path)&&!path.startsWith('dist/')&&!path.startsWith('.git/')&&!path.startsWith('.paperclip-recovery/')&&(
      path==='paperclip.tool.json'||path==='ARCHITECTURE.md'||path==='SKILL.md'||/^(src|skills|prompts|assets|tests)\/[A-Za-z0-9._/-]+$/.test(path)
    );
  }
  function cloneEntries(entries){
    return [...entries].sort((a,b)=>a.path.localeCompare(b.path)).map(e=>({path:e.path,bytes:new Uint8Array(e.bytes)}));
  }
  function entryMap(entries){return new Map(entries.map(e=>[e.path,e]))}
  function text(entries,path){
    const entry=entryMap(entries).get(path);
    if(!entry) fail('Missing project file: '+path);
    try{return dec.decode(entry.bytes)}catch{fail('Expected UTF-8 text file: '+path)}
  }
  async function digestEntries(entries){
    const sorted=[...entries].sort((a,b)=>a.path.localeCompare(b.path));
    let total=0;
    const parts=[];
    for(const e of sorted){
      const head=enc.encode(e.path+'\0'+e.bytes.length+'\0');
      const zero=Uint8Array.of(0);
      parts.push(head,e.bytes,zero);
      total+=head.length+e.bytes.length+1;
    }
    const all=new Uint8Array(total);
    let offset=0;
    for(const p of parts){all.set(p,offset);offset+=p.length}
    return sha(all);
  }
  function unwrapPacket(source,tag){
    let value=String(source||'').trim();
    const fence=value.match(/^```(?:text|json)?\s*([\s\S]*?)\s*```$/i);
    if(fence) value=fence[1].trim();
    const re=new RegExp('<'+tag+'>\\s*([\\s\\S]*?)\\s*</'+tag+'>','i');
    const match=value.match(re);
    if(!match) fail('Expected '+tag+' packet.');
    return match[1].trim();
  }
  function validateBrief(brief){
    if(!plain(brief)||typeof brief.summary!=='string'||typeof brief.approach!=='string'||!Array.isArray(brief.requirementsCovered)||!Array.isArray(brief.significantDecisions)||!Array.isArray(brief.operatorAttention)) fail('Invalid build brief.');
    return brief;
  }
  function parseJsonPacket(source,tag){
    if(enc.encode(String(source||'')).length>MAX_PROPOSAL_BYTES) fail('Proposal exceeds bounded size.');
    try{return JSON.parse(unwrapPacket(source,tag))}
    catch(e){fail('Malformed '+tag+' JSON: '+e.message)}
  }
  function parseProposal(source){
    const proposal=parseJsonPacket(source,'PATCHBAY_CHANGE_PROPOSAL');
    const required=['schemaVersion','type','baseDigest','contextDigest','proposalId','buildBrief','operations'];
    if(!plain(proposal)||!required.every(k=>Object.hasOwn(proposal,k))) fail('Proposal is missing required fields.');
    if(proposal.schemaVersion!=='0.1'||proposal.type!=='change_proposal'||!HEX.test(proposal.baseDigest||'')||!HEX.test(proposal.contextDigest||'')||typeof proposal.proposalId!=='string'||!proposal.proposalId.trim()) fail('Invalid proposal identity.');
    validateBrief(proposal.buildBrief);
    if(!Array.isArray(proposal.operations)||proposal.operations.length<1||proposal.operations.length>MAX_OPS) fail('Proposal must contain 1–'+MAX_OPS+' operations.');
    const paths=new Set();
    for(const op of proposal.operations){
      if(!plain(op)||!['create','replace'].includes(op.op)||!editablePath(op.path)||typeof op.content!=='string') fail('Invalid proposal operation.');
      if(paths.has(op.path)) fail('Duplicate proposal path: '+op.path);
      paths.add(op.path);
    }
    return proposal;
  }
  function parseCreateProject(source){
    const proposal=parseJsonPacket(source,'PATCHBAY_CREATE_PROJECT');
    const required=['schemaVersion','type','contextDigest','proposalId','buildBrief','files'];
    if(!plain(proposal)||!required.every(k=>Object.hasOwn(proposal,k))) fail('Create-project proposal is missing required fields.');
    if(proposal.schemaVersion!=='0.1'||proposal.type!=='create_project'||!HEX.test(proposal.contextDigest||'')||typeof proposal.proposalId!=='string'||!proposal.proposalId.trim()) fail('Invalid create-project identity.');
    validateBrief(proposal.buildBrief);
    if(!Array.isArray(proposal.files)||proposal.files.length<REQUIRED_CREATE_ROOTS.length||proposal.files.length>MAX_CREATE_FILES) fail('Create-project proposal must contain '+REQUIRED_CREATE_ROOTS.length+'–'+MAX_CREATE_FILES+' files.');
    const paths=new Set();
    for(const file of proposal.files){
      if(!plain(file)||!editablePath(file.path)||typeof file.content!=='string') fail('Invalid create-project file.');
      if(paths.has(file.path)) fail('Duplicate create-project path: '+file.path);
      paths.add(file.path);
    }
    for(const path of REQUIRED_CREATE_ROOTS) if(!paths.has(path)) fail('Create-project proposal is missing required file: '+path);
    return proposal;
  }
  function lineDiff(path,before,after){
    if(before===after) return '';
    const a=String(before??'').split('\n');
    const b=String(after??'').split('\n');
    const out=['--- '+path+' (current)','+++ '+path+' (candidate)'];
    const max=Math.max(a.length,b.length);
    for(let i=0;i<max;i++){
      if(a[i]===b[i]) continue;
      if(i<a.length) out.push('- '+a[i]);
      if(i<b.length) out.push('+ '+b[i]);
    }
    return out.join('\n');
  }
  async function constructCandidate(proposal,baseEntries,{baseDigest,contextDigest}){
    if(proposal.baseDigest!==baseDigest) fail('Proposal base digest does not match the disclosed project.');
    if(proposal.contextDigest!==contextDigest) fail('Proposal context digest does not match the disclosed packet.');
    const map=entryMap(cloneEntries(baseEntries));
    const changes=[];
    for(const op of proposal.operations){
      const prior=map.get(op.path);
      const exists=!!prior;
      if(op.op==='create'&&exists) fail('Create target already exists: '+op.path);
      if(op.op==='replace'&&!exists) fail('Replace target does not exist: '+op.path);
      const before=exists?dec.decode(prior.bytes):null;
      const bytes=enc.encode(op.content);
      map.set(op.path,{path:op.path,bytes});
      changes.push({op:op.op,path:op.path,before,after:op.content,diff:lineDiff(op.path,before,op.content)});
    }
    const entries=[...map.values()].sort((a,b)=>a.path.localeCompare(b.path));
    const candidateDigest=await digestEntries(entries);
    return Object.freeze({
      mode:'edit',
      proposalId:proposal.proposalId,
      buildBrief:proposal.buildBrief,
      baseDigest,
      contextDigest,
      candidateDigest,
      entries:Object.freeze(entries),
      changes:Object.freeze(changes),
      diff:changes.map(x=>x.diff).filter(Boolean).join('\n\n')
    });
  }
  function projectManifest(entries){
    let m;
    try{m=JSON.parse(text(entries,'paperclip.tool.json'))}
    catch(e){fail('Malformed paperclip.tool.json: '+e.message)}
    if(!plain(m)||m.schemaVersion!=='1.0.0'||!ID.test(m.id||'')||!VERSION.test(m.version||'')||typeof m.title!=='string'||!m.title.trim()||!plain(m.source)||!safePath(m.source.html)||!safePath(m.source.css)||!safePath(m.source.javascript)||!safePath(m.output)||!plain(m.skill)||!['authored','generated'].includes(m.skill.mode)||!ID.test(m.skill.slug||'')||!Array.isArray(m.prompts)||!Array.isArray(m.dependencies)||m.stickshiftInstallable!==true) fail('Invalid Paperclip project manifest.');
    if(m.skill.mode==='authored'&&!safePath(m.skill.path)) fail('Invalid authored runtime skill path.');
    if(m.output.split('/').at(-1)!==m.id+'.html') fail('Output filename must equal the stable tool ID plus .html.');
    const seen=new Set();
    for(const pin of m.dependencies){
      if(!plain(pin)||!ID.test(pin.id||'')||!VERSION.test(pin.version||'')||!safePath(pin.path)) fail('Invalid governed capability pin.');
      if(seen.has(pin.id)) fail('Duplicate governed capability pin: '+pin.id);
      seen.add(pin.id);
    }
    return m;
  }
  function validateProjectClosure(entries){
    const manifest=projectManifest(entries);
    const required=[...REQUIRED_CREATE_ROOTS,manifest.source.html,manifest.source.css,manifest.source.javascript,...manifest.prompts];
    if(manifest.skill.mode==='authored') required.push(manifest.skill.path);
    for(const path of new Set(required)){
      if(!editablePath(path)) fail('Manifest references a source path outside Anvil editable roots: '+path);
      text(entries,path);
    }
    return manifest;
  }
  async function constructCreatedProject(proposal,{contextDigest}){
    if(proposal.contextDigest!==contextDigest) fail('Create-project context digest does not match the disclosed packet.');
    const entries=proposal.files.map(file=>({path:file.path,bytes:enc.encode(file.content)})).sort((a,b)=>a.path.localeCompare(b.path));
    validateProjectClosure(entries);
    const candidateDigest=await digestEntries(entries);
    const baseDigest=await digestEntries([]);
    const changes=proposal.files.slice().sort((a,b)=>a.path.localeCompare(b.path)).map(file=>({
      op:'create',
      path:file.path,
      before:null,
      after:file.content,
      diff:lineDiff(file.path,null,file.content)
    }));
    return Object.freeze({
      mode:'create',
      proposalId:proposal.proposalId,
      buildBrief:proposal.buildBrief,
      baseDigest,
      contextDigest,
      candidateDigest,
      entries:Object.freeze(entries),
      changes:Object.freeze(changes),
      diff:changes.map(x=>x.diff).filter(Boolean).join('\n\n')
    });
  }
  function normalizeTask(task){
    const value=String(task||'').trim();
    if(value.length>2000) fail('Task must be no more than 2000 characters.');
    return value;
  }
  function authoringSkillRef(){
    return {id:'paperclip-anvil',path:'skills/paperclip-anvil.md'};
  }
  function capabilityEnvelope(capabilities){
    return {
      catalog:Array.isArray(capabilities)?capabilities:[],
      implementationSourceIncluded:false,
      rule:'Only pin capabilities present in this catalog. Use their model-facing skill; never reproduce governed implementation source.'
    };
  }
  async function makeContext({projectEntries,baseDigest,libraryDigest,task,capabilities}){
    const normalizedTask=normalizeTask(task);
    const manifest=projectManifest(projectEntries);
    const paths=['paperclip.tool.json','ARCHITECTURE.md','SKILL.md',manifest.source.html,manifest.source.css,manifest.source.javascript,...manifest.prompts];
    if(manifest.skill.mode==='authored'&&manifest.skill.path) paths.push(manifest.skill.path);
    const packet={
      schemaVersion:'0.1',
      type:'patchbay_context',
      mode:'edit',
      authoringSkill:authoringSkillRef(),
      project:{id:manifest.id,title:manifest.title,version:manifest.version,baseDigest,dependencies:manifest.dependencies},
      library:{digest:libraryDigest,mode:'separately_authorized_read_only'},
      conversationIntent:normalizedTask||'Use the current programming request in the StickShift conversation; Anvil does not own the programming prompt.',
      projectInventory:[...projectEntries].sort((a,b)=>a.path.localeCompare(b.path)).map(entry=>({path:entry.path,bytes:entry.bytes.length,editable:editablePath(entry.path)})),
      projectFiles:[...new Set(paths)].sort().map(path=>({path,content:text(projectEntries,path)})),
      capabilities:capabilityEnvelope(capabilities),
      modelGuidance:{
        role:'StickShift + the frontier model are the programmer. Anvil is the deterministic build/candidate/promotion workbench. Apply the current StickShift programming request to this disclosed project context.',
        sourceRule:'Return complete contents for every file you create or replace. Make the smallest correct modular change; do not collapse the project into one HTML file.',
        capabilityRule:'Use only governed capabilities listed in the catalog. Never paste bundled library source and never add CDN or network dependencies.',
        decisionRule:'Make routine implementation decisions yourself. Put consequential choices in buildBrief.significantDecisions or buildBrief.operatorAttention.',
        authorityRule:'Do not claim compilation, filesystem writes, integrity verification, recovery, or release assembly. Anvil performs those deterministically after the operator acts.',
        transport:'Return exactly one PATCHBAY_CHANGE_PROPOSAL inside a fenced text code block with no prose outside the fence.'
      },
      responseContract:{
        tag:'PATCHBAY_CHANGE_PROPOSAL',
        type:'change_proposal',
        operations:['create','replace'],
        editableRoots:['paperclip.tool.json','ARCHITECTURE.md','SKILL.md','src/','skills/','prompts/','assets/','tests/'],
        buildBrief:['summary','approach','requirementsCovered','significantDecisions','operatorAttention']
      }
    };
    const contextDigest=await sha(stable(packet));
    return Object.freeze({...packet,contextDigest});
  }
  async function makeCreateContext({libraryDigest,task,capabilities}){
    const normalizedTask=normalizeTask(task);
    const packet={
      schemaVersion:'0.1',
      type:'patchbay_create_context',
      mode:'create',
      authoringSkill:authoringSkillRef(),
      library:{digest:libraryDigest,mode:'separately_authorized_read_only'},
      conversationIntent:normalizedTask||'Use the current programming request in the StickShift conversation; Anvil does not own the programming prompt.',
      capabilities:capabilityEnvelope(capabilities),
      projectContract:{
        authority:'The proposed modular project is an in-memory candidate until the operator explicitly chooses a destination and clicks Create Project.',
        requiredFiles:[...REQUIRED_CREATE_ROOTS,'src/index.html','src/style.css','src/app.js'],
        optionalRoots:['skills/','prompts/','assets/','tests/'],
        forbiddenRoots:['dist/','.git/','.paperclip-recovery/'],
        manifest:{
          schemaVersion:'1.0.0',
          id:'lowercase-kebab-id',
          title:'Human-readable title',
          version:'1.0.0',
          source:{html:'src/index.html',css:'src/style.css',javascript:'src/app.js'},
          output:'dist/{id}.html',
          skill:{mode:'generated',slug:'{id}'},
          prompts:[],
          dependencies:[{id:'catalog-id',version:'catalog-version',path:'catalog-descriptorPath'}],
          stickshiftInstallable:true
        }
      },
      modelGuidance:{
        role:'StickShift + the frontier model are the programmer. Produce a complete modular Paperclip project for the current StickShift programming request.',
        completenessRule:'Return every text file required for a production-compilable project, including paperclip.tool.json, ARCHITECTURE.md, SKILL.md, and modular src files.',
        architectureRule:'Keep HTML structure, CSS, and JavaScript in their declared modular source files. Add prompts, authored runtime skills, tests, or assets only when the tool needs them.',
        capabilityRule:'Use only governed capabilities listed in the catalog and pin exact id/version/path values in paperclip.tool.json. Never paste bundled library source and never use a CDN.',
        decisionRule:'Make routine implementation decisions yourself. Surface consequential product/architecture choices in buildBrief.significantDecisions or buildBrief.operatorAttention.',
        authorityRule:'Do not claim compilation, filesystem writes, integrity verification, recovery, or release assembly. Anvil performs those deterministically after human approval.',
        transport:'Return exactly one PATCHBAY_CREATE_PROJECT inside a fenced text code block with no prose outside the fence.'
      },
      responseContract:{
        tag:'PATCHBAY_CREATE_PROJECT',
        type:'create_project',
        fileShape:{path:'relative/path',content:'complete UTF-8 file contents'},
        maxFiles:MAX_CREATE_FILES,
        editableRoots:['paperclip.tool.json','ARCHITECTURE.md','SKILL.md','src/','skills/','prompts/','assets/','tests/'],
        buildBrief:['summary','approach','requirementsCovered','significantDecisions','operatorAttention']
      }
    };
    const contextDigest=await sha(stable(packet));
    return Object.freeze({...packet,contextDigest});
  }
  function fenced(tag,payload){
    return '```text\n<'+tag+'>\n'+JSON.stringify(payload,null,2)+'\n</'+tag+'>\n```';
  }
  function recoveryRecord(baseEntries,candidate){
    const base=entryMap(baseEntries);
    const files=candidate.changes.map(change=>{
      const prior=base.get(change.path);
      return {path:change.path,existed:!!prior,content:prior?dec.decode(prior.bytes):null};
    });
    return {
      schemaVersion:'0.1',
      type:'paperclip_authoring_recovery',
      mode:candidate.mode||'edit',
      baseDigest:candidate.baseDigest,
      candidateDigest:candidate.candidateDigest,
      createdAt:new Date().toISOString(),
      files
    };
  }

  return Object.freeze({
    MAX_OPS,
    MAX_CREATE_FILES,
    REQUIRED_CREATE_ROOTS,
    stable,
    sha,
    safePath,
    editablePath,
    cloneEntries,
    entryMap,
    text,
    digestEntries,
    parseProposal,
    parseCreateProject,
    constructCandidate,
    constructCreatedProject,
    projectManifest,
    validateProjectClosure,
    makeContext,
    makeCreateContext,
    fenced,
    recoveryRecord
  });
});

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const ID=/^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const SEMVER=/^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$/;
const HEX=/^[0-9a-f]{64}$/;
const CAPABILITY_PATH=/^capabilities\/([a-z0-9]+(?:-[a-z0-9]+)*)\/((?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*))\/capability\.json$/;

function fail(message){throw new Error(message)}
function plain(v){return !!v&&typeof v==='object'&&!Array.isArray(v)}
function exact(v,required){
  if(!plain(v)||!required.every(k=>Object.hasOwn(v,k))||Object.keys(v).some(k=>!required.includes(k))) return false;
  return true;
}
export function stable(value){
  if(Array.isArray(value)) return '['+value.map(stable).join(',')+']';
  if(plain(value)) return '{'+Object.keys(value).sort().map(k=>JSON.stringify(k)+':'+stable(value[k])).join(',')+'}';
  return JSON.stringify(value);
}
export function sha256(value){
  const bytes=Buffer.isBuffer(value)?value:Buffer.from(value);
  return crypto.createHash('sha256').update(bytes).digest('hex');
}
export function safeRelative(value){
  return typeof value==='string'&&value.length>0&&value.length<=240&&!path.isAbsolute(value)&&!value.includes('\\')&&!value.split('/').includes('..')&&value.split('/').every(x=>/^[A-Za-z0-9._-]+$/.test(x));
}
export function safeResolve(base,relative){
  if(!safeRelative(relative)) fail('Unsafe relative path: '+relative);
  const b=path.resolve(base),r=path.resolve(b,relative);
  if(r===b||!r.startsWith(b+path.sep)) fail('Path escapes authorized root: '+relative);
  return r;
}
function readUtf8(base,relative){return fs.readFileSync(safeResolve(base,relative),'utf8')}
function validateAssetRef(value,label){
  if(!exact(value,['path','sha256'])||!safeRelative(value.path)||!HEX.test(value.sha256||'')) fail('Invalid '+label+' asset metadata.');
}
export function validateDescriptor(value){
  if(!exact(value,['schemaVersion','type','id','version','title','summary','approval','skill','implementation','tests'])) fail('Invalid capability descriptor shape.');
  if(value.schemaVersion!=='0.1'||value.type!=='paperclip_capability'||!ID.test(value.id||'')||!SEMVER.test(value.version||'')) fail('Invalid capability identity.');
  if(typeof value.title!=='string'||!value.title.trim()||value.title.length>120||typeof value.summary!=='string'||!value.summary.trim()||value.summary.length>500) fail('Invalid capability title/summary.');
  if(value.approval!=='approved') fail('Capability is not approved.');
  validateAssetRef(value.skill,'skill'); validateAssetRef(value.implementation,'implementation'); validateAssetRef(value.tests,'tests');
  return value;
}
export function loadProjectManifest(projectDir){
  const value=JSON.parse(readUtf8(projectDir,'paperclip.tool.json'));
  const required=['schemaVersion','id','title','version','source','output','skill','prompts','dependencies','stickshiftInstallable'];
  if(!exact(value,required)||value.schemaVersion!=='1.0.0'||!ID.test(value.id||'')||!SEMVER.test(value.version||'')) fail('Invalid M5 project manifest.');
  if(!plain(value.source)||!['html','css','javascript'].every(k=>safeRelative(value.source[k]))||!safeRelative(value.output)) fail('Invalid project source/output.');
  if(!plain(value.skill)||!['authored','generated'].includes(value.skill.mode)||!ID.test(value.skill.slug||'')) fail('Invalid project skill.');
  if(value.skill.mode==='authored'&&!safeRelative(value.skill.path)) fail('Invalid authored project skill path.');
  if(!Array.isArray(value.prompts)||!value.prompts.every(safeRelative)||!Array.isArray(value.dependencies)||value.stickshiftInstallable!==true) fail('Invalid project arrays/installability.');
  const seen=new Set();
  for(const pin of value.dependencies){
    if(!exact(pin,['id','version','path'])||!ID.test(pin.id||'')||!SEMVER.test(pin.version||'')||!safeRelative(pin.path)) fail('Invalid capability pin.');
    if(seen.has(pin.id)) fail('Duplicate project capability pin: '+pin.id);
    seen.add(pin.id);
  }
  return value;
}
function descriptorFromPath(libraryDir,descriptorPath){
  const match=CAPABILITY_PATH.exec(descriptorPath);
  if(!match) fail('Capability pin path must use capabilities/{id}/{version}/capability.json: '+descriptorPath);
  const raw=readUtf8(libraryDir,descriptorPath),descriptor=validateDescriptor(JSON.parse(raw));
  const packageDir=path.dirname(safeResolve(libraryDir,descriptorPath));
  if(descriptor.id!==match[1]||descriptor.version!==match[2]) fail('Capability descriptor identity does not match its governed path.');
  const readAsset=(ref,label)=>{
    const target=safeResolve(packageDir,ref.path),bytes=fs.readFileSync(target);
    if(!target.startsWith(packageDir+path.sep)) fail('Capability '+label+' escapes package directory.');
    if(sha256(bytes)!==ref.sha256) fail('Capability '+label+' integrity mismatch for '+descriptor.id+'@'+descriptor.version);
    return bytes;
  };
  const skillBytes=readAsset(descriptor.skill,'skill'),implementationBytes=readAsset(descriptor.implementation,'implementation'),testBytes=readAsset(descriptor.tests,'tests');
  const skill=skillBytes.toString('utf8');
  if(!/^type:\s*Skill\s*$/mi.test(skill)) fail('Capability SKILL.md must declare type: Skill.');
  let tests;
  try{tests=JSON.parse(testBytes.toString('utf8'))}catch{fail('Capability test metadata is malformed JSON.')}
  if(!plain(tests)||tests.schemaVersion!=='0.1'||!Array.isArray(tests.cases)||!tests.cases.length) fail('Capability test metadata is invalid.');
  return Object.freeze({
    descriptorPath,
    descriptor,
    descriptorDigest:sha256(raw),
    skill,
    skillDigest:descriptor.skill.sha256,
    implementation:implementationBytes.toString('utf8'),
    implementationDigest:descriptor.implementation.sha256,
    tests,
    testsDigest:descriptor.tests.sha256
  });
}
export function scanCapabilityCatalog(libraryDir){
  const capRoot=safeResolve(libraryDir,'capabilities');
  if(!fs.existsSync(capRoot)||!fs.statSync(capRoot).isDirectory()) fail('Governed library is missing capabilities/.');
  const descriptors=[];
  function walk(dir,relative='capabilities'){
    for(const name of fs.readdirSync(dir).sort()){
      const full=path.join(dir,name),rel=relative+'/'+name,st=fs.lstatSync(full);
      if(st.isSymbolicLink()) fail('Governed library symlinks are not supported in M5: '+rel);
      if(st.isDirectory()){walk(full,rel);continue}
      if(name==='capability.json') descriptors.push(rel);
    }
  }
  walk(capRoot);
  const logical=new Set(),items=[];
  for(const descriptorPath of descriptors.sort()){
    const raw=JSON.parse(readUtf8(libraryDir,descriptorPath)),descriptor=validateDescriptor(raw),key=descriptor.id+'@'+descriptor.version;
    if(logical.has(key)) fail('Duplicate capability ID/version in governed library: '+key);
    logical.add(key);
    items.push(descriptorFromPath(libraryDir,descriptorPath));
  }
  return items.sort((a,b)=>(a.descriptor.id+'@'+a.descriptor.version).localeCompare(b.descriptor.id+'@'+b.descriptor.version));
}
export function resolveProjectCapabilities(projectDir,libraryDir){
  const manifest=loadProjectManifest(projectDir),catalog=scanCapabilityCatalog(libraryDir),byPath=new Map(catalog.map(x=>[x.descriptorPath,x])),resolved=[];
  for(const pin of manifest.dependencies){
    const item=byPath.get(pin.path);
    if(!item) fail('Missing governed capability pin: '+pin.id+'@'+pin.version+' at '+pin.path);
    if(item.descriptor.id!==pin.id||item.descriptor.version!==pin.version) fail('Governed capability pin identity mismatch: '+pin.id+'@'+pin.version);
    resolved.push(item);
  }
  const identities=resolved.map(x=>({id:x.descriptor.id,version:x.descriptor.version,descriptorDigest:x.descriptorDigest,skillDigest:x.skillDigest,implementationDigest:x.implementationDigest,testsDigest:x.testsDigest}));
  return {manifest,catalog,resolved,capabilitySetDigest:sha256(stable(identities))};
}
export function capabilityModelContext(projectDir,libraryDir){
  const state=resolveProjectCapabilities(projectDir,libraryDir),pinnedIds=new Set(state.resolved.map(x=>x.descriptor.id));
  const family=state.catalog.filter(x=>pinnedIds.has(x.descriptor.id)).map(x=>({
    id:x.descriptor.id,
    version:x.descriptor.version,
    title:x.descriptor.title,
    summary:x.descriptor.summary,
    approval:x.descriptor.approval,
    descriptorPath:x.descriptorPath,
    descriptorDigest:x.descriptorDigest,
    skillDigest:x.skillDigest,
    implementationDigest:x.implementationDigest,
    testsDigest:x.testsDigest,
    skill:x.skill,
    pinned:state.resolved.some(r=>r.descriptorPath===x.descriptorPath)
  }));
  return {capabilitySetDigest:state.capabilitySetDigest,capabilityFamily:family,implementationSourceIncluded:false};
}
function escapeSkill(value){return value.replace(/<\/script/gi,'<\\/script')}
function projectRead(projectDir,p){return readUtf8(projectDir,p)}
export function assembleToolWithCapabilities(projectDir,libraryDir){
  const state=resolveProjectCapabilities(projectDir,libraryDir),m=state.manifest,filename=path.basename(m.output),skillPath='skills/'+m.skill.slug+'.md';
  const body=projectRead(projectDir,m.source.html),css=projectRead(projectDir,m.source.css),js=projectRead(projectDir,m.source.javascript);
  let runtimeSkill=m.skill.mode==='authored'?projectRead(projectDir,m.skill.path):`---\ntype: Skill\ntitle: ${m.title}\ndescription: Launch ${m.title}.\ntags: [html-tool]\n---\n\n# ${m.title}`;
  if(!/^type:\s*Skill\s*$/mi.test(runtimeSkill)) fail('Runtime skill must declare type: Skill.');
  const open=`<HTML_OPEN>\ntool: ${filename}\ninclude:\n- ${skillPath}\n</HTML_OPEN>`;
  if(/<HTML_OPEN>/i.test(runtimeSkill)){
    if(!runtimeSkill.includes(`tool: ${filename}`)||!runtimeSkill.includes(`- ${skillPath}`)) fail('Runtime skill HTML_OPEN is invalid.');
  }else runtimeSkill+='\n\n'+open+'\n';
  const capScripts=state.resolved.map(x=>`<script data-paperclip-capability="${x.descriptor.id}@${x.descriptor.version}">\n${x.implementation.trim()}\n<\/script>`).join('\n');
  const identity={file:filename,skillSlug:m.skill.slug,title:m.title};
  const html=`<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>${m.title.replace(/[&<>]/g,'')}</title>\n<style>\n${css.trim()}\n</style>\n</head>\n<body>\n${body.trim()}\n<script>window.STICKSHIFT_TOOL = ${JSON.stringify(identity)};<\/script>\n<script type="text/markdown" id="stickshift-skill" data-skill-slug="${m.skill.slug}">\n${escapeSkill(runtimeSkill.trim())}\n<\/script>\n${capScripts}\n<script>\n${js.trim()}\n<\/script>\n</body>\n</html>\n`;
  return {html,manifest:m,resolved:state.resolved,capabilitySetDigest:state.capabilitySetDigest};
}
export function buildToolWithCapabilities(projectDir,libraryDir,outputFile){
  const built=assembleToolWithCapabilities(projectDir,libraryDir),target=path.resolve(outputFile),dir=path.dirname(target),temp=path.join(dir,'.'+path.basename(target)+'.'+process.pid+'.tmp');
  fs.mkdirSync(dir,{recursive:true});
  try{fs.writeFileSync(temp,built.html,{encoding:'utf8',flag:'wx'});fs.renameSync(temp,target)}
  catch(error){try{fs.rmSync(temp,{force:true})}catch{} throw error}
  return {...built,output:target};
}

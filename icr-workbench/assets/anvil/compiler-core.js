(function(root,factory){
  'use strict';
  const api=factory();
  if(typeof module==='object'&&module&&module.exports) module.exports=api;
  if(root) root.PaperclipCompilerCore=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';
  const ID=/^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  const VERSION=/^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/;
  const PLACEHOLDER=/\{\{[A-Z][A-Z0-9_]*\}\}/;
  function fail(message){throw new Error(message)}
  function plain(v){return !!v&&typeof v==='object'&&!Array.isArray(v)}
  function htmlAttr(value){return String(value).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
  function htmlText(value){return String(value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
  function escapeScript(value){return String(value).replace(/<\/script/gi,'<\\/script')}
  function escapeStyle(value){return String(value).replace(/<\/style/gi,'<\\/style')}
  function safeJson(value){return JSON.stringify(value).replace(/</g,'\\u003c')}
  function outputFile(manifest){const parts=String(manifest.output||'').split('/');return parts[parts.length-1]||''}
  function ensureOffline(body,css,javascript,capabilities){
    const resource=/<(?:script|img|audio|video|source|iframe)\b[^>]*\b(?:src|srcset)\s*=\s*["']\s*(?:https?:)?\/\//i;
    const stylesheet=/<link\b[^>]*\bhref\s*=\s*["']\s*(?:https?:)?\/\//i;
    if(resource.test(body)||stylesheet.test(body)) fail('External network resource is not allowed in portable HTML body.');
    if(/@import\s+(?:url\()?\s*["']?\s*(?:https?:)?\/\//i.test(css)||/url\(\s*["']?\s*(?:https?:)?\/\//i.test(css)) fail('External network resource is not allowed in portable CSS.');
    const importRe=/(?:import\s+(?:[^;]*?\s+from\s+)?|import\s*\()\s*["']\s*(?:https?:)?\/\//i;
    if(importRe.test(javascript)) fail('External network import is not allowed in portable JavaScript.');
    for(const cap of capabilities) if(importRe.test(cap.implementation)) fail('External network import is not allowed in governed capability '+cap.id+'@'+cap.version+'.');
  }
  function validateManifest(m){
    if(!plain(m)||m.schemaVersion!=='1.0.0'||!ID.test(m.id||'')||!VERSION.test(m.version||'')||typeof m.title!=='string'||!m.title.trim()) fail('Invalid Paperclip project manifest.');
    if(!plain(m.skill)||!ID.test(m.skill.slug||'')||!['authored','generated'].includes(m.skill.mode)) fail('Invalid runtime skill declaration.');
    if(!Array.isArray(m.prompts)||!Array.isArray(m.dependencies)||m.stickshiftInstallable!==true) fail('Invalid Paperclip project arrays/installability.');
    const filename=outputFile(m); if(filename!==m.id+'.html') fail('Output filename must equal the stable tool ID plus .html.');
    return filename;
  }
  function canonicalSkill(manifest,runtimeSkill,filename){
    let skill=manifest.skill.mode==='authored'?String(runtimeSkill||''):`---\ntype: Skill\ntitle: ${manifest.title}\ndescription: Launch ${manifest.title} when the operator requests it.\ntags: [html-tool]\n---\n\n# ${manifest.title}\n\nUse this generated registration skill to launch the deterministic local tool.`;
    if(!/^type:\s*Skill\s*$/mi.test(skill)) fail('Runtime skill must declare canonical type: Skill.');
    const skillPath='skills/'+manifest.skill.slug+'.md';
    const open=`<HTML_OPEN>\ntool: ${filename}\ninclude:\n- ${skillPath}\n</HTML_OPEN>`;
    if(/<HTML_OPEN>/i.test(skill)){
      if(!skill.includes('tool: '+filename)||!skill.includes('- '+skillPath)) fail('Runtime skill has an invalid HTML_OPEN filename or skill path.');
    } else skill=skill.replace(/\s+$/,'')+'\n\n## Open this tool\n\n'+open+'\n';
    return {skill,skillPath};
  }
  function validateInputs(input){
    if(!plain(input)) fail('Compiler input must be an object.');
    const manifest=input.manifest,filename=validateManifest(manifest);
    for(const k of ['body','css','javascript']) if(typeof input[k]!=='string') fail('Compiler input '+k+' must be text.');
    const prompts=Array.isArray(input.prompts)?input.prompts:[];
    if(prompts.length!==manifest.prompts.length) fail('Prompt inputs must exactly match manifest prompts.');
    for(let i=0;i<prompts.length;i++) if(!plain(prompts[i])||prompts[i].path!==manifest.prompts[i]||typeof prompts[i].content!=='string') fail('Prompt input order/path does not match manifest.');
    const capabilities=Array.isArray(input.capabilities)?input.capabilities:[];
    if(capabilities.length!==manifest.dependencies.length) fail('Capability inputs must exactly match manifest dependencies.');
    for(let i=0;i<capabilities.length;i++){
      const cap=capabilities[i],pin=manifest.dependencies[i];
      if(!plain(cap)||cap.id!==pin.id||cap.version!==pin.version||typeof cap.implementation!=='string') fail('Capability input order/identity does not match manifest pin.');
    }
    const runtime=canonicalSkill(manifest,input.runtimeSkill,filename);
    const fields=[['body',input.body],['css',input.css],['javascript',input.javascript],['skill',runtime.skill],...prompts.map(x=>['prompt '+x.path,x.content]),...capabilities.map(x=>['capability '+x.id+'@'+x.version,x.implementation])];
    for(const [label,value] of fields) if(PLACEHOLDER.test(value)) fail('Unresolved source placeholder in '+label+'.');
    if(/<script\b/i.test(input.body)) fail('Executable script tags are not allowed in modular body source; use source.javascript or a governed capability.');
    ensureOffline(input.body,input.css,input.javascript,capabilities);
    return {manifest,filename,prompts,capabilities,runtime};
  }
  function compileTool(input){
    const s=validateInputs(input),m=s.manifest;
    const identity={file:s.filename,skillSlug:m.skill.slug,title:m.title};
    const descriptor={schema:'paperclip-portable-tool',version:'1.0',file:s.filename,skillSlug:m.skill.slug,title:m.title,projectVersion:m.version,prompts:s.prompts.map(x=>x.path),capabilities:s.capabilities.map(x=>({id:x.id,version:x.version}))};
    const promptBlocks=s.prompts.map((p,i)=>`<script type="text/markdown" class="paperclip-prompt" data-prompt-path="${htmlAttr(p.path)}" data-prompt-index="${i}">\n${escapeScript(p.content.trim())}\n<\/script>`).join('\n');
    const capabilityBlocks=s.capabilities.map(cap=>`<script data-paperclip-capability="${htmlAttr(cap.id+'@'+cap.version)}">\n${escapeScript(cap.implementation.trim())}\n<\/script>`).join('\n');
    const sections=[
      '<!doctype html>', '<html lang="en">', '<head>', '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width,initial-scale=1">',
      '<title>'+htmlText(m.title)+'</title>', '<style>', escapeStyle(input.css.trim()), '</style>', '</head>', '<body>', input.body.trim(),
      '<script id="tool-descriptor" type="application/json">'+safeJson(descriptor)+'<\/script>',
      '<script>window.STICKSHIFT_TOOL = '+safeJson(identity)+';<\/script>',
      '<script type="text/markdown" id="stickshift-skill" data-skill-slug="'+htmlAttr(m.skill.slug)+'" data-skill-kind="'+m.skill.mode+'">', escapeScript(s.runtime.skill.trim()), '<\/script>'
    ];
    if(promptBlocks) sections.push(promptBlocks);
    if(capabilityBlocks) sections.push(capabilityBlocks);
    sections.push('<script>',escapeScript(input.javascript.trim()),'<\/script>','</body>','</html>','');
    return {html:sections.join('\n'),fileName:s.filename,skillPath:s.runtime.skillPath,descriptor,identity};
  }
  return Object.freeze({compileTool,validateInputs,escapeScript,escapeStyle});
});

import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {gzipSync} from 'node:zlib';
import {createRequire} from 'node:module';
import {sha256, stable, resolveProjectCapabilities, loadProjectManifest} from '../assets/anvil/governed-capability.mjs';
const require = createRequire(import.meta.url);
const Compiler = require('../assets/anvil/compiler-core.js');
const Authoring = require('../assets/anvil/anvil-authoring.js');
export const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const root = path.dirname(project);
export const release = fs.existsSync(path.join(root, 'release/icr-evidence/v1.0.0')) ? path.join(root, 'release/icr-evidence/v1.0.0') : path.join(root, 'evidence/icr-evidence/v1.0.0');
export const library = path.join(root, 'governed-library');
export const read = p => fs.readFileSync(path.join(project, p), 'utf8');
export const pin = JSON.parse(read('assets/evidence-pin.json'));
export const manifest = JSON.parse(read('paperclip.tool.json'));
export function paths(dir) {
  return fs.readdirSync(dir).sort().flatMap(name => {
    const full = path.join(dir, name), st = fs.lstatSync(full);
    if (st.isSymbolicLink()) throw Error('Symlink not permitted: ' + full);
    return st.isDirectory() ? paths(full).map(p => name + '/' + p) : [name];
  });
}
export function write(p, value) {
  fs.mkdirSync(path.dirname(p), {recursive:true});
  fs.writeFileSync(p, typeof value === 'string' ? value : JSON.stringify(value, null, 2) + '\n');
}
export function evidenceEntries() { return paths(release).map(p => [p, fs.readFileSync(path.join(release,p))]); }
export async function verifyEvidence() {
  const Consumer = await import(path.join(release, 'runtime/consumer.mjs'));
  const actual = paths(release);
  const result = await Consumer.loadRelease(p => fs.readFileSync(path.join(release,p)), {expectedManifestHash:pin.manifest_sha256, listPaths:() => actual.filter(p => !['FREEZE-RECEIPT.json','validation/final-acceptance-gate.json'].includes(p))});
  for (const [key,value] of Object.entries({release_id:pin.release_id, graph_version:pin.tsa_graph, canonical_model_version:pin.canonical_model, rubric_version:pin.rubric})) if (result.manifest[key] !== value) throw Error('Evidence pin mismatch: ' + key);
  if (result.manifest.evidence_versions.federal !== pin.federal_evidence || result.manifest.evidence_versions.tsa !== pin.tsa_evidence) throw Error('Evidence version mismatch');
  const receipt = JSON.parse(fs.readFileSync(path.join(release,'FREEZE-RECEIPT.json')));
  if (receipt.terminal_state !== 'ICR_EVIDENCE_RELEASE_FROZEN' || receipt.release_manifest_sha256 !== pin.manifest_sha256 || receipt.release_id !== pin.release_id) throw Error('Invalid administrative freeze receipt');
  return result;
}
export function sourceValidation() {
  const upstream = JSON.parse(read('assets/anvil/upstream-pin.json'));
  for (const [file, hash] of Object.entries(upstream.files)) if (sha256(fs.readFileSync(path.join(project,'assets/anvil',file))) !== hash) throw Error('Altered upstream Anvil contract: ' + file);
  loadProjectManifest(project);
  const entries = paths(project).filter(p => !p.startsWith('dist/')).map(p => ({path:p,bytes:fs.readFileSync(path.join(project,p))}));
  Authoring.validateProjectClosure(entries);
  const codePaths = [...paths(path.join(project,'assets/foundation')).map(p=>'assets/foundation/'+p), 'src/app.js'];
  for (const p of codePaths) {
    const code = read(p);
    if (/\b(?:eval|Function)\s*\(|\b(?:innerHTML|outerHTML|insertAdjacentHTML)\b|document\.write\s*\(|\b(?:fetch|XMLHttpRequest|WebSocket|EventSource|importScripts)\s*\(/.test(code)) throw Error('Unsafe rendering or runtime network path: '+p);
    if (/\bimport\s*\(|\bon\w+\s*=/.test(code)) throw Error('Dynamic import/inline handler: '+p);
  }
  const html = read('src/index.html'), css = read('src/style.css');
  if (/\bon\w+\s*=|<script\b|<(?:iframe|object|embed)\b/i.test(html)) throw Error('Unsafe modular body');
  if (/@import|url\(/i.test(css)) throw Error('External/local CSS asset dependencies are not allowed');
  for (const p of Object.values(manifest.source)) if (!fs.existsSync(path.join(project,p))) throw Error('Missing source: '+p);
  return {status:'PASS',upstream_files:Object.keys(upstream.files).length,source_files:codePaths};
}
export function capabilityInputs() {
  const inputs = ['assets/evidence-pin.json',...paths(path.join(project,'assets/foundation')).map(p=>'assets/foundation/'+p)];
  return Object.fromEntries([...inputs.map(p => [p,sha256(read(p))]),...evidenceEntries().map(([p,b]) => ['evidence/'+p,sha256(b)])]);
}
export function implementation() {
  const consumer = fs.readFileSync(path.join(release,'runtime/consumer.mjs'),'utf8');
  const names = [...consumer.matchAll(/^export (?:async )?(?:const|function) (\w+)/gm)].map(m=>m[1]);
  const payload = gzipSync(Buffer.from(JSON.stringify(Object.fromEntries(evidenceEntries().map(([p,b])=>[p,b.toString('base64')])))), {level:9}).toString('base64');
  const body = ['adapter','render','provider','stores'].map(p=>read('assets/foundation/'+p+'.js')).join('\n');
  return `(function(root){\n'use strict';\nconst Consumer = (function(){\n${consumer.replace(/^export /gm,'')}\nreturn Object.freeze({${names.join(',')}});\n})();\nconst PIN = ${JSON.stringify(pin)};\nconst PAYLOAD = ${JSON.stringify(payload)};\n${body}\nroot.ICRFoundation = Object.freeze({appVersion:${JSON.stringify(manifest.version)},capabilityVersion:${JSON.stringify(manifest.dependencies[0].version)},pin:deepFreeze(PIN),loadAdapter,bytesAdapter,fileAdapter,bundledAdapter,createQueryProvider,createStores,textNode,safeSourceURL,sourceLink});\n})(globalThis);\n`;
}
export async function build({prepare=false}={}) {
  const validation = sourceValidation();
  const evidence = await verifyEvidence();
  const inputs = capabilityInputs();
  const dep = manifest.dependencies[0];
  if (prepare) {
    const dir = path.dirname(path.join(library,dep.path));
    const impl = implementation();
    const skill = '---\ntype: Skill\ntitle: ICR Evidence Foundation\ndescription: Use verified immutable public evidence through the bounded ICRFoundation APIs.\n---\n\nCall ICRFoundation.loadAdapter(await ICRFoundation.bundledAdapter()), then createQueryProvider(base) and createStores(base). Never mutate public evidence. Render text with textNode and sourceLink. No language queries, executable packets or calculation model are implemented.\n';
    const tests = JSON.stringify({schemaVersion:'0.1',cases:[{id:'pinned-evidence-load',command:'node --test tests/foundation.test.mjs'},{id:'isolated-state-safe-text',command:'node --test tests/foundation.test.mjs'}]},null,2)+'\n';
    write(path.join(dir,'implementation.js'),impl); write(path.join(dir,'SKILL.md'),skill); write(path.join(dir,'tests.json'),tests);
    write(path.join(dir,'capability.json'),{schemaVersion:'0.1',type:'paperclip_capability',id:dep.id,version:dep.version,title:'ICR Evidence Foundation',summary:'Pinned offline evidence loading, bounded retrieval, isolated state and safe text rendering. Scoped repository authorization establishes this technical capability release; no institutional analytical approval is implied.',approval:'approved',skill:{path:'SKILL.md',sha256:sha256(skill)},implementation:{path:'implementation.js',sha256:sha256(impl)},tests:{path:'tests.json',sha256:sha256(tests)}});
    const state = resolveProjectCapabilities(project,library);
    write(path.join(project,'assets/dependencies.lock.json'),{schema_version:'1.0.0',capability_set_sha256:state.capabilitySetDigest,source_inputs:inputs,dependencies:state.resolved.map(r=>({path:r.descriptorPath,descriptor_sha256:r.descriptorDigest,implementation_sha256:r.implementationDigest,skill_sha256:r.skillDigest,tests_sha256:r.testsDigest}))});
  }
  const lock = JSON.parse(read('assets/dependencies.lock.json'));
  if (stable(lock.source_inputs)!==stable(inputs)) throw Error('Stale capability source lock; reviewed capability release preparation required');
  const state = resolveProjectCapabilities(project,library);
  if (state.capabilitySetDigest!==lock.capability_set_sha256) throw Error('Governed capability lock mismatch');
  const built = Compiler.compileTool({manifest,body:read(manifest.source.html),css:read(manifest.source.css),javascript:read(manifest.source.javascript),runtimeSkill:read(manifest.skill.path),prompts:manifest.prompts.map(p=>({path:p,content:read(p)})),capabilities:state.resolved.map(r=>({id:r.descriptor.id,version:r.descriptor.version,implementation:r.implementation}))});
  write(path.join(project,manifest.output),built.html);
  const report = {schema_version:'1.0.0',status:'PASS',project_version:manifest.version,project_root:'icr-workbench',evidence_release_id:pin.release_id,manifest_sha256:pin.manifest_sha256,source_validation:validation,anvil_contract:'PASS',standalone:{path:'icr-workbench/'+manifest.output,sha256:sha256(built.html),bytes:Buffer.byteLength(built.html)},capability_set_sha256:state.capabilitySetDigest,evidence_validation:evidence.validation};
  write(path.join(project,'validation/build-report.json'),report);
  return {built,report};
}
if (process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const result = await build({prepare:process.argv.includes('--prepare-capability')});
  console.log(JSON.stringify({status:result.report.status,standalone:result.report.standalone}));
}

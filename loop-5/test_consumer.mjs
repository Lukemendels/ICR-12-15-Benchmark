#!/usr/bin/env node
import {readFile,readdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {webcrypto} from 'node:crypto';
import {loadRelease,query,sha256,schemaValidate} from './consumer.mjs';
globalThis.crypto??=webcrypto;
const root=resolve(process.argv[2]),out=process.argv[3];
const originalManifest=JSON.parse(await readFile(root+'/release-manifest.json','utf8'));
const base=new Map([['release-manifest.json',await readFile(root+'/release-manifest.json')]]);
for(const x of originalManifest.files)base.set(x.path,await readFile(root+'/'+x.path));
const enc=x=>new TextEncoder().encode(JSON.stringify(x));let tests=[];
async function reject(name,change,{rehash=false,expectedHash=null,listExtra=false}={}) {
  const bytes=new Map(base);await change(bytes);
  if(rehash) {
    const m=JSON.parse(new TextDecoder().decode(bytes.get('release-manifest.json')));
    for(const f of m.files)if(bytes.has(f.path)){f.bytes=bytes.get(f.path).byteLength;f.sha256=await sha256(bytes.get(f.path));}
    bytes.set('release-manifest.json',enc(m));
  }
  let error=null;try{await loadRelease(p=>{if(!bytes.has(p))throw Error('Missing '+p);return bytes.get(p);},{expectedManifestHash:expectedHash,listPaths:()=>[...bytes.keys(),...(listExtra?['unregistered.txt']:[])]});}catch(e){error=e.message;}
  if(!error)throw Error('Negative test unexpectedly passed: '+name);tests.push({name,status:'PASS',rejected_with:error});
}
const mutate=(bytes,p,fn)=>{let x=JSON.parse(new TextDecoder().decode(bytes.get(p)));fn(x);bytes.set(p,enc(x));};
await reject('wrong_manifest_pin',()=>{},{expectedHash:'0'.repeat(64)});
await reject('corrupt_artifact_byte',b=>{b.set('tsa/portfolio.json',new Uint8Array([0]));});
await reject('missing_artifact',b=>b.delete('tsa/portfolio.json'));
await reject('unregistered_file',()=>{},{listExtra:true});
await reject('schema_missing_required_field',b=>mutate(b,'tsa/portfolio.json',x=>{delete x[0].ref;}),{rehash:true});
await reject('dangling_graph_edge',b=>mutate(b,'tsa/edges.json',x=>{x[0].target='MISSING';}),{rehash:true});
await reject('dangling_claim_source',b=>mutate(b,'federal/claims.json',x=>{x[0].source_ids=['MISSING'];}),{rehash:true});
await reject('dangling_comparison_observation',b=>mutate(b,'tsa/comparisons.json',x=>{x[0].observations[0].id='MISSING';}),{rehash:true});
await reject('dangling_provenance',b=>mutate(b,'tsa/nodes.json',x=>{x[0].provenance_refs=['MISSING'];}),{rehash:true});
await reject('registered_counts_mismatch',b=>mutate(b,'release-manifest.json',x=>{x.record_counts.tsa_recent_packages=89;}),{rehash:true});
await reject('bridge_component_arithmetic',b=>mutate(b,'tsa/item15-bridges.json',x=>{x[0].component_deltas[0]++;}),{rehash:true});
await reject('duplicate_node_identity',b=>mutate(b,'tsa/nodes.json',x=>{x[1].id=x[0].id;}),{rehash:true});
await reject('unsupported_schema_keyword',b=>mutate(b,'schemas/claim.schema.json',x=>{x.anyOf=[];}),{rehash:true});
await reject('unsupported_release_version',b=>mutate(b,'release-manifest.json',x=>{x.version='2.0.0';}),{rehash:true});
const loaded=await loadRelease(p=>base.get(p));
for(const [name,request] of [['unbounded_limit',{limit:101}],['unknown_query_operator',{sql:'select *'}],['unknown_facet',{filters:{execute:'code'}}]]) {
  let error=null;try{query(loaded.files,request);}catch(e){error=e.message;}
  if(!error)throw Error('Unsafe query accepted '+name);tests.push({name,status:'PASS',rejected_with:error});
}
const pages=[];let after=null;do{const p=query(loaded.files,{filters:{type:'ACTIVITY'},limit:37,after});pages.push(...p.records.map(x=>x.key));after=p.next;}while(after);
if(pages.length!==493||new Set(pages).size!==493)throw Error('Pagination loss or duplicates');
tests.push({name:'pagination_complete_without_duplicates',status:'PASS',records:pages.length});
const report={status:'PASS',tests};if(out)await writeFile(out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));

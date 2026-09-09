/** Dependency-free ES module; browser File/ArrayBuffer adapters or WebView2 may supply readBytes.
 * Never evaluates formulas, HTML, model packets, or arbitrary code contained in evidence.
 */
export const VERSION = '1.0.0';
const fail = message => { throw new Error(message); };
const text = b => new TextDecoder('utf-8', {fatal:true}).decode(b);
const stable = x => JSON.stringify(x && typeof x==='object' ? Array.isArray(x) ? x.map(v=>JSON.parse(stable(v))) : Object.fromEntries(Object.keys(x).sort().map(k=>[k,JSON.parse(stable(x[k]))])) : x);
export const sha256 = async bytes => Array.from(new Uint8Array(await globalThis.crypto.subtle.digest('SHA-256',bytes)), b=>b.toString(16).padStart(2,'0')).join('');
const schemaKeywords = new Set(['$schema','$id','title','description','type','required','properties','additionalProperties','items','enum','const','minimum','maximum','minItems','minLength','pattern']);
export function schemaValidate(value, schema, path='$') {
  for(const k of Object.keys(schema)) if(!schemaKeywords.has(k)) fail(`Unsupported schema keyword ${k}`);
  const type = value===null?'null':Array.isArray(value)?'array':typeof value;
  if(schema.type && ![schema.type].flat().some(t=>t===type || t==='integer'&&Number.isInteger(value))) fail(`Schema type ${path}: ${type}`);
  if(schema.enum && !schema.enum.some(x=>stable(x)===stable(value))) fail(`Schema enum ${path}`);
  if('const' in schema && stable(value)!==stable(schema.const)) fail(`Schema const ${path}`);
  if(typeof value==='number' && (!Number.isFinite(value) || schema.minimum!==undefined&&value<schema.minimum || schema.maximum!==undefined&&value>schema.maximum)) fail(`Schema number ${path}`);
  if(typeof value==='string' && (schema.minLength!==undefined&&value.length<schema.minLength || schema.pattern&&!new RegExp(schema.pattern).test(value))) fail(`Schema string ${path}`);
  if(type==='object') {
    for(const k of schema.required||[]) if(!Object.hasOwn(value,k)) fail(`Schema required ${path}.${k}`);
    for(const [k,v] of Object.entries(value)) {
      if(schema.properties?.[k])schemaValidate(v,schema.properties[k],`${path}.${k}`);
      else if(schema.additionalProperties===false)fail(`Schema extra ${path}.${k}`);
    }
  }
  if(type==='array') {
    if(schema.minItems!==undefined&&value.length<schema.minItems)fail(`Schema array ${path}`);
    if(schema.items)value.forEach((v,i)=>schemaValidate(v,schema.items,`${path}[${i}]`));
  }
}
export function resolve(files,address) {
  const [p,pointer,...extra]=address.split('#');if(extra.length||!Object.hasOwn(files,p))fail(`Unresolved file ${address}`);
  let x=files[p];
  if(pointer) {if(!pointer.startsWith('/'))fail(`Invalid JSON pointer ${address}`);for(const part of pointer.slice(1).split('/')) {const key=part.replace(/~1/g,'/').replace(/~0/g,'~');if(x===null||typeof x!=='object'||!Object.hasOwn(x,key))fail(`Unresolved pointer ${address}`);x=x[key];}}
  return x;
}
export function hydrate(value, provenance) {
  if(Array.isArray(value))return value.map(x=>hydrate(x,provenance));
  if(!value||typeof value!=='object')return value;
  const out={};for(const [k,v] of Object.entries(value)) {
    if(k==='provenance_refs')out.provenance=v.map(id=>provenance[id]??fail(`Unresolved provenance ${id}`));
    else out[k]=hydrate(v,provenance);
  }return out;
}
export function query(files, {filters={},limit=50,after=null,...rest}={}) {
  if(Object.keys(rest).length)fail('Unknown query fields');
  if(!Number.isInteger(limit)||limit<1||limit>100)fail('Query limit must be 1..100');
  if(!filters || typeof filters!=='object'||Array.isArray(filters))fail('Invalid filters');
  if(after!==null&&typeof after!=='string')fail('Invalid cursor');
  const facets=files['indexes/facets.json'],addresses=files['indexes/addresses.json'];let allowed=null;
  for(const [name,value] of Object.entries(filters)) {
    if(!Object.hasOwn(facets,name)||typeof value!=='string')fail(`Invalid exact facet ${name}`);
    const set=new Set(facets[name][value]||[]);allowed=allowed===null?set:new Set([...allowed].filter(x=>set.has(x)));
  }
  const keys=[...(allowed??new Set(Object.keys(addresses)))].sort();
  const page=keys.filter(k=>after===null||k>after).slice(0,limit);
  return {total:keys.length,records:page.map(key=>({key,address:addresses[key],record:resolve(files,addresses[key])})),next:page.length===limit && keys.some(k=>k>page.at(-1))?page.at(-1):null};
}
export async function loadRelease(readBytes,{expectedManifestHash=null,listPaths=null}={}) {
  const manifestBytes=await readBytes('release-manifest.json'),manifestHash=await sha256(manifestBytes);
  if(expectedManifestHash && manifestHash!==expectedManifestHash)fail('Manifest hash mismatch');
  const m=JSON.parse(text(manifestBytes));
  if(m.release_id!=='ICR-EVIDENCE-1.0.0'||m.version!==VERSION||m.schema_version!==VERSION)fail('Unsupported release identity/schema');
  if(!Array.isArray(m.files)||!m.files.length)fail('Empty file inventory');
  const files={},seen=new Set();let bytes=0;
  for(const f of m.files) {
    if(typeof f.path!=='string'||f.path.includes('\\')||f.path.startsWith('/')||f.path.split('/').some(x=>!x||x==='.'||x==='..')||seen.has(f.path)||f.path==='release-manifest.json')fail('Unsafe or duplicate inventory path');
    seen.add(f.path);const b=await readBytes(f.path);
    if(b.byteLength!==f.bytes||await sha256(b)!==f.sha256)fail(`Integrity mismatch ${f.path}`);
    bytes+=b.byteLength;if(f.path.endsWith('.json'))files[f.path]=JSON.parse(text(b));
  }
  if(listPaths) {const actual=await listPaths();const expected=[...seen,'release-manifest.json'].sort();if(stable(actual.sort())!==stable(expected))fail('Unexpected/missing files in directory');}
  schemaValidate(m,files['schemas/manifest.schema.json']);
  for(const f of m.files) {
    if(!f.path.endsWith('.json'))continue;
    if(f.record_count!==null&&f.record_count!==undefined&&(!Array.isArray(files[f.path])||files[f.path].length!==f.record_count))fail(`Manifest file count ${f.path}`);
    if(!f.schema||!files[f.schema])fail(`Unregistered schema ${f.path}`);
    const values=f.schema_mode==='each_record'?files[f.path]:[files[f.path]];
    if(!Array.isArray(values))fail(`Expected record array ${f.path}`);
    values.forEach((v,i)=>schemaValidate(v,files[f.schema],`${f.path}#/${i}`));
  }
  const nodes=files['tsa/nodes.json'],edges=files['tsa/edges.json'],p=files['provenance/observations.json'];
  const unique=(xs,field,label)=>{const map=new Map();for(const x of xs){if(map.has(x[field]))fail(`Duplicate ${label} ${x[field]}`);map.set(x[field],x);}return map;};
  const nodeMap=unique(nodes,'id','node');unique(edges,'id','edge');
  const sources=files['indexes/sources.json'];
  const allSources=unique([...files['federal/source-registry.json'],...files['tsa/source-registry.json']],'id','source');
  unique(files['federal/claims.json'],'claim_id','claim');
  if(allSources.size!==Object.keys(sources).length||[...allSources.keys()].some(id=>!Object.hasOwn(sources,id)))fail('Source registry index coverage');
  for(const [id,address] of Object.entries(sources))if(resolve(files,address).id!==id)fail('Source index mismatch');
  for(const [id,observation] of Object.entries(p)) {schemaValidate(observation,files['schemas/provenance.schema.json']);if(!sources[observation.source_id])fail(`Missing source ${id}`);}
  let provenanceLinks=0;
  function walk(x) {if(!x||typeof x!=='object')return; if(Array.isArray(x)){x.forEach(walk);return;}for(const [k,v] of Object.entries(x)){if(k==='provenance_refs')for(const id of v){if(!Object.hasOwn(p,id))fail(`Missing provenance ${id}`);provenanceLinks++;}else {if((k==='source_id'||k==='source_ids')&&(typeof v==='string'||Array.isArray(v)))for(const id of (Array.isArray(v)?v:v.split(';')))if(typeof id==='string'&&/^(SRC-|M3-SRC-|M3-META-)/.test(id)&&!sources[id])fail(`Unresolved embedded source ${id}`);walk(v);}}}
  for(const [path,x] of Object.entries(files))if(!path.startsWith('schemas/'))walk(x);
  for(const n of nodes) {
    if(n.type==='ACTIVITY')schemaValidate(n.data,files['schemas/activity-data.schema.json']);
    if(n.type==='ASSUMPTION')schemaValidate(n.data,files['schemas/assumption-data.schema.json']);
  }
  for(const e of edges)if(!nodeMap.has(e.source)||!nodeMap.has(e.target))fail(`Edge endpoint ${e.id}`);
  const models=unique(files['federal/models.json'],'icr_id','model');
  const benchmark=unique(files['federal/benchmark.json'],'icr_id','benchmark');
  for(const r of files['federal/claims.json']) {if(r.icr_id&&!models.has(r.icr_id))fail(`Claim ICR ${r.claim_id}`);for(const id of r.source_ids)if(!sources[id])fail(`Claim source ${r.claim_id}`);}
  for(const r of files['federal/benchmark.json']) {if(!models.has(r.icr_id))fail('Benchmark model');for(const id of r.source_ids.split(';'))if(!sources[id])fail('Benchmark source');}
  for(const r of models.values())for(const id of r.source_ids)if(!sources[id])fail('Model source');
  for(const r of files['federal/assumption-library.json'])for(const ref of r.example_icrs.split(';'))if(!benchmark.has(ref))fail(`Assumption exemplar ${ref}`);
  const comparisons=unique(files['tsa/comparisons.json'],'id','comparison'),within=unique(files['tsa/within-icr-findings.json'],'id','within finding'),qa=unique(files['tsa/quantitative-checks.json'],'id','QA');
  const groups=unique(files['tsa/comparison-groups.json'],'id','comparison group');
  for(const r of [...comparisons.values(),...within.values()]) {
    if(!nodeMap.has(r.id))fail(`Finding projection missing ${r.id}`);
    if(nodeMap.get(r.id).data.classification!==r.classification)fail(`Finding classification mismatch ${r.id}`);
    for(const ref of r.refs)if(!nodeMap.has('VER-'+ref))fail(`Finding version ${ref}`);
    for(const check of r.check_ids||[])if(!qa.has(check))fail(`Finding check ${check}`);
    if(comparisons.has(r.id)) {
      if(!groups.has(r.comparison_group))fail(`Comparison group ${r.id}`);
      for(const o of r.observations)if(!nodeMap.has(o.id))fail(`Comparison observation ${o.id}`);
    }
  }
  for(const r of groups.values())for(const id of r.members)if(!nodeMap.has(id))fail(`Group member ${id}`);
  for(const r of files['tsa/review-questions.json'])if(!comparisons.has(r.finding_id)&&!within.has(r.finding_id))fail('Question target');
  for(const r of files['tsa/challenges.json'])if(r.finding_id?!comparisons.has(r.finding_id)&&!within.has(r.finding_id):!qa.has(r.check_id))fail('Challenge target');
  for(const r of files['tsa/federal-comparators.json']) {if(!models.has(r.ref))fail('Federal comparator model');for(const id of r.related_findings)if(!comparisons.has(id)&&!within.has(id)&&!files['tsa/item15-bridges.json'].some(b=>b.id===id))fail('Comparator finding');}
  for(const r of files['analysis/findings.json'])for(const address of r.evidence_refs)resolve(files,address);
  for(const [key,address] of Object.entries(files['indexes/addresses.json']))resolve(files,address);
  for(const values of Object.values(files['indexes/facets.json']))for(const keys of Object.values(values))for(const key of keys)if(!Object.hasOwn(files['indexes/addresses.json'],key))fail('Facet target');
  const adjacency={};for(const e of edges)((adjacency[e.source]??={})[e.type]??=[]).push(e.target);
  for(const d of Object.values(adjacency))for(const v of Object.values(d))v.sort();
  if(stable(adjacency)!==stable(files['indexes/adjacency.json']))fail('Adjacency projection differs');
  const countBy=(xs,f)=>xs.reduce((a,x)=>(a[f(x)]=(a[f(x)]||0)+1,a),{});
  const actual={tsa_recent_packages:files['tsa/portfolio.json'].length,tsa_control_histories:files['tsa/control-histories.json'].length,unassigned_control_packages:files['tsa/portfolio.json'].filter(x=>!x.control).length,represented_versions_including_lineage:nodes.filter(x=>x.type==='ICR_VERSION').length,archived_statement_versions:files['tsa/source-registry.json'].filter(x=>x.original_record.path).length,activity_representations:nodes.filter(x=>x.type==='ACTIVITY'&&x.data.record_kind==='normalized_activity_representation').length,graph_activity_nodes:nodes.filter(x=>x.type==='ACTIVITY').length,assumption_context_activity_nodes:nodes.filter(x=>x.type==='ACTIVITY'&&x.data.record_kind==='assumption_task_context').length,assumption_observations:nodes.filter(x=>x.type==='ASSUMPTION').length,reviewed_scalar_categorical_assumptions:nodes.filter(x=>x.type==='ASSUMPTION'&&Object.hasOwn(x.data,'normalized_value')).length,formula_header_observations:nodes.filter(x=>x.type==='ASSUMPTION'&&Object.hasOwn(x.data,'formula')).length,task_method_comparisons:comparisons.size,within_icr_findings:within.size,adjudicated_records:comparisons.size+within.size,comparison_classifications:countBy([...comparisons.values()],x=>x.classification),within_icr_classifications:countBy([...within.values()],x=>x.classification),combined_classifications:countBy([...comparisons.values(),...within.values()],x=>x.classification),quantitative_checks:qa.size,versions_with_quantitative_checks:new Set([...qa.values()].map(x=>x.ref)).size};
  const frozen=files['provenance/frozen-state.json'];
  if(stable(actual)!==stable(frozen.mission3_counts))fail('Authoritative Mission 3 counts do not reconcile');
  if(nodes.length!==frozen.graph_manifest.node_count||edges.length!==frozen.graph_manifest.edge_count)fail('Graph counts');
  if(stable(countBy(nodes,x=>x.type))!==stable(frozen.graph_manifest.node_types)||stable(countBy(edges,x=>x.type))!==stable(frozen.graph_manifest.edge_types))fail('Graph type counts');
  for(const [key,count] of Object.entries({icrs_reviewed:benchmark.size,source_count:files['federal/source-registry.json'].length,claim_count:files['federal/claims.json'].length,calculation_checks:files['federal/calculation-checks.json'].length}))if(frozen.mission1[key]!==count)fail(`M1 count ${key}`);
  if(stable(m.record_counts)!==stable(actual))fail('Manifest record counts');
  for(const r of files['tsa/item15-bridges.json']) {
    if(!nodeMap.has('VER-'+r.current_ref)||!nodeMap.has('VER-'+r.prior_ref))fail('Bridge lineage');
    const sum=a=>a.reduce((a,b)=>a+b,0);
    if(r.components.length!==r.prior_values.length||r.components.length!==r.current_values.length||r.components.length!==r.component_deltas.length||sum(r.prior_values)!==r.baseline||sum(r.current_values)!==r.current||r.component_deltas.some((d,i)=>d!==r.current_values[i]-r.prior_values[i])||sum(r.component_deltas)!==r.net_change||r.current-r.baseline-r.net_change!==r.residual)fail('Bridge reconciliation');
  }
  const unresolved=[...comparisons.values()].filter(r=>r.classification==='UNRESOLVED').map(r=>r.id).sort();
  if(stable(unresolved)!==stable(files['tsa/unresolved-questions.json'].map(r=>r.finding_id).sort()))fail('Unresolved register mismatch');
  return {manifest:m,manifestHash,files,validation:{status:'PASS',artifacts:seen.size,bytes,nodes:nodes.length,edges:edges.length,provenance_records:Object.keys(p).length,provenance_links:provenanceLinks,record_counts:actual,unresolved_ids:unresolved}};
}

export function acceptance(files) {
  const results=[];
  const check=(name,condition,detail)=>{if(!condition)fail(`Clean-load acceptance: ${name}`);results.push({name,status:'PASS',detail});};
  const portfolio=files['tsa/portfolio.json'];check('enumerate_tsa_portfolio',portfolio.length===90,{count:portfolio.length});
  const ref='202406-1652-001';const selected=portfolio.find(x=>x.ref===ref);check('select_icr_version',!!selected,selected?.title);
  const acts=query(files,{filters:{package:ref,type:'ACTIVITY'},limit:100});check('normalized_activities',acts.total>0,{ref,count:acts.total});
  const assumptions=query(files,{filters:{package:ref,type:'ASSUMPTION'},limit:100});check('associated_assumptions',assumptions.total>0,{count:assumptions.total,relationship:'same package context; direct task use requires USES_ASSUMPTION edge'});
  const comps=query(files,{filters:{package:ref,dataset:'tsa/comparisons.json'},limit:100});check('comparison_adjudications',comps.total>0,comps.records.map(x=>x.record.id));
  const sourceIds=[...new Set([...acts.records,...assumptions.records,...comps.records].flatMap(x=>(x.record.provenance_refs||[]).map(id=>files['provenance/observations.json'][id].source_id)))];
  const sources=sourceIds.map(id=>resolve(files,files['indexes/sources.json'][id]));check('linked_public_sources',sources.length>0&&sources.every(s=>/^https?:\/\//.test(s.url)),sources.map(x=>({id:x.id,url:x.url})));
  const pipeline=files['tsa/quantitative-checks.json'].find(x=>x.id==='QA-CYBER-COST');const finding=files['tsa/within-icr-findings.json'].find(x=>x.id==='FIND-CYBER-COST');
  check('pipeline_federal_cost_case',pipeline&&finding&&Math.abs(pipeline.calculated_value-100*(8*122.27+24*104.17))<1e-8,{check_id:pipeline?.id,finding_id:finding?.id,published:pipeline?.published_value,recomputed:pipeline?.calculated_value,interpretation:pipeline?.interpretation});
  const bridge=files['tsa/item15-bridges.json'].find(x=>x.id==='BASELINE-TWIC-2025');check('validated_twic_item15_bridge',bridge?.residual===0&&bridge?.baseline_identity==='VERIFIED_MATCH_TO_ITEM15_AND_PREDECESSOR',{id:bridge?.id,prior:bridge?.baseline,change:bridge?.net_change,current:bridge?.current,residual:bridge?.residual});
  const questions=files['tsa/unresolved-questions.json'];check('six_unresolved_task_method_questions',questions.length===6,questions.map(x=>({id:x.finding_id,question:x.question})));
  const comparators=files['tsa/federal-comparators.json'];check('federal_comparator_material',comparators.length===4&&comparators.every(x=>files['federal/models.json'].some(m=>m.icr_id===x.ref)),comparators.map(x=>({id:x.id,application:x.application})));
  const federalReview=query(files,{filters:{type:'ASSUMPTION',assumption_family:'federal_review_time'},limit:100});check('federal_review_time_assumption_query',federalReview.total>0,{count:federalReview.total});
  const amendment=files['tsa/comparisons.json'].find(x=>x.id==='CMP-01');check('carrier_amendment_query',amendment?.classification==='CONSISTENT',{id:amendment?.id,observations:amendment?.observations.map(x=>x.id)});
  return {status:'PASS',manifest_load:'PASS',integrity:'PASS',tests:results};
}

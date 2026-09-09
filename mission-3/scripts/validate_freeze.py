"""Bounded release closure checks. No retrieval, normalization or graph rebuild."""
from final_common import *
import collections, re
import validate_final_graph as graph
errors=[]
def check(ok,name,detail=None):
 if not ok: errors.append({'check':name,'detail':detail})
def blob(p):
 b=(ROOT/p).read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
m1_sources={x['source_id'] for x in rows('data/sources.jsonl')}
C=rows('analysis/adjudicated-comparisons.jsonl');F=rows('analysis/adjudicated-findings.jsonl');A=rows('analysis/adversarial-challenge.jsonl');Q=rows('analysis/within-icr-qa.jsonl');M=read('evidence-graph/manifest.json');S=read('evidence-graph/schema.json');counts=read('mission-3/release-counts.json')
for name,rs in [('comparisons',C),('findings',F),('challenges',A),('checks',Q)]:
 check(len({x['id'] for x in rs})==len(rs),'unique_ledger_ids',name)
for x in C+F:
 check(x['classification'] in S['classifications'],'classification',x['id'])
 check(bool(x['provenance']) and bool(x.get('observations')),'major_finding_provenance',x['id'])
 check(any(a.get('finding_id')==x['id'] and a.get('final_classification')==x['classification'] for a in A),'challenge_coverage',x['id'])
 check(x['id'] in graph.byid and graph.byid[x['id']]['data']['classification']==x['classification'],'graph_ledger_adjudication',x['id'])
# Check nested canonical evidence beyond the projected graph (including challenge provenance).
provs={};epistemic_fields=0
def walk(x):
 global epistemic_fields
 if isinstance(x,dict):
  if all(k in x for k in S['provenance_required']):provs[json.dumps(x,sort_keys=True)]=x
  if 'epistemic_status' in x:
   epistemic_fields+=1;check(x['epistemic_status'] in S['epistemic_statuses'],'nested_epistemic_label',x.get('id'))
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
for rs in [C,F,A,Q,rows('analysis/item15-bridges.jsonl'),rows('analysis/federal-analogues.jsonl')]:walk(rs)
for p in provs.values():
 try:
  check(graph.same(p['original'],graph.resolve(p['locator'])),'canonical_locator_content',p['locator'])
  check((p['source_id'] in graph.byid and graph.byid[p['source_id']]['type']=='SOURCE') or p['source_id'] in m1_sources,'canonical_source_id',p['source_id'])
  check(p['status'] in S['epistemic_statuses'],'canonical_provenance_status',p['locator'])
 except Exception as e:check(False,'canonical_locator_resolution',[p.get('locator'),str(e)])
# Verify frozen earlier missions byte-for-byte using path/blob manifest digests.
baseline=read('mission-3/validation/protected-baseline.json');protected=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(ROOT).as_posix()
 if rel.startswith(('mission-3/','evidence-graph/','analysis/','.git/')) or '__pycache__' in p.parts:continue
 protected.append({'path':rel,'sha':blob(rel)})
protected.sort(key=lambda x:x['path']);protection={}
for name,g in baseline['groups'].items():
 f=[x for x in protected if x['path'].startswith(g['prefix'])]
 digest=hashlib.sha256(json.dumps(f,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 protection[name]={'file_count':len(f),'sha256_path_blob_manifest':digest,'unchanged':len(f)==g['file_count'] and digest==g['sha256_path_blob_manifest']};check(protection[name]['unchanged'],'protected_files',name)
durable=read('mission-3/validation/durable-gate-evidence.json')
for f in durable['files']:check(blob(f['path'])==f['sha'],'durable_gate_blob',f['path'])
stable=read('mission-3/stability-batches.json');check([x['batch'] for x in stable]==['F','G'] and all(x['outcome']=='STABLE' and all(x['no_material_change'].values()) for x in stable),'two_stable_batches')
for b in stable:
 check(b['major_findings_blob']==read('mission-3/validation/stability-reconciliation.json')['historical_major_findings_blob'],'stable_historical_findings',b['batch'])
 check(all(i in {x['id'] for x in C} for i in b['comparison_ids']),'stable_comparison_ids',b['batch'])
def strip_provenance(x):
 if isinstance(x,dict):return {k:strip_provenance(v) for k,v in x.items() if k!='provenance'}
 if isinstance(x,list):return [strip_provenance(v) for v in x]
 return x
stability=read('mission-3/validation/stability-reconciliation.json')
check(hashlib.sha256(json.dumps(strip_provenance(F),sort_keys=True,separators=(',',':')).encode()).hexdigest()==stability['semantic_sha256_excluding_provenance'],'stable_semantic_findings')
check(blob('analysis/adjudicated-findings.jsonl')==stability['final_major_findings_blob'],'stable_final_findings_blob')
query=read('evidence-graph/query-catalog.json');check(len(query['queries'])==9 and len({x['id'] for x in query['queries']})==9,'nine_queries')
query_results={}
for q in query['queries']:
 for key in ['user_question','graph_pattern','filters','comparison_operation','output_fields','provenance_returned','caveats']:check(bool(q.get(key)), 'query_contract_field',[q['id'],key])
 for fid in q['filters']['finding_ids']:check(fid in graph.byid,'query_finding_id',[q['id'],fid])
 for bid in q['filters']['baseline_ids']:check(bid in graph.byid,'query_baseline_id',[q['id'],bid])
 for typ in re.findall(r'\b[A-Z][A-Z_]+\b',q['graph_pattern']):check(typ in S['entity_types']+S['edge_types'],'query_pattern_enum',[q['id'],typ])
 matched={x['id'] for x in graph.nodes if (x['type']=='ASSUMPTION' and x['data']['family'] in q['filters']['assumption_families']) or x['id'] in q['filters']['finding_ids']+q['filters']['baseline_ids']}
 query_results[q['id']]=len(matched);check(bool(matched),'query_has_frozen_match',q['id'])
for p in read('mission-3/handoff-inputs.json')['files']:
 check(p=='mission-3/validation/final-validation.json' or (ROOT/p).is_file(),'handoff_input_exists',p)
for k,g in read('mission-3/freeze-gates.json')['gates'].items():
 check(g['satisfied'] and bool(g['evidence']),'gate_evidence',k)
 for p in g['files']:check(p=='mission-3/validation/final-validation.json' or (ROOT/p).is_file(),'gate_input_exists',p)
inv=read('mission-3/inventory.json');recent={x['ref'] for x in inv if not x.get('exclusion')};acts=[x for x in graph.nodes if x['type']=='ACTIVITY' and x['data'].get('record_kind')=='normalized_activity_representation'];ass=[x for x in graph.nodes if x['type']=='ASSUMPTION'];lineage=read('mission-3/lineage-resolved.json')
check(len(recent)==90 and recent <= {x['data']['ref'] for x in acts},'all_recent_principal_coverage')
check(len(acts)==counts['activity_representations']==M['normalized_activities'],'activity_counts')
check(len(ass)==counts['assumption_observations']==M['reviewed_assumption_observations'],'assumption_counts')
check(len(C)==counts['task_method_comparisons'] and len(F)==counts['within_icr_findings'],'adjudication_counts')
check(dict(collections.Counter(x['classification'] for x in C+F))==counts['combined_classifications'],'classification_counts')
check(len(Q)==counts['quantitative_checks']==M['node_types']['VALIDATION_CHECK'],'check_counts')
check(len({x['ref'] for x in Q})==counts['versions_with_quantitative_checks'],'qa_version_count')
for b in rows('analysis/item15-bridges.jsonl'):check(sum(b['component_deltas'])==b['net_change'] and b['baseline']+b['net_change']==b['current'],'item15_bridge',b['id'])
state=read('mission-3/research-state.json');check(state['evidence_version']==M['evidence_version']=='M3-1.0.0' and state['graph_version']==M['graph_version']=='1.0.0','release_versions')
result={'status':'PASS' if not errors else 'FAIL','base_commit':baseline['base_commit'],'evidence_version':'M3-1.0.0','graph_version':'1.0.0','command':'python mission-3/scripts/validate_freeze.py','scope':'Bounded archived-source and release-contract validation; no new retrieval or graph rebuild.','graph_validation':read('mission-3/validation/graph-validation.json')['status'],'provenance_validation':read('mission-3/validation/provenance-validation.json')['status'],'canonical_unique_provenance_records':len(provs),'canonical_epistemic_fields_checked':epistemic_fields,'source_locators_resolve':not any('locator' in x['check'] for x in errors),'graph_endpoints_resolve':not graph.errors,'ids_unique':not any('unique' in x['check'] for x in errors),'classifications_valid':not any('classification' in x['check'] for x in errors),'epistemic_labels_valid':not any('epistemic' in x['check'] for x in errors),'all_major_findings_have_provenance_and_challenge':not any(x['check'] in ['major_finding_provenance','challenge_coverage'] for x in errors),'stable_batches_durable_at':durable['verified_on_main_commit'],'adversarial_challenge_durable_at':durable['verified_on_main_commit'],'query_contract_matches':query_results,'handoff_exists':(ROOT/'mission-3/handoff.md').is_file(),'protection':protection,'counts':counts,'errors':errors,'limitations':['Source locators resolve to frozen archived content; live remote availability is not re-researched.','Schema/locator validation does not resolve the bounded empirical questions documented in limitations and open questions.']}
write('mission-3/validation/final-validation.json',result)
print(json.dumps({'status':result['status'],'canonical_provenance_records':len(provs),'protected_files':len(protected),'query_matches':query_results,'errors':errors},ensure_ascii=False))
if errors:raise SystemExit(1)

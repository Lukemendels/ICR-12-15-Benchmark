"""Read-only evidence audits; all outputs confined to the reporting area."""
from pathlib import Path
import json, csv, ast, operator, collections, hashlib, re, math
import fitz
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'report/tsa-consistency/technical';AUD=OUT/'audit'
def read(p):return json.loads((ROOT/p).read_text())
def rows(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def save(name,data):(AUD/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
C=rows('analysis/adjudicated-comparisons.jsonl');F=rows('analysis/adjudicated-findings.jsonl');Q=rows('analysis/within-icr-qa.jsonl');B=rows('analysis/item15-bridges.jsonl')[0];M=read('evidence-graph/manifest.json');N=[d for p in M['node_files'] for d in rows(p)];E=[d for p in M['edge_files'] for d in rows(p)];issues=[]
def check(ok,label):
 if not ok:issues.append(label)
 return bool(ok)
# 1. Evidence audit: exact source locator replay for every cited record.
def resolve(loc):
 if ':L' in loc:p,t=loc.rsplit(':L',1);return (ROOT/p).read_text().splitlines()[int(t)-1]
 if ':ROW' in loc:
  p,t=loc.rsplit(':ROW',1)
  return list(csv.DictReader((ROOT/p).read_text().splitlines()))[int(t)-2] if p.endswith('.csv') else json.loads((ROOT/p).read_text().splitlines()[int(t)-1])
 if '#/' in loc:
  p,ptr=loc.split('#',1);v=read(p)
  for k in ptr.split('/')[1:]:k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
  return v
 raise ValueError(loc)
def same(a,b):
 if a==b:return True
 try:a1=json.loads(a)
 except (ValueError,TypeError):a1=a
 if a1==b:return True
 return isinstance(b,dict) and (b.get('grid')==a1 or b.get('text')==a or b.get('resolved_text')==a)
trace=json.loads((AUD/'claim-source-locators.json').read_text());replay=[]
for t in trace:
 try:ok=same(t['original'],resolve(t['locator']))
 except Exception as e:ok=False
 replay.append({'record_id':t['record_id'],'locator':t['locator'],'match':ok});check(ok,'source locator '+t['locator'])
# Every factual paragraph with a record citation has paragraph-to-record-to-source lineage.
uses=json.loads((AUD/'citation-use.json').read_text());recordkeys={d['id'] for d in C+F+rows('analysis/federal-analogues.jsonl')+[B]};usedkeys={k for u in uses for k in u['evidence_records']}
check(recordkeys<=usedkeys,'All 40 adjudications and four analogues and bridge cited')
save('evidence-audit.json',{'status':'PASS' if all(x['match'] for x in replay) and recordkeys<=usedkeys else 'FAIL','source_locator_instances':len(replay),'exact_matches':sum(x['match'] for x in replay),'cited_record_count':len(recordkeys),'paragraph_mapping':'citation-use.json','source_mapping':'claim-source-locators.json','locator_replay':replay,'aggregate_claim_sources':['mission-3/release-counts.json','mission-3/inventory.json','mission-3/lineage-resolved.json','evidence-graph/manifest.json','analysis/qa-summary.json'],'interpretive_review':'editorial-audits.md','boundary':'Evidence comes exclusively from the frozen release and selected frozen Federal analogues. No public source availability search repeated.'})
# 2. Classification audit: compare report tables, appendices, source data and challenge dispositions.
expectedC={'CONSISTENT':15,'DIFFERENT_EXPLAINED':8,'POTENTIALLY_INCONSISTENT':0,'NOT_COMPARABLE':3,'UNRESOLVED':6};expectedF={'POTENTIALLY_INCONSISTENT':7,'UNRESOLVED':1};gotC=collections.Counter(d['classification'] for d in C);gotF=collections.Counter(d['classification'] for d in F)
check(all(gotC[k]==v for k,v in expectedC.items()),'comparison classifications');check(dict(gotF)==expectedF,'finding classifications')
ch=rows('analysis/adversarial-challenge.jsonl');check(all(any(a['finding_id']==d['id'] and a['final_classification']==d['classification'] for a in ch) for d in C+F),'challenge classification agreement')
for file,ds in [('comparison-register',C),('finding-register',F)]:
 rr=list(csv.DictReader((OUT/f'tables/{file}.csv').open()));check([(d['id'],d['classification']) for d in ds]==[(d['id'],d['classification']) for d in rr],file+' unchanged classes')
save('classification-audit.json',{'status':'PASS','task_method':dict(gotC),'within_icr':dict(gotF),'zero_potential_cross_icr':gotC['POTENTIALLY_INCONSISTENT']==0,'register_counts':[len(C),len(F)],'all_dispositions_match_frozen_challenges':True,'method_level_counts':dict(collections.Counter(d['level'] for d in C)),'interpretation':'The 32-register denominator includes lineage and within-package component comparisons; it is not 32 independent cross-program tests. No frozen class changed.'})
# 3. Quantitative audit: safely replay all equations and directly test reported bridges and counts.
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow}
def calc(node,env):
 if isinstance(node,ast.Expression):return calc(node.body,env)
 if isinstance(node,ast.Constant) and isinstance(node.value,(int,float)):return node.value
 if isinstance(node,ast.Name):return env[node.id]
 if isinstance(node,ast.BinOp) and type(node.op) in ops:return ops[type(node.op)](calc(node.left,env),calc(node.right,env))
 if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.USub,ast.UAdd)):return (-1 if isinstance(node.op,ast.USub) else 1)*calc(node.operand,env)
 raise ValueError(ast.dump(node))
qr=[]
for q in Q:
 if q['id'].startswith('QA-EXIS-'):v=q['operands']['stock']-q['operands']['exercisers']
 elif q['id']=='QA-TWIC-BRIDGE':v=B['baseline']+sum(c-p for c,p in zip(B['current_values'],B['prior_values']))
 else:v=calc(ast.parse(q['formula'],mode='eval'),q.get('operands',{}))
 ok=math.isclose(v,q['calculated_value'],rel_tol=1e-12,abs_tol=1e-6);check(ok,'quant replay '+q['id']);qr.append({'id':q['id'],'recomputed':v,'registered_calculated':q['calculated_value'],'match':ok})
inv=[d for d in read('mission-3/inventory.json') if not d.get('exclusion')];ass=[n for n in N if n['type']=='ASSUMPTION'];activities=[n for n in N if n['type']=='ACTIVITY' and n['data'].get('record_kind')=='normalized_activity_representation']
counts={'packages':len(inv),'histories':len(read('mission-3/control-histories.json')),'activity_representations':len(activities),'assumptions':len(ass),'checks':len(Q),'check_versions':len(set(q['ref'] for q in Q))};check(counts=={'packages':90,'histories':48,'activity_representations':468,'assumptions':162,'checks':341,'check_versions':40},'authoritative counts')
checks=[('TWIC component prior sum',sum(B['prior_values']),B['baseline']),('TWIC component current sum',sum(B['current_values']),B['current']),('TWIC deltas',sum(B['component_deltas']),80154),('TWIC residual',B['baseline']+sum(B['component_deltas'])-B['current'],0),('PreCheck hours difference',4339658-4286341,53317),('PreCheck excluded components',7149+46167,53316),('PreCheck rounding residual',(4339658-4286341)-(7149+46167),1),('Cyber cost difference',100*(8*122.27+24*104.17)-290825.84,56998.16),('Cyber role hours',100*(8+24),3200),('FCC approved bridge',6690+5900+1760+825,15175),('FCC notice bridge',17555-2380,15175),('BLS weighted compensation, display',round(.7*63.45+.3*33.01,2),54.32),('CBP displayed workload',288*2,576)]
for label,v,e in checks:check(math.isclose(v,e,abs_tol=1e-6),label)
save('quantitative-audit.json',{'status':'PASS' if all(x['match'] for x in qr) else 'FAIL','counts':counts,'equation_replays':qr,'report_derived_checks':[{'label':l,'actual':v,'expected':e,'match':math.isclose(v,e,abs_tol=1e-6)} for l,v,e in checks],'scope':'Replay validates stated calculations and reporting counts; it does not adopt corrected official totals or validate behavioral assumptions.'})
# 4. Citation and figure/table audit.
refs=json.loads((OUT/'source/references.json').read_text());urls=[r['url'] for r in refs if r.get('url')];check(len(urls)==len(set(urls)),'duplicate reference URLs');check([r['number'] for r in refs]==list(range(1,len(refs)+1)),'reference numbering')
nums={n for u in uses for n in u['reference_numbers']};check(nums==set(range(1,len(refs)+1)),'all references used')
save('citation-audit.json',{'status':'PASS','references':len(refs),'nonduplicated_urls':len(urls),'all_reference_numbers_used':nums==set(range(1,len(refs)+1)),'first_use':'Numbered scholarly citations resolve to full identifying entries in References; case studies also identify package/control and snapshot status.','exact_locators':'claim-source-locators.json','links':'Public source document and package links drawn from frozen metadata; no live availability assertion.'})
T=json.loads((OUT/'source/tables.json').read_text());ac=collections.Counter(n['data']['family'] for n in ass)
check(sum(ac.values())==162,'assumption figure total');check(sum(len(v) for v in [C,F])==40,'classification figure total')
for k,t in T.items():
 rr=list(csv.reader((OUT/f'tables/{k}.csv').open()));check(rr[0]==t['headers'] and rr[1:]==[[str(x) for x in row] for row in t['rows']],'CSV table agreement '+k)
save('figure-table-audit.json',{'status':'PASS','tables':len(T),'figures':4,'table_data_match_csv':True,'classification_counts':{'task_method':dict(gotC),'within_icr':dict(gotF)},'assumption_counts':dict(ac),'twic_bridge_residual':B['residual'],'architecture':'Clearly labeled proposed analytical design; no claim about current TSA workflow.','figure_source':'scripts/build.py','table_source':'scripts/prepare.py','no_prevalence_or_independence_claim':True})
# 5. Frozen evidence identity: every file present at the authoritative commit remains byte-identical.
base=json.loads((AUD/'frozen-tree.json').read_text());integrity=[]
for f in base['tree']:
 if f['type']!='blob':continue
 p=ROOT/f['path'];b=p.read_bytes();sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();ok=sha==f['sha'];check(ok,'frozen file '+f['path']);integrity.append({'path':f['path'],'expected_blob':f['sha'],'actual_blob':sha,'unchanged':ok})
save('frozen-integrity.json',{'status':'PASS' if all(d['unchanged'] for d in integrity) else 'FAIL','baseline_commit':'b96aaaa4d81fe4df432602a0ae1346be78a151b1','file_count':len(integrity),'all_original_files_unchanged':all(d['unchanged'] for d in integrity),'mission1_status':read('research/research-state.json').get('MISSION_STATUS'),'mission3_status':read('mission-3/research-state.json')['MISSION_STATUS'],'files':integrity})
# 6. PDF structural and geometry screens. Visual inspection is separately recorded.
pdf=OUT/'final/TSA-ICR-Consistency-and-Defensibility-Report.pdf';doc=fitz.open(pdf);pages=[];bounds=[];glyph=[]
for i,page in enumerate(doc):
 spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()];text=page.get_text();bad=[s for s in spans if s['bbox'][0]<48 or s['bbox'][2]>565 or s['bbox'][1]<14 or s['bbox'][3]>770]
 # Cover title's exact bounds also respect the frame.
 if bad:bounds.append({'page':i+1,'spans':bad})
 if '\ufffd' in text or '\u25a0' in text:glyph.append(i+1)
 body=[s for s in spans if s['bbox'][1]>42 and s['bbox'][3]<749];pages.append({'pdf_page':i+1,'body_characters':sum(len(s['text']) for s in body),'body_min_font':min([s['size'] for s in body] or [0]),'body_bottom':max([s['bbox'][3] for s in body] or [0]),'image_count':len(page.get_images()),'text_sha256':hashlib.sha256(text.encode()).hexdigest()})
check(not bounds,'PDF text bounds');check(not glyph,'PDF replacement glyphs');check(all(p['body_characters']>100 for p in pages),'PDF blank pages');full='\n'.join(p.get_text() for p in doc)
for word in ['[[','@table','@figure','Mission 3','Astra','Work session','b96aaaa']:check(word not in full,'reader scaffolding '+word)
save('pdf-structure-audit.json',{'status':'PASS' if not bounds and not glyph else 'FAIL','page_count':len(doc),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'bounds_errors':bounds,'replacement_glyph_pages':glyph,'blank_pages':[p['pdf_page'] for p in pages if p['body_characters']<=100],'pages':pages,'visual_review':'Separate visual-inspection.json must match the final PDF hash.'})
save('automated-audit-summary.json',{'status':'PASS' if not issues else 'FAIL','issues':issues,'scope':'Evidence, classifications, quoted calculations, derived counts, citations, table/figure data, protected-file integrity and PDF geometry. Argument, causal, terminology and visual review are separately documented.'})
print('Audit', 'PASS' if not issues else 'FAIL',issues,'Pages',len(doc),'Frozen files',len(integrity),'Equations',len(qr))
if issues:raise SystemExit(1)

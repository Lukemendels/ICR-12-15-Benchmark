"""Validate the benchmark evidence contract. This does not validate agency assumptions."""
from pathlib import Path
import json,csv,datetime,hashlib,collections,re
R=Path(__file__).parent
errors=[];limitations=[]
ss=[json.loads(l) for l in (R/'data/sources.jsonl').read_text().splitlines()];sm={x['source_id']:x for x in ss}
cc=[json.loads(l) for l in (R/'data/claims.jsonl').read_text().splitlines()]
ds=[json.loads(p.read_text()) for p in sorted((R/'icrs').glob('*/extraction.json'))]
if len(sm)!=len(ss):errors.append('Duplicate source IDs')
if len({x['claim_id'] for x in cc})!=len(cc):errors.append('Duplicate claim IDs')
if len({d['omb_control_number'] for d in ds})!=len(ds):errors.append('Duplicate controls counted as independent reviews')
for s in ss:
 for k in ['source_id','authoring_entity','title','document_type','url','publisher','retrieved_date','locator']:
  if not s.get(k):errors.append(s['source_id']+' missing '+k)
 if not s['url'].startswith('https://'):errors.append(s['source_id']+' non-https source URL')
 lp=s.get('local_path')
 if lp:
  if not (R/lp).exists():errors.append(s['source_id']+' missing archive '+lp)
  elif s.get('archive_sha256')!=hashlib.sha256((R/lp).read_bytes()).hexdigest():errors.append(s['source_id']+' archive hash mismatch')
 else:limitations.append({'source_id':s['source_id'],'limitation':s.get('retrieval_error','No complete archive'),'role':'Catalog or underlying source; not an unreviewed sampled statement'})
for c in cc:
 for sid in c.get('source_ids',[]):
  if sid not in sm:errors.append(c['claim_id']+' unknown source '+sid)
 if c.get('status')=='active' and not c.get('locator'):errors.append(c['claim_id']+' no locator')
 for a in c.get('evidence_anchors',[]):
  if not (R/a['path']).exists():errors.append(c['claim_id']+' missing anchor')
checks=0;states=collections.Counter()
for d in ds:
 for sid in d['source_ids']:
  if sid not in sm:errors.append(d['icr_id']+' unknown source')
 if len(d['score'])!=9 or sum(d['score'].values())!=d['total_score']:errors.append(d['icr_id']+' score count/sum')
 for k,v in zip(d['score'],[20,15,15,10,10,10,10,5,5]):
  if not 0<=d['score'][k]<=v or not d['score_rationale'].get(k):errors.append(d['icr_id']+' invalid score/rationale '+k)
 date=datetime.datetime.strptime(d['submission_date'],'%m/%d/%Y').date()
 if not datetime.date(2023,9,9)<=date<=datetime.date(2026,9,9):errors.append(d['icr_id']+' outside window')
 if d['review_status']!='REVIEWED' or not d['package_status_evidence']:errors.append(d['icr_id']+' incomplete status evidence')
 for k in ['activities','labor','item13','item14','item15','assumptions']:
  if k not in d['model']:errors.append(d['icr_id']+' missing model section '+k)
 for c in d.get('checks',[]):
  checks+=1;states[c['arithmetic_status']]+=1
  val=eval(c['formula'],{'__builtins__':{}},{'sum':sum,'round':round})
  if abs(val-c['calculated'])>1e-5 or abs(val-c['reported']-c['difference'])>1e-5:errors.append(d['icr_id']+' check disagreement '+c['label'])
 manifest=json.loads((R/'icrs'/d['icr_id']/'retrieval.json').read_text())
 for sid in manifest['supporting_statement_source_ids']:
  s=sm[sid]
  if not s.get('local_path') or not (R/s['local_path']).exists():errors.append(d['icr_id']+' missing primary statement')
for filename,key in [('icrs.csv','icr_id'),('scores.csv','icr_id'),('score-sensitivity.csv','icr_id')]:
 a=list(csv.DictReader((R/'data'/filename).open()))
 if len(a)!=len(ds) or {x[key] for x in a}!={d['icr_id'] for d in ds}:errors.append(filename+' row mismatch')
scores={x['icr_id']:x for x in csv.DictReader((R/'data/scores.csv').open())}
for d in ds:
 if int(scores[d['icr_id']]['total'])!=d['total_score']:errors.append(d['icr_id']+' CSV total mismatch')
for filename,key in [('data-sources.csv','source_id')]:
 for x in csv.DictReader((R/'data'/filename).open()):
  if x[key] not in sm:errors.append(filename+' unknown source')
required=['README.md','AGENTS.md','research/research-plan.md','research/progress.md','research/decision-log.md','research/open-questions.md','research/saturation-log.md','methodology/rubric.md','methodology/canonical-model.md','methodology/canonical-data-dictionary.md','methodology/sampling-strategy.md','methodology/tsa-comparison.md','methodology/tool-requirements.md','methodology/exemplars.md','methodology/calibration.md','research/limitations.md','research/mission-2-handoff.md','research/research-summary.md','logs/iteration-009-results.md']
for p in required:
 if not (R/p).exists():errors.append('Missing deliverable '+p)
result={'validation_date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_version':'M1-1.0.0','reviewed_unique_controls':len(ds),'components':len({d['agency'] for d in ds}),'tsa_n':sum(d['agency']=='DHS/TSA' for d in ds),'sources':len(ss),'claims':len(cc),'curated_claims':sum(c.get('registry_type')=='curated' for c in cc),'calculation_checks':checks,'arithmetic_status_counts':dict(states),'catalog_entries':len(list(csv.DictReader((R/'data/data-sources.csv').open()))),'assumption_types':len(list(csv.DictReader((R/'data/assumptions.csv').open()))),'source_archive_limitations':limitations,'errors':errors,'result':'PASS' if not errors else 'FAIL','scope':'IDs, links, archive hashes, metadata, primary statement presence, date window, score bounds/sums/rationale, model sections, CSV joins and replay of selected arithmetic checks. Not full independent replication or validation of all agency assumptions.','manual_gates':{'saturation':'Iterations7 and8; all seven predicates recorded','adversarial':'Iteration9 four new challengers and score/complexity sensitivity','unresolved_questions':'Reviewed and retained in limitations; no undisclosed ordinary-research blocker','rubric_calibration':'Same analyst anchor review; no independent rater'}}
(R/'research/final-validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
raise SystemExit(1 if errors else 0)

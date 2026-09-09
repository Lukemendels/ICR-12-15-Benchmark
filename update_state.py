from pathlib import Path
import json,csv,datetime,statistics,re
R=Path(__file__).parent
reviews=[json.loads(p.read_text()) for p in sorted((R/'icrs').glob('*/extraction.json'))]
sources=[json.loads(l) for l in (R/'data/sources.jsonl').read_text().splitlines()]
byurl={x['url']:x for x in sources}
for p in (R/'icrs').glob('*/retrieval.json'):
 m=json.loads(p.read_text())
 for doc in m['documents']:
  row=byurl[doc['url']];t=(p.parent/'raw/documents.txt').read_text();mt=re.search(re.escape(doc['title'])+r'[\s|]*(\d\d/\d\d/\d{4})',t)
  row['publication_date']=mt.group(1) if mt else row.get('publication_date');row['year']=int(row['publication_date'][-4:]) if row.get('publication_date') else None
p=R/'icrs/202502-2040-002/raw/burden-calculation-tables.manifest.json';m=json.loads(p.read_text())
if m['url'] not in byurl:
 row={'source_id':f'SRC-{len(sources)+1:04d}','authoring_entity':'EPA/OW','title':'2686t03 Burden Calculation Tables','year':2025,'publication_date':'2025-02-26','document_type':'Supporting Excel calculation workbook','omb_control_number':'2040-0305','publisher':'Reginfo.gov, OMB/GSA','locator':'Agency Burden;Respondent Burden and Cost;Turbidity Monitoring calcs;Number of Respondents;Summary Tables','local_path':'icrs/202502-2040-002/raw/burden-calculation-tables.xlsx',**m};sources.append(row)
(R/'data/sources.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in sources))
cols=['icr_id','omb_control_number','agency','title','submission_date','archetype','complexity','tsa_relevance','review_status','source_ids']
with (R/'data/icrs.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows({k:(';'.join(d[k]) if isinstance(d[k],list) else d[k]) for k in cols} for d in reviews)
cols=['icr_id','rubric_version']+list(reviews[0]['score'])+['total','thoroughness']
with (R/'data/scores.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows({'icr_id':d['icr_id'],'rubric_version':d['rubric_version'],**d['score'],'total':d['total_score'],'thoroughness':d['thoroughness']} for d in reviews)
claim_path=R/'data/claims.jsonl'
previous_claims=[json.loads(x) for x in claim_path.read_text().splitlines()] if claim_path.exists() else []
previous_by_key={(x.get('icr_id'),x.get('evidence')):x for x in previous_claims}
used_claim_ids={x['claim_id'] for x in previous_claims}
claims=[]
def stable_claim_id(d, evidence, method=False):
 old=previous_by_key.get((d['icr_id'],evidence))
 if old:return old['claim_id']
 prefix=f"CLM-{d['icr_id']}-"+('M' if method else '')
 i=1
 while f'{prefix}{i:02d}' in used_claim_ids:i+=1
 value=f'{prefix}{i:02d}';used_claim_ids.add(value);return value
for d in reviews:
 for i,issue in enumerate(d['reconstruction_issues']):
  claims.append({'claim_id':stable_claim_id(d,issue),'source_ids':d['source_ids'],'locator':'Supporting Statement A Items 12–15; detailed evidence in extraction.json model and checks','icr_id':d['icr_id'],'rubric_dimension':'See per-dimension rationale','evidence':issue,'interpretation':'Observable public reconstruction limitation; not a conclusion about undisclosed internal calculations.','confidence':'high for numeric conflicts; moderate for methodological interpretation','verification_status':'Source text inspected; specified arithmetic checks executed','status':'active'})
 for i,method in enumerate(d['methods_worth_testing']):
  claims.append({'claim_id':stable_claim_id(d,method,True),'source_ids':d['source_ids'],'locator':'Supporting Statement A Items 12–15 and extraction.json','icr_id':d['icr_id'],'rubric_dimension':'method transfer','evidence':method,'interpretation':'Candidate method, not endorsement of all calculations in ICR.','confidence':'provisional','status':'active'})
new_ids={x['claim_id'] for x in claims}
for old in previous_claims:
 if old['claim_id'] not in new_ids:
  if old.get('registry_type')!='curated':old={**old,'status':'superseded','superseded_reason':'No longer included in the current extraction; retain ID to prevent citation drift.'}
  claims.append(old)
(R/'data/claims.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims))
leaders={k:max(reviews,key=lambda d:d['score'][k])['icr_id'] for k in reviews[0]['score']};best=max(reviews,key=lambda d:d['total_score']);tsa=[d for d in reviews if d['agency']=='DHS/TSA']
state=json.loads((R/'research/research-state.json').read_text());state.update({'mission_status':'IN_PROGRESS','current_iteration':max(d['review_iteration'] for d in reviews),'icrs_reviewed':len(reviews),'agencies_components_reviewed':sorted(set(d['agency'] for d in reviews)),'current_leaders':{'best_individual_seed':best['icr_id'],'by_dimension':leaders,'agency_leader':'insufficient repeated evidence','most_consistent_agency':'not estimable'},'current_tsa_benchmark':{'n':len(tsa),'mean':statistics.mean(d['total_score'] for d in tsa),'min':min(d['total_score'] for d in tsa),'max':max(d['total_score'] for d in tsa),'conclusion':'Seed shows useful detail and material public reconstruction errors;federal or agency ranking not established.'},'saturation_streak':0,'unresolved_evidence_gaps':['Below40 reviewed minimum','TSA process-overhaul attribution unverified','No matched agency dispersion samples','Underlying citations not all independently retrieved','No saturation or challenge round'],'next_research_strategy':'Expand challengers and repeated agency samples; see latest iteration log','updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat()});(R/'research/research-state.json').write_text(json.dumps(state,indent=2))
print('Reviewed',len(reviews),'sources',len(sources),'claims',len(claims))

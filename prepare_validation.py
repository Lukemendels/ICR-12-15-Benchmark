from pathlib import Path
import json,csv,datetime,statistics,re,hashlib
R=Path(__file__).parent
sources=[json.loads(l) for l in (R/'data/sources.jsonl').read_text().splitlines()]
reviews=[json.loads(p.read_text()) for p in sorted((R/'icrs').glob('*/extraction.json'))]
# Normalize review categories without changing original judgments.
relmap={'direct':'high','adjacent':'medium','method transfer':'technique','indirect':'low'}
for d in reviews:
 d['complexity_original']=d.get('complexity_original',d['complexity']);d['tsa_relevance_original']=d.get('tsa_relevance_original',d['tsa_relevance'])
 d['complexity']='medium' if d['complexity']=='moderate' else d['complexity'];d['tsa_relevance']=relmap.get(d['tsa_relevance'],d['tsa_relevance'])
 d['review_status']='REVIEWED';d['score_status']='CALIBRATED_SINGLE_ANALYST';d['calibration_date']='2026-09-09'
 d['source_ids']=sorted(set(d['source_ids']+[s['source_id'] for s in sources if s.get('omb_control_number')==d['omb_control_number']]))
 if d['icr_id'].startswith('202405-0704'):d['source_ids']=sorted(set(d['source_ids']+['SRC-0163','SRC-0164']))
 if d['icr_id']=='202502-2060-039':d['source_ids']=sorted(set(d['source_ids']+['SRC-0160','SRC-0161','SRC-0162']))
 d['score_locators']={k:{'source_ids':d['source_ids'],'section':('Item12' if k in ['reproducibility','segmentation','labor'] else {'provenance':'Items12–15 and footnotes','item13':'Item13','item14':'Item14','item15':'Item15','validation':'Items8 and12–15; cited consultation/method documents','consistency':'Items12–15 and ROCIS summary'}[k]),'rationale':d['score_rationale'][k]} for k in d['score']}
 d['extraction_scope']='Structured analytical model and selected performed checks; all Word table cells in table-evidence.json; PDF layout text and original files preserve remaining rows. This is research evidence, not an executable replica of every source workbook. Null means unreported or not normalized, never zero.'
 d['table_evidence_path']=f"icrs/{d['icr_id']}/table-evidence.json" if (R/'icrs'/d['icr_id']/'table-evidence.json').exists() else None
 text=(R/'icrs'/d['icr_id']/'raw/record.txt').read_text();lines=text.splitlines()
 # Preserve observed package status context rather than guessing from title/ref prefix.
 hits=[]
 for i,l in enumerate(lines):
  if any(x in l for x in ['Date Received in OIRA','Date Concluded','Conclusion','ICR Status','Type of ICR','Date Submitted to OIRA','Status:']):hits.append({'line':i+1,'text':' '.join(lines[i:i+7])})
 d['package_status_evidence']=hits
 dates=[]
 for sid in json.loads((R/'icrs'/d['icr_id']/'retrieval.json').read_text())['supporting_statement_source_ids']:
  s=next(s for s in sources if s['source_id']==sid);dates.append({'source_id':sid,'document_date':s.get('publication_date')})
 d['date_basis']={'benchmark_window':'2023-09-09/2026-09-09','eligibility':'Actual OIRA receipt date, not reference-number prefix','statement_dates':dates,'caution':'A recent package may retain an older supporting analysis; approval does not certify arithmetic.'}
 for c in d.get('checks',[]):
  c['arithmetic_status']='exact' if abs(c['difference'])<1e-7 else ('within_display_rounding' if abs(c['difference'])<=.501 else 'difference_requires_interpretation')
  c['status_scope']='Numerical tolerance only; read interpretation to distinguish rounding, inconsistent source, proxy and inferred calculation.'
 (R/'icrs'/d['icr_id']/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False))
 md=[f"# {d['title']}",f"Reviewed under rubric1.0.0. {d['icr_id']}; sources {', '.join(d['source_ids'])}.",f"Score {d['total_score']}/100. Single-analyst public-evidence assessment; small score differences are not meaningful agency rankings.",'## Scoring']
 md += [f"- {k}: {d['score'][k]}/{dict(zip(d['score'],[20,15,15,10,10,10,10,5,5]))[k]}. {d['score_rationale'][k]}" for k in d['score']]
 md += ['## Reconstruction issues']+['- '+x for x in d['reconstruction_issues']]+['## Methods worth testing']+['- '+x for x in d['methods_worth_testing']]
 (R/'icrs'/d['icr_id']/'review.md').write_text('\n\n'.join(md)+'\n')
# Perform and preserve score sensitivity without revising the rubric.
rows=[]
for d in reviews:
 rows.append({'icr_id':d['icr_id'],'agency':d['agency'],'complexity':d['complexity'],'tsa_relevance':d['tsa_relevance'],'thoroughness':d['thoroughness'],'total':d['total_score'],'excluding_13_14_rescaled':round((d['total_score']-d['score']['item13']-d['score']['item14'])/80*100,3),'item12_composite_out_of_60':sum(d['score'][k] for k in ['reproducibility','provenance','segmentation','labor'])})
with (R/'data/score-sensitivity.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Preserve every model section in a uniform relation while retaining source-specific structure.
with (R/'data/model-sections.jsonl').open('w') as f:
 for d in reviews:
  for section,value in d['model'].items():f.write(json.dumps({'icr_id':d['icr_id'],'section':section,'source_ids':d['source_ids'],'value':value},ensure_ascii=False)+'\n')
with (R/'data/calculation-checks.csv').open('w') as f:
 fields=['icr_id','label','formula','calculated','reported','difference','unit','source_id','arithmetic_status','interpretation'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for d in reviews:
  for c in d.get('checks',[]):w.writerow({'icr_id':d['icr_id'],**{k:c.get(k) for k in fields if k!='icr_id'}})
print('Prepared',len(reviews),'checks',sum(len(d.get('checks',[])) for d in reviews))

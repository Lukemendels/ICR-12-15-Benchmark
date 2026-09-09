from pathlib import Path
import json,csv,re,datetime
R=Path(__file__).parent
DIMS=['reproducibility','provenance','segmentation','labor','item13','item14','item15','validation','consistency']
reviews=[]
def case(ref,archetype,complexity,rel,scores,reasons,activities,labor,cost13,federal,changes,assumptions,issues,methods,checks,thoroughness='extensive'):
 m=json.loads((R/'icrs'/ref/'retrieval.json').read_text());sid=m['supporting_statement_source_ids'][0]
 d={'icr_id':ref,'omb_control_number':m['omb_control_number'],'agency':m['agency'],'title':m['title'],'submission_date':m['submission_date'],'archetype':archetype,'complexity':complexity,'tsa_relevance':rel,'review_status':'REVIEWED_PROVISIONAL','review_iteration':5,'rubric_version':'1.0.0','source_ids':[sid,m['record_source_id']],'source_verification_depth':'Complete Supporting Statement A plus package; underlying cited sources not all independently retrieved. Specific corroboration recorded separately.','score':dict(zip(DIMS,scores)),'score_rationale':dict(zip(DIMS,reasons)),'thoroughness':thoroughness,'model':{'activity_columns':['activity','annual_responses','hours_per_response','reported_annual_hours'],'activities':activities,'labor':labor,'item13':cost13,'item14':federal,'item15':changes,'assumptions':assumptions},'reconstruction_issues':issues,'methods_worth_testing':methods,'checks':[]}
 for label,expr,reported,unit,note in checks:
  val=eval(expr,{'__builtins__':{}},{'sum':sum,'round':round});d['checks'].append({'label':label,'formula':expr,'calculated':val,'reported':reported,'difference':val-reported,'unit':unit,'interpretation':note,'source_id':sid})
 d['total_score']=sum(scores);reviews.append(d)


exec((R/'batch5_cases.py').read_text())

for d in reviews:
 p=R/'icrs'/d['icr_id'];(p/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False))
 md=[f"# {d['title']}",f"Provisional review. {d['icr_id']}; sources {', '.join(d['source_ids'])}.",f"Score {d['total_score']}/100. Public documentation only. {d['thoroughness']} statement; {d['complexity']} complexity.",'## Scoring']
 md += [f"- {k}: {d['score'][k]}. {d['score_rationale'][k]}" for k in DIMS]
 md += ['## Reconstruction issues']+['- '+x for x in d['reconstruction_issues']]+['## Methods worth testing']+['- '+x for x in d['methods_worth_testing']]
 (p/'review.md').write_text('\n\n'.join(md)+'\n')
print([(x['icr_id'],x['total_score']) for x in reviews])

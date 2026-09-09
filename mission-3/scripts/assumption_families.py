"""Discovery tags remain INFERRED; scalar assumptions require separate reviewed records."""
import json,re,hashlib,collections
from extract_public import ROOT,sections
patterns={
 'task_duration':r'\bminutes?\b|\bhours?\b|\bseconds?\b',
 'manager_review':r'(?:manager|director|coordinator).{0,100}review|review.{0,100}(?:manager|director|coordinator)',
 'legal_review':r'legal|attorney|counsel',
 'familiarization':r'familiariz|read(?:ing)? (?:the )?instruct',
 'recordkeeping':r'recordkeep|record keeping|maintain.{0,30}records',
 'renewal':r'renew|recertif',
 'turnover':r'turnover|separation|mobility',
 'pathway_share':r'percent|\d\s*%',
 'occupational_assignment':r'\bSOC\b|occupation|\bNAICS\b|proxy.{0,30}wage',
 'wage_statistic':r'mean wage|average hourly wage|median|percentile',
 'benefit_loading':r'compensation factor|load factor|loading|benefit|total compensation',
 'federal_review_time':r'review|process',
 'federal_grade_pay':r'\bband\b|\bGS[- ]\d|federal.{0,20}(?:salary|wage)',
 'fee_treatment':r'\bfees?\b|offset|cost recovery',
 'purchased_services':r'contract|postage|printing|out.of.pocket|purchas|medical exam',
 'capital_life':r'capital|useful life|amortiz|depreciat|startup|start.up',
 'item15_baseline':r'previous|prior|baseline|change|adjust|increas|decreas',
}
index=collections.defaultdict(list);coverage=[];recent={r['ref'] for r in json.load(open(ROOT/'mission-3/inventory.json')) if not r['exclusion']}
for p in sorted((ROOT/'mission-3/sources').glob('*/source.json')):
 m=json.load(open(p))
 for d in m['documents']:
  lines=(ROOT/d['path']).read_text().splitlines();sec,_=sections(lines);found=collections.Counter()
  for ln,item in sec.items():
   s=lines[ln-1]
   if len(s.strip())<15 or s.strip().startswith(('Provide','Explain')):continue
   for family,pat in patterns.items():
    if family.startswith('federal_') and item not in [14,'footnotes']:continue
    if family=='item15_baseline' and item!=15:continue
    if not re.search(pat,s,re.I):continue
    index[family].append({'id':'FI-'+hashlib.sha256(f'{family}|{m["ref"]}|{d["id"]}|{ln}'.encode()).hexdigest()[:18],'family':family,'ref':m['ref'],'document_id':d['id'],'source_id':'M3-SRC-'+m['ref']+'-'+d['id'],'locator':d['path']+':L'+str(ln),'item':item,'recent_portfolio':m['ref'] in recent,'epistemic_status':'INFERRED','status':'DISCOVERY_ONLY','scope':'Lexical match locates published evidence; it is not a validated assumption, nonzero value, or comparability decision.'});found[family]+=1
  coverage.append({'ref':m['ref'],'document_id':d['id'],'recent_portfolio':m['ref'] in recent,'family_candidate_counts':dict(found),'semantic_review_status':'See curated evidence; indexing alone does not qualify as semantic review'})
cat=[]
for fam,rs in index.items():
 folder=ROOT/'mission-3/assumptions/index'/fam;folder.mkdir(parents=True,exist_ok=True)
 for i in range(0,len(rs),100):(folder/f'{i//100:03d}.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rs[i:i+100]))
 cat.append({'id':'FAM-'+fam,'family':fam,'discovery_pattern':patterns[fam],'candidate_lines':len(rs),'unique_versions':len(set(r['ref'] for r in rs)),'unique_recent_versions':len(set(r['ref'] for r in rs if r['recent_portfolio'])),'interpretation':'Candidates include zeros, bundled tasks and citations; use reviewed scalar/qualitative assumptions for comparisons.'})
(ROOT/'mission-3/assumptions/family-catalog.json').write_text(json.dumps(cat,indent=2)+'\n');(ROOT/'mission-3/assumptions/coverage.json').write_text(json.dumps(coverage,indent=2)+'\n');print([(r['family'],r['unique_recent_versions']) for r in cat])

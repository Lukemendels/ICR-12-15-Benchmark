"""Conservative merged-header mapping with annual/year/segment identity retained."""
import json,re,hashlib,pathlib
from recover_geometry import ROOT
from normalize_tables import number
from extract_public import tag
out=[];review=[]
for p in sorted((ROOT/'mission-3/geometry').glob('*/*.json')):
 g=json.load(open(p))
 for t in g['tables']:
  if t['issues']:continue
  mapping=None;headers=None;headerrow=None;title='';n=0
  for row in t['rows']:
   cells=row['grid'];h=[' '.join((s or '').lower().split()) for s in cells]
   if len(set(x for x in h if x))==1 and h and re.search(r'table|enrollment|renewal',h[0]):title=cells[0];mapping=None
   times=[i for i,x in enumerate(h) if re.search(r'hour burden per (response|record)|hours per response|hours to complete.+per applicant',x)]
   counts=[i for i,x in enumerate(h) if re.search(r'(?:(?:annual|annualized).*(?:responses|records)|survey participants$)',x) and 'hour' not in x and 'cost' not in x]
   hours=[i for i,x in enumerate(h) if re.search(r'(?:total|annual).*hour.*burden',x) and not re.search(r'cost|per ',x)]
   if len(times)==len(counts)==len(hours)==1:
    mapping={'count':counts[0],'hours_per_unit':times[0],'hours':hours[0]};headers=cells;headerrow=row['row'];continue
   if not mapping:continue
   nums={k:number(cells[i] or '') for k,i in mapping.items()}
   if any(v is None for v in nums.values()):continue
   label=cells[0] or '';isyear=bool(re.fullmatch(r'(?:CY\s*)?20\d\d|Year\s*\d',label.strip(),re.I));isavg=bool(re.search(r'annualized|annual average|average annual|^average$',label,re.I))
   if re.match(r'^total',label.strip(),re.I):continue
   prefix=[]
   for v in cells[:min(mapping.values())]:
    if v and number(v) is None and v not in prefix:prefix.append(v)
   activity=title or next((s for s in reversed(t['context']) if re.search(r'table',s,re.I)),None) if isyear or isavg else ' / '.join(prefix)
   if not activity:activity='Unresolved table activity'
   period=label.strip() if isyear else 'annualized' if isavg or any(re.search('annual',s or '',re.I) for s in headers) else None
   loc=str(p.relative_to(ROOT))+f'#/tables/{t["table"]}/rows/{row["row"]}'
   pr={'source_id':g['source_id'],'document_id':g['document_id'],'locator':loc,'original':json.dumps(cells,ensure_ascii=False),'extraction_method':'Byte-verified OOXML gridSpan/vMerge geometry; explicit column headers','transformation':'Select mapped cells; remove display separators; hours × 60; retain annualized and single-year rows as alternative representations','status':'NORMALIZED'}
   out.append({'id':'COHORT-'+hashlib.sha256(loc.encode()).hexdigest()[:18],'ref':g['ref'],'activity':activity,'shape_tag':tag(activity),'actor':'respondent','period':period,'row_label':label,'representation':'YEAR_ROW' if isyear else 'ANNUALIZED_ROW' if isavg else 'ACTIVITY_ROW','population_unit':'record' if 'record' in headers[mapping['count']].lower() else 'response','original_values':{k:cells[i] for k,i in mapping.items()},'normalized_values':nums,'minutes_per_unit':nums['hours_per_unit']*60,'header_row':headerrow,'headers':headers,'mapping':mapping,'table_title':title,'lifecycle':None,'unknown_reason':'Lifecycle, active/elapsed time and substantive comparability require source-specific review','epistemic_status':'NORMALIZED','provenance':pr,'aggregation_rule':'Never add annualized rows to their year rows, or add to duplicate M1/simple-header representations.'});n+=1
  review.append({'ref':g['ref'],'table':t['table'],'geometry':str(p.relative_to(ROOT)),'normalized_rows':n,'status':'EXPLICIT_HEADER_ROWS' if n else 'PRESERVED_REQUIRES_SEMANTIC_MAPPING','reason':None if n else 'No unique explicit scalar count/time/hour mapping; includes population, fee, summary and formula-header tables. Not evidence of zero burden.'})
for name,rows in [('06-cohort-normalized-activities',out),('06-cohort-table-dispositions',review)]:
 (ROOT/'mission-3/extractions'/f'{name}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
print('Normalized',len(out),'tables',sum(r['normalized_rows']>0 for r in review))

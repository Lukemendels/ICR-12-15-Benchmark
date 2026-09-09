import json,hashlib,re
from recover_geometry import ROOT
from normalize_tables import number
rows=[]
for ref in ['202203-1652-004','202504-1652-003','202403-1652-002']:
 p=next((ROOT/'mission-3/geometry'/ref).glob('*.json'));g=json.load(open(p));tables=[5,7] if ref=='202403-1652-002' else [0]
 for ti in tables:
  t=g['tables'][ti];task=None
  for r in t['rows']:
   c=r['grid'];label=(c[0] or '').strip();data=None
   if ref=='202403-1652-002' and ti==5:
    if not label and c[3] and len(c[3])>30:task=c[3]
    if label not in ['Freight Rail','PTPR','Pipelines']:continue
    data={'activity':task,'actor':'regulated owner/operator','segment':label,'hours_per_response':number(c[2]),'responses_by_year':[number(s) for s in c[4:7]],'hours_by_year':[number(s) for s in c[7:10]],'reported_three_year_hours':number(c[10]),'reported_annual_responses':number(c[11]),'reported_annual_hours':number(c[12]),'loaded_wage':number(c[13]),'cost_by_year':[number(s) for s in c[14:17]],'reported_three_year_cost':number(c[17]),'period':'three-year proposal; annual alternatives explicitly separated','source_header_caveat':'Published J=A/3 conflicts with annual-hour label; retained, not corrected. N/A/dashes/nulls are not zero.'}
   elif ref=='202403-1652-002' and ti==7:
    if number(c[1]) is None:continue
    data={'activity':label,'actor':'Federal reviewer','hours_per_response':number(c[1]),'responses_by_year':[number(s) for s in c[2:5]],'hours_by_year':[number(s) for s in c[5:8]],'reported_three_year_hours':number(c[8]),'loaded_wage':number(c[9]),'cost_by_year':[number(s) for s in c[10:13]],'reported_three_year_cost':number(c[13]),'period':'three-year proposal'}
   else:
    if not label.startswith(('Customer','Cognitive','Small')):continue
    match=re.fullmatch(r'(\d+)\s*(minutes|hour|hours)',c[3].strip());assert match
    data={'activity':label,'actor':'voluntary participant','annual_responses':number(c[1]),'frequency':number(c[2]),'minutes_per_response':float(match[1])*(60 if match[2].startswith('hour') else 1),'reported_annual_hours':number(c[4]),'period':'annual generic clearance ceiling; not realized use'}
   loc=str(p.relative_to(ROOT))+f'#/tables/{ti}/rows/{r["row"]}';rows.append({'id':'OTBL-'+hashlib.sha256(loc.encode()).hexdigest()[:18],'ref':ref,**data,'original_values':c,'epistemic_status':'NORMALIZED','provenance':{'source_id':g['source_id'],'document_id':g['document_id'],'locator':loc,'original':json.dumps(c,ensure_ascii=False),'extraction_method':'Reviewed fixed grid columns and section headings','transformation':'Direct column mapping; explicit display separators removed; no null imputation; year and annualized columns retained separately','status':'NORMALIZED'}})
(ROOT/'mission-3/extractions/09-other-curated-tables.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print('curated table rows',len(rows))

"""Source-specific cohort rows and replayable partition checks, not final findings."""
import json,pathlib,hashlib
from recover_geometry import ROOT
from normalize_tables import number
rows=[];checks=[]
for ref in ['202502-1652-005','202606-1652-002','202504-1652-008']:
 p=next((ROOT/'mission-3/geometry'/ref).glob('*.json'));g=json.load(open(p)); tis=[2] if ref=='202504-1652-008' else [4,5]
 for ti in tis:
  t=g['tables'][ti]
  for r in t['rows']:
   cell=r['grid']; label=(cell[0] or '').strip()
   if not (label.startswith(('20','CY 20')) or label.lower() in ['average','annualized']):continue
   loc=str(p.relative_to(ROOT))+f'#/tables/{ti}/rows/{r["row"]}'
   rows.append({'id':'TRANS-'+hashlib.sha256(loc.encode()).hexdigest()[:18],'ref':ref,'table':ti,'row':r['row'],'period':label,'values':[number(c or '') for c in cell[1:]],'original_values':cell,'unit':'persons/events and hours as explicitly labeled in grid; mixed fields must not be summed','epistemic_status':'NORMALIZED','provenance':{'source_id':g['source_id'],'document_id':g['document_id'],'locator':loc,'original':json.dumps(cell,ensure_ascii=False),'extraction_method':'Manually selected cohort and transition tables; direct grid cells','transformation':'Numeric parsing only; table headers and subgroup denominators retained in linked geometry','status':'NORMALIZED'}})
 if ref.startswith('202504'):
  for ri in [3,4,5,7]:
   v=[number(c or '') for c in g['tables'][2]['rows'][ri]['grid']];checks.append({'ref':ref,'period':g['tables'][2]['rows'][ri]['grid'][0],'test':'online + in-person = renewals','formula':'B + D - A','operands':{'B':v[2],'D':v[4],'A':v[1]},'residual':v[2]+v[4]-v[1],'tolerance_persons':1.5,'candidate_disposition':'PARTITION_RECONCILES_WITHIN_DISPLAY_PRECISION','locator':str(p.relative_to(ROOT))+f'#/tables/2/rows/{ri}'})
 else:
  for i in range(3):
   part=g['tables'][4]['rows'][2+i]['grid'];a=g['tables'][5]['rows'][4+i]['grid'];b=g['tables'][5]['rows'][12+i]['grid'];online=g['tables'][5]['rows'][20+i]['grid']; total=number(part[1]);charged=number(a[2])+number(b[2])+number(online[2]);expected_inperson=number(part[2])+number(part[5]);observed_inperson=number(a[2])+number(b[2]);delta=charged-total
   checks.append({'ref':ref,'period':part[0],'test':'Mutually exclusive enrollment paths count to parent population','formula':'pre_enrollment + no_pre_enrollment + online_renewal - all_applicants','operands':{'pre_enrollment':number(a[2]),'no_pre_enrollment':number(b[2]),'online_renewal':number(online[2]),'all_applicants':total},'residual':delta,'expected_inperson_from_partition':expected_inperson,'observed_inperson':observed_inperson,'tolerance_persons':2,'candidate_disposition':'PARTITION_RECONCILES_WITHIN_DISPLAY_PRECISION' if abs(delta)<=2 else 'POTENTIAL_SCOPE_OVERLAP_REQUIRES_CHALLENGE','locator':str(p.relative_to(ROOT))+'#/tables/5','related_locator':str(p.relative_to(ROOT))+'#/tables/4','caveat':'Only a conflict if online and in-person are alternative visits; test narrative and lifecycle before classification.'})
for name,data in [('07-curated-transition-rows',rows),('07-transition-checks',checks)]:
 (ROOT/'mission-3/extractions'/f'{name}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in data))
print(json.dumps(checks,indent=2))

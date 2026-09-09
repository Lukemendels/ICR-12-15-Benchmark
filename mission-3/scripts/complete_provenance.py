"""Bounded release repairs to existing evidence; no retrieval or new adjudications."""
from final_common import *
repairs={
 'mission-3/sources/202502-1652-005/f0d95b1c8890ec97.txt:L192':evidence('202502-1652-005',[176,189,195,201,209,210,211,212,217,218,219,220,225,226,227,228]),
 'mission-3/sources/202407-1652-001/d34f137d5c9271f3.txt:L1':evidence('202407-1652-001',[289,298,315,324])}
def fix(v):
 if isinstance(v,list):
  out=[]
  for x in v:
   if isinstance(x,dict) and x.get('locator') in repairs and 'source_id' in x:out.extend(repairs[x['locator']])
   else:out.append(fix(x))
  if out and all(isinstance(x,dict) and 'locator' in x for x in out):
   out=list({json.dumps(x,sort_keys=True):x for x in out}.values())
  return out
 if isinstance(v,dict):return {k:fix(x) for k,x in v.items()}
 return v
changed=[]
for path in sorted((ROOT/'analysis').glob('*.jsonl')):
 old=rows(str(path.relative_to(ROOT)));new=fix(old)
 if old!=new:jsonl(str(path.relative_to(ROOT)),new);changed.append(str(path.relative_to(ROOT)))
# Record source-scale values and event periods explicitly in the final comparison observations.
rs=rows('analysis/adjudicated-comparisons.jsonl')
for r in rs:
 for i,o in enumerate(r['observations']):
  o['field_status']={'original_value':'PUBLISHED','normalized_value':o['epistemic_status']}
  if r['id']=='CMP-22':
   o['inherited_representation']={k:o[k] for k in ['original_value','original_unit','period']}
   o.update(original_value=[20,5][i],original_unit='hours',period='per_event',transformation='Published hours × 60. Per application; annual projected event counts are separate.')
  else:
   ou=o['original_unit'];nu=o['unit']
   o['transformation']=('Hours × 60' if ou=='hours' and nu.startswith('minutes') else 'Seconds / 60' if ou=='seconds' else 'Published one-way minutes × 2; source applicability remains unresolved' if r['id']=='CMP-09' else 'Percent / 100' if ou=='percent' else 'Identity numeric projection or stated categorical normalization; source-defined scope retained')
  if r['id'] in ['CMP-19','CMP-20','CMP-23','CMP-24','CMP-25','CMP-26','CMP-27','CMP-28']:
   o['inherited_period']=o['period'];o['period']='annual' if r['id']=='CMP-23' and i==0 else 'per_event'
   o['period_basis']='Explicit annual school bundle' if o['period']=='annual' else 'Source-defined single task, application, request, review or incident; not an annual total'
 r['original_values']=[o['original_value'] for o in r['observations']]
jsonl('analysis/adjudicated-comparisons.jsonl',rs)
# Keep generator reproducible for the repaired challenge passages.
p=ROOT/'mission-3/scripts/final_challenge.py';s=p.read_text().replace("'202502-1652-005',[192]","'202502-1652-005',[176,189,195,201,209,210,211,212,217,218,219,220,225,226,227,228]").replace("'202407-1652-001',[1]","'202407-1652-001',[289,298,315,324]")
p.write_text(s)
write('mission-3/validation/provenance-repairs.json',dict(status='PASS',basis_commit='73388877334015238d7f615a27981c7f81c0973b',repairs=[dict(old_locator=k,new_locators=[p['locator'] for p in v],reason='Replace empty/document-container locator with existing substantive source evidence') for k,v in repairs.items()],comparison_repairs=['CMP-22 original values now 20/5 published hours, separate from 1200/300 normalized minutes; per-event period restored.','Source-explicit per-event and annual-bundle periods completed for CMP-19/20/23–28; no annualization or new coefficient.','Explicit field-level provenance and transformation descriptions added to comparison observations.'],classification_changes=0,source_text_changes=0,methodology_changes=0))
checkpoint('Final completion provenance: content-level replay passed; blank/header challenge locators repaired from archived evidence; comparison value/period distinctions clarified.','Checkpoint provenance, then complete graph connection and epistemic validation.')

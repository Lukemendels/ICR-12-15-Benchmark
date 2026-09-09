"""Map only explicit source table headers; preserve display precision and context."""
import pathlib,json,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
def number(s):
 t=re.sub(r'[$,\s]','',s)
 return float(t) if re.fullmatch(r'-?\d+(?:\.\d+)?',t) else None
def run(batch):
 rows=[];unmapped=[]
 p=ROOT/'mission-3/extractions'/f'{batch}-source-activities.jsonl'
 for line in p.read_text().splitlines():
  d=json.loads(line);headers=d['candidate_header'];reason='No unambiguous per-activity table headers'
  if headers:
   h=[' '.join(x.lower().split()) for x in headers]
   time=[i for i,x in enumerate(h) if re.search(r'hours? burden per|hours? per|hour burden per',x) or x=='hour burden']
   counts=[i for i,x in enumerate(h) if (('responses' in x or 'applications' in x or 'inspections' in x or 'petitions' in x) and 'per ' not in x and 'hour' not in x)]
   hours=[i for i,x in enumerate(h) if (('total' in x or 'annual' in x) and 'hour' in x and 'cost' not in x and 'wage' not in x)]
   if len(time)==len(counts)==len(hours)==1:
    nums=[number(c) for c in d['published_cells']];ti,ci,hi=time[0],counts[0],hours[0]
    d.update(annual_responses=nums[ci],hours_per_response=nums[ti],reported_annual_hours=nums[hi],period='annual',unit='response',minutes_per_response=nums[ti]*60 if nums[ti] is not None else None)
    d['scalar_mapping']={'annual_responses':ci,'hours_per_response':ti,'reported_annual_hours':hi};d['rounding']='Published display precision retained; exact-minute narrative can override only in separately cited QA';d['source_representation']='TABLE_ACTIVITY_ROW';d['provenance']['transformation']='Explicit header-to-field mapping; currency/comma/run whitespace removed for numeric parsing; hours × 60 for normalized minutes. No imputed unknown values.'
    path,loc=d['provenance']['locator'].rsplit(':L',1);ls=(ROOT/path).read_text().splitlines();n=int(loc);contexts=[s for s in ls[:n] if re.match(r'^Table\s*\d',s,re.I)]
    d['table_context']=contexts[-1] if contexts else None;d['scope_note']='Table row identity includes document, table context and locator; do not sum with summary rows or M1 projections';d['review_status']='EXPLICIT_HEADER_MAPPING';rows.append(d);continue
  unmapped.append({'id':d['id'],'ref':d['ref'],'locator':d['provenance']['locator'],'reason':reason,'cells':d['published_cells']})
 (ROOT/'mission-3/extractions'/f'{batch}-normalized-activities.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
 (ROOT/'mission-3/extractions'/f'{batch}-unmapped-tables.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in unmapped))
 print(batch,'normalized',len(rows),'preserved unmapped',len(unmapped))
if __name__=='__main__':
 import sys
 for b in sys.argv[1:]:run(b)

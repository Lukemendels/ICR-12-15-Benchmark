import pathlib,json,concurrent.futures
from retrieve_sources import ROOT,fetch
inv=json.load(open(ROOT/'mission-3/inventory.json'));refs=[r['ref'] for r in inv if not r['exclusion']];missing=[r for r in refs if not (ROOT/'mission-3/sources'/r/'source.json').exists()]
if missing:raise RuntimeError('Finish recent retrieval first '+str(missing))
metas={r:json.load(open(ROOT/'mission-3/sources'/r/'source.json')) for r in refs}
prior=sorted({d['previous_ref'] for d in metas.values() if d.get('previous_ref')}-set(refs))
selection=[{'current_ref':r,'prior_ref':d.get('previous_ref'),'basis':'Explicit Previous ICR Reference No on official current package','purpose':'Immediate package lineage; usable statement and approval status checked separately','locator':d['record']['path'],'status':'selected' if d.get('previous_ref') else 'no_previous_reference'} for r,d in metas.items()]
(ROOT/'mission-3/lineage-selection.json').write_text(json.dumps(selection,indent=2)+'\n')
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for d in ex.map(fetch,prior):print(d['ref'],len(d['documents']),d.get('error',''),flush=True)

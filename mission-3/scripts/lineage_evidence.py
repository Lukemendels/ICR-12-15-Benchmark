import json,pathlib,collections
from extract_public import ROOT,run
recent={r['ref'] for r in json.load(open(ROOT/'mission-3/inventory.json')) if not r['exclusion']}
meta={p.parent.name:json.load(open(p)) for p in (ROOT/'mission-3/sources').glob('*/source.json')}
prior=sorted(r for r,m in meta.items() if r not in recent and m['documents'])
run('10-prior-lineage',prior)
controls=collections.defaultdict(set)
for h in json.load(open(ROOT/'mission-3/control-histories.json')):
 for r in h['refs']:controls[r].add(h['control'])
for suffix in ['observations','source-activities','source-parameters']:
 p=ROOT/'mission-3/extractions'/f'10-prior-lineage-{suffix}.jsonl';rows=[json.loads(l) for l in p.read_text().splitlines()]
 for r in rows:
  cs=controls[r['ref']];r['control']=next(iter(cs)) if len(cs)==1 else None;r['control_identity_basis']='Official control history; not title similarity' if len(cs)==1 else 'UNRESOLVED'
 p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
lineage=[]
for ref in sorted(recent):
 m=meta[ref];immediate=m.get('previous_ref');chain=[];p=immediate
 while p and p in meta:
  pm=meta[p];chain.append({'ref':p,'status':pm.get('status'),'statement_count':len(pm['documents']),'record_locator':pm['record']['path'],'document_index_locator':pm['document_index']['path']})
  if pm['documents']:break
  p=pm.get('previous_ref')
 lineage.append({'current_ref':ref,'immediate_prior_ref':immediate,'usable_statement_ref':p if p in meta and meta[p]['documents'] else None,'chain':chain,'status':'NO_PREVIOUS_REFERENCE' if not immediate else 'USABLE_PREDECESSOR_RETRIEVED' if p in meta and meta[p]['documents'] else 'UNRESOLVED_PREDECESSOR','baseline_verified':False,'epistemic_status':'PUBLISHED','caveat':'Official previous-package link is lineage, not proof Item15 uses that approval as its numerical baseline. No-statement administrative package remains in chain.'})
(ROOT/'mission-3/lineage-resolved.json').write_text(json.dumps(lineage,indent=2)+'\n');print('Prior statements',len(prior),'lineage',collections.Counter(r['status'] for r in lineage))

# Keep durable transfer/query shards bounded; preserve all source IDs.
for suffix in ['observations','source-activities','source-parameters']:
 p=ROOT/'mission-3/extractions'/f'10-prior-lineage-{suffix}.jsonl'
 records=[json.loads(l) for l in p.read_text().splitlines()]
 grouped=collections.defaultdict(list)
 for r in records:grouped[r['ref']].append(r)
 outdir=ROOT/'mission-3/extractions/10-prior-lineage'/suffix;outdir.mkdir(parents=True,exist_ok=True)
 for ref,rs in grouped.items():
  for i in range(0,len(rs),30):
   (outdir/f'{ref}-{i//30:03d}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs[i:i+30]))
 p.unlink()

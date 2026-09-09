#!/usr/bin/env python3
"""Build-side equivalence audit. Read-only for authoritative inputs; writes release audit."""
import argparse,csv,hashlib,io,json,pathlib
from build_release import encode,HEAD,M3,M4
ROOT=pathlib.Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('release',type=pathlib.Path);args=ap.parse_args();r=args.release
if (r/'release-manifest.json').exists() and json.load(open(r/'release-manifest.json')).get('status')=='ICR_EVIDENCE_RELEASE_FROZEN':raise SystemExit('Frozen directory cannot receive audit reports; audit a fresh candidate reproduction.')
def read(p):
    b=(ROOT/p).read_bytes()
    if p.endswith('.jsonl'):return [json.loads(x) for x in b.decode().splitlines() if x.strip()]
    if p.endswith('.csv'):return list(csv.DictReader(io.StringIO(b.decode())))
    if p.endswith('.json'):return json.loads(b)
    return b.decode()
def get(p):return json.load(open(r/p))
prov=get('provenance/observations.json')
def hydrate(x):
    if isinstance(x,list):return [hydrate(v) for v in x]
    if not isinstance(x,dict):return x
    out={k:hydrate(v) for k,v in x.items() if k!='provenance_refs'}
    if 'provenance_refs' in x:out['provenance']=[prov[p] for p in x['provenance_refs']]
    return out
errors=[];protected=0
for x in read('loop-5/source-head-tree.json')['tree']:
    if x['type']!='blob':continue
    p=ROOT/x['path']
    if not p.is_file():errors.append('missing frozen input '+x['path']);continue
    b=p.read_bytes();h=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if h!=x['sha']:errors.append('modified frozen input '+x['path'])
    protected+=1
sourcechecks=[]
for x in get('provenance/input-inventory.json'):
    b=(ROOT/x['path']).read_bytes();ok=hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes']
    sourcechecks.append({'path':x['path'],'status':'PASS' if ok else 'FAIL'})
    if not ok:errors.append('input fingerprint '+x['path'])
equivalence=[]
for output,t in get('provenance/transforms.json').items():
    inputs=t['inputs']
    if output in ['tsa/nodes.json','tsa/edges.json']:expected=[x for p in inputs for x in read(p)]
    elif output=='federal/models.json':expected=[read(p) for p in inputs]
    else:expected=read(inputs[0])
    actual=hydrate(get(output));ok=actual==expected
    equivalence.append({'output':output,'records':len(actual) if isinstance(actual,list) else None,'status':'PASS' if ok else 'FAIL','method':'JSON structural equality after provenance hydration; CSV via standard parser'})
    if not ok:errors.append('lossless equivalence '+output)
for output,predicate in [('tsa/portfolio.json',lambda x:not x['exclusion']),('tsa/excluded-search-records.json',lambda x:bool(x['exclusion']))]:
    if get(output)!=[x for x in read('mission-3/inventory.json') if predicate(x)]:errors.append('inventory projection '+output)
if [x['original_record'] for x in get('federal/source-registry.json')]!=read('data/sources.jsonl'):errors.append('federal source preservation')
fedids={x['source_id'] for x in read('data/sources.jsonl')}
gnodes=[x for p in read('evidence-graph/manifest.json')['node_files'] for x in read(p)]
if [x['original_record'] for x in get('tsa/source-registry.json')]!=[x['data'] for x in gnodes if x['type']=='SOURCE' and x['id'] not in fedids]:errors.append('TSA source preservation')
for pid,p in prov.items():
    if pid!='PROV-'+hashlib.sha256(encode(p)).hexdigest():errors.append('provenance content address '+pid)
model=get('federal/canonical-model.json')
if model['dictionary']!=read('methodology/canonical-data-dictionary.md') or model['specification']!=read('methodology/canonical-model.md') or len(model['entities'])!=27:errors.append('canonical model transcribed architecture')
state=get('provenance/frozen-state.json')
reportdata=get('analysis/completed-report-register.json')['technical_findings']
for x in reportdata['comparisons']:
    canonical=next(r for r in get('tsa/comparisons.json') if r['id']==x['id'])
    if canonical['classification']!=x['classification']:errors.append('report comparison '+x['id'])
for x in reportdata['findings']:
    canonical=next(r for r in get('tsa/within-icr-findings.json') if r['id']==x['id'])
    if canonical['classification']!=x['classification']:errors.append('report within finding '+x['id'])
report={'status':'PASS' if not errors else 'FAIL','protected_source_head':HEAD,'mission3_freeze':M3,'mission4_completion':M4,'protected_blobs_checked':protected,'input_fingerprints_checked':len(sourcechecks),'provenance_objects_reconstituted':len(prov),'lossless_dataset_checks':equivalence,'report_classifications_reconciled':len(reportdata['comparisons'])+len(reportdata['findings']),'canonical_model_entities':27,'new_research':False,'frozen_evidence_modified':False if not errors else 'SEE_ERRORS','errors':errors,'scope':'All original source-head files including frozen evidence and all completed reports/briefs; exact raw Git blob identity, release input SHA-256 and hydrated analytical record equality.'}
(r/'validation/source-preservation-report.json').write_bytes(encode(report))
print(json.dumps(report,indent=2));raise SystemExit(0 if not errors else 1)

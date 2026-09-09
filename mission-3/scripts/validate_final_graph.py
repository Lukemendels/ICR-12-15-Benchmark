"""Structural, content-level provenance and epistemic validation."""
from final_common import *
import re,csv,collections,functools,math
M=read('evidence-graph/manifest.json');S=read('evidence-graph/schema.json')
nodes=sum([rows(p) for p in M['node_files']],[]);edges=sum([rows(p) for p in M['edge_files']],[]);ids={x['id'] for x in nodes};byid={x['id']:x for x in nodes};errors=[];pe=[]
def need(ok,code,detail):
    if not ok:errors.append(dict(code=code,detail=detail))
need(len(ids)==len(nodes),'DUPLICATE_NODE_ID',len(nodes)-len(ids));need(len({x['id'] for x in edges})==len(edges),'DUPLICATE_EDGE_ID','edge ids')
for x in nodes+edges:
    node='source' not in x
    need(all(k in x for k in S['node_required' if node else 'edge_required']),'REQUIRED_FIELDS',x['id'])
    need(x['type'] in S['entity_types' if node else 'edge_types'],'ENUM_TYPE',x['id'])
    need(x['epistemic_status'] in S['epistemic_statuses'],'EPISTEMIC_STATUS',x['id'])
    need(isinstance(x['provenance'],list) and bool(x['provenance']),'PROVENANCE_EMPTY',x['id'])
    if not node:need(x['source'] in ids and x['target'] in ids,'DANGLING_ENDPOINT',x['id'])
    else:
        d=x['data'];ref=d.get('ref')
        if ref and x['type']!='SOURCE':need('VER-'+ref in ids,'VERSION_REFERENCE',(x['id'],ref))
        if 'unit' in d:need(d['unit'] is None or isinstance(d['unit'],str),'INVALID_UNIT',x['id'])
        if 'period' in d:need(d['period'] is None or isinstance(d['period'],(str,int)),'INVALID_PERIOD',x['id'])
        if x['type']=='CONSISTENCY_FINDING':need(d['classification'] in S['classifications'],'CLASSIFICATION',x['id'])
@functools.lru_cache(None)
def document(p):return (ROOT/p).read_text()
def resolve(locator):
    if ':L' in locator:
        p,tail=locator.rsplit(':L',1);return document(p).splitlines()[int(tail)-1]
    if ':ROW' in locator:
        p,tail=locator.rsplit(':ROW',1);i=int(tail)
        if p.endswith('.csv'):return list(csv.DictReader(document(p).splitlines()))[i-2]
        return json.loads(document(p).splitlines()[i-1])
    if '#/' in locator:
        p,pointer=locator.split('#',1);v=json.loads(document(p))
        for k in pointer.split('/')[1:]:
            k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
        return v
    raise ValueError('Unsupported locator '+locator)
def same(original,value):
    if original==value:return True
    try:o=json.loads(original)
    except (ValueError,TypeError):o=original
    if o==value:return True
    if isinstance(value,dict):
        if value.get('grid')==o:return True
        if value.get('text')==original or value.get('resolved_text')==original:return True
    return False
unique={json.dumps(p,sort_keys=True):p for x in nodes+edges for p in x['provenance']}
for p in unique.values():
    try:
        assert all(k in p for k in S['provenance_required']),'missing provenance fields'
        assert p['source_id'] in byid and byid[p['source_id']]['type']=='SOURCE','source id not SOURCE'
        assert p['status'] in S['epistemic_statuses'],'provenance status'
        v=resolve(p['locator']);assert same(p['original'],v),'original content does not match locator'
    except Exception as e:pe.append(dict(locator=p.get('locator'),error=str(e),original=p.get('original'),resolved=str(v)[:500] if 'v' in locals() else None))
hashchecks=[]
for sp in sorted((ROOT/'mission-3/sources').glob('*/source.json')):
    for d in json.loads(sp.read_text()).get('documents',[]):
        actual=hashlib.sha256((ROOT/d['path']).read_bytes()).hexdigest();hashchecks.append(dict(path=d['path'],expected=d['sha256_text'],actual=actual,match=actual==d['sha256_text']))
        need(actual==d['sha256_text'],'SOURCE_TEXT_HASH',d['path'])
# Representation duplicates are explicitly described and cannot be implicitly added.
overlap=read('evidence-graph/representation-overlap.json')
for d in overlap:need(len(d['node_ids'])>1 and all(i in ids for i in d['node_ids']) and bool(d['explanation']),'OVERLAP_RECORD',d)
summary=dict(status='PASS' if not errors else 'FAIL',nodes=len(nodes),edges=len(edges),unique_node_ids=len(ids),unique_edge_ids=len({x['id'] for x in edges}),source_text_hashes_verified=len(hashchecks),representation_overlap_groups=len(overlap),errors=errors,epistemic_status_counts=dict(collections.Counter(x['epistemic_status'] for x in nodes)),limitations=['Exact source/locator validation does not validate empirical assumptions.','Absence of an occupation or assumption-to-activity edge means the relationship is not resolved, not inapplicable.','Alternative semantic representations are preserved with explicit nonaggregation rules.'])
write('mission-3/validation/graph-validation.json',summary)
write('mission-3/validation/provenance-validation.json',dict(status='PASS' if not pe and not any(not x['match'] for x in hashchecks) else 'FAIL',unique_provenance_records=len(unique),content_match_errors=pe,source_hash_checks=hashchecks,source_resolution='Every graph material node and edge resolves to exact archived text, frozen CSV row, JSON pointer or original geometry cell/grid.',limitations=['Raw source bytes are not all duplicated in Mission3; source metadata retains raw hashes and exact archived extracted text.','M1 references resolve through the unchanged source registry and frozen model/check records.']))
write('mission-3/validation/unit-period-register.json',dict(units=sorted({x['data']['unit'] for x in nodes if isinstance(x['data'].get('unit'),str)}),periods=sorted({str(x['data']['period']) for x in nodes if x['data'].get('period') is not None}),rule='Source-defined units retained. Compare only compatible units, denominators and periods in an adjudicated group. Null/absent fields explicitly remain unknown; no silent normalization to annual values.'))
print('structural errors',errors[:10],'provenance errors',len(pe));print(json.dumps(pe[:12],ensure_ascii=False)[:9500])
if errors or pe:raise SystemExit(1)

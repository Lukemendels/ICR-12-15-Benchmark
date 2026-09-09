#!/usr/bin/env python3
"""Reproduce ICR-EVIDENCE-1.0.0 from pinned repository inputs. Standard library only.
Build into a NEW destination; never overwrite a frozen release.
"""
import argparse, collections, csv, hashlib, json, pathlib, re, shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
HEAD = '1a5b3e852ad1c7d837d65e578bd706a46218311f'
M3 = 'b96aaaa4d81fe4df432602a0ae1346be78a151b1'
M4 = '34d94576f95b3a780ea3ec869b7c9c4fb653baa6'
STAMP = '2026-09-09T21:00:00Z'
VERSION = '1.0.0'
def encode(x): return (json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()
def sha(b): return hashlib.sha256(b).hexdigest()

def build(out):
    if out.exists(): raise SystemExit('Destination exists; immutable releases are not overwritten. Choose a fresh --output.')
    out.mkdir(parents=True)
    inputs={}; objects={}; schemas={}; prov={}; transforms={}
    def read(p):
        b=(ROOT/p).read_bytes(); inputs[p]={'path':p,'sha256':sha(b),'bytes':len(b),'source_commit':HEAD}
        if p.endswith('.jsonl'): return [json.loads(l) for l in b.decode().splitlines() if l.strip()]
        if p.endswith('.json'): return json.loads(b)
        if p.endswith('.csv'): return list(csv.DictReader(b.decode().splitlines()))
        return b.decode()
    def pack(x):
        if isinstance(x,list):return [pack(a) for a in x]
        if not isinstance(x,dict):return x
        intern=isinstance(x.get('provenance'),list) and all(isinstance(p,dict) and 'source_id' in p for p in x['provenance'])
        r={k:pack(v) for k,v in x.items() if k!='provenance' or not intern}
        if intern:
            refs=[]
            for p in x['provenance']:
                key='PROV-'+sha(encode(p));prov[key]=p;refs.append(key)
            r['provenance_refs']=refs
        return r
    def put(p,x,schema=None):
        objects[p]=x
        if schema:schemas[p]=schema
    def copied(p,source,schema=None):
        put(p,pack(read(source)),schema);transforms[p]={'inputs':[source],'operation':'lossless JSON/CSV parse; intern provenance arrays by SHA-256'}
    def obj(required,props=None,additional=True):return {'type':'object','required':required,'properties':props or {},'additionalProperties':additional}
    st={'type':'string'};nullable={'type':['string','null']};num={'type':'number'};arrstr={'type':'array','items':st}
    def arr(s):return {'type':'array','items':s}
    oldschema=read('evidence-graph/schema.json')
    enum=lambda xs:{'type':'string','enum':xs}
    baseprops={'id':st,'epistemic_status':enum(oldschema['epistemic_statuses']),'provenance_refs':arrstr}
    defs={
      'node':obj(['id','type','epistemic_status','data','provenance_refs'],dict(baseprops,type=enum(oldschema['entity_types']),data={'type':'object'}),False),
      'edge':obj(['id','type','source','target','epistemic_status','provenance_refs'],dict(baseprops,type=enum(oldschema['edge_types']),source=st,target=st,data={'type':'object'}),False),
      'provenance':obj(oldschema['provenance_required'],{k:st for k in oldschema['provenance_required']}),
      'comparison':obj(['id','level','family','refs','classification','similarity','observations','limitations','provenance_refs'],dict(baseprops,level=enum(['cross_ICR','within_ICR','cross_ICR_or_lineage','lineage','cross_ICR_and_lineage']),refs=arrstr,classification=enum(oldschema['classifications']),observations={'type':'array'},similarity={'type':'object'})),
      'within-finding':obj(['id','level','refs','classification','provenance_refs'],dict(baseprops,level={'const':'within_ICR'},refs=arrstr,classification=enum(oldschema['classifications']))),
      'bridge':obj(['id','current_ref','prior_ref','baseline','current','components','prior_values','current_values','component_deltas','net_change','residual','unit','period','baseline_identity','classification','provenance_refs'],dict(baseprops,baseline=num,current=num,net_change=num,residual=num,components=arrstr,prior_values=arr(num),current_values=arr(num),component_deltas=arr(num),unit=st,period=st,classification=enum(oldschema['classifications']))),
      'claim':obj(['claim_id','source_ids','evidence','interpretation'],{'claim_id':st,'source_ids':arrstr,'icr_id':nullable,'evidence':st,'interpretation':st}),
      'source':obj(['id','agency','control','package_ref','document_id','url','date','reference_period','source_type','evidence_status','original_record'],{'id':st,'agency':nullable,'control':nullable,'package_ref':nullable,'document_id':nullable,'url':nullable,'date':{'type':['string','number','null']},'reference_period':{'type':['string','number','null']},'source_type':nullable,'evidence_status':st,'original_record':{'type':'object'}},False),
      'benchmark':obj(['icr_id','omb_control_number','agency','title','source_ids'],{'icr_id':st,'source_ids':st}),
      'model':obj(['icr_id','model','source_ids','checks','reconstruction_issues'],{'icr_id':st,'model':{'type':'object'},'source_ids':arrstr,'checks':{'type':'array'}}),
      'qa':obj(['id','ref','formula','unit','status','provenance_refs'],dict(baseprops,ref=st,unit=nullable,status=st)),
      'question':obj(['finding_id','classification','question','evidence_needed','provenance_refs'],{'finding_id':st,'classification':enum(oldschema['classifications']),'question':st,'provenance_refs':arrstr}),
      'assumption-method':obj(['assumption_id','type','observed_methods','appropriate_context','example_icrs'],{'assumption_id':st,'type':st,'example_icrs':st}),
      'analysis-finding':obj(['id','kind','conclusion','evidence_refs','limitations','origin'],{'id':st,'kind':st,'conclusion':st,'evidence_refs':arrstr,'limitations':st,'origin':st},False),
    }
    # Typed graph payload contracts supplement the frozen ontology, without revising it.
    defs['activity-data']=obj(['ref','activity','period','record_kind'],{'ref':st,'activity':st,'actor':nullable,'period':nullable,'record_kind':enum(['normalized_activity_representation','assumption_task_context']),'aggregation_rule':st})
    defs['assumption-data']=obj(['ref','family','original_value','original_unit','unit','period','scope','record_kind'],{'ref':st,'family':st,'unit':nullable,'period':nullable,'record_kind':{'const':'reviewed_assumption_observation'}})
    copied('federal/benchmark.json','data/icrs.csv','benchmark')
    copied('federal/claims.json','data/claims.jsonl','claim')
    copied('federal/assumption-library.json','data/assumptions.csv','assumption-method')
    for dst,src in [('scores','scores.csv'),('calculation-checks','calculation-checks.csv'),('data-source-catalog','data-sources.csv'),('agency-summary','agency-summary.csv')]:copied('federal/'+dst+'.json','data/'+src)
    benchmark=objects['federal/benchmark.json']
    modelpaths=['icrs/'+r['icr_id']+'/extraction.json' for r in benchmark]
    put('federal/models.json',[pack(read(p)) for p in modelpaths],'model');transforms['federal/models.json']={'inputs':modelpaths,'operation':'lossless aggregation by benchmark order'}
    dic=read('methodology/canonical-data-dictionary.md');entities=[]
    for line in dic.splitlines():
        if line.startswith('|') and not line.startswith('| Entity') and not line.startswith('|---'):
            cells=[c.strip() for c in line.strip('|').split('|')];entities.append({'entity':cells[0],'principal_fields':cells[1],'relationships_and_constraints':cells[2]})
    put('federal/canonical-model.json',{'model_version':'0.5.0','status':'FROZEN_RESEARCH_ARCHITECTURE_NOT_EXECUTABLE_MODEL_SCHEMA','entities':entities,'specification':read('methodology/canonical-model.md'),'dictionary':dic})
    put('federal/rubric.json',{'version':'1.0.0','specification':read('methodology/rubric.md'),'calibration':read('methodology/calibration.md')})
    put('federal/context.json',{p:read('methodology/'+p+'.md') for p in ['tsa-comparison','tool-requirements','leaders','exemplars','requirements-floor']})
    gm=read('evidence-graph/manifest.json');nodes=[n for p in gm['node_files'] for n in read(p)];edges=[n for p in gm['edge_files'] for n in read(p)]
    put('tsa/nodes.json',pack(nodes),'node');put('tsa/edges.json',pack(edges),'edge')
    transforms['tsa/nodes.json']={'inputs':gm['node_files'],'operation':'lossless shard concatenation; intern provenance'}
    transforms['tsa/edges.json']={'inputs':gm['edge_files'],'operation':'lossless shard concatenation; intern provenance'}
    inventory=read('mission-3/inventory.json')
    put('tsa/portfolio.json',[r for r in inventory if not r['exclusion']]);put('tsa/excluded-search-records.json',[r for r in inventory if r['exclusion']])
    copied('tsa/control-histories.json','mission-3/control-histories.json')
    copied('tsa/representation-overlap.json','evidence-graph/representation-overlap.json')
    for target,source,contract in [('comparisons','adjudicated-comparisons','comparison'),('within-icr-findings','adjudicated-findings','within-finding'),('quantitative-checks','within-icr-qa','qa'),('item15-bridges','item15-bridges','bridge'),('review-questions','review-questions','question'),('comparison-groups','comparison-groups',None),('challenges','adversarial-challenge',None),('consistency-matrix','consistency-matrix',None),('qa-coverage','qa-coverage',None),('federal-comparators','federal-analogues',None)]:
        copied('tsa/'+target+'.json','analysis/'+source+'.jsonl',contract)
    copied('tsa/assumption-library.json','mission-3/assumptions/family-catalog.json')
    put('tsa/unresolved-questions.json',[x for x in objects['tsa/review-questions.json'] if x['finding_id'] in {r['id'] for r in objects['tsa/comparisons.json'] if r['classification']=='UNRESOLVED'}],'question')
    # One citation registry per mission; SRC IDs shared with graph resolve to federal registry.
    fed=read('data/sources.jsonl');fedids={s['source_id'] for s in fed}
    control={r['ref']:r['control'] or None for r in inventory}
    def source(s,identity,m3=False):
        ref=s.get('ref');url=s.get('url') or s.get('record',{}).get('url')
        return {'id':identity,'agency':'DHS/TSA' if m3 else s.get('authoring_entity'),'control':control.get(ref) if m3 else s.get('omb_control_number'),'package_ref':ref,'document_id':s.get('id'),'url':url,'date':s.get('publication_date') or s.get('year'),'reference_period':s.get('reference_period'),'source_type':s.get('document_type') or s.get('format') or ('package_metadata' if s.get('administrative_only') else None),'evidence_status':'PUBLISHED','original_record':s}
    put('federal/source-registry.json',[source(s,s['source_id']) for s in fed],'source')
    put('tsa/source-registry.json',[source(n['data'],n['id'],True) for n in nodes if n['type']=='SOURCE' and n['id'] not in fedids],'source')
    # Store completed analytical implications with explicit evidence addresses.
    findings=[]
    def finding(i,kind,conclusion,refs,limits,origin):findings.append({'id':i,'kind':kind,'conclusion':conclusion,'evidence_refs':refs,'limitations':limits,'origin':origin})
    for i,r in enumerate(objects['tsa/comparisons.json']):finding('ANALYSIS-'+r['id'],'task_method_adjudication',r['evidence_assessed'],['tsa/comparisons.json#/'+str(i)],r['limitations'],'completed Mission 3 adjudication; reported in Mission 4')
    for i,r in enumerate(objects['tsa/within-icr-findings.json']):finding('ANALYSIS-'+r['id'],'within_icr_reconciliation',r['evidence_assessed'],['tsa/within-icr-findings.json#/'+str(i)],r.get('limitations') or r.get('causal_boundary','Published reconstruction only; no official corrected total.'),'completed Mission 3 finding; reported in Mission 4')
    finding('ANALYSIS-TWIC-BRIDGE','positive_reconciliation','TWIC displayed annual component bridge reconciles with independently verified predecessor baseline.',['tsa/item15-bridges.json#/0'],objects['tsa/item15-bridges.json'][0]['limitations'],'completed Mission 3; Mission 4 positive reconciliation exhibit')
    for i,r in enumerate(objects['federal/models.json']):
        for j,text in enumerate(r['methods_worth_testing']):finding('FED-METHOD-'+r['icr_id']+'-'+str(j),'federal_construction_method',text,['federal/models.json#/'+str(i)],'Method exemplar requires task, source vintage, scope and applicability review; no automatic numeric transfer.','frozen Mission 1 extraction methods_worth_testing')
    for i,r in enumerate(objects['federal/assumption-library.json']):finding('FED-ASSUMPTION-'+r['assumption_id'],'assumption_applicability',r['appropriate_context'],['federal/assumption-library.json#/'+str(i)],'Method library is not a set of approved TSA default values.','frozen Mission 1 assumption library')
    architecture=read('report/tsa-consistency/technical/tables/architecture.csv')
    put('analysis/architecture-source.json',architecture)
    for i,r in enumerate(architecture):finding('IMPLICATION-'+str(i+1),'architectural_implication',r['Stage']+': '+r['Required content']+' '+r['Review or control'],['analysis/architecture-source.json#/'+str(i),'federal/canonical-model.json'], 'Proposed control architecture; efficacy, adoption and savings have not been measured.','completed Mission 4 architecture table')
    opportunities=[('PATHWAY-PARTITION','FIND-HME','Check mutually exclusive pathways against the declared parent population.'),('FREQUENCY','FIND-MD3','Carry frequency through row, subtotal and Federal workload formulas.'),('NARRATIVE-BINDING','FIND-EXIS','Bind numerical statements, tables and narrative to one approved model version.'),('FEDERAL-COST','FIND-CYBER-COST','Recompute Federal review count × sum of role hours × loaded rates; retain published and calculated values separately.')]
    for code,fid,txt in opportunities:
        ix=next(i for i,x in enumerate(objects['tsa/within-icr-findings.json']) if x['id']==fid)
        finding('CONTROL-'+code,'deterministic_control_opportunity',txt,['tsa/within-icr-findings.json#/'+str(ix),'federal/canonical-model.json'],'A control flags a reconstruction conflict; an analyst decides scope and official correction.','completed findings and canonical model control implications')
    put('analysis/findings.json',findings,'analysis-finding')
    put('analysis/completed-report-register.json',{'mission4':read('mission-4/report-state.json'),'leadership':read('report/tsa-consistency/leadership/audit/completion-audit.json'),'technical_findings':read('report/tsa-consistency/technical/source/report-data.json')})
    put('provenance/frozen-state.json',{'mission1':read('research/research-state.json'),'mission1_validation':read('research/final-validation.json'),'mission3_counts':read('mission-3/release-counts.json'),'graph_manifest':gm,'mission3_validation':read('mission-3/validation/final-validation.json'),'qa_summary':read('analysis/qa-summary.json')})
    put('provenance/limitations.json',{'federal':read('research/limitations.md'),'tsa':read('mission-3/limitations.md'),'federal_open_questions':read('research/open-questions.md'),'tsa_open_questions':read('mission-3/open-questions.md')})
    put('schemas/frozen-graph-ontology.json',oldschema)
    put('contracts/methods.json',{p:read('evidence-graph/'+p+'.md') for p in ['normalization-rules','shape-taxonomy','similarity-rules']})
    put('contracts/prior-query-catalog.json',read('evidence-graph/query-catalog.json'))
    put('provenance/observations.json',prov)
    # Definitions and all JSON documents have an explicit JSON Schema contract.
    for name,d in defs.items():put('schemas/'+name+'.schema.json',dict({'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:icr-evidence:schema:1.0.0:'+name},**d))
    for path,s in list(schemas.items()):schemas[path]='schemas/'+s+'.schema.json'
    put('schemas/object.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object'})
    put('schemas/record.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object'})
    # Address indexes are deterministic projections, never new analytical classifications.
    addresses={};facets={k:collections.defaultdict(set) for k in ['dataset','type','control','package','activity','actor','population_event','assumption_family','source','comparator_family','adjudication_status','federal_category','item']}
    def add(key,path,i,r,typ=None):
        addresses[key]=path+'#/'+str(i);d=r.get('data',r)
        def facet(k,v):
            if isinstance(v,list):
                for x in v:facet(k,x)
            elif v is not None and v!='':facets[k][str(v)].add(key)
        facet('dataset',path);facet('type',typ or r.get('type'))
        refs=d.get('refs',[]) or ([d['ref']] if d.get('ref') else ([d['icr_id']] if d.get('icr_id') else []))
        for k in ['current_ref','prior_ref']:
            if d.get(k):refs=refs+[d[k]]
        facet('package',refs);facet('control',d.get('control') or d.get('omb_control_number'))
        for ref in refs:facet('control',control.get(ref))
        for k in ['activity','shape_tag']:facet('activity',d.get(k))
        facet('actor',d.get('actor'));facet('population_event',d.get('population_unit') or (d.get('unit') if r.get('type')=='POPULATION' else None))
        facet('assumption_family',d.get('family') if r.get('type') in ['ASSUMPTION','ASSUMPTION_FAMILY'] else d.get('type') if path=='federal/assumption-library.json' else None)
        facet('comparator_family',d.get('family') if path in ['tsa/comparisons.json','tsa/comparison-groups.json'] else None)
        facet('adjudication_status',d.get('classification'));facet('federal_category',d.get('archetype'))
        sourceids=d.get('source_ids',[])
        if isinstance(sourceids,str):sourceids=sourceids.split(';')
        facet('source',sourceids)
        for pid in r.get('provenance_refs',[]):facet('source',prov[pid]['source_id'])
        if path.endswith('source-registry.json'):facet('source',r['id'])
        item=d.get('item')
        if item is not None:
            for n in re.findall(r'1[2-5]',str(item)):facet('item',n)
        if path=='tsa/item15-bridges.json':facet('item','15')
        if path=='federal/models.json':
            for item in ['12','13','14','15']:
                if ('activities' in d['model'] if item=='12' else 'item'+item in d['model']):facet('item',item)
    for i,n in enumerate(objects['tsa/nodes.json']):add('graph:'+n['id'],'tsa/nodes.json',i,n)
    indexed=['federal/benchmark.json','federal/models.json','federal/claims.json','federal/source-registry.json','tsa/source-registry.json','federal/assumption-library.json','tsa/comparisons.json','tsa/within-icr-findings.json','tsa/quantitative-checks.json','tsa/item15-bridges.json','tsa/comparison-groups.json','tsa/federal-comparators.json','tsa/control-histories.json']
    for path in indexed:
        for i,r in enumerate(objects[path]):add(path.split('/')[-1].replace('.json','')+':'+str(r.get('id') or r.get('claim_id') or r.get('icr_id') or r.get('assumption_id') or r.get('control')),path,i,r)
    # Shared package IDs for benchmark/models would collide if basename were not included.
    put('indexes/addresses.json',addresses)
    put('indexes/facets.json',{k:{v:sorted(ids) for v,ids in sorted(vals.items())} for k,vals in facets.items()})
    sourceidx={s['id']:p+'#/'+str(i) for p in ['federal/source-registry.json','tsa/source-registry.json'] for i,s in enumerate(objects[p])}
    put('indexes/sources.json',sourceidx)
    locidx=collections.defaultdict(list)
    for pid,p in prov.items():locidx[p['locator']].append('provenance/observations.json#/'+pid)
    put('indexes/locators.json',dict(locidx))
    relations=collections.defaultdict(lambda:collections.defaultdict(list))
    for e in objects['tsa/edges.json']:
        relations[e['source']][e['type']].append(e['target'])
    put('indexes/adjacency.json',{k:{t:sorted(v) for t,v in d.items()} for k,d in relations.items()})
    put('contracts/query-contract.json',{'version':VERSION,'mode':'read_only_exact_facets','allowed_facets':list(facets),'operators':['intersection'],'limit':{'minimum':1,'maximum':100,'default':50},'sort':'qualified address key ascending','pagination':'after exact qualified key, exclusive','unknown_fields':'reject','unknown_values':'empty result','missing_facets':'unknown, never evidence of zero or absence','item_index_scope':'explicit source item tags, validated bridges and federal model sections only; incomplete tags do not imply irrelevance','activity_assumption_join':'USES_ASSUMPTION edge is explicit activity linkage; package facet yields context only and must be labeled as such','comparability':'Index co-membership is candidate retrieval only; existing adjudication governs allowed comparison.'})
    # Original paths retained only to reproduce; consumers use output addresses above.
    put('provenance/transforms.json',transforms)
    put('provenance/input-inventory.json',list(inputs.values()))
    # File schema mapping is inventory metadata, not embedded $schema in historical data.
    for p,x in list(objects.items()):
        if not p.startswith('schemas/') and p not in schemas:schemas[p]='schemas/record.schema.json' if isinstance(x,list) else 'schemas/object.schema.json'
    for p,x in objects.items():
        dest=out/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(encode(x))
    (out/'contracts/schema-map.json').write_bytes(encode({p:{'schema':s,'mode':'each_record' if isinstance(objects[p],list) else 'document'} for p,s in schemas.items()}))
    print(json.dumps({'output':str(out),'json_files':len(objects)+1,'provenance_records':len(prov),'nodes':len(nodes),'edges':len(edges),'bytes':sum(p.stat().st_size for p in out.rglob('*') if p.is_file())}))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=pathlib.Path,required=True);build(ap.parse_args().output)

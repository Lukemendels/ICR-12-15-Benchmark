"""Deterministic, provenance-preserving projection; no inferred default values."""
from final_common import *
import collections,itertools
N={};E={};registry={x['source_id']:(i,x) for i,x in enumerate(rows('data/sources.jsonl'))}
def plist(p):return p if isinstance(p,list) else [p]
def node(id,typ,status,data,p):
    x=dict(id=id,type=typ,epistemic_status=status,data=data,provenance=plist(p))
    if id in N:assert N[id]==x,('node identity conflict',id)
    else:N[id]=x
    return id
def edge(typ,s,t,p,status='INFERRED',**data):
    id=ident('EDGE',typ,s,t,json.dumps(data,sort_keys=True));x=dict(id=id,type=typ,source=s,target=t,epistemic_status=status,provenance=plist(p))
    if data:x['data']=data
    if id in E:
        assert {k:v for k,v in E[id].items() if k!='provenance'}=={k:v for k,v in x.items() if k!='provenance'},('edge identity conflict',id)
        merged={json.dumps(v,sort_keys=True):v for v in E[id]['provenance']+x['provenance']}
        E[id]['provenance']=[merged[k] for k in sorted(merged)]
    else:E[id]=x
def meta(source_id,document_id,locator,value,status='PUBLISHED'):
    return dict(source_id=source_id,document_id=document_id,locator=locator,original=json.dumps(value,ensure_ascii=False),extraction_method='Exact archived metadata/JSON pointer',transformation='Identity projection; metadata is not task evidence',status=status)
def ensure_sources(p):
    for v in plist(p):
        sid=v['source_id']
        if sid not in N:
            i,d=registry[sid];node(sid,'SOURCE','PUBLISHED',d,meta(sid,v['document_id'],'data/sources.jsonl:ROW'+str(i+1),d))
def supported(id,p):
    ensure_sources(p)
    for v in plist(p):edge('SUPPORTED_BY',id,v['source_id'],v,'PUBLISHED')
inventory={x['ref']:x for x in read('mission-3/inventory.json') if x.get('scope')=='recent' and not x.get('exclusion')}
source_meta={}
for sp in sorted((ROOT/'mission-3/sources').glob('*/source.json')):
    d=json.loads(sp.read_text());ref=d['ref'];docs=d.get('documents',[]);source_meta[ref]=d
    for j,doc in enumerate(docs):
        sid='M3-SRC-'+ref+'-'+doc['id'];p=meta(sid,doc['id'],str(sp.relative_to(ROOT))+'#/documents/'+str(j),doc)
        node(sid,'SOURCE','PUBLISHED',dict(ref=ref,**doc),p)
    if docs:p=meta('M3-SRC-'+ref+'-'+docs[0]['id'],docs[0]['id'],str(sp.relative_to(ROOT))+'#/ref',ref)
    else:
        sid='M3-META-'+ref;p=meta(sid,ref,str(sp.relative_to(ROOT))+'#/ref',ref);node(sid,'SOURCE','PUBLISHED',dict(ref=ref,record=d.get('record'),administrative_only=True),p)
    vi=inventory.get(ref,{});node('VER-'+ref,'ICR_VERSION','PUBLISHED',dict(ref=ref,recent=ref in inventory,inventory=vi,record_status=d.get('status'),source_documents=len(docs),baseline_verified=False),p)
    if vi.get('control'):
        cid='CONTROL-'+vi['control']
        if cid not in N:node(cid,'CONTROL','PUBLISHED',dict(control=vi['control']),p)
        edge('HAS_VERSION',cid,'VER-'+ref,p,'PUBLISHED')
    for doc in docs:edge('USES_SOURCE','VER-'+ref,'M3-SRC-'+ref+'-'+doc['id'],p,'PUBLISHED')
for l in read('mission-3/lineage-resolved.json'):
    ref=l['current_ref'];old=l.get('immediate_prior_ref')
    if not old:continue
    p=meta(N['VER-'+ref]['provenance'][0]['source_id'],ref,'mission-3/sources/'+ref+'/source.json#/previous_ref',old)
    edge('UPDATES_FROM','VER-'+ref,'VER-'+old,p,'PUBLISHED',meaning='official_previous_package',baseline_verified=False)
    usable=l.get('usable_statement_ref')
    if usable and usable!=old:edge('UPDATES_FROM','VER-'+old,'VER-'+usable,p,'INFERRED',meaning='usable_statement_predecessor',baseline_verified=False)
ACT_FILES=['01-security-activities.jsonl','02-credentialing-activities.jsonl','03-security-portfolio-normalized-activities.jsonl','05-cyber-portfolio-normalized-activities.jsonl','05a-frozen-remaining-activities.jsonl','06-cohort-normalized-activities.jsonl','06-operational-portfolio-normalized-activities.jsonl','07-other-portfolio-normalized-activities.jsonl','08-operational-curated-activities.jsonl','09-other-curated-activities.jsonl','09-other-curated-tables.jsonl','12-portfolio-task-coverage.jsonl']
activities=[];locacts=collections.defaultdict(list)
for name in ACT_FILES:
    for x in rows('mission-3/extractions/'+name):
        p=x['provenance'];data={k:v for k,v in x.items() if k not in ['id','provenance','epistemic_status']};data['record_kind']='normalized_activity_representation';data['input_file']='mission-3/extractions/'+name
        data['aggregation_rule']='Do not sum representations across narrative, table, annualized/year, or frozen M1 projections.'
        node(x['id'],'ACTIVITY','NORMALIZED',data,p);supported(x['id'],p);edge('ESTIMATES_ACTIVITY','VER-'+x['ref'],x['id'],p,'NORMALIZED');locacts[p['locator']].append(x['id']);activities.append(x)
        n=x.get('annual_responses',x.get('normalized_values',{}).get('count'))
        if n is not None:
            pop=ident('POP',x['id']);node(pop,'POPULATION','NORMALIZED',dict(ref=x['ref'],value=n,unit=x.get('population_unit','response'),period=x.get('period'),identity=x['activity'],meaning='Source activity response count; not necessarily unique respondents.'),p);edge('APPLIES_TO_POPULATION',x['id'],pop,p,'NORMALIZED')
assumptions=rows('mission-3/assumptions/reviewed.jsonl')+rows('mission-3/assumptions/reviewed-review-and-fees.jsonl')+rows('mission-3/extractions/07-cohort-formula-assumptions.jsonl')
for x in assumptions:
    p=x['provenance'];data={k:v for k,v in x.items() if k not in ['id','provenance','epistemic_status']};data['record_kind']='reviewed_assumption_observation'
    if x['id']=='ASSUM-10a116a7234d4beeb2':data['original_period']=data['period'];data['period']='one-time';data['normalization_correction']='Source explicitly says one-time build; inherited annual period corrected in graph, original record retained.'
    node(x['id'],'ASSUMPTION','NORMALIZED',data,p);supported(x['id'],p)
    fam='FAM-'+x['family']
    if fam not in N:node(fam,'ASSUMPTION_FAMILY','INFERRED',dict(family=x['family'],kind='assumption_family'),p)
    edge('MEMBER_OF',x['id'],fam,p,'INFERRED')
    for a in locacts[p['locator']]:edge('USES_ASSUMPTION',a,x['id'],p,'INFERRED',scope='Shared source location; inspect actor/component before numerical reuse.')
    if x['family'] in ['manager_review','legal_review','federal_review_time','familiarization','renewal']:
        aid=ident('CONTEXT',x['id']);node(aid,'ACTIVITY','NORMALIZED',dict(ref=x['ref'],activity=x['scope'],actor=x.get('actor'),record_kind='assumption_task_context',unit=x['unit'],period=data.get('period')),p);edge('USES_ASSUMPTION',aid,x['id'],p,'NORMALIZED');edge('ESTIMATES_ACTIVITY','VER-'+x['ref'],aid,p,'NORMALIZED')
    if x['family']=='occupational_assignment':
        occ=ident('OCC',x['ref'],x['id']);node(occ,'OCCUPATION','NORMALIZED',dict(ref=x['ref'],value=x['normalized_value'],unit=x['unit'],scope=x['scope']),p)
        for a in locacts[p['locator']]:edge('USES_OCCUPATION',a,occ,p,'INFERRED',scope='Source paragraph occupation; actor must match.')
for x in rows('analysis/within-icr-qa.jsonl'):
    p=x['provenance'];node(x['id'],'VALIDATION_CHECK','CALCULATED',{k:v for k,v in x.items() if k not in ['id','provenance','epistemic_status']},p);supported(x['id'],p)
    f=ident('FORMULA',x['id']);result=ident('RESULT',x['id']);node(f,'FORMULA','CALCULATED',dict(ref=x['ref'],expression=x.get('replay_formula',x['formula']),operands=x.get('operands',{}),check_id=x['id']),p)
    node(result,'RESULT','CALCULATED',dict(ref=x['ref'],calculated_value=x['calculated_value'],published_value=x.get('published_value'),difference=x['difference'],unit=x['unit'],period=x.get('period'),field_status={'calculated_value':'CALCULATED','published_value':'PUBLISHED' if x.get('published_value') is not None else 'UNRESOLVED'},check_id=x['id']),p)
    edge('USES_FORMULA',x['id'],f,p,'CALCULATED');edge('PRODUCES_RESULT',f,result,p,'CALCULATED')
    if x.get('activity_id'):edge('USES_FORMULA',x['activity_id'],f,p,'CALCULATED')
    edge('CONFLICTS_WITH' if abs(x['difference'])>x.get('tolerance',.5) else 'RECONCILES_WITH',x['id'],'VER-'+x['ref'],p,'CALCULATED',scope='Registered check only; arithmetic residual is not final inconsistency classification.')
allfind=rows('analysis/adjudicated-comparisons.jsonl')+rows('analysis/adjudicated-findings.jsonl');matrix=[]
for r in allfind:
    p=r['provenance'];node(r['id'],'CONSISTENCY_FINDING','INFERRED',{k:v for k,v in r.items() if k not in ['provenance','observations','adversarial_challenge','epistemic_status']},p);supported(r['id'],p)
    group=r['comparison_group'];node(group,'ASSUMPTION_FAMILY','INFERRED',dict(kind='comparison_group',family=r['family'],rationale=r['similarity']['rationale'],classification=r['classification'],finding_id=r['id']),p)
    members=[]
    for o in r['observations']:
        op=o['provenance'];node(o['id'],'SOURCE_OBSERVATION',o['epistemic_status'],{k:v for k,v in o.items() if k not in ['id','provenance','epistemic_status']},op);supported(o['id'],op);edge('MEMBER_OF',o['id'],group,op,'INFERRED');edge('SUPPORTED_BY',r['id'],o['id'],op,'INFERRED')
        if o.get('source_record_id') in N:edge('DERIVED_FROM',o['id'],o['source_record_id'],op,'NORMALIZED')
        aids=[a for v in op for a in locacts.get(v['locator'],[])];members.extend(aids)
        matrix.append(dict(finding_id=r['id'],family=r['family'],ref=o['ref'],activity=o['activity'],original_value=o['original_value'],normalized_value=o['normalized_value'],unit=o['unit'],period=o.get('period'),source_ids=[v['source_id'] for v in op],source_locators=[v['locator'] for v in op],evidence_quality='source_backed_'+o['epistemic_status'].lower(),method=r['similarity']['rationale'],comparison_group=group,classification=r['classification'],explanation=r['evidence_assessed'],confidence=r['confidence'],level=r['level'],observation_id=o['id']))
    for a,b in itertools.combinations(sorted(set(members)),2):
        if r['classification'] not in ['NOT_COMPARABLE','UNRESOLVED']:edge('SIMILAR_ACTIVITY_TO',a,b,p,'INFERRED',finding_id=r['id'],strength=r['similarity']['strength'],scope='Use only the named comparison component.')
    if r['classification']=='DIFFERENT_EXPLAINED':
        expl=ident('EXPLANATION',r['id']);node(expl,'SOURCE_OBSERVATION','INFERRED',dict(meaning='Supported explanation',text=r['evidence_assessed'],finding_id=r['id']),p);edge('EXPLAINED_BY',r['id'],expl,p,'INFERRED')
    for q in r.get('check_ids',[]):edge('SUPPORTED_BY',r['id'],q,p,'INFERRED')
for b in rows('analysis/item15-bridges.jsonl'):
    p=b['provenance'];node(b['id'],'BASELINE','CALCULATED',b,p);change='CHANGE-'+b['id'];node(change,'CHANGE_EVENT','CALCULATED',dict(ref=b['current_ref'],prior_ref=b['prior_ref'],value=b['net_change'],unit=b['unit'],period=b['period'],component_deltas=b['component_deltas']),p);edge('DERIVED_FROM',change,b['id'],p,'CALCULATED');edge('CHANGES_TO',change,'VER-'+b['current_ref'],p,'CALCULATED');edge('RECONCILES_WITH',b['id'],'VER-'+b['prior_ref'],p,'CALCULATED')
jsonl('analysis/consistency-matrix.jsonl',matrix)
# Exact same-location representations are explicitly documented, never silently summed.
dups=[]
for loc,ids in sorted(locacts.items()):
    if len(ids)>1:dups.append(dict(locator=loc,node_ids=ids,explanation='Separate source-normalization representations or distinct tasks within one paragraph. Preserve identities; no additive or equivalent-task inference.'))
write('evidence-graph/representation-overlap.json',dups)
for id,x in N.items():
    d=x['data'];d.setdefault('unknown_fields_policy','Unobserved numeric value, unit, period, role or scope is null/absent; never a zero or matching feature.')
def shards(kind,data):
    directory=ROOT/'evidence-graph'/kind;directory.mkdir(exist_ok=True)
    # Fixed sorted-ID chunks make graph output deterministic.
    files=[]
    for i in range(0,len(data),100):
        p=f'evidence-graph/{kind}/{i//100:04}.jsonl';jsonl(p,data[i:i+100]);files.append(p)
    return files
nf=shards('nodes',sorted(N.values(),key=lambda x:x['id']));ef=shards('edges',sorted(E.values(),key=lambda x:x['id']))
write('evidence-graph/manifest.json',dict(graph_version='1.0.0',evidence_version='M3-1.0.0',schema_version='0.1.0',status='VALIDATION_PENDING',node_files=nf,edge_files=ef,node_count=len(N),edge_count=len(E),node_types=dict(collections.Counter(x['type'] for x in N.values())),edge_types=dict(collections.Counter(x['type'] for x in E.values())),normalized_activities=len(activities),reviewed_assumption_observations=len(assumptions),reviewed_scalar_categorical_assumptions=69,formula_header_observations=93,recent_versions=len(inventory),represented_versions=len(source_meta),archived_statement_versions=sum(bool(x.get('documents')) for x in source_meta.values()),matrix_rows=len(matrix),duplicate_representation_groups=len(dups),scope='Material normalized evidence, reviewed comparisons, QA and lineage. Discovery indexes remain separate and are not treated as reviewed assumptions.'))
checkpoint('Final analysis E: deterministic graph and consistency matrix built from468 activity representations,162 assumption observations,36 adjudications and341 checks.','Validate source locators, graph endpoints and epistemic labels; complete query catalog and two stable analytical review batches.')
print(read('evidence-graph/manifest.json'))

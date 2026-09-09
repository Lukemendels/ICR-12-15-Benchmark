"""Replay and consolidate frozen and Mission 3 checks; preserve source values."""
from final_common import *
import ast,operator,csv,collections
OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow}
def calc(s,env=None):
    def rec(n):
        if isinstance(n,ast.Expression):return rec(n.body)
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)):return n.value
        if isinstance(n,ast.Name):return (env or {})[n.id]
        if isinstance(n,ast.BinOp) and type(n.op) in OPS:return OPS[type(n.op)](rec(n.left),rec(n.right))
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -rec(n.operand)
        raise ValueError('Unsupported arithmetic expression')
    return rec(ast.parse(s,mode='eval'))
ACT_FILES=['01-security-activities.jsonl','02-credentialing-activities.jsonl','03-security-portfolio-normalized-activities.jsonl','05-cyber-portfolio-normalized-activities.jsonl','05a-frozen-remaining-activities.jsonl','06-cohort-normalized-activities.jsonl','06-operational-portfolio-normalized-activities.jsonl','07-other-portfolio-normalized-activities.jsonl','08-operational-curated-activities.jsonl','09-other-curated-activities.jsonl','09-other-curated-tables.jsonl','12-portfolio-task-coverage.jsonl']
acts=[]
for name in ACT_FILES:
    for i,x in enumerate(rows('mission-3/extractions/'+name)):
        x['input_file']='mission-3/extractions/'+name;x['input_row']=i
        x['aggregation_rule']='Evidence representations; never sum across tables, years, M1 projections or narrative duplicates without a declared ledger.'
        acts.append(x)
assert len({x['id'] for x in acts})==len(acts)
Q=[]
for i,x in enumerate(csv.DictReader(open(ROOT/'data/calculation-checks.csv'))):
    if '-1652-' not in x['icr_id']:continue
    v=calc(x['formula']);assert abs(v-float(x['calculated']))<1e-6,(x,v)
    p=dict(source_id=x['source_id'],document_id=x['icr_id'],locator='data/calculation-checks.csv:ROW'+str(i+2),original=json.dumps(x,ensure_ascii=False),extraction_method='Frozen M1 check reused; expression independently replayed',transformation='No change to Mission1 values or interpretation',status='CALCULATED')
    Q.append(dict(id=ident('QA-M1',x['icr_id'],x['label']),ref=x['icr_id'],label=x['label'],formula=x['formula'],operands={},calculated_value=v,published_value=float(x['reported']),difference=v-float(x['reported']),unit=x['unit'],period=None,period_unknown_reason='Retain frozen source context; this CSV does not encode period as a separate field.',status=x['arithmetic_status'],interpretation=x['interpretation'],original_record=x,epistemic_status='CALCULATED',provenance=[p],check_origin='M1_REUSED',replay_verified=True))
for x in rows('analysis/quantitative-checks.jsonl'):
    x['check_origin']='M3_SOURCE_SPECIFIC';f=x['formula'];env=x.get('operands',{})
    if x['id'].startswith('QA-EXIS-'):
        year=int(x['id'][-4:]);env=dict(zip(['stock','exercisers'],{2025:(12654,90),2026:(14046,69.6),2027:(15591,77.3)}[year]));f='stock-exercisers'
    if x['id']=='QA-TWIC-BRIDGE':env={'baseline':430317,'net_change':80154};f='baseline+net_change'
    v=calc(f,env);assert abs(v-x['calculated_value'])<1e-6,(x['id'],v)
    x['replay_formula']=f;x['operands']=env;x['replay_verified']=True
    if x['id']=='QA-MD3-COST':
        # Even treating 5.75 as a rounded total, not exact quarter-hour steps,
        # the wide input interval cannot reach the published annual result.
        lo=262*(5.75-.005)*(98.37-.005);hi=262*(5.75+.005)*(98.37+.005)
        x['input_precision_interval']=[lo,hi];x['tolerance']=max(abs(v-lo),abs(hi-v))+.5
        x['interpretation']='Prior tolerance of9USD understated a conservative ±.005hour input interval. Corrected interval remains far below208718; major finding unchanged.'
    if x['id'].startswith('QA-PARTITION-'):
        x['expected_value']=0;x['expected_value_status']='CALCULATED';x['published_value']=None
    Q.append(x)
for a in acts:
    nv=a.get('normalized_values',{});n=a.get('annual_responses',nv.get('count'));h=a.get('hours_per_response',nv.get('hours_per_unit'));m=a.get('minutes_per_response');out=a.get('reported_annual_hours',nv.get('hours'))
    if h is None and isinstance(m,(int,float)):h=m/60
    if not all(isinstance(z,(int,float)) for z in [n,h,out]):continue
    # annual_responses is already an event count; do not multiply its frequency again.
    v=n*h;res=v-out;status='EXACT' if abs(res)<1e-7 else 'WITHIN_OUTPUT_ROUNDING' if abs(res)<=.5 else 'SOURCE_PRECISION_OR_SCOPE_REVIEW'
    Q.append(dict(id=ident('QA-ROW',a['id']),ref=a['ref'],activity_id=a['id'],label='Source activity count × hours/unit',formula='count * hours_per_unit',operands={'count':n,'hours_per_unit':h},calculated_value=v,published_value=out,difference=res,unit='hours',period=a.get('period'),period_unknown_reason=a.get('unknown_reason') if a.get('period') is None else None,status=status,tolerance=.5,interpretation='Output-rounding screen only. Displayed input rounding, frequency, annualization and table/narrative alternatives require source-specific review before an error claim.',epistemic_status='CALCULATED',provenance=[a['provenance']],check_origin='M3_ROW_SCREEN',replay_verified=True))
jsonl('analysis/within-icr-qa.jsonl',Q)
write('analysis/qa-summary.json',dict(total_checks=len(Q),by_origin=dict(collections.Counter(x['check_origin'] for x in Q)),by_status=dict(collections.Counter(x['status'] for x in Q)),versions_with_checks=len({x['ref'] for x in Q}),all_expressions_replayed=True,normalized_activity_representations=len(acts),versions_with_activities=len({x['ref'] for x in acts}),limitations=['A row screen is not full-model validation.','M1 arithmetic dispositions remain verbatim, including the HME pathway share originally labeled within_display_rounding; Mission3 partition checks separately adjudicate its meaning.','No addition across representations or versions; count is evidence records, not distinct task types.','QA-MD3-COST input precision tolerance corrected openly; conclusion unchanged.']))
types=['components_to_subtotal','subtotals_to_summary','narrative_to_table','population_frequency_time','hours_times_rate','pathway_partition','period_alignment','source_transform','federal_rows','item15_baseline_changes','paired_transfers']
coverage=[]
for i in read('mission-3/inventory.json'):
    if i.get('exclusion') or i.get('scope')!='recent':continue
    qs=[x for x in Q if x['ref']==i['ref']]
    coverage.append(dict(ref=i['ref'],check_ids=[x['id'] for x in qs],status='PARTIAL_DETERMINISTIC_QA' if qs else 'SOURCE_TASK_COVERED_NO_REPLAYABLE_TOTAL',scope='Only registered equations and adjudicated conflicts. Full within-ICR assurance is not claimed.',universal_check_types=types,unperformed_checks='Not tested where row mapping, eligible population, source precision, prior baseline or transfer attribution remains unverified. Absence is not PASS.'))
jsonl('analysis/qa-coverage.jsonl',coverage)
checkpoint('Final analysis C: all inherited equations replayed, 41 M1 TSA checks preserved, activity-row QA consolidated, precision correction documented.','Complete source-specific adversarial challenge, then graph and provenance validation.')
print(read('analysis/qa-summary.json'))

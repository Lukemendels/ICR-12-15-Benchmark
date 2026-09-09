"""Explicit component mappings for the 15 inherited adjudications."""
from final_common import *
# ref, source line, component, original numeric value, original unit, normalized value, unit, period
V={
1:[('202406-1652-001',122,'carrier request',1,'hours',60,'minutes/request','per_event'),('202411-1652-003',83,'foreign carrier request',1,'hours',60,'minutes/request','per_event'),('202402-1652-002',104,'cargo request',1,'hours',60,'minutes/request','per_event')],
2:[('202304-1652-002',n,mode,8,'hours',480,'minutes/amendment','per_event') for n,mode in [(118,'freight'),(129,'passenger rail'),(140,'bus')]]+[('202504-1652-004',109,'consolidated amendment',8,'hours',480,'minutes/amendment','per_event')],
3:[('202304-1652-002',n,mode,1,'minutes',1,'minutes/record','per_event') for n,mode in [(164,'freight'),(175,'passenger rail'),(186,'bus')]],
4:[('202412-1652-001',144,'airport amendment preparation',25,'hours',1500,'minutes/amendment','per_event'),('202406-1652-001',122,'carrier request documentation',1,'hours',60,'minutes/request','per_event')],
5:[('202606-1652-001',183,'new coordinator or alternate contact',5,'minutes',5,'minutes/contact','per_event'),('202504-1652-005',107,'coordinator and/or alternate update',30,'minutes',30,'minutes/operator_update','per_event')],
6:[('202601-1652-004',140,'compensation ratio',1.467370066,'factor',1.467370066,'factor','not_applicable'),('202512-1652-001',259,'compensation ratio',1.467370,'factor',1.467370,'factor','not_applicable')],
7:[('202412-1652-001',294,'full-time private industry ratio',1.454667,'factor',1.454667,'factor','not_applicable'),('202406-1652-001',254,'transportation occupation ratio',1.4582,'factor',1.4582,'factor','not_applicable')],
8:[(ref,line,'all-occupation applicant wage',32.66,'USD/hour',32.66,'USD/hour','price_vintage_in_source') for ref,line in [('202605-1652-001',55),('202606-1652-003',68)]],
9:[('202605-1652-001',73,'medical trip each way',20,'minutes',40,'minutes/round_trip','per_event'),('202606-1652-003',66,'medical trip each way',34,'minutes',68,'minutes/round_trip','per_event')],
10:[('202504-1652-008',140,'TWIC online renewal',10,'minutes',10,'minutes/renewal','per_event'),('202606-1652-002',217,'HME online renewal',10,'minutes',10,'minutes/renewal','per_event'),('202605-1652-002',238,'PreCheck online renewal',1.8,'minutes',1.8,'minutes/renewal','per_event')],
11:[('202504-1652-006',119,'Federal threat triage',30,'seconds',.5,'minutes/comment','per_event'),('202504-1652-006',119,'contractor response',5,'minutes',5,'minutes/comment','per_event')],
12:[('202411-1652-006',95,'removed verbal certification interview',10,'minutes',10,'minutes/interview_removed','change_event')],
13:[('202206-1652-001',53,'checkpoint login',1,'minutes',1,'minutes/form','per_event'),('202509-1652-001',64,'checkpoint login',4,'minutes',4,'minutes/form','per_event')],
14:[('202402-1652-002',141,'pooled amendment review',120,'hours',7200,'minutes/amendment','per_event'),('202411-1652-003',123,'field carrier request review',4,'hours',240,'minutes/request','per_event'),('202411-1652-003',125,'headquarters carrier request review',6.75,'hours',405,'minutes/request','per_event')],
15:[('202606-1652-003',103,'removed Federal contractor exam cost',2531250,'USD/year',2531250,'USD/year','annual'),('202606-1652-003',103,'new candidate examination cost',150,'USD/exam',150,'USD/exam','per_event')],
16:[(ref,line,role+' plan review',v,'hours',v*60,'minutes/plan','per_plan') for ref,line in [('202207-1652-001',206),('202210-1652-001',248),('202212-1652-001',221),('202303-1652-001',263),('202512-1652-001',216)] for role,v in [('manager',8),('analyst',24)]],
17:[('202405-1652-002',102,'crew registration review',5,'minutes',5,'minutes/registration','per_event'),('202512-1652-001',216,'cyber implementation plan review',8,'hours',480,'minutes/plan','per_plan')],
18:[('202606-1652-002',384,'program funding','user fee','cost boundary','user fee','cost boundary','not_applicable'),('202504-1652-008',371,'program funding','applicant fees','cost boundary','user fee','cost boundary','not_applicable')]
}
old=rows('analysis/comparisons.jsonl');groups=[];out=[]
for r in old:
    n=int(r['id'].split('-')[1]); obs=[]
    for ref,line,component,ov,ou,nv,nu,period in V[n]:
        p=next((p for p in r['provenance'] if p['locator'].endswith(':L'+str(line)) and ref in p['source_id']),None)
        assert p,(r['id'],ref,line)
        obs.append(dict(id=ident('CMPOBS',r['id'],ref,line,component),ref=ref,activity=component,original_value=ov,original_unit=ou,normalized_value=nv,unit=nu,period=period,epistemic_status='NORMALIZED',provenance=[p]))
    r['finding_id']=r['id'];r['comparison_group']='GRP-'+r['id'][4:];r['observations']=obs
    r['confidence']={'level':'high' if r['similarity']['strength']=='strong' else 'moderate','basis':'Confidence is in the bounded published-evidence classification, not accuracy of unobserved actual task performance.'}
    r['practitioner_significance']={'priority':'review' if r['classification']=='UNRESOLVED' else 'reusable_method','reason':{'benefit_loading':'Labor valuation and reusable compensation inputs.','purchased_services':'Payer and cost-routing changes must remain separate from savings.','item15_baseline':'Versioned workflow changes need an explicit bridge.'}.get(r['family'],'Task boundaries and recurring burden coefficients affect reusable estimates.')}
    r['material_differences']=r['difference_observed'];r['original_values']=[x['original_value'] for x in obs];r['normalized_values']=[x['normalized_value'] for x in obs];r['units']=[x['unit'] for x in obs]
    r['method_dimensions']={k:dict(status='SEE_CITED_CONTEXT',evidence=r['similarity']['observable_matches'] if k in ['activity_definition','population','frequency'] else r['evidence_assessed']) for k in ['activity_definition','population','frequency','task_duration','role_occupation','wage_source','wage_vintage','compensation_method','source_evidence','proxy_transformation','cost_routing','federal_workload','item15_treatment']}
    r['causal_boundary']='Published estimation methods only; no inference about analysts, offices, internal procedures or intent.'
    groups.append(dict(id=r['comparison_group'],family=r['family'],title=r['title'],level=r['level'],members=[x['id'] for x in obs],refs=r['refs'],rationale=r['similarity']['observable_matches'],similarity=r['similarity'],inclusion_rule='Only the identified component and cited task boundary. A shared label does not authorize extending this group.',exclusions=r['candidate_explanation_tested'],numeric_comparison_allowed=r['classification'] not in ['UNRESOLVED','NOT_COMPARABLE'],provenance=r['provenance']))
    out.append(r)
jsonl('analysis/comparison-groups.jsonl',groups);jsonl('analysis/adjudicated-comparisons.jsonl',out)
checkpoint('Final analysis A: inherited 18 comparisons made inspectable with explicit component values, units, similarity, confidence and practitioner significance.','Extend reviewed assumption-family and activity comparisons; consolidate within-ICR QA and challenge.')
print('groups',len(groups),'observations',sum(len(r['observations']) for r in out))

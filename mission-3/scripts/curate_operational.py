"""Reviewed operational activity boundaries; calculated and published fields separate."""
import json,hashlib
from recover_geometry import ROOT
specs=[
('202411-1652-002',55,'Quarterly passenger-fee report','carrier',60,188*4,None,'recurring quarterly report','188 × 4'),
('202411-1652-002',55,'Independent audit preparation if reinstated','carrier',1200,113,2260,'conditional annual audit; probability-weighted dollars differ from full conditional hours',None),
('202202-1652-002',59,'FFDO questionnaire','pilot',60,1796,1796,'application',None),
('202202-1652-002',61,'FFDO verbal interview','pilot',10,1796,None,'application; count from L59','L59 applicant count applied to subsequent each-applicant interview'),
('202411-1652-006',65,'FFDO questionnaire','pilot',60,1700,1700,'application',None),
('202202-1652-003',77,'Domestic airspace waiver application','administrative assistant',33,4657,None,'domestic; count L75',None),
('202202-1652-003',77,'Foreign airspace waiver application','administrative assistant',60,4224,None,'international; count L75',None),
('202505-1652-002',89,'Domestic airspace waiver application','administrative assistant',33,5587,None,'domestic; count L87',None),
('202505-1652-002',89,'Foreign airspace waiver application','administrative assistant',60,4100,None,'international; count L87',None),
('202411-1652-001',62,'LEO flying armed training request','law enforcement agency',5,2000,166.67,'one-time request including follow-up; count L58',None),
('202301-1652-003',79,'Secure Flight VID submission, covered carrier','ticket agent',130/60,None,None,'electronic identity information; 990 events/carrier/year',None),
('202301-1652-003',79,'Secure Flight resolution call, covered carrier','ticket agent',12,None,None,'conditional additional information; 230 calls/carrier/year',None),
('202301-1652-003',94,'Secure Flight VID submission, Twelve-Five/private charter','ticket agent',130/60,None,None,'electronic identity information; 9.9 events/carrier/year',None),
('202301-1652-003',94,'Secure Flight resolution call, Twelve-Five/private charter','ticket agent',12,None,None,'conditional additional information; 2.3 calls/carrier/year',None),
('202508-1652-001',76,'Secure Flight VID submission, covered carrier','ticket agent',130/60,None,None,'electronic identity information; 865 events/carrier/year',None),
('202508-1652-001',76,'Secure Flight resolution call, covered carrier','ticket agent',5+10/60,None,None,'conditional additional information; 149 calls/carrier/year',None),
('202508-1652-001',91,'Secure Flight VID submission, Twelve-Five/private charter','ticket agent',130/60,None,None,'electronic identity information; 8.7 events/carrier/year',None),
('202508-1652-001',91,'Secure Flight resolution call, Twelve-Five/private charter','ticket agent',5+10/60,None,None,'conditional additional information; 1.5 calls/carrier/year',None),
('202508-1652-001',106,'Visitor pass request by non-traveler','individual',2,300000,10000,'new direct-to-TSA individual pathway',None),
('202508-1652-001',106,'Non-federal low-risk traveler list','list provider',90,51,76.5,'three list responses per provider; manual transmission',None),
('202411-1652-004',122,'EXIS full-access exercise design','full-access user',210,2228,7798,'50% of full-access stock; counts L131',None),
('202411-1652-004',134,'EXIS new limited-access exercise design','new limited-access user',210,79,276.3,'5% of new-user flow; displayed average count L143',None),
('202411-1652-004',146,'EXIS limited-access survey','limited-access user',15,13392.2,3348,'Narrative remainder vs 95% of total stock in table; count L155; scope conflict queued',None),
('202109-1652-005',53,'LEO monthly reimbursement request','clerk',60,3528,3528,'294 airports ×12 monthly requests',None),
('202504-1652-002',54,'Screening Partnership Program application','airport director',15,2,None,'two expected annually; narrative also discusses 10+ PRA threshold',None),
('202411-1652-005',68,'infoBoards responses','manager',60,5000,5000,'annual bundle per user; component of 10000-hour total', '5000 × 1 hour'),
('202411-1652-005',68,'infoBoards SSI training','manager',60,5000,5000,'annual additional training; Item15 documents added hour','5000 × 1 hour'),
('202412-1652-002',68,'MSIJSOC screening assistance request','individual',5,1291,None,'traveler data submission; count L66',None),
('202412-1652-002',68,'TPO travel support request','administrative services manager proxy',5,4045,None,'point-of-contact submission; count L66, role L70',None),
('202301-1652-001',74,'RSSP participation request','airport security coordinator',1920,15,480,'initial request; administrative data revised earlier 8h estimate',None),
('202301-1652-001',82,'RSSP amendment','airport security coordinator',480,1.5,12,'regulated entity requests amendment; 10% expected frequency',None),
('202601-1652-002',68,'RSSP participation request','airport security coordinator',1920,15,480,'initial request',None),
('202601-1652-002',76,'RSSP amendment','airport security coordinator',480,1.5,12,'regulated entity requests amendment; 10% expected frequency',None),
]
rows=[]
for ref,ln,label,actor,mins,count,hours,scope,calc in specs:
 meta=json.load(open(ROOT/'mission-3/sources'/ref/'source.json'));d=meta['documents'][0];lines=(ROOT/d['path']).read_text().splitlines();original=lines[ln-1];assert original.strip()
 rows.append({'id':'OPA-'+hashlib.sha256(f'{ref}|{ln}|{label}'.encode()).hexdigest()[:18],'ref':ref,'activity':label,'actor':actor,'minutes_per_response':mins,'annual_responses':count,'reported_annual_hours':None if calc else hours,'calculated_annual_hours':hours if calc else None,'period':'annual','unit':'response' if 'bundle' not in scope else 'user-year bundle','lifecycle_scope':scope,'unknown_reason':'No value imputed for unextracted total; exact-minute and rounded-hour display distinguished','epistemic_status':'NORMALIZED','field_status':{'minutes_per_response':'NORMALIZED','annual_responses':'CALCULATED' if calc else 'PUBLISHED' if count is not None else 'UNRESOLVED'},'count_or_component_transformation':calc,'provenance':{'source_id':'M3-SRC-'+ref+'-'+d['id'],'document_id':d['id'],'locator':d['path']+':L'+str(ln),'original':original,'extraction_method':'Analyst-reviewed source paragraph and explicitly identified linked counts/roles','transformation':'Hours ×60 or seconds /60; preserve component task boundary; component calculations labeled separately','status':'NORMALIZED'}})
(ROOT/'mission-3/extractions/08-operational-curated-activities.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print('curated',len(rows))

import json,hashlib,pathlib
from recover_geometry import ROOT
# source values and units, then explicit normalization; do not inflation-adjust.
specs=[
('202406-1652-001',254,'benefit_loading',1.4582,'factor','ratio total compensation/wages; production/transportation/material moving','March2023 source; published paragraph mislabels June','respondent'),
('202402-1652-002',191,'benefit_loading',1.4582,'factor','ratio33.13/22.72; transportation/material moving','March2023','respondent'),
('202412-1652-001',294,'benefit_loading',1.454667,'factor','ratio50.31/34.59; full-time private-industry workers','June2024','respondent'),
('202504-1652-004',251,'benefit_loading',1.4812,'factor','ratio36.57/24.69; transportation/material moving','September2024','respondent'),
('202601-1652-004',140,'benefit_loading',1.467370066,'factor','transportation/material moving; source March14 release','December2024','respondent'),
('202512-1652-001',259,'benefit_loading',1.467370,'factor','transportation/material moving; source March14 release','December2024','respondent'),
('202606-1652-001',297,'benefit_loading',1.46993,'factor','civilian transportation/material moving;36.91/25.11','June2025','respondent'),
('202605-1652-001',55,'benefit_loading',1.4582,'factor','all-occupation mean wage32.66; applicant proxy; loading-source context retained',None,'FAMS applicant'),
('202606-1652-003',68,'benefit_loading',1.4582,'factor','all-occupation mean wage32.66; applicant proxy; loading-source context retained',None,'TSO applicant'),
('202605-1652-001',64,'benefit_loading',1.4771,'factor','management/professional totalcomp divided by wages; healthcare providers',None,'healthcare provider'),
('202606-1652-001',185,'turnover',4,'percent','annual application to coordinator/alternate stock; source L309 is mean monthly separations','2025 monthly source applied annually','coordinator'),
('202606-1652-001',310,'turnover',9.06,'percent','annual residential mobility proxy, not directly job-contact updates','2023 CPS','coordinator'),
('202606-1652-001',185,'pathway_share',13,'percent','4% turnover +9% contact update; overlap not modeled explicitly','annual','coordinator'),
('202504-1652-005',107,'turnover',1,'operator update/year','one pipeline operator updates due to turnover or other POC changes',None,'owner/operator'),
('202504-1652-005',107,'task_duration',30,'minutes','pipeline cybersecurity coordinator and/or alternate update; bundle cardinality unresolved',None,'owner/operator'),
('202606-1652-001',183,'task_duration',5,'minutes','email name,title,phone,email for a new coordinator or alternate',None,'owner/operator'),
('202304-1652-002',118,'pathway_share',10,'percent','freight-rail STP amendment probability per year',None,'owner/operator'),
('202304-1652-002',129,'pathway_share',10,'percent','PTPR STP amendment probability per year',None,'owner/operator'),
('202304-1652-002',140,'pathway_share',10,'percent','OTRB STP amendment probability per year',None,'owner/operator'),
('202504-1652-004',109,'pathway_share',10,'percent','consolidated STP amendment probability per year; transferred1652-0066',None,'owner/operator'),
('202304-1652-002',164,'recordkeeping',1,'minutes','freight-rail new/updated employee training record',None,'administrative assistant'),
('202304-1652-002',175,'recordkeeping',1,'minutes','PTPR new/updated employee training record',None,'administrative assistant'),
('202304-1652-002',186,'recordkeeping',1,'minutes','OTRB new/updated employee training record',None,'administrative assistant'),
('202112-1652-002',74,'familiarization',0.5,'hours','read program directions/familiarize with process',None,'respondent'),
('202501-1652-002',77,'familiarization',0.5,'hours','read program directions/familiarize with process',None,'respondent'),
('202403-1652-002',301,'legal_review',4,'hours','COIP legal review; Federal actor; proposal',None,'Federal legal reviewer'),
('202409-1652-001',301,'legal_review',4,'hours','COIP legal review; Federal actor; proposal revision',None,'Federal legal reviewer'),
('202409-1652-001',385,'pathway_share',50,'percent','COIP submissions requiring legal review',None,'Federal legal reviewer'),
('202411-1652-006',83,'federal_review_time',3,'minutes','FFDO application review; electronic processing',None,'TSA employee'),
('202411-1652-001',72,'federal_review_time',45,'minutes','LEO training eligibility determination and verification',None,'TSA employee'),
('202109-1652-005',67,'federal_review_time',15,'minutes','monthly airport reimbursement request',None,'TSA F-H band'),
('202412-1652-002',80,'federal_review_time',15,'minutes','same process/submit/file for MSIJSOC and TPO',None,'TSA F/G band'),
('202504-1652-006',119,'federal_review_time',0.5,'minutes','electronic-comment security-threat triage',None,'Federal employee'),
('202504-1652-006',119,'federal_review_time',5,'minutes','electronic-comment read/select template/respond',None,'contractor'),
('202606-1652-005',72,'federal_review_time',15,'minutes','insider-threat report processing',None,'TSA employee'),
('202409-1652-003',138,'purchased_services',26974,'USD/application','mDL audit for initial waiver; ten/year average',None,'State'),
('202606-1652-003',103,'purchased_services',150,'USD/exam','local medical exam now paid by candidates;18000/year',None,'TSO applicant'),
('202606-1652-004',64,'capital_life',5178.40,'USD one-time construction','Federal intake system build; useful life unspecified; not an annual respondent capital charge',None,'Federal software engineer'),
('202504-1652-008',140,'renewal',10,'minutes','online TWIC renewal; source-tested completion times4min online and8min in-person retained conservative10min L58',None,'TWIC applicant'),
('202606-1652-002',217,'renewal',10,'minutes','online HME renewal avoiding physical visit',None,'HME applicant'),
]
rows=[]
for ref,ln,fam,value,unit,scope,vintage,actor in specs:
 d=json.load(open(ROOT/'mission-3/sources'/ref/'source.json'))['documents'][0];s=(ROOT/d['path']).read_text().splitlines()[ln-1];factor=60 if unit=='hours' else .01 if unit=='percent' else 1;nu='minutes' if unit=='hours' else 'fraction' if unit=='percent' else unit;loc=d['path']+':L'+str(ln)
 rows.append({'id':'ASSUM-'+hashlib.sha256(f'{ref}|{ln}|{fam}|{scope}'.encode()).hexdigest()[:18],'ref':ref,'family':fam,'original_value':value,'original_unit':unit,'normalized_value':value*factor,'unit':nu,'period':'annual' if 'annual' in scope or '/year' in unit else None,'vintage':vintage,'actor':actor,'scope':scope,'confidence':'high_transcription; comparability separately adjudicated','status':'REVIEWED_SOURCE_ASSUMPTION','epistemic_status':'NORMALIZED','provenance':{'source_id':'M3-SRC-'+ref+'-'+d['id'],'document_id':d['id'],'locator':loc,'original':s,'extraction_method':'Analyst-selected numeric value from complete source paragraph/table line','transformation':f'Original {unit} ×{factor}; no inflation adjustment or inferred numeric default','status':'NORMALIZED'}})
(ROOT/'mission-3/assumptions/reviewed.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print('reviewed assumptions',len(rows))

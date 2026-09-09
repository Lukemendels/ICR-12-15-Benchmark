import json,hashlib
from recover_geometry import ROOT,extract
specs=[
('202304-1652-001',136,'mDL initial waiver application','State employee',1200,10,'initial cohort; 15/10/5 States in years1/2/3; average10'),
('202304-1652-001',136,'mDL insufficient-application resubmission','State employee',300,9,'90% resubmission; distinct additional event, not mutually exclusive path'),
('202409-1652-003',118,'mDL initial waiver application','State employee',1200,10,'initial cohort; renewals start year4, outside initial 3-year horizon'),
('202409-1652-003',118,'mDL insufficient-application resubmission','State employee',300,9,'90% resubmission; incremental work after initial application'),
('202606-1652-004',54,'Automated real-time wait data transmission','airport/aircraft operator',0,None,'Published zero incremental respondent hours; existing systems; no inference of zero Federal cost'),
('202606-1652-005',55,'Insider threat incident report','respondent',10,312,'online report'),
('202112-1652-001',73,'Aviation security customer survey','traveler',5,9600,'up to ten questions; mixed online/paper/verbal channels'),
('202405-1652-002',75,'CMSDT individual registration and sign-in','crew member',6,495,'field office location; includes registration and injury waiver'),
('202405-1652-002',77,'CMSDT airline class roster','airline',2,300,'airline-center location; no individual registration or injury waiver'),
('202405-1652-002',79,'CMSDT course evaluation','crew member',10,10,'voluntary; source observed fewer than10 over3years but assumes10/year'),
('202504-1652-006',70,'Customer comment paper card','traveler',3,10363,'source says UX reduced prior5min'),
('202504-1652-006',80,'Electronic customer comment','traveler',5,245878,'email and online forms'),
('202504-1652-006',87,'Civil rights/disability submission','traveler',8,4805,'narrative count elsewhere4663; preserve conflict'),
('202305-1652-001',55,'SOMQ medical screening and questionnaire','TSO applicant',45,22500,'combined old task boundary'),
('202305-1652-001',55,'SOMQ medical trip','TSO applicant',54,22500,'round trip to contracted medical service provider'),
('202606-1652-003',62,'SOMQ online questionnaire','TSO applicant',30,18000,'online form; separate examination added'),
('202606-1652-003',64,'TSO medical examination','TSO applicant',30,18000,'local physician examination distinct from online form'),
('202606-1652-003',64,'TSO print and submit medical form','TSO applicant',5,18000,'print and email form'),
('202606-1652-003',66,'TSO medical trip','TSO applicant',68,18000,'34min each way to local physician'),
('202606-1652-003',66,'TSO medical office waiting','TSO applicant',11,18000,'waiting room separate from examination'),
('202202-1652-001',63,'Claim filing','claimant',30,9000,'manual submission'),
('202202-1652-001',63,'Approved claim payment information','claimant',10,1250,'approved-claim subset'),
('202411-1652-007',74,'Claim filing','claimant',30,7500,'all by mail in Item12; challenge Item13 mail share'),
('202411-1652-007',74,'Approved claim payment information','claimant',10,900,'approved-claim subset'),
('202411-1652-007',74,'TSA Form600','claimant',2.5,2,'rare approved-claim subset, source labels de minimis'),
('202204-1652-002',49,'Explosives course evaluation','student officer',30,156,'course-specific survey'),
('202503-1652-004',54,'Explosives course evaluation','student officer',30,156,'course-specific survey'),
('202305-1652-002',62,'FAMS mental health self-certification','FAMS applicant',60,100,'self-report form'),
('202605-1652-001',55,'FAMS mental health self-certification','FAMS applicant',60,100,'self-report form'),
('202605-1652-001',62,'FAMS two provider forms','healthcare provider',30,100,'15min each; includes50 applicants and50 incumbent officers'),
('202605-1652-001',73,'FAMS medical trip','FAMS applicant',40,50,'20min each way; incumbent travel excluded from public burden'),
('202605-1652-001',73,'FAMS medical office waiting','FAMS applicant',11,50,'waiting room distinct from30min provider form completion'),
('202605-1652-001',73,'FAMS print and submit medical forms','FAMS applicant',5,50,'print and email'),
('202303-1652-002',55,'Canine adoption application','individual',10,300,'voluntary adoption'),
('202601-1652-003',60,'Canine adoption application','individual',10,300,'voluntary adoption'),
('202504-1652-001',57,'Speaker request','individual',10,300,'online request'),
]
rows=[]
for ref,ln,activity,actor,mins,count,scope in specs:
 m=json.load(open(ROOT/'mission-3/sources'/ref/'source.json'));d=m['documents'][0];source=(ROOT/d['path']).read_text().splitlines()[ln-1]
 rows.append({'id':'OTHER-'+hashlib.sha256(f'{ref}|{ln}|{activity}'.encode()).hexdigest()[:18],'ref':ref,'activity':activity,'actor':actor,'minutes_per_response':mins,'annual_responses':count,'period':'annual','unit':'response','lifecycle_scope':scope,'unknown_reason':'Counts may depend on preceding population paragraph; full source retained. Active time vs elapsed distinguished only where stated.','epistemic_status':'NORMALIZED','provenance':{'source_id':'M3-SRC-'+ref+'-'+d['id'],'document_id':d['id'],'locator':d['path']+':L'+str(ln),'original':source,'extraction_method':'Analyst-reviewed task and source paragraph','transformation':'Minutes retained; hours ×60 where necessary; separate additive tasks and respondent roles','status':'NORMALIZED'}})
for ref in ['202203-1652-004','202504-1652-003','202403-1652-002','202409-1652-003']:
 m=json.load(open(ROOT/'mission-3/sources'/ref/'source.json'));d=m['documents'][0];g=extract(d,ref);p=ROOT/'mission-3/geometry'/ref/(d['id']+'.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(g,ensure_ascii=False,separators=(',',':'))+'\n')
 if ref in ['202203-1652-004','202504-1652-003']:
  t=g['tables'][0]
  for rr in t['rows']:
   if rr['grid'][0] and rr['grid'][0].strip().startswith(('Customer','Cognitive','Small')):
    print(ref,rr['row'],rr['grid'])
(ROOT/'mission-3/extractions/09-other-curated-activities.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print('curated',len(rows))

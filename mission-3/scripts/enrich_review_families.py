import json,hashlib
from build_comparisons import ROOT,evidence,add,rows
out=[]
def value(ref,n,family,v,unit,actor,scope,period):
 p=evidence(ref,[n])[0];factor=60 if unit=='hours' else 1
 out.append(dict(id='ASSUM-EX-'+hashlib.sha256(f'{ref}|{n}|{family}|{actor}'.encode()).hexdigest()[:18],ref=ref,family=family,original_value=v,original_unit=unit,normalized_value=v*factor if isinstance(v,(int,float)) else v,unit='minutes' if unit=='hours' else unit,period=period,actor=actor,scope=scope,epistemic_status='NORMALIZED',confidence='reviewed source transcription',status='REVIEWED_SOURCE_ASSUMPTION',provenance={**p,'status':'NORMALIZED','transformation':'Hours ×60; categorical wording normalized; no imputed labor role or life.'}))
for ref,n in [('202207-1652-001',206),('202210-1652-001',248),('202212-1652-001',221),('202303-1652-001',263),('202512-1652-001',216)]:
 value(ref,n,'manager_review',8,'hours','Federal manager','Cybersecurity implementation plan review; manager component','annual plan review' if ref=='202512-1652-001' else 'one-time plan review')
 value(ref,n,'federal_review_time',24,'hours','Federal analyst','Cybersecurity implementation plan review; analyst component','annual plan review' if ref=='202512-1652-001' else 'one-time plan review')
 value(ref,n,'federal_grade_pay','K band','grade','Federal manager','Cybersecurity implementation plan review',None)
 value(ref,n,'federal_grade_pay','J band','grade','Federal analyst','Cybersecurity implementation plan review',None)
for ref,n in [('202109-1652-004',90),('202405-1652-002',102)]:value(ref,n,'manager_review',5,'minutes','Federal CMSDT program manager','Review/respond to crew registration; separate waiver handling also5minutes','per registration')
value('202606-1652-002',384,'fee_treatment','User fee covers STA and operational costs','cost boundary','applicant/TSA','Fee financing does not imply zero resource cost',None)
value('202504-1652-008',371,'fee_treatment','Entirely applicant-fee funded; no appropriated augmentation','cost boundary','applicant/TSA','Fee financing; credential lifetime5years',None)
value('202504-1652-008',405,'fee_treatment','Fee revenue exceeding administration costs is a transfer','cost boundary','applicant/TSA','Do not add all fees to underlying Federal resource costs as social cost',None)
for ref,n in [('202605-1652-001',55),('202606-1652-003',68)]:
 value(ref,n,'wage_statistic','mean','statistic','public applicant','All occupations mean, not a wage percentile',None)
 value(ref,n,'occupational_assignment','00-0000','SOC','public applicant','All occupations applicant wage proxy',None)
(ROOT/'mission-3/assumptions/reviewed-review-and-fees.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
add('16','Federal cybersecurity plan review staffing','cross_ICR_and_lineage','manager_review',{'202207-1652-001':[206],'202210-1652-001':[248],'202212-1652-001':[221],'202303-1652-001':[263],'202512-1652-001':[216]},'Federal manager and analyst review a cybersecurity implementation plan; component labor per plan.','8 manager hours and24analyst hours repeated across pipeline and surface plan-review packages.','Test whether equal components also imply equal annual totals, recurrence or wage.','Per-plan roles and durations align. Serial revisions are not independent replications; later annual wording and wage changes require separate checks.','CONSISTENT','strong')
add('17','Manager title alone does not define comparable review','cross_ICR','manager_review',{'202405-1652-002':[102],'202512-1652-001':[216]},'Both name a Federal manager and review work, but deliverables differ.','Crew registration5minutes versus cyber implementation plan manager review8hours.','Test task complexity, artifact and workflow stage before ratio comparison.','Registration/waiver processing and substantive cyber implementation review are distinct deliverables with no matched scope. Reject candidate.','NOT_COMPARABLE','weak')
add('18','Credential fees and Federal resource-cost boundary','cross_ICR','fee_treatment',{'202606-1652-002':[340,384],'202504-1652-008':[371,405]},'Applicant-fee financing of security threat assessment and related program operations.','Both describe fee financing; TWIC additionally distinguishes excess revenue as transfer.','Test whether fee-funded means costless and whether fees should be summed with underlying Federal costs.','Shared financing approach is visible. TWIC makes resource/transfer distinction explicit; HME paragraph alone does not quantify net resource cost.','CONSISTENT',limitation='Consistency is limited to financing convention; no complete net social cost or fee adequacy comparison.')
(ROOT/'analysis/comparisons.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
# Appended records receive the same adversarial record shape as earlier comparisons.
for r in rows:
 if 'adversarial_challenge' not in r:r['adversarial_challenge']={'alternative':r['candidate_explanation_tested'],'evidence':r['evidence_assessed'],'result':r['classification']}
(ROOT/'analysis/comparisons.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
print('additional reviewed assumptions',len(out),'comparisons',len(rows))

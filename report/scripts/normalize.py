from pathlib import Path
import csv,json,hashlib
R=Path(__file__).resolve().parents[2];O=R/'report'
def write(name,rows):
 with open(O/'tables'/name,'w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
risks=[
('R01','202406-1652-001','SRC-0038','Item 12, first-flight checklist and Table 2','inconsistent_displayed_values','material','Narrative 54658; table 20165327 USD','Possible copy/versioning issue; intended internal editing history unestablished','TR-02'),
('R02','202408-1652-002','SRC-0040','Item 12, Table 7','confirmed_displayed_arithmetic_discrepancy','material','Components 6049; reported subtotal 4451 hours','Intended component/subtotal version unresolved','TR-02;TR-19'),
('R03','202606-1652-002','SRC-0054','Item 12, Tables 5a-5c','potential_scope_duplication','material','0.44+0.56+0.52*0.60=1.312','Alternative versus additive pathways require resolution; frozen numerical label conflicts with interpretation','TR-05'),
('R04','202606-1652-002','SRC-0054','Item 12, Tables 7, 8 and 10','inconsistent_displayed_values','material','About 519 survey hours; summary 5187','Source survey equation reproduces 518.712; no complete corrected package total asserted','TR-02;TR-19'),
('R05','202606-1652-001','SRC-0022;SRC-0026','Item 12, coordinator updates; JOLTS reference periods','unclear_source_transformation','methodological','Monthly separations plus annual mobility','Different periods and event definitions; overlapping events not resolved','TR-01;TR-03'),
('R06','202606-1652-001','SRC-0022','Item 14','confirmed_displayed_arithmetic_discrepancy','material','Printed rows 1149; reported 881 hours','Disclosed equation also differs; intended version unresolved','TR-12;TR-19'),
('R07','202412-1652-001','SRC-0176','Item 12, applicant wage footnote','rate_version_ambiguity','material','Used 34.48; footnote transformation 50.1936426713 USD/hour','Neither alternative certified as intended corrected input','TR-01;TR-02;TR-06'),
('R08','202412-1652-001','SRC-0176','Item 13, Table 11','displayed_precision_residual','small_relative_residual','1042500*56.55=58953375; reported 58954925 USD','Check source precision and versions before attributing cause','TR-03;TR-19'),
('R09','202504-1652-008','SRC-0180','Item 12, wage table','weak_task_representativeness','methodological','2044400 of 2113450 employment weight are heavy truck drivers','Transparent workforce weights do not establish applicant/task weights','TR-06'),
('R10','202504-1652-008','SRC-0180','Item 14','unavailable_resource_model','public_support_gap','Federal costs equated with fee revenue','Financing is not an independently exposed gross resource breakdown','TR-10;TR-12'),
('R11','202508-1652-001','SRC-0048','Item 14, table and footnote','unit_label_conflict','resolved_order_of_magnitude','Annual 156874666.67 USD from thousands table','Footnote resolves intended approximately 156.875 million; retain rounding','TR-03'),
('R12','202402-1652-002','SRC-0004','Item 14, KSMS O&M narrative and table','inconsistent_displayed_values','material','Narrative 1.2 million; table 1.6 million USD','Possible version mismatch; intended estimate unresolved','TR-02'),
('R13','202411-1652-007','SRC-0018','Item 14','inconsistent_displayed_values','material','Federal annual totals 344209 and 283225 USD','Disclosed workload reproduces 344209; pay band labels also conflict','TR-02;TR-12'),
('R14','202405-1652-001','SRC-0036','Item 12, summary hours','rounding_or_precision_question','small_residual','29638+3958=33596; reported 33594 hours','Do not equate small residual with material scope defect','TR-03'),
('R15','202412-1652-001','SRC-0176','Item 14','rounding_or_precision_question','small_residual','921400.97149 recomputed; 921402 reported USD','Precision check rather than material-error claim','TR-03'),
('R16','202504-1652-008','SRC-0180','Items 12-13 totals','rounding_or_precision_question','small_residual','One-hour and one-dollar differences','Frozen numerical labels require semantic interpretation','TR-03')]
write('reconstruction-risks.csv',[dict(risk_id=k,icr_id=i,source_ids=s,locator=l,classification=c,significance=z,observed_comparison=v,interpretation=t,requirement_ids=req,evidence_version='M1-1.0.0',classification_authority='Mission 2 synthesis; no frozen record edited') for k,i,s,l,c,z,v,t,req in risks])
actions=[
('KEEP','Atomic activities and applicant/employer separation','202406-1652-001;202412-1652-001','SRC-0038;SRC-0176','TR-04;TR-12'),
('KEEP','Occupation rationale, compensation metadata and transition cohorts','202405-1652-001','SRC-0036','TR-01;TR-06'),
('KEEP','Explicit alternative renewal pathways','202504-1652-008','SRC-0180','TR-05'),
('IMPROVE','Partition checks, rate periods and unique-person counts','202606-1652-001;202606-1652-002;202504-1652-008','SRC-0022;SRC-0054;SRC-0180','TR-03;TR-04;TR-05'),
('IMPROVE','Single-version tables, footnotes and narrative','202406-1652-001;202408-1652-002;202412-1652-001;202508-1652-001','SRC-0038;SRC-0040;SRC-0176;SRC-0048','TR-02;TR-19'),
('IMPROVE','Task evidence and gross Federal resource costs','202504-1652-008;202412-1652-001;202405-1652-001','SRC-0180;SRC-0176;SRC-0036','TR-06;TR-10;TR-12'),
('ADOPT','Named-baseline driver bridges and obligation transfer ledger','202503-3060-020;202508-1218-005;202404-1220-001;202408-1625-012','SRC-0064;SRC-0187;SRC-0008;SRC-0174','TR-08;TR-13;TR-14'),
('ADOPT','Measurement scope, make-or-buy partition and case funnels','202310-0607-003;202405-1218-005;202405-1506-005','SRC-0099;SRC-0060;SRC-0191','TR-04;TR-09;TR-16'),
('ADOPT','Asset life, replacement cohorts and separate reporting horizon','202502-2060-039;202401-2070-005','SRC-0161;SRC-0162;SRC-0183','TR-11'),
('INVESTIGATE','Overhead allocation and instruction routing','202501-1210-006','SRC-0102;SRC-0001;SRC-0002','TR-07;TR-09'),
('INVESTIGATE','Federal system allocations and vendor/internal prices','202405-0704-002;202412-1205-002','SRC-0164;SRC-0144','TR-10;TR-12'),
('INVESTIGATE','Restricted-model replication and calibration','202511-1545-005','SRC-0094;SRC-0100','TR-15;TR-17'),
('INVESTIGATE','Effects of recent internal TSA changes are not observable','202606-1652-001;202606-1652-002','SRC-0022;SRC-0054','')]
write('tsa-action-framework.csv',[dict(action_id=f'A{i+1:02}',category=a,practice=p,icr_ids=ids,source_ids=s,requirement_ids=req,evidence_version='M1-1.0.0',basis='methodology/tsa-comparison.md; cited Items 12-15 and supplements') for i,(a,p,ids,s,req) in enumerate(actions)])
rows=[]
for line in (R/'methodology/tool-requirements.md').read_text().splitlines():
 if line.startswith('| TR-'):
  id,behavior,basis,acceptance=[x.strip() for x in line.strip('|').split('|')]
  rows.append(dict(requirement_id=id,priority='SHOULD' if id in ['TR-15','TR-16'] else 'MUST',behavior=behavior,empirical_basis=basis,acceptance_condition=acceptance,priority_authority='Mission 2 implementation judgment',evidence_version='M1-1.0.0'))
write('tool-requirements.csv',rows)
rows=[]
for line in (R/'methodology/canonical-data-dictionary.md').read_text().splitlines():
 if line.startswith('| ') and not line.startswith('| Entity'):
  c=[x.strip() for x in line.strip('|').split('|')]
  rows.append(dict(entity=c[0],principal_fields=c[1],constraints=c[2],model_version='0.5.0'))
write('canonical-entities.csv',rows)
# Validate the local byte-preserving snapshot, restoring only transport newline differences.
manifest=json.loads((R/'research/evidence-manifest.json').read_text());matched=[];not_local=[];unresolved=[]
for x in manifest['files']:
 p=R/x['path']
 if not p.exists():not_local.append(x['path']);continue
 b=p.read_bytes();v={'exact':b,'no_final_newline':b[:-1] if b.endswith(b'\n') else b,'crlf':b.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')}
 match=next((k for k,val in v.items() if hashlib.sha256(val).hexdigest()==x['sha256']),None)
 if match:
  if match!='exact':p.write_bytes(v[match])
  matched.append(x['path'])
 else:unresolved.append(x['path'])
# Large duplicate text renditions returned empty by the connector are not used as evidence.
for path in unresolved:
 if path in ['raw/methods/cmmc-final-rule-2024.pdf.layout.txt','raw/methods/cmmc-final-rule-2024.pdf.txt']:(R/path).unlink()
 else:raise ValueError(path)
(O/'audit/local-evidence-integrity.json').write_text(json.dumps({'evidence_commit':'16aeb85d976eb3a89ecb3872d4dda94753e77cd3','matched_manifest_files':len(matched),'matched_paths':matched,'not_materialized':not_local+unresolved,'note':'Byte hashes of materialized evidence match frozen manifest. Two oversized duplicate CMMC text renditions were not available locally; the separate canonical cmmc-final-rule-2024.txt was used. Frozen remote tree is preserved; only report/* and the authorized README update are committed.'},indent=2)+'\n')
print('Normalized tables written; verified local evidence files:',len(matched))

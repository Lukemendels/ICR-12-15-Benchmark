"""Persist iteration 4 interpretation without rerunning manual extractions."""
from pathlib import Path
import csv,json,statistics,datetime
R=Path(__file__).parent
reviews=[json.loads(p.read_text()) for p in sorted((R/'icrs').glob('*/extraction.json'))]
state=json.loads((R/'research/research-state.json').read_text())
state.update(canonical_model_version='0.5.0',next_research_strategy='Iteration 5: MSHA silica and respiratory protection, SEC Form PF, and complete EPA/FERC amendment lineage; then select strategic batches after the minimum gate.',updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
(R/'research/research-state.json').write_text(json.dumps(state,indent=2)+'\n')
(R/'research/progress.md').write_text('''# Mission 1 progress

Status: IN_PROGRESS. Iteration 4 completed with 39 provisional reviews, including eight TSA collections. The minimum of 40 has not been met. Saturation streak is zero. No evidence freeze or final report is authorized by the evidence state.

Completed: governing instructions; four research batches; structured extractions and dimension rationales; arithmetic checks; source and claim registries; data-source and assumption catalogs; canonical model v0.5.0; provisional tool requirements and TSA comparison.

New in iteration 4: statistical burden-model architecture (IRS), burden measurement triangulation (Census AIES), occupational overhead allocation (EBSA), and repeated agency evidence. These are substantive findings, so the batch would not qualify as saturated even after the numerical minimum.

Next: finish deliberate MSHA/SEC challengers and EPA/FERC baseline reconstruction. Review coverage and scoring calibration before post-minimum saturation testing. Validate source archival paths and remaining underlying citations. Then conduct two qualifying saturated batches and the separate adversarial round if supported by evidence.
''')
with (R/'research/saturation-log.md').open('a') as f:f.write('''
## Iteration 4

Reviewed: 39. Minimum gate: FAIL. No new major dimension: FAIL (statistical calibration, measurement scope, allocated overhead). No rubric revision: PASS. Only trivial canonical change: FAIL (v0.5.0). No material leader change: FAIL (Census validation evidence; EBSA compact high-scoring comparator). No new data-source category: FAIL (survey-calibrated burden models and overhead allocation inputs). No new tool requirement: FAIL. Ordinary additional ICRs unlikely to resolve uncertainty: FAIL. Result: NOT ELIGIBLE / NOT SATURATED. Streak: 0.
''')
(R/'logs/iteration-004-results.md').write_text('''# Iteration 4 results

Ten complete provisional reviews added. EPA gasoline-distribution amendment remains deferred because its statement covers incremental amendments rather than the full approved collection. This is not counted as an additional reviewed ICR. Two MSHA collections and SEC Form PF have been retrieved for the next challenger batch, alongside older/current baseline evidence for EPA/FERC.

Selection tested statistical agencies, IRS modeling, repeated FDA/SEC, benefit programs and transport security/approvals. IRS and Census altered the reference architecture. EBSA explicitly documents shared PRA/RIA labor methodology, which is direct counterevidence to any claim that such analytical reuse is unique to TSA. Its worked overhead example contains visible arithmetic inconsistencies; the methodology remains a candidate, not a validated universal default.

All reviews remain provisional. Underlying citations are not uniformly retrieved; measured burden is distinct from documentation quality. One agency's simple collection must not establish agency-wide superiority over a complex TSA program.
''')
groups={}
for d in reviews:groups.setdefault(d['agency'],[]).append(d)
with (R/'data/agency-summary.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['component','n','mean','median','min','max','population_sd','interpretation'])
 for a,rs in sorted(groups.items()):
  v=[d['total_score'] for d in rs];w.writerow([a,len(v),round(statistics.mean(v),2),statistics.median(v),min(v),max(v),round(statistics.pstdev(v),2),'Purposive heterogeneous sample; descriptive, not agency rank'])
best=max(d['total_score'] for d in reviews)
lines=['# Provisional observed leaders','',f'Current reviewed sample: {len(reviews)}. Scores measure accessible documentation and remain provisional. Ties are retained. One-point differences are not evidence of substantive superiority.','',f'Highest overall observed score: {best}/100 — '+', '.join(d['icr_id'] for d in reviews if d['total_score']==best)+'.','', '| Dimension | Score | Observed ties |','|---|---:|---|']
for dim in reviews[0]['score']:
 high=max(d['score'][dim] for d in reviews);lines.append(f"| {dim} | {high} | "+'; '.join(d['icr_id'] for d in reviews if d['score'][dim]==high)+' |')
lines += ['', 'Item 12 must be assessed across reproducibility, segmentation, provenance and labor rather than one column alone. SEC ADV-E is a concise reconstruction exemplar; BLS SOII is the strongest overall observed package. Census AIES contributes the strongest directly observed burden-measurement triangulation. FCC IPCS is the clearest exact change-bridge example.', '', 'A legitimate zero is eligible for full Item 13 credit. For nonzero purchased services, OSHA extinguishers and FCC satellite are useful but imperfect exemplars. A fully validated nonzero capital annualization leader is still unresolved.', '', 'Highest agency-level quality and most consistent agency are not established. See data/agency-summary.csv for descriptive means and dispersion; most components have too few and too heterogeneous collections for a defensible agency ranking.']
(R/'methodology/leaders.md').write_text('\n'.join(lines)+'\n')
(R/'methodology/tsa-comparison.md').write_text('''# TSA comparison — provisional, iteration 4

Eight TSA collections score 50–76, with mean 66. These are purposively selected public packages, not a random sample or a measure of unpublished internal analysis. Document dates do not establish adoption of the user-reported process overhaul. Two June-2026-reference packages are potentially relevant to the recent period, but before/after attribution remains unverified.

The evidence does not support declaring TSA universally best-in-class. TSA provides useful occupational detail, multi-year projections and federal workload tables, while some public estimates contain major reconstruction problems. Other agencies outperform specific TSA methods: FCC IPCS change reconciliation; Census AIES burden measurement; BLS SOII obligation boundaries; EBSA's documented shared PRA/RIA compensation architecture. This does not establish that another agency is universally superior.

| Action | Provisional finding | Evidence |
|---|---|---|
| KEEP | Role-specific wage selection, explicit benefits loading and transition-year arrays. | TSA flight training, SRC-0036 |
| KEEP | Detailed atomic activity and federal workload tables. | TSA aircraft operator, SRC-0038 |
| IMPROVE | Validate mutually exclusive enrollment paths and reconcile summary hours. | TSA HME, SRC-0054 |
| IMPROVE | Preserve rate periods and verify that turnover/mobility proxies measure contact updates. | TSA surface cyber, SRC-0022; JOLTS SRC-0026 |
| IMPROVE | Reconcile row totals, applicant populations, fees and federal-cost units. | TSA certified cargo and Secure Flight, SRC-0040/0048 |
| ADOPT | Exact driver bridges against both prior approval and public-notice estimates. | FCC IPCS, SRC-0064 |
| ADOPT | Structured measurement evidence with sample sizes, distributions and task scope. | Census AIES, SRC-0099 printed page 19 |
| ADOPT | Cross-control obligation and make-or-buy ledgers. | BLS SOII and OSHA extinguishers, SRC-0008/0060 |
| INVESTIGATE | Data-derived occupational overhead instead of a universal factor. | EBSA SRC-0102; worked example requires correction/replication |
| INVESTIGATE | Statistical calibration for heterogeneous populations when justified by complexity. | IRS business tax, SRC-0094; public reconstruction incomplete |
| INVESTIGATE | Whether internal TSA review changes improve public output, and whether public statements omit stronger internal models. | No verified internal evidence; dates alone insufficient |

The causal part of the TSA hypothesis remains untested: observable rigor cannot establish why an agency performs analysis. EBSA's explicit PRA/RIA methodology demonstrates that downstream analytical reuse is not unique to TSA. More matched collections and model evidence are needed before interpreting agency means.
''')
# Preserve parsed table cells with exact text, without pretending automatic normalization is validated.
for d in reviews:
 p=R/'icrs'/d['icr_id']; tables=[]
 for source in (p/'raw').glob('supporting-statement-a-*.txt'):
  context='';rows=[]
  for n,line in enumerate(source.read_text().splitlines(),1):
   if ' | ' in line:rows.append({'text_line':n,'cells':line.split(' | ')})
   else:
    if rows:tables.append({'source_file':str(source.relative_to(R)),'preceding_text':context,'rows':rows});rows=[]
    if line.strip():context=line.strip()
  if rows:tables.append({'source_file':str(source.relative_to(R)),'preceding_text':context,'rows':rows})
 (p/'table-evidence.json').write_text(json.dumps({'status':'Parsed source cells; not automatically normalized model inputs','tables':tables},indent=2))
 d['table_evidence_path']=str((p/'table-evidence.json').relative_to(R));d['extraction_scope']='Analytical model and key checks in this record; all DOCX table cells preserved separately. PDF tables remain in page-preserving text. Peripheral rows require normalization before final software reuse.'
 (p/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print('Checkpoint interpretation and table evidence updated:',len(reviews))

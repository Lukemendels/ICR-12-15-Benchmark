"""Derive reporting tables and references without modifying the frozen evidence."""
from pathlib import Path
import json, csv, re, collections, hashlib
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'report/tsa-consistency/technical'
def read(p):return json.loads((ROOT/p).read_text())
def rows(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def write(p,d):
 p=OUT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
M=read('evidence-graph/manifest.json');nodes=[d for p in M['node_files'] for d in rows(p)];edges=[d for p in M['edge_files'] for d in rows(p)]
C=rows('analysis/adjudicated-comparisons.jsonl');F=rows('analysis/adjudicated-findings.jsonl');B=rows('analysis/item15-bridges.jsonl')[0];Q=rows('analysis/within-icr-qa.jsonl');A=rows('analysis/federal-analogues.jsonl')
records={d['id']:d for d in C+F+A+[B]};inv={d['ref']:d for d in read('mission-3/inventory.json') if not d.get('exclusion')};sources={d['id']:d['data'] for d in nodes if d['type']=='SOURCE'};sources.update({d['source_id']:d for d in rows('data/sources.jsonl')});versions={n['data']['ref']:n['data'] for n in nodes if n['type']=='ICR_VERSION'}
# Read and record the complete authoritative analysis contracts, QA and validation artifacts.
inputs=set(M['node_files']+M['edge_files'])
inputs.update(['mission-3/research-state.json','mission-3/handoff.md','mission-3/open-questions.md','mission-3/limitations.md','mission-3/stability-batches.json','mission-3/release-counts.json','mission-3/inventory.json','mission-3/control-histories.json','mission-3/lineage-resolved.json','evidence-graph/manifest.json','evidence-graph/query-catalog.json','evidence-graph/representation-overlap.json','evidence-graph/normalization-rules.md','evidence-graph/shape-taxonomy.md','evidence-graph/similarity-rules.md','analysis/comparability-protocol.md','analysis/adjudicated-comparisons.jsonl','analysis/adjudicated-findings.jsonl','analysis/adversarial-challenge.jsonl','analysis/comparison-groups.jsonl','analysis/consistency-matrix.jsonl','analysis/explainable-variation.jsonl','analysis/findings.jsonl','analysis/item15-bridges.jsonl','analysis/within-icr-qa.jsonl','analysis/quantitative-checks.jsonl','analysis/qa-summary.json','analysis/qa-coverage.jsonl','analysis/review-questions.jsonl','analysis/federal-analogues.jsonl','mission-3/assumptions/family-catalog.json','mission-3/assumptions/reviewed.jsonl','mission-3/assumptions/reviewed-review-and-fees.jsonl','mission-3/extractions/07-cohort-formula-assumptions.jsonl','mission-3/external-sources/external-source-review.json','data/sources.jsonl','research/research-state.json','methodology/canonical-model.md','methodology/leaders.md','report/source/report.md'])
inputs.update(p.relative_to(ROOT).as_posix() for p in (ROOT/'mission-3/validation').glob('*') if p.is_file())
for a in A:inputs.add(f"icrs/{a['ref']}/extraction.json")
for p in sorted(inputs):
 if p.endswith('.json'):read(p)
 elif p.endswith('.jsonl'):rows(p)
 else:(ROOT/p).read_text()
write('audit/input-register.json',[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in sorted(inputs)])

def nice(s):
 s=str(s).replace('_',' ')
 return re.sub(r'(?<=\d)(?=[A-Za-z])|(?<=[a-z])(?=\d)', ' ', s)
labels={'CONSISTENT':'Consistent','DIFFERENT_EXPLAINED':'Different, explained','POTENTIALLY_INCONSISTENT':'Potentially inconsistent','NOT_COMPARABLE':'Not comparable','UNRESOLVED':'Unresolved'}
T={}
def table(key,title,heads,rs,widths,note,record_ids=()):T[key]={'title':title,'headers':heads,'rows':rs,'widths':widths,'note':note,'record_ids':list(record_ids)}
table('definitions','How are the analytical classifications used?',['Classification','Interpretation'],[[labels[k],v] for k,v in [
 ('CONSISTENT','Agreement in the tested published component or method, with source-defined scope preserved.'),('DIFFERENT_EXPLAINED','Observed variation has a source-supported explanation; proxy optimality may remain unverified.'),('POTENTIALLY_INCONSISTENT','A material published conflict remains after comparability and explanation challenge.'),('NOT_COMPARABLE','A proposed match fails because the actor, task, denominator, or other essential scope differs.'),('UNRESOLVED','Available evidence cannot settle the relevant scope, methodological difference, or interpretation.')]], [0.29,0.71],'Source: analytical comparability protocol. Classifications are component-specific, not whole-package grades.')
table('coverage','What does each evidence count measure?',['Evidence measure','Count','Interpretation'],[
 ['Recent TSA packages','90','Versions received within the five-year window; all have principal-task and Items 12–15 coverage.'],['Assigned control histories','48','Control-number histories, distinct from recent package count.'],['Unassigned-control packages','5','Included among the 90; not five additional independent histories.'],['Package / statement versions with lineage','135 / 134','Includes one administrative version without a statement.'],['Normalized activity representations','468','Nonadditive across overlapping source representations and versions.'],['Reviewed assumption observations','162','69 scalar/categorical observations plus 93 formula-header coefficients.'],['Task/method comparisons','32','15 consistent; 8 explained; 6 unresolved; 3 not comparable.'],['Within-ICR findings','8','7 potentially inconsistent; 1 unresolved.'],['Quantitative checks / covered versions','341 / 40','Checks are not independent findings or full-model validation.']], [0.36,0.14,0.50],'Source: reviewed inventory, graph manifest, adjudication and QA registers. Evidence snapshot: September 9, 2026.')
portfolio=[];coveragefiles=[('03-security-portfolio','Security-program activities'),('04-credential-portfolio','Credentialing, redress and vetting'),('05-cyber-portfolio','Cyber and surface assessment'),('06-operational-portfolio','Operational, fee and system activities'),('07-other-portfolio','Other collections')]
allrefs=[]
for prefix,label in coveragefiles:
 rs=rows(f'mission-3/extractions/{prefix}-coverage.jsonl');refs=sorted(set(d['ref'] for d in rs));allrefs+=refs;portfolio.append([label,str(len(refs))])
assert len(allrefs)==len(set(allrefs))==90
portfolio.append(['Total','90'])
table('portfolio','Which broad collection groups are covered?',['Descriptive portfolio group','Recent versions'],portfolio,[0.78,0.22],'Source: archived portfolio coverage registers. Grouping supports coverage description, not administrative ranking.')
status=collections.Counter(d['conclusion'] or 'Pending' for d in inv.values())
table('status','What administrative outcomes appear in the recent corpus?',['Recorded conclusion or status','Packages'],[[k,str(v)] for k,v in status.items()]+[['Total','90']],[0.78,0.22],'Source: official package inventory at September 9, 2026. Active-search membership (42) is separate from these conclusion categories. [[INVENTORY]]')
table('explained','Which differences have an observable explanation?',['Case','Observed difference','Explanation and boundary'],[[d['title']+f" [[{d['id']}]]",nice(d['difference_observed']),nice(d['evidence_assessed'])] for d in C if d['classification']=='DIFFERENT_EXPLAINED'],[0.25,0.29,0.46],'Source: eight adjudicated task/method comparisons. Published explanations do not independently validate actual task performance.',[d['id'] for d in C if d['classification']=='DIFFERENT_EXPLAINED'])
needs={'CMP-04':'Decompose preparation, submission and implementation for aligned amendment types.','CMP-05':'Align persons, coordinator/alternate bundles, fields and operator events.','CMP-09':'Establish one-way/round-trip statistic, travel purpose and applicant-population fit.','CMP-10':'Align form content, conditional biometrics and timing evidence.','CMP-14':'Decompose active work by role and amendment type; establish pooled scope.','CMP-21':'Align person-stock and operator-event denominators; provide annual calibration.'}
table('unresolved','What evidence would resolve the six open comparisons?',['Comparison','Why unresolved','Evidence needed'],[[d['title']+f" [[{d['id']}]]",nice(d['evidence_assessed']),needs[d['id']]] for d in C if d['classification']=='UNRESOLVED'],[0.25,0.43,0.32],'Source: adjudications and evidence-needed records. These are not established cross-ICR inconsistencies.',list(needs))
fnames={'FIND-HME':'HME pathways','FIND-MD3':'Maryland Three costs','FIND-GENERIC':'Generic clearance','FIND-EXIS':'EXIS populations','FIND-LEO':'LEO Federal cost','FIND-TURNOVER':'Surface-cyber turnover','FIND-PRECHECK':'PreCheck valuation','FIND-CYBER-COST':'Pipeline plan-review cost'}
fmode={'FIND-HME':'Potential duplication / pathway definition','FIND-MD3':'Arithmetic / cost product','FIND-GENERIC':'Arithmetic, totals and narrative conflict','FIND-EXIS':'Stock/flow definition mismatch','FIND-LEO':'Period-label conflict','FIND-TURNOVER':'Source transformation / event definition','FIND-PRECHECK':'Unresolved valuation scope','FIND-CYBER-COST':'Arithmetic / wage-workload product'}
table('findings','Which within-ICR risks remain after challenge?',['Case / package','Type of risk','Disposition / status'],[[fnames[d['id']]+'\n'+d['refs'][0]+f" [[{d['id']}]]",fmode[d['id']],labels[d['classification']]+'\n'+('Pending' if inv[d['refs'][0]]['conclusion']=='' else 'Active; '+inv[d['refs'][0]]['conclusion'].lower())] for d in F],[0.35,0.34,0.31],'Source: eight adjudicated findings and package inventory. Status is the September 9, 2026 snapshot. Each case is one finding, even when several equations are checked.',[d['id'] for d in F])
hq=[d for d in Q if d['id'] in ['QA-PARTITION-4','QA-PARTITION-5','QA-PARTITION-6']]
table('hme','Do HME pathway counts partition the stated parent cohort?',['Year','Parent cohort','In-person rows, summed','Online renewals','Partition residual'],[[d['period'],f"{d['operands']['all_applicants']:,.0f}",f"{d['operands']['pre_enrollment']+d['operands']['no_pre_enrollment']:,.0f}",f"{d['operands']['online_renewal']:,.0f}",f"{d['calculated_value']:,.0f}"] for d in hq],[0.1,0.22,0.24,0.22,0.22],'Source: HME pending package 202606-1652-002, enrollment pathway tables. Residual = in-person rows + online renewals - parent cohort, in persons. Zero is the analyst partition identity. [[FIND-HME]]',['FIND-HME'])
table('twic','Does the TWIC annualized component bridge reconcile?',['Activity component','Prior hours','Current hours','Change'],[[a,f'{p:,}',f'{c:,}',f'{d:+,}'] for a,p,c,d in zip(B['components'],B['prior_values'],B['current_values'],B['component_deltas'])]+[['Total',f"{B['baseline']:,}",f"{B['current']:,}",f"{B['net_change']:+,}"]],[0.43,0.19,0.19,0.19],'Source: TWIC 202502-1652-004 and 202504-1652-008, annualized burden tables and Item 15. Residual is zero; this is not a causal factor decomposition. [[BASELINE-TWIC-2025]]',['BASELINE-TWIC-2025'])
ass=[n for n in nodes if n['type']=='ASSUMPTION'];ac=collections.Counter(n['data']['family'] for n in ass)
advice={'pathway_share':'Explicit eligibility and exclusive/additive relationships; case-specific shares.','task_duration':'Reuse only with actor, scope, statistic, mode and period.','federal_review_time':'Retain reviewer roles, case types and recurrence.','benefit_loading':'Standardize formula/base; select universe and vintage case by case.','federal_grade_pay':'Identify grade/band, pay basis, effective date and load.','manager_review':'Reuse bounded review archetypes; title alone is insufficient.','turnover':'Require annual event calibration and overlap mapping.','recordkeeping':'Distinguish annual bundles from per-record tasks.','fee_treatment':'Separate financing, resource cost and transfer.','purchased_services':'Identify purchaser, quantity, price and nonduplication.','familiarization':'Preserve separately timed step and applicability.','legal_review':'Retain legal task, eligibility share and proposal status.','wage_statistic':'Preserve mean/median and valuation purpose.','occupational_assignment':'Justify occupation and worker universe.','renewal':'Define form scope and conditional tasks.','capital_life':'Sparse evidence; no universal life or annualization default.'}
table('assumptions','How should reviewed assumption families be governed?',['Family','Observations','Proposed treatment'],[[nice(k).capitalize(),str(v),advice[k]] for k,v in ac.most_common()]+[['Total','162','Counts describe reviewed evidence, not independent defaults.']],[0.29,0.17,0.54],'Source: reviewed assumption observations, including formula-header coefficients. Item 15 is represented separately by baseline/change records.')
table('analogues','What can the four Federal analogues contribute?',['Federal example','TSA application','Boundary'],[
 ['Census AIES [[ANALOGUE-202310-0607-003]]','Timing scope and statistic for amendments, travel and renewals.','Do not transfer survey durations or treat medians as expected means.'],['Federal Communications Commission (FCC), IPCS [[ANALOGUE-202503-3060-020]]','Baseline identity and component bridges.','Do not substitute a Federal exemplar for a TSA baseline.'],['Bureau of Labor Statistics (BLS), National Compensation Survey [[ANALOGUE-202310-1220-004]]','Direct compensation and occupational mixes.','Does not establish an optimal TSA proxy.'],['Customs and Border Protection (CBP), Global Interoperability Standards [[ANALOGUE-202411-1651-004]]','Federal workload reconstruction and gross-cost/savings boundaries.','Analogous risk, not a best-practice total or prevalence comparison.']],[0.32,0.34,0.34],'Source: four previously reviewed Federal methodological analogues selected for the TSA analysis.',[d['id'] for d in A])
table('architecture','What must the recommended model preserve?',['Stage','Required content','Review or control'],[
 ['Sources','Document identity, exact locator, source period, original value.','Source content and applicability verified.'],['Structured inputs','Units, population, actor, period, evidence status.','Missing values remain explicit; zero requires source support.'],['Assumptions','Coefficient, rationale, applicability, owner, review trigger.','Approve proxy and scope; retain overrides.'],['Calculations','Formulas, full precision, role/pathway relationships.','Recompute independently; preserve units and periods.'],['Validation','Rule, operands, tolerance, result, disposition.','Separate arithmetic failures from scope/evidence questions.'],['Output tables','Approved result identity, label, unit and period.','Totals and summaries refer to the same model version.'],['Items 12–15 narrative','Bound numerical claims and reviewed analytical explanation.','Human review; no invention of missing rationale.']],[0.22,0.42,0.36],'Source: report synthesis of the canonical analytical architecture and TSA findings; proposed design, not observed current practice. [[CANONICAL]]')
controls=[['Cost products','Role hours × loaded rates must reproduce all published costs.','Maryland Three; pipeline review [[FIND-MD3,FIND-CYBER-COST]]'],['Cross-output totals','Rows, subtotals, summaries and narrative reconcile to identified results.','Generic clearance [[FIND-GENERIC]]'],['Pathway relationships','Exclusive alternatives exhaust the parent; additive follow-up has a trigger.','HME; mDL contrast [[FIND-HME,CMP-22]]'],['Population identity','Stock, new inflow and subset subtraction use the stated denominator.','EXIS [[FIND-EXIS]]'],['Period labels','Annual and multi-year values carry inherited period labels.','LEO [[FIND-LEO]]'],['Source transformations','Source period and event unit map explicitly to the model coefficient.','Turnover; analyst calibration still required [[FIND-TURNOVER]]'],['Valuation coverage','Valued plus explicitly excluded activities reconcile to all burden hours.','PreCheck [[FIND-PRECHECK]]'],['Baseline/change bridge','Identified prior values plus changes reconcile to the current endpoint.','TWIC [[BASELINE-TWIC-2025]]']]
table('controls','Which reconciliation controls should be implemented?',['Control','Acceptance rule','Motivating evidence'],controls,[0.24,0.48,0.28],'Source: analytical recommendations tied to the cited cases. A passing arithmetic check does not validate the underlying behavioral assumption.')
write('source/tables.json',T)
for key,t in T.items():
 with (OUT/f'tables/{key}.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(t['headers']);w.writerows(t['rows'])
write('source/report-data.json',{'comparisons':[{k:d[k] for k in ['id','classification','refs','title']} for d in C],'findings':[{k:d[k] for k in ['id','classification','refs','title']} for d in F],'bridge':B,'assumption_counts':dict(ac),'comparison_counts':dict(collections.Counter(d['classification'] for d in C)),'finding_counts':dict(collections.Counter(d['classification'] for d in F)),'labels':labels,'inventory':inv,'check_count':len(Q),'check_versions':len(set(d['ref'] for d in Q))})
# Compact complete register: explicit distinctions and every frozen classification.
app=['## Appendix A. Complete task/method comparison register','The following entries retain the 32 adjudications and their substantive boundaries. The register includes cross-collection, lineage and within-package method comparisons. It is separate from the eight within-ICR discrepancy findings. Entry numbers are reference labels, not quality scores.']
for d in C:
 app += [f"### A{int(d['id'].split('-')[1]):02d}. {d['title']}",f"**Disposition: {labels[d['classification']]}.** Comparison type: {nice(d['level'])}. Package references: {', '.join(d['refs'])}. [[{d['id']}]]",nice(d['difference_observed'])+' '+nice(d['evidence_assessed']), '**Boundary.** '+nice(d['limitations'])]
app += ['## Appendix B. Numerical reconstruction register','These are independent calculations or cross-representation comparisons using published inputs. They preserve source values and do not establish corrected official estimates. Source precision and scope govern interpretation.']
for d in F:
 app += ['### '+fnames[d['id']],f"**{labels[d['classification']]}.** "+nice(d['difference_observed'])+f" [[{d['id']}]]"]
 for q in Q:
  if q['id'] not in d['check_ids']:continue
  def fmt(v):return 'Not a published scalar; identity test' if v is None else f'{v:,.6f}'.rstrip('0').rstrip('.')
  app += [f"Expression: {q['formula']}. Calculated: {fmt(q['calculated_value'])}; published/comparator: {fmt(q.get('published_value'))}. Unit: {q['unit']}; period: {q.get('period') or 'not separately encoded'}. "+nice(q['interpretation'])]
 app += ['**Evidence needed.** '+nice(d['adversarial_challenge']['legitimating_evidence_needed'])]
app += ['## Appendix C. Terminology and reading guide',
 '**Burden.** Time or other resources represented as necessary to perform the information-collection activities in scope; the report distinguishes respondent hours, their labor valuation, nonlabor costs and Federal costs.',
 '**ICR and control number.** An Information Collection Request is a package/version. An OMB control number identifies an assigned collection history and can span multiple packages.',
 '**Supporting Statement A, Items 12–15.** The portions covering respondent burden and labor valuation, nonlabor costs, Federal costs, and changes from the applicable baseline.',
 '**Activity archetype.** A reusable structured definition of a task, actor, population unit, time statistic, frequency and cost construction. Reuse requires an applicability decision.',
 '**Population partition.** A declared division of a parent population into mutually exclusive pathways. It differs from additive or conditional activities performed by the same person.',
 '**Stock and flow.** A stock describes a population at a relevant point or period; a flow describes additions or events over time. New users and all users are not interchangeable.',
 '**Resource cost and transfer.** Resource cost concerns inputs consumed; a transfer concerns payment between parties. Payer and net budget effects should be recorded separately.',
 '**Baseline bridge.** An identified prior estimate plus explicit changes reconciled to a current estimate. A component bridge is not necessarily a causal driver decomposition.',
 '**Deterministic QA.** Quality assurance using explicit, replayable rules. Arithmetic validation does not establish behavioral or proxy validity.',
 '**OIRA.** Office of Information and Regulatory Affairs within the Office of Management and Budget (OMB). **EAB.** Economic Analysis Branch. **DHS.** Department of Homeland Security.',
 '**Program abbreviations.** AIES: Annual Integrated Economic Survey; CBP: Customs and Border Protection; CHRC: criminal history records check; DASSP: DCA Access Standard Security Program; DCA: Ronald Reagan Washington National Airport; EXIS: Exercise Information System; FAMS: Federal Air Marshal Service; FFDO: Federal Flight Deck Officer; HME: Hazardous Materials Endorsement; IPCS: Incarcerated People\'s Communications Services; LEO: law enforcement officer; LEOSA: Law Enforcement Officers Safety Act; mDL: mobile driver\'s license; SSI: Sensitive Security Information; STP: security training program; TRIP: Traveler Redress Inquiry Program; TSO: Transportation Security Officer; TWIC: Transportation Worker Identification Credential.']
(OUT/'source/appendices.md').write_text('\n\n'.join(app)+'\n')
# Citation targets preserve underlying document identity, deduplicated by canonical URL.
refs={};key_sources={};trace=[]
def source_entry(sid):
 s=sources[sid];url=s.get('url');ref=s.get('ref')
 if not ref:
  match=re.search(r'(20\d{4}-\d{4}-\d{3})',s.get('local_path',''));ref=match.group(1) if match else None
 meta=inv.get(ref,versions.get(ref,{}).get('inventory',{})) or {}
 title=meta.get('title') or s['title'];agency=meta.get('agency') or s.get('authoring_entity','TSA');control=meta.get('control') or s.get('omb_control_number');date=meta.get('received')
 detail=f"{agency}. {title}. Supporting Statement A, Items 12–15 and associated footnotes."
 if ref:detail+=f" ICR {ref}."
 if control:detail+=f" OMB control {control}."
 if date:detail+=f" Package received {date}."
 if not date and s.get('publication_date'):detail+=f" Document date {s['publication_date']}."
 detail+=' Reviewed September 9, 2026.'
 return {'url':url,'text':detail,'source_ids':[sid],'ref':ref,'record_url':meta.get('record_url') or (f'https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr={ref}' if ref else None)}
for key,d in records.items():
 ss=[]
 for p in d.get('provenance',[])+d.get('adversarial_challenge',{}).get('provenance',[]):
  sid=p['source_id'];s=source_entry(sid);url=s['url']
  if url not in refs:refs[url]=s
  elif sid not in refs[url]['source_ids']:refs[url]['source_ids'].append(sid)
  if url not in ss:ss.append(url)
  trace.append({'record_id':key,'source_id':sid,'locator':p['locator'],'original':p['original'],'reference_url':url})
 key_sources[key]=ss
# Previously reviewed primary travel studies support the bounded source-interpretation claim.
for ext in read('mission-3/external-sources/external-source-review.json')['sources']:
 u=ext['url'];refs[u]={'url':u,'text':ext['title']+'. '+('Altarum, 2019. PDF pages 1, 3, 5-6.' if 'ALTARUM' in ext['id'] else 'JAMA Network Open, 2025. DOI: '+ext['doi']+'. Methods and Results.')+' Previously reviewed September 9, 2026; interpretation remains bounded by study population and measurement scope.','source_ids':[ext['id']]}
 key_sources['CMP-09'].append(u)
# Canonical architecture / benchmark are prior analytical works, not new external evidence.
custom={
 'INVENTORY':{'url':'https://www.reginfo.gov/public/do/PRASearch','text':'Office of Management and Budget. Information Collection Review: TSA recent, active and pending package searches and control histories. Search snapshot September 9, 2026; agency/component 1652; recent receipt window September 9, 2021–September 9, 2026. Individual package identifiers and statuses are retained in the accompanying inventory table.','source_ids':[]},
 'CANONICAL':{'url':None,'text':'Federal ICR Items 12–15 Benchmark: canonical analytical model and data dictionary. September 9, 2026. Source-to-input, compensation, population, validation, baseline/change and generated-output architecture. Prior analytical design used selectively in this report.','source_ids':[]},
 'BENCHMARK':{'url':None,'text':'Federal ICR Items 12–15 Benchmark Report. September 9, 2026. Comparative analysis of 73 recent Federal ICRs and distributed methodological strengths; selective reference to the four cases identified in Section 9.','source_ids':[]}}
for key,v in custom.items():refs[key]=v;key_sources[key]=[key]
write('source/reference-registry.json',{'references':refs,'key_sources':key_sources})
write('audit/claim-source-locators.json',trace)
# Export reusable source registers and exact classifications.
for name,ds,keys in [('comparison-register',C,['id','title','level','family','classification','difference_observed','evidence_assessed','limitations']),('finding-register',F,['id','title','classification','difference_observed','evidence_assessed','limitations'])]:
 with (OUT/f'tables/{name}.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:d.get(k) for k in keys} for d in ds)
with (OUT/'tables/package-inventory.csv').open('w',newline='') as f:
 keys=['ref','control','title','received','conclusion','record_url'];w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:d.get(k) for k in keys} for d in inv.values())
print('Prepared',len(T),'tables;',len(refs),'available references;',len(trace),'source locator mappings.')

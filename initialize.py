from pathlib import Path
import json,datetime
R=Path(__file__).parent
files={
'AGENTS.md':'''# Mission 1 research protocol
Read research/research-state.json at the start of each iteration, then methodology/rubric.md, methodology/canonical-model.md, research/open-questions.md, research/saturation-log.md and methodology/leaders.md.
The user mission controls scope. Do not build the application or final publication report. Use only public material; distinguish current source evidence from user-reported internal history.
Preserve retrieved evidence, extraction, scoring and inference separately. Stable source and claim IDs are append-only. No score from search snippets or package metadata alone. Count an ICR as reviewed only after model extraction and evidence-based dimension scoring. Record missing evidence explicitly; unobserved is not zero.
Record versions, dates, units, source precision, assumptions, rounding and prior/current reconciliations. Do not infer agency-wide rank from a single collection. Distinguish family versions from independent collections.
Freeze gates: >=40 unique recent ICR reviews, >=8 components, meaningful TSA and relevant archetype coverage, TWO consecutive fully saturated strategic batches after the minimum, subsequent adversarial round, consistency and provenance validation, unresolved limitations and Mission 2 handoff. Never relax these gates to finish a turn. If interrupted, keep IN_PROGRESS and commit exact continuation steps.
''',
'research/research-plan.md':'''# Research plan
Test the TSA hypothesis through purposive, information-gain sampling over 2023-09-09 through 2026-09-09. Primary inclusion date is OIRA receipt/submission; record document upload and approval separately. An earlier submission with within-window substantive revised supporting statement may be included only with explicit explanation. Approval dates alone do not prove recent analytical work.
Iteration 0: establish authoritative requirements, preserve the provisional rubric and initialize state.
Iteration 1: diverse seed including three TSA collections (air cargo, current surface cybersecurity, claims), OSHA variances, EPA construction discharge permit, FDA premarket tobacco, FMCSA safety, BLS injuries, SEC custody accounting and SSA disability appeal.
Further iterations respond to findings. Seek complex nonzero capital, wage loading alternatives, statistical validation, federal workload and prior-to-new change bridges. Expand TSA across size, complexity and dates. Target CFPB, Census, FCC and other DHS components as challengers.
At >=40 reviews assess, but do not presume, saturation. Continue strategic batches, then challenge and validate. No statistical generalization from purposive means. Report component n, median/range and archetype caveats when n supports comparison.
''',
'methodology/rubric.md':'''# Rubric v1.0.0
Weights unchanged from the user mission. This measures observable public reconstruction quality, not all internal agency analysis or OMB approval quality.
|Dimension|Max|Full-credit standard|
|---|---:|---|
|Calculation reproducibility|20|Population, responses, activities, frequency, hours, units, annualization and rounding allow independent total reconstruction.|
|Source provenance and currency|15|Material inputs identify authority, dataset/table/series, occupation, geography, dates and transformations; aging input justified.|
|Burden structure and segmentation|15|Meaningful variation captured without rewarding gratuitous complexity.|
|Labor compensation|10|Occupation choice, wages, vintage, fringe/overhead bases and transformations are transparent and defensible.|
|Item 13|10|Applicable capital/O&M/purchased costs, life and annualization reconstruct; justified zero eligible for full credit.|
|Item 14|10|Incremental federal workload, grades/occupations, compensation, contracts and systems reconstruct or defensible zero.|
|Item 15|10|Old total to input/requirement change to reason to classification to quantified effect to new total.|
|Validation and uncertainty|5|Material assumptions supported by administrative evidence, testing, consultation or justified ranges; uncertainty proportionate.|
|Cross-item consistency|5|Narrative, tables, package totals and prior baseline reconcile with explained tolerances.|

Score anchors: 0=no usable support; approximately 25%=bare asserted total; 50%=partly reconstructable with material gaps; 75%=mostly reconstructable with bounded gaps; 100%=independent reconstruction supported. Integer scores require dimension-specific rationale and source locators. Missing/inaccessible evidence means review incomplete, not automatically a zero. Confirmed omission in a retrieved complete document can lose points.
Do not punish a legitimate zero or irrelevant segmentation. Full marks require the reason to be explicit and consistent with collection scope. Do not require sensitivity analysis for simple collections; credible validation can earn full validation marks. Store document thoroughness separately (brief/moderate/extensive), plus complexity and TSA relevance.
Record model arithmetic checks as pass, fail, rounding, or not_tested. A reported equation is not a performed check. Record source retrieval depth separately from scoring.
Revision history: 2026-09-09 v1.0.0: adopts user weights and provides operational scoring anchors; no empirical reweighting.
''',
'methodology/canonical-model.md':'''# Canonical model v0.1.0 — provisional architecture
Inputs → assumptions → calculations → validation → output tables → Items 12–15 narrative.
This starting architecture reflects mission requirements, not an empirical conclusion.
Each scenario/version owns collection identity, analysis period, price year, annualization horizon, approval lineage and baseline reference.
Entities: population; segment; activity; population-activity eligibility; frequency; response; time-by-occupation; occupation/SOC; wage observation; benefit observation; loading method; capital asset; recurring purchase; federal activity; federal labor; contract/system allocation; assumption; source; formula; validation; change event; output.
Atomic input fields: stable ID, numeric value, unit, year/period, source ID and locator, extraction versus assumption flag, method, applicability, confidence and owner. Formula fields reference input IDs, preserve full precision, declare rounding only at output, and carry explicit units.
Hours = eligible population × responses/person/year × hours/response; alternative event-based activities explicitly use events/year. Labor = sum(hours by role × loaded hourly cost). Unique respondents must not equal a naive sum of overlapping activity populations.
Compensation alternatives remain separate: direct total compensation; wage × (total compensation/wages); wage + benefit amount; wage/(1-benefit share). A fraction of compensation is not a wage markup. Overhead requires its own base and nonoverlap check. Household time value is distinct from employer compensation.
Item 13: recurring purchases plus documented annualized capital; record useful life, discounting convention, price year, cohort timing, one-time versus recurring, exclusions and potential overlap with labor.
Item 14: incremental government hours × loaded pay plus nonduplicative contract/system/operating allocations. Keep gross cost, offsetting fees and net budget effect separate pending guidance evidence.
Item 15: versioned baseline + quantified program changes + quantified adjustments = proposed estimate, independently for responses, hours and nonlabor cost; labor dollar bridge separately. Interactions require a declared decomposition order or explicit interaction term. Withdrawn/expired approval baseline is not automatically identical to the last historical study baseline.
Outputs are deterministic tables and source-aware narrative. Missing input cannot be filled by prose generation. Validation must distinguish arithmetic accuracy, plausible assumptions, scope completeness and cross-record agreement.
''',
'methodology/sampling-strategy.md':'''# Sampling strategy
Purposive discovery sample, not a random federal survey. Use collection family (OMB control number) for independent counts and retain ICR reference/version for reproducibility. Avoid inflating sample with non-substantive versions of the same family. Separate approved, proposed and pending cases.
Record archetype, complexity, regulated private sector relevance, positive Item 13, scope/recordkeeping activity and evidence accessibility. Compare matched archetypes before interpreting component averages. Seek both exceptionally strong and ordinary TSA cases. A third-quarter 2026 submission is only potentially post-overhaul; process attribution needs corroboration.
First seed selection is documented in research/research-plan.md. Subsequent target rationales must respond to observed gaps, not retrieval convenience.
''',
'research/open-questions.md':'''# Open questions
- Can current ROCIS guidance and supporting statement instructions be retrieved with version dates and reconciled?
- Which public TSA statements, if any, actually reflect the reportedly June–September 2026 internal overhaul? Dates are insufficient to establish attribution.
- What are the strongest supported time-per-response validation methods?
- Which loading methods distinguish compensation and overhead without duplication?
- Which collections quantify nonzero capital, O&M and external professionals well?
- Do changes decompose exactly and classify consistently with ROCIS?
- How sensitive are observed ranks to collection complexity and legitimate-zero treatment?
- What internal evidence is inaccessible, limiting conclusions about actual agency rigor?
''',
'research/saturation-log.md':'''# Saturation record
Iteration 0: not eligible. Reviewed=0; saturation streak=0. No saturation claim.
A saturated batch must have no major new method, rubric change, canonical-model change, leader shift, data-source category or tool requirement; remaining uncertainty unlikely to resolve through ordinary ICR review. Eligibility requires the minimum evidence base. Require two consecutive batches followed by an adversarial round. Record each predicate separately.
''',
'research/decision-log.md':'''# Decision log
2026-09-09 D001: Repository verified private and empty; README initialized through GitHub connector. User explicitly authorizes research-state commits.
2026-09-09 D002: Preserve user rubric weights. Add scoring anchors without pretending empirical validation.
2026-09-09 D003: Count only extracted/scored unique collection families. Retain incomplete retrievals outside reviewed totals.
2026-09-09 D004: Use direct Reginfo downloads and preserve raw bytes/hash plus text and package HTML. Search snippets are discovery only.
''',
'research/progress.md':'# Progress\nMission initialized. Primary evidence retrieval underway. No benchmark conclusions yet.\n',
'methodology/tsa-comparison.md':'# TSA comparison\nNot yet established. No inference about relative rigor or process overhaul is justified until matched evidence is reviewed.\n',
'methodology/leaders.md':'# Observed leaders\nNone assigned. No scored evidence yet.\n',
'methodology/tool-requirements.md':'# Tool requirements\nInitial requirements are provisional: typed inputs, explicit formulas, source IDs, compensation method alternatives, cost boundary checks, versioned baselines and deterministic change bridges. Link empirical requirements to claim IDs as research develops. No application implementation in Mission 1.\n',
'report/README.md':'# Mission 2 reserved\nPublication report begins only after evidence freeze and handoff.\n',
'logs/iteration-000.md':'# Iteration 0\nRepository inspected and found empty. Establish governing instructions, scoring anchors, retrieval and durable state. Status: IN_PROGRESS.\n',
'data/icrs.csv':'icr_id,omb_control_number,agency,title,submission_date,document_date,archetype,complexity,tsa_relevance,status,source_ids\n',
'data/scores.csv':'icr_id,rubric_version,reproducibility,provenance,segmentation,labor,item13,item14,item15,validation,consistency,total,thoroughness\n',
'data/sources.jsonl':'', 'data/claims.jsonl':'',
'data/data-sources.csv':'source_id,name,publisher,url,dataset,variables,item_use,update_frequency,occupation,industry,geography,limitations,transformation,citation_approach,example_icrs\n',
'data/assumptions.csv':'assumption_id,type,observed_methods,strong_evidence,weak_evidence,authoritative_data,appropriate_context,example_icrs\n'
}
for name,content in files.items():
 p=R/name;p.parent.mkdir(parents=True,exist_ok=True)
 if not p.exists():p.write_text(content)
s={'mission_status':'IN_PROGRESS','current_iteration':0,'icrs_reviewed':0,'agencies_components_reviewed':[],'rubric_version':'1.0.0','canonical_model_version':'0.1.0','current_leaders':{},'current_tsa_benchmark':None,'open_methodological_questions':['See research/open-questions.md'],'unresolved_evidence_gaps':['Governing instructions verification in progress','Seed model extraction and scoring incomplete'],'saturation_streak':0,'next_research_strategy':'Complete authoritative instructions and diverse seed extraction, then select falsifying comparators','updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(R/'research/research-state.json').write_text(json.dumps(s,indent=2))

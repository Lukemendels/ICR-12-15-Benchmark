# Executive summary

**Strong Items 12-15 analysis is a traceable model of obligations, people, activities, resources, and change.** The strongest observed practices make both the arithmetic and the reasons for the inputs visible. They distinguish unique respondents from repeated responses; support activity times and occupational choices; separate compensation, purchases, and Federal resources; and reconcile prior estimates to new estimates through quantified drivers. No single agency in the reviewed evidence supplies the complete model. The most useful benchmark combines complementary practices across collections.[@M1|research/research-summary.md; methodology/exemplars.md]

**TSA demonstrates strong methods, but the evidence does not establish unique best-in-class performance.** The ten reviewed TSA collections span 50-76 points, with a descriptive mean of 67.4 under the study's 100-point rubric. Flight Training Security earns 52 of 60 points on the Item 12 composite, close to the highest observed 53 for two BLS collections. These are assessments of published reconstruction quality in a purposive sample, not estimates of institutional competence or government-wide performance.[@M1|data/scores.csv; data/score-sensitivity.csv; methodology/calibration.md]

**Federal frontier.** BLS illustrates obligation boundaries and phased burden; Census illustrates the importance of measuring preparation as well as questionnaire completion; FCC illustrates exact reconciliation from named baselines; OSHA and the Coast Guard offer useful regulatory and security comparators. Each example has limitations. FCC's precise bridge does not validate every time or wage assumption, and the selected FCC package was withdrawn. A method can be informative without being an endorsed current estimate.[@SRC-0008|Item 12, recording burden and Table 9][@SRC-0099|printed p. 19, burden measurement comparison][@SRC-0064|Item 15 and paragraph 18][@SRC-0063|OIRA conclusion action, July 8, 2025]

**TSA observed practice.** Retain atomic activities, explicit occupation and wage metadata, year-specific cohorts, applicant/employer distinctions, and workload-based Federal costing. Strengthen the connection among these elements. Important published risks include a full-population enrollment calculation with an additional online-renewal subset, a monthly turnover proxy combined with annual mobility, wage-footnote and applied-rate conflicts, and table/narrative values that do not independently reconcile. These observations identify public reconstruction problems; they do not establish what happened in unavailable internal models.[@SRC-0036|Item 12, cohorts and wage footnotes][@SRC-0054|Item 12, Tables 5a-5c][@SRC-0022|Item 12, coordinator updates; Item 14][@SRC-0176|Item 12, applicant wage footnote][@SRC-0038|Item 12, first-flight checklist and Table 2]

**TSA opportunity.** The immediate priority is a common quantitative record that produces the workbook, tables, and narrative together. Pair it with explicit pathway tests, occupation-to-task justifications, cost-scope checks, and separate bridges for responses, hours, and nonlabor dollars. Adopt burden-validation records that retain measurement scope and a ledger assigning obligations to control numbers. Investigate unresolved cost-routing and allocation questions before setting universal defaults.[@M1|methodology/tsa-comparison.md; methodology/tool-requirements.md]

**Implication for the future tool.** The frozen canonical model provides a 27-entity reference architecture. It should support the sequence **structured model → validated calculations → defensible Excel model → Items 12-15 narrative**. Formula preservation, input-level sources, scenario identity, and documented assumptions are essential. Software can prevent avoidable inconsistencies and expose unresolved judgments; it cannot make an unsupported assumption defensible by calculating it precisely.[@M1|methodology/canonical-data-dictionary.md; methodology/canonical-model.md]

**Interpretive boundary.** The evidence comprises 73 unique recent controls across 38 agency/component labels. It is purposive, scored by one analyst, and based on public packages. Selected arithmetic was replayed; complete internal models were not independently replicated. Recent internal TSA process changes may not yet be visible in the public record, and their effects cannot be evaluated from this release.[@M1|research/final-validation.json; research/limitations.md]

\newpage

# 1. Research question and analytical context

TSA's use of burden and cost estimates in policy, program, and regulatory analysis creates a practical need for estimates that are reproducible, well sourced, internally consistent, and defensible. The institutional question is which observable federal practices meet that need, where reviewed TSA methods align with them, and what controls would improve future analysis. The objective is methodological learning with TSA as the principal application case.

Supporting Statement A separates four related outputs. Item 12 describes respondent burden hours and their labor valuation. Item 13 addresses non-hour respondent costs, including applicable capital, operations and maintenance, and purchased services. Item 14 addresses Federal Government costs. Item 15 explains changes in the collection's estimates. Together, these outputs should describe a coherent quantitative system rather than four independently maintained narratives.[@SRC-0001|Items 12-15, pp. 2-3]

The regulatory framework calls for an objectively supported burden estimate. The study treats empirical support as part of the analytical floor, while formula-preserving workbooks, detailed input lineage, and deterministic narrative generation are proposed improvements in reproducibility. It does not present a particular software format as a uniform legal requirement.[@SRC-0025|5 CFR 1320.8(a)(4)][@M1|methodology/requirements-floor.md]

Provenance makes an estimate reviewable and renewable: a reviewer can identify the observed input, its period, its population, and the transformation producing the modeled value. Internal consistency allows downstream users to know which estimate they are reusing. An accurate multiplication cannot compensate for the wrong respondent universe, and a carefully sourced wage cannot resolve an unsupported task-time assumption.

PRA and downstream regulatory analysis may share inputs without sharing the same cost boundary. EBSA's labor methodology explicitly serves both purposes, and the CMMC final-rule analysis provides another concrete connection. The lesson is to preserve shared input lineage while making the scope mapping explicit; reuse alone does not distinguish one agency's methodological quality.[@SRC-0102|p. 1, purpose and labor-cost definition][@SRC-0164|89 FR 83177-83192 and 83211-83213]

# 2. Methodology

## Evidence release and sample

The report uses only frozen evidence release **M1-1.0.0**, rubric **1.0.0**, and canonical model **0.5.0**, identified by repository commit `16aeb85d976eb3a89ecb3872d4dda94753e77cd3`. The package eligibility window is September 9, 2023-September 9, 2026, based on actual OIRA receipt/submission dates. Source upload dates, document dates, and conclusion status are separate. Historical methodological supplements inform the analysis but are not additional recent observations.[@M1|research/mission-2-handoff.md; research/research-state.json]

The 73 reviewed ICRs represent 73 unique controls and 38 agency/component labels, including ten TSA collections. The corpus spans statistical surveys, security and safety compliance, financial reporting, benefits, tax models, and environmental recordkeeping. Components within a department are retained as distinct labels; related controls are not treated as independent replications of agency quality. Appendix A provides the full sample.[@M1|data/icrs.csv; research/limitations.md]

Selection was purposive and directed toward information gain: seek methods, counterexamples, complex cost structures, and TSA-relevant comparators that could change the analytical architecture. This is not a random sample of federal ICRs. No score average, observed frequency, or dispersion estimate is interpreted as a population statistic.[@M1|methodology/sampling-strategy.md; research/research-plan.md]

## Review, scoring, and independent reconstruction

A collection counted as reviewed only after the Supporting Statement was inspected, its analytical structure extracted, and dimension scores assigned with rationale. Nine dimensions total 100 points: reproducibility (20), provenance (15), segmentation (15), labor compensation (10), each of Items 13, 14, and 15 (10 each), validation (5), and consistency (5). Appendix B gives the standards.[@M1|AGENTS.md; methodology/rubric.md; data/scores.csv]

The **Independent Reconstruction Test**, as operationalized in this evidence base, asks whether a reader can move from disclosed populations, frequencies, activities, times, rates, and cost inputs to the reported outputs. It includes inspection of source transformations, scope, periods, and change baselines, plus performed arithmetic checks where recorded. It is a test of accessible reconstruction, not a certification that every internal agency workbook was independently rebuilt.[@M1|methodology/rubric.md; research/final-validation.json; data/calculation-checks.csv]

The freeze contains 267 performed checks: 133 labeled exact, 52 within display rounding, and 82 requiring interpretation. These are selected expressions with unequal coverage by collection, not 267 independent agency outcomes. The labels are numerical screening categories; the interpretation field remains necessary. One HME share check is labeled within rounding despite a semantic partition problem. Appendix E documents this frozen-record inconsistency; this report neither changes it nor treats the counts as an error rate.[@M1|research/final-validation.json; data/calculation-checks.csv, HME Agentpathway share]

## Saturation and challenge

After the sample crossed the minimum evidence gate, two successive strategic batches were classified as saturated at 61 and 69 reviews. The recorded tests covered new major methods, rubric changes, canonical-model changes, material leader changes, source categories, software requirements, and whether ordinary additional ICR reviews were likely to resolve remaining uncertainty. A separate four-collection challenge then examined FinCEN suspicious activity reports, OSHA process safety, EPA chemical reporting, and NASS agricultural surveys, bringing the total to 73.[@M1|research/saturation-log.md; logs/iteration-007-results.md; logs/iteration-008-results.md; logs/iteration-009-results.md]

Saturation means that these targeted searches stopped materially expanding the study's framework. It does not prove that all useful federal practices have been discovered. The remaining gaps chiefly concern unavailable inputs, independent scoring, representative sampling, and interpretive questions. Final validation covered identifiers, joins, source links and archive hashes, date eligibility, score bounds and sums, structured model presence, and replay of recorded arithmetic.[@M1|research/final-validation.json; research/open-questions.md]

## Limitations affecting interpretation

Scores reflect one analyst's judgments; close differences are not established superiority. Complexity categories are qualitative rather than a statistical adjustment. Some current packages contain older analyses, and some were pending or withdrawn. Not every underlying administrative extract, quote, pay table, or model coefficient was available. The machine-readable extraction is a research record, not an executable replica of every collection. All these qualifications apply to both favorable and unfavorable examples.[@M1|methodology/calibration.md; research/limitations.md]

# 3. Interpreting the benchmark

**Scores measure observable public reconstruction quality under the study rubric. They are not direct measures of all internal agency analytical work, institutional competence, or OMB approval quality.** A documentation gap may conceal a strong internal calculation; a detailed public statement may conceal a weak assumption. The evidence does not establish either possibility without further support.[@M1|methodology/rubric.md; research/limitations.md]

A legitimate zero-cost case can earn full credit if the scope and rationale support it. Such a case is not an exemplar of estimating nonzero capital or Federal workload. Simple collections can expose their complete structure briefly. Conversely, extensive segmentation is valuable only when it captures meaningful variation. Document length is not analytical rigor.[@M1|methodology/calibration.md; methodology/exemplars.md]

The Item 12 composite combines the first four rubric dimensions for a maximum of 60 points. It is a useful lens on respondent architecture, provenance, segmentation, and compensation, not a separately validated index. A sensitivity view removes Items 13 and 14 and rescales the remaining 80 points to 100. TSA's descriptive mean becomes 68.375; the broader finding that TSA is not uniquely superior is unchanged. This does not eliminate all applicability or complexity differences.[@M1|data/score-sensitivity.csv; methodology/calibration.md]

The report therefore prioritizes three questions: What is the strongest observed method? What does TSA demonstrate publicly? What practical improvement follows? Scores help locate teaching examples; they do not settle whether a method fits a different collection.

# 4. What strong Items 12-15 analysis looks like

The federal frontier is best understood as a chain:

**Inputs → assumptions → calculations → validation → outputs → Supporting Statement.**

Each link has a distinct function. Inputs identify observed values. Assumptions explain judgments and proxies. Calculations preserve equations and units. Validation tests arithmetic, empirical plausibility, and scope. Outputs summarize a specific model version. The Supporting Statement explains that same version, including its limitations. The frozen model synthesizes these requirements from the reviewed methods and reconstruction risks.[@M1|methodology/canonical-model.md]

| Analytical function | Federal frontier | TSA observed practice | TSA opportunity |
|:--|:--|:--|:--|
| Burden structure | Obligations, actors, activities, and cohorts are explicit | Detailed activities and enrollment pathways | Test partitions and unique-person counts |
| Labor valuation | Occupation, wage basis, benefits, and overhead are distinguishable | SOC/NAICS detail and explicit loading in several cases | Validate task weights and synchronize footnotes |
| Cost boundaries | Internal work, purchases, capital, and Federal resources are separated | Fees and workload equations are often explicit | Preserve gross costs and fee offsets separately |
| Changes | Named baselines and quantified driver bridges | Some old/new totals and described drivers | Generate complete bridges from model versions |
| Validation | Evidence has sample, task scope, period, and statistic | Administrative counts and selected proxies | Add proportionate empirical support for timing and mixes |

Table source: synthesis of the frozen exemplar and TSA comparison artifacts. This table describes transferable practices, not a claim that every federal exemplar satisfies every standard.[@M1|methodology/exemplars.md; methodology/tsa-comparison.md]

Reconstruction and empirical support are complementary. A precisely reproduced estimate can still be weak if its population proxy or time assumption is unsuitable. Likewise, well-supported assumptions lose public usefulness when displayed units or totals conflict. Quality assurance should test both, preserving the difference between an arithmetic defect and a substantive modeling judgment.

# 5. Item 12: respondent burden and labor cost

## Define who does what, how often

A useful starting equation is annual hours equal to eligible entities multiplied by events per entity per year and hours per event. Different respondent segments, activities, modes, and years require distinct rows when they change these terms. Event-based or statistically calibrated models may use a different structure; they should declare it rather than force a misleading population-times-frequency identity.[@M1|methodology/canonical-model.md; methodology/canonical-data-dictionary.md]

Unique respondents must be counted as the union of relevant populations, not the sum of every activity row. The same person can enroll, appeal, and answer a survey. An asset is not automatically a respondent, and a submission is not automatically a unique person. A model should distinguish mutually exclusive paths from additive tasks: an online renewal may replace in-person enrollment, while preparation and employer data entry may be additional activities.[@SRC-0180|Item 12, Tables 1-9][@SRC-0054|Item 12, Tables 5a-5c][@SRC-0176|Item 12, STA applicant and airport data-entry activities]

BLS SOII distinguishes establishments already subject to OSHA recordkeeping from normally exempt establishments newly required to keep records for the survey. This makes the ownership of an obligation visible and avoids treating all recording as newly induced burden. TSA's flight-training model offers another useful structure: year-specific populations reflect transition to a multiyear security threat assessment rather than applying a flat average population before modeling the transition.[@SRC-0008|Item 12, recording burden and Table 9][@SRC-0036|Item 12, candidate and provider cohort tables]

A complete activity model can include effort that does not result in a final submission. NASS separates 196,035 response hours and 10,924 nonresponse hours, totaling 206,959. FinCEN's historical method includes stages that end without filing. These examples suggest a case funnel for screening or compliance work: potential cases, assessments, qualifying cases, filings, and follow-up should have distinct populations and conversion assumptions.[@SRC-0189|Item 12, Tables 1-2][@SRC-0191|85 FR 31605-31611, including Tables 21-22]

## Match occupations to work

For each activity, record the role, occupation code, industry, geography, wage statistic, reference year, and selection rationale. Where several roles contribute, use role-specific hours or justified task shares. National employment shares describe a workforce distribution; they do not by themselves show who performs a collection's work.[@M1|data/assumptions.csv, ASM-0006 and ASM-0007]

TSA's flight-training statement explains an entry-career wage percentile and identifies wage and benefits sources. TWIC provides a transparent seven-occupation basket, but heavy and tractor-trailer truck drivers comprise about 96.7% of its employment weight. The published calculation supports reconstruction of the basket; it does not establish that the basket matches TWIC applicants or their relevant task mix. This is a representativeness question, separate from the calculation's arithmetic.[@SRC-0036|Item 12, wage selection footnotes][@SRC-0180|Item 12, weighted wage table]

## Preserve compensation methods

| Method | Equation | Required distinction |
|:--|:--|:--|
| Direct compensation | $c=C$ | Do not add benefits already included in $C$ |
| Wage plus benefit dollars | $c=w+b$ | Match hourly units and worker universe |
| Wage markup | $c=w(1+m)$ | $m$ is benefits divided by wages |
| Compensation ratio | $c=w(C/W)$ | Preserve the source numerator and denominator |
| Benefit share | $c=w/(1-s)$ | $s$ is benefits divided by total compensation |
| Separate overhead | $l=c+o$ | Define components, allocation base, and nonoverlap |

Here $w$ is the selected hourly wage, $b$ hourly benefits, $C$ and $W$ source compensation and wages, and $o$ hourly overhead. These alternative equations belong in the frozen architecture; they are not interchangeable labels for one generic multiplier.[@M1|methodology/canonical-model.md, compensation alternatives][@SRC-0102|pp. 1-3, compensation and overhead methods]

A matched source ratio does not automatically validate its application to a different occupation or sector. A price update also needs a rationale: an employment-cost index and a broad output-price index measure different changes. Store the original rate and every transformation; updating only the final loaded rate destroys the audit trail.[@SRC-0031|Employment Cost Index, source catalog entry][@SRC-0033|GDP price index, source catalog entry][@M1|data/data-sources.csv; methodology/canonical-data-dictionary.md]

## Validate times as well as totals

The strongest validation evidence matches the population, task boundary, period, and statistic used in the model. Census AIES demonstrates why this matters. Its burden study compares respondent-reported estimates and paradata with different measurement scopes. The overall medians shown are 4.5 hours in the response-analysis survey, 4 hours in the instrument, and 1.1 hours in paradata; these are not three interchangeable estimates of the same mean.[@SRC-0099|printed p. 19, burden table]

Before multiplying a time by a population, identify whether it measures preparation, active completion, elapsed session time, or multiple contributors. A median should not be presented as expected total burden without a justified distributional relationship. Structured expert judgment remains usable when measurement is impractical, but its task assumptions and uncertainty should remain visible.[@M1|data/assumptions.csv, ASM-0001 and ASM-0017; methodology/canonical-model.md]

# 6. Item 13: non-labor respondent costs

A strong Item 13 begins with scope: which information-collection activities require purchases or capital beyond labor already counted? Distinguish equipment, software, systems, purchased professional services, and recurring operations and maintenance. Identify the payer, quantity, price, price year, and whether the cost is one-time or recurring. Explain exclusions and any supported zero.[@SRC-0001|Item 13, pp. 2-3]

OSHA's portable-extinguisher model offers a useful make-or-buy structure. It separates the portion treated as noncustomary from customary work, then divides that portion into in-house and outsourced activity. The observed shares are 15% noncustomary, with 10% in-house and 90% outsourced within that portion. This prevents charging the same work as both respondent employee time and purchased service. Its price and customary-share evidence still require scrutiny before reuse.[@SRC-0060|Items 12-13, annual maintenance and purchased-service calculations]

A supported zero is a scope conclusion, not missing data. Census and BLS provide useful zero-cost cases under the rubric, but they do not demonstrate capital annualization. Conversely, a large positive cost does not establish completeness. No recent case in the frozen sample is certified as a universally complete nonzero capital exemplar.[@M1|methodology/exemplars.md; research/limitations.md, limitation 10]

## Useful life is not the approval period

Capital modeling should retain asset principal, installation scope, purchase cohorts, useful life, replacement schedule, residual value where relevant, and the selected annualization convention. An annual purchase flow should not be divided by an approval horizon simply because approval lasts several years. The model needs separate fields for the service life of an asset and the time span summarized in the ICR.[@M1|methodology/canonical-model.md; data/assumptions.csv, ASM-0011 and ASM-0022]

The historical EPA continuous-emissions-monitoring material illustrates explicit capital recovery. For a principal $P$, rate $r$, and useful life $n$, the annuity is $P r/[1-(1+r)^{-n}]$. The frozen example uses $510,899, ten years, and 7%, with $72,752 reported annually. Recomputing the displayed annuity gives $72,740.52, a residual of $11.48; the report preserves both values. This is a teaching example of a specified method, not a recommended current price, discount rate, or complete PRA scope. Historical engineering costs include boundaries that must be mapped before reuse.[@SRC-0161|Costs sheet, rows 152 and 181-184; Summary Info rows 44-47][@SRC-0162|pp. 2-5, Tables 2-1 through 4-1][@M1|data/claims.jsonl, CLM-FINDING-017]

EPA chemical reporting offers a separate period lesson: its 36-month approval period spans 18 months of one four-year reporting cycle and 18 months of the next. The published analysis prorates those cycles rather than treating reporting periodicity and approval horizon as identical. Its useful method coexists with a summary-table discrepancy and a Federal unit-time mismatch.[@SRC-0183|Tables 3-4 and 6][@M1|logs/iteration-009-results.md]

Financing, respondent payments, and resource cost answer different questions. Keep cash flows, fee payments, and annualized resource estimates identifiable. Official instruction wording contains a purchased-service routing conflict, recorded in the frozen interpretation register. The recommended architecture records payer and economic type separately and requires agency PRA/OIRA resolution before hardcoding a disputed default.[@SRC-0001|Items 12-13][@SRC-0002|pp. 120-121, supporting-statement appendix][@M1|methodology/requirements-floor.md, instruction defects]

# 7. Item 14: Federal Government cost

Federal cost should expose the workload and resources attributable to the collection. For labor, identify review activities, annual workload, time per case, grade or role, locality, pay year, benefits, and the annual-hours divisor if converting annual compensation. Add nonduplicative contractor, system, and operating costs with an allocation rationale. The full program budget is not automatically the collection cost.[@SRC-0001|Item 14][@M1|methodology/canonical-data-dictionary.md, Federal activity and Federal allocation]

TSA's aircraft-operator statement provides three explicit Federal workloads: large-operator verification, small-operator verification, and incidents. The disclosed hours reconstruct as $48\times25+586\times4+1{,}200\times0.25=3{,}844$. This is a useful retained practice even though internal pay components are not independently available and rounded rates leave small dollar residuals.[@SRC-0038|Item 14, workload tables][@M1|data/calculation-checks.csv, aircraft-operator Federal hours and dollars]

Airport security likewise discloses 435 airports, 28.5 hours each, annual compensation of $155,109, and a 2,087-hour denominator. Recalculation yields approximately $921,401 against $921,402 reported. The small residual is qualitatively different from the applicant wage-footnote conflict discussed later. It should prompt a precision check, not an allegation of material Federal cost error.[@SRC-0176|Item 14][@M1|data/calculation-checks.csv, Airport Security Federal check]

Federal zero-cost claims require the same scope discipline as Item 13 zeros. EBSA's settlement collection receives the highest observed Item 14 score for a justified incremental zero; it is not the strongest demonstrated nonzero workload model. Other useful nonzero examples include EPA CSAPR and FAA repair stations. These teach workload decomposition while retaining limitations in pay, contracts, or allocations.[@M1|methodology/exemplars.md][@SRC-0086|Item 14]

Fee recovery does not reconstruct staff, contracts, or systems. TWIC equates the relevant Federal cost estimate with fee revenue, while flight training refers to fee-development analysis. Those links are useful, but a resource ledger is still needed to reproduce the Federal estimate. Store gross resource cost, fee offsets, and net budget effect as separate outputs.[@SRC-0180|Item 14][@SRC-0036|Item 14]

Shared systems require an allocation driver and its complete denominator. CMMC and ETA provide relevant examples for further investigation, but equal shares, total budgets, productive-hour denominators, and vendor prices should not become universal defaults. A vendor price containing profit and an internal staff cost have different interpretations.[@SRC-0164|89 FR 83177-83192, cost analysis][@SRC-0144|Item 14][@M1|data/assumptions.csv, ASM-0020 and ASM-0021]

# 8. Item 15: change reconciliation

The strongest architecture is **old baseline → input or requirement change → reason → classification → quantified effect → new estimate**. Maintain separate bridges for responses, burden hours, and nonlabor cost; a labor-dollar bridge can separately explain rate and workload effects. An arithmetically correct total change is insufficient when the published explanation does not identify its drivers.[@M1|methodology/canonical-model.md, Item 15; methodology/tool-requirements.md, TR-13 and TR-14]

## An exact bridge with two named baselines

The FCC IPCS statement exposes an annual-hours bridge from 6,690 to 15,175: 5,900 hours for new rules, 1,760 for revised rules, and 825 for expanded population. The expansion is described as resulting from the broadened jurisdiction, so the report preserves the agency's program-change classification rather than relabeling every population change as an adjustment.[@SRC-0064|Item 15][@SRC-0063|OIRA conclusion action and date]

![Figure 1. FCC IPCS annual burden bridge: each driver connects the prior baseline to the new estimate. Source: frozen model extraction and calculation checks for one ICR, 202503-3060-020, SRC-0064, Item 15. Units are annual burden hours. The selected package was withdrawn and continued on July 8, 2025; the exhibit illustrates its published method, not an operative approval.](report/figures/fcc-change-bridge.pdf){width=95%}

A second bridge connects the public-notice estimate of 17,555 hours to 15,175. Reducing waiver time from 240 to 100 hours for seven respondents removes 980 hours; reducing one disability-access obligation from 80 to 40 hours for 35 respondents removes 1,400. Together these explain 2,380 hours. Both bridges are correct because they refer to different baselines. The exact arithmetic does not independently validate all underlying timing and wage assumptions.[@SRC-0064|paragraph 18; Items 12 and 15]

## Classify the cause, preserve the lineage

A baseline can mean prior approved inventory, a prior analytical estimate, a regulatory-program baseline, or an earlier notice proposal. Its identity, date, scope, and status should be explicit. ROCIS classifications and an analyst's more detailed causal categories should be stored separately. The recorded guide distinguishes adjustments from changes resulting from deliberate Federal action; a model should retain the authority and reasoning behind each classification.[@SRC-0002|pp. 49-51][@M1|methodology/canonical-data-dictionary.md, Change event]

The Coast Guard provides a close security example: removing 980 two-minute addendum responses produces about 33 fewer annual hours. OSHA process safety provides a larger activity bridge from 2,325,294 to 2,269,066 hours, a decrease of 56,228. These examples link a requirement or population change to an interpretable effect.[@SRC-0174|Item 15, removal of CG-6025A][@SRC-0181|revised calculation supplement, annual responses][@SRC-0187|Table 3 and Item 15]

Transfers between control numbers need paired source and destination entries to prevent omission or double counting. Where both time and population change, driver effects depend on decomposition order unless an interaction is shown explicitly. Statistical recalibration can change estimated hours and purchases without an equivalent change in real obligations; the IRS example makes preserving model version and analytical cause especially important.[@M1|methodology/canonical-model.md, baseline and interaction requirements][@SRC-0094|Items 12-15][@SRC-0100|change supplement]

# 9. How TSA compares

## Strong observable practice

TSA's strongest examples expose meaningful operational detail. Aircraft operators distinguish 18 activities and three Federal workloads. Airports separate applicant time from airport data entry. Flight training preserves transition cohorts and a career-stage wage rationale. TWIC separates enrollment, renewal modes, replacement, pickup, appeals, and survey effort. These practices make future refinement possible without rebuilding the model conceptually.[@SRC-0038|Items 12 and 14][@SRC-0176|Item 12][@SRC-0036|Item 12][@SRC-0180|Item 12, Tables 1-9]

The ten TSA scores range from 50 to 76. The Item 12 composite mean is 46.2 of 60; flight training's 52 is near the observed maximum of 53. This supports recognizing strong methods in particular TSA collections. It does not establish that TSA is unusually rigorous across the full federal population, or that every TSA collection is comparably strong.[@M1|data/scores.csv; data/score-sensitivity.csv]

![Figure 2. TSA and relevant complex comparators show overlapping reconstruction scores. Source: M1-1.0.0, icrs.csv joined to scores.csv. Each point is one reviewed ICR; overlapping values are offset vertically. TSA: n=10. Other components: n=36, selected only for high TSA relevance and high/very-high complexity. This is a descriptive subset of the purposive sample, not matched estimation or an agency ranking. The scale is the complete 0-100 rubric.](report/figures/tsa-comparators.pdf){width=95%}

## Distinct risks require distinct responses

**Inconsistent displayed values.** The aircraft-operator first-flight checklist narrative gives $54,658 while Table 2 gives $20,165,327. The narrative amount also appears for the adjacent foreign-airport employee activity. That pattern is consistent with a copy or versioning issue; the published record establishes the conflict, not the internal editing history. The first-flight table and displayed-rate recomputation are close but not identical, so the report does not substitute a new exact total for the agency's table.[@SRC-0038|Item 12, first-flight checklist, foreign-airport employees, and Table 2]

**Confirmed displayed arithmetic discrepancy.** The certified-cargo program subtotal is 4,451 hours although its displayed component values sum to 6,049, a difference of 1,598. This establishes a discrepancy in the published subtotal. It does not establish whether one component, the subtotal, or an underlying version is the intended estimate. Its fee passage also uses 6,959 assessments while the reported dollars reproduce with 6,859 from Item 12.[@SRC-0040|Item 12, Table 7; Item 13][@M1|data/calculation-checks.csv, Program subtotal and Fee using Item12]

**Pathway and summary risk.** HME's Tables 5a and 5b allocate all agent applicants to in-person pathways, while Table 5c adds online renewal for a subset. The disclosed shares sum to $0.44+0.56+(0.52\times0.60)=1.312$. This is potential duplicated enrollment burden if those are alternative pathways. The report does not infer the correct replacement total without resolving the intended scope. Separately, roughly 519 survey hours become 5,187 in summary tables.[@SRC-0054|Item 12, Tables 5a-5c, 7, 8, and 10]

**Source-transformation risk.** Surface cybersecurity combines a monthly separations proxy with annual residential mobility for contact updates. The event definitions and periods differ; residential moves may not change professional contacts, and overlaps are not resolved. Its Federal displayed rows sum to 1,149 hours against a stated 881. Its package-level hour bridge does reconcile, but that alone does not reconcile the narrative classification and driver explanation.[@SRC-0022|Item 12, coordinator update assumptions; Items 14-15][@SRC-0026|JOLTS FAQ, reference periods][@M1|data/calculation-checks.csv, surface cybersecurity Federal table hours and ROCIS hour bridge]

**Rate/version ambiguity.** Airport applicant calculations use $34.48 per hour, while the stated footnote transformation yields about $50.19. These alternatives materially affect labor valuation, but the evidence does not establish which input was intended. The displayed CHRC fee multiplication produces $58,953,375 against $58,954,925 reported, a $1,550 residual. Keep the large rate conflict distinct from this much smaller displayed-fee residual, which needs a precision and source check.[@SRC-0176|Item 12, applicant wage footnote; Item 13, Table 11]

**Assumption and scope risk.** TWIC's employment-weighted wage basket is calculable but not established as the relevant applicant mix. Fee revenue does not expose its Federal workload. Airport amendment times are attributed to program expertise, but the public record does not supply direct timing evidence. These are support and scope gaps, not arithmetic errors.[@SRC-0180|Items 12 and 14][@SRC-0176|Item 12, amendment-time assumptions]

**Unit and rounding distinctions.** Secure Flight's Federal cost labels conflict, but the footnote and three-year inputs resolve the intended order of magnitude, approximately $156.875 million annually. Flight training's two-hour summary difference and TWIC's one-hour and one-dollar residuals should be treated as precision or reconciliation questions rather than grouped with material pathway or rate conflicts.[@SRC-0048|Item 14, Federal cost table and footnote][@SRC-0036|Item 12, summary hours][@SRC-0180|Items 12-13, totals]

## Relative position and process-change limits

The evidence does not support calling TSA uniquely best-in-class. It also does not establish that TSA is typical or unusually weak government-wide. Methods worth adopting occur in statistical, regulatory, and security collections, including comparators with substantial complexity. Figure 3 shows why total scores alone are inadequate: strength in one dimension coexists with limits elsewhere.[@M1|methodology/calibration.md; methodology/tsa-comparison.md]

![Figure 3. Selected exemplars offer complementary strengths across rubric dimensions. Source: M1-1.0.0, scores.csv and icrs.csv; ten selected teaching examples, not a representative subsample. Cells show raw points; color shows the fraction of each dimension's maximum. Brackets report complexity (L=low, M=medium, H=high, VH=very high) and TSA relevance. A high score for a justified zero does not demonstrate nonzero-cost methodology.](report/figures/dimension-profile.pdf){width=100%}

The two newest reviewed TSA packages were received August 21 and September 1, 2026, and were pending at retrieval. Those dates do not show that a particular internal process was used. Recent internal changes may not yet be visible in public packages, so their effect cannot be evaluated from this release. No before/after or causal conclusion is drawn.[@M1|research/limitations.md, limitation 5; icrs/202606-1652-001/extraction.json; icrs/202606-1652-002/extraction.json]

# 10. TSA action framework

The framework below translates frozen findings into implementation priorities. It is a report recommendation, not an assessment of any office or individual. Preserve source-reported estimates; any proposed correction should be a separately identified analyst scenario.[@M1|methodology/tsa-comparison.md; methodology/canonical-data-dictionary.md]

| Action | Practical requirement | Evidence basis |
|:--|:--|:--|
| **KEEP** | Preserve atomic tasks, applicant/employer distinctions, year-specific cohorts, and explicit wage/loading methods | Aircraft operators; airports; flight training; TWIC |
| **IMPROVE** | Validate pathways and unique populations before summing; retain precise time units and rate periods | HME; surface cybersecurity; TWIC |
| **IMPROVE** | Generate tables, formulas, footnotes, and narrative totals from one version; resolve conflicting displayed rates | Aircraft operators; certified cargo; airports; Secure Flight |
| **IMPROVE** | Support task weights and timing assumptions; separate fee recovery from Federal resources | TWIC; airports; flight training |
| **ADOPT** | Produce named-baseline, driver-level bridges and cross-control obligation records | FCC IPCS; OSHA process safety; BLS SOII; Coast Guard |
| **ADOPT** | Record measurement scope, empirical distributions, make-or-buy shares, and case funnels | Census AIES; OSHA extinguishers; FinCEN |
| **ADOPT** | Separate asset life, replacement cohorts, reporting cycle, and approval horizon | EPA historical CEMS methods; chemical reporting |
| **INVESTIGATE** | Resolve purchased-service routing, overhead allocation, system allocations, and restricted-model replication | Instruction register; EBSA; CMMC; ETA; IRS |

Table source: the frozen TSA KEEP/IMPROVE/ADOPT/INVESTIGATE framework; the associated external sources and qualifications are discussed in Sections 5-9 and 11. Machine-readable action records accompany this report.[@M1|methodology/tsa-comparison.md]

Begin with controls that prevent contradictions within a single package: scenario identity, unit checking, population partitioning, and synchronized outputs. Next, make the change bridge a required model view rather than a closing narrative exercise. Then improve recurring assumptions by collecting task-matched evidence. This order is an implementation judgment based on the observed failure mechanisms, not an estimated ranking of benefits or a quantified return on investment.

# 11. Federal exemplars

An exemplar teaches a bounded method. The following selections are deliberately broader than a list of the highest totals. The highest observed total is BLS SOII at 83, followed closely by EBSA settlement at 82 and OSHA process safety at 80; those differences do not establish meaningful superiority.[@M1|methodology/exemplars.md; data/scores.csv]

| Teaching purpose | Example | Transferable lesson and limit |
|:--|:--|:--|
| Overall reconstruction and provenance | BLS SOII | Activity/sector/year tables and obligation boundaries; Federal budget detail remains limited |
| Item 12 and compensation | BLS NCS; TSA flight training | Phases, nonresponse, direct compensation or explicit wage loading; task-fit still matters |
| Nonzero purchased costs | OSHA extinguishers; FCC satellite | Quantities, make-or-buy structure, price evidence; revalidate scope and aging quotes |
| Capital method | Historical EPA CEMS | Explicit principal, life, and rate; not current prices or an entire PRA model |
| Federal workload | TSA aircraft operators and airports | Workload × time × compensation; internal pay and precision limits remain |
| Incremental Federal zero | EBSA settlement | A justified zero can be strong; it is not a nonzero workload exemplar |
| Item 15 | FCC IPCS | Two named baseline bridges; selected package withdrawn and assumptions remain contestable |
| Burden validation | Census AIES | Preparation, instrument estimates, and paradata differ in scope and statistic |
| Close security comparator | Coast Guard security | Obligation overlap and addendum removal; underlying administrative query unavailable |
| Close regulatory comparator | OSHA process safety | Coverage adjustments and activity bridge; stale displayed response entries remain |
| Methodological counterexample | SEC ADV-E | Compact arithmetic can be transparent; narrow scope limits transfer |
| Shared labor methodology | EBSA labor-cost appendix | Explicit occupation/overhead allocation; its worked example needs independent checking |

The examples and limits are retained from the frozen exemplar review. BLS's $32.91 compensation observation illustrates the need to inspect provenance even in a leading case: it matches September 2023 data released in December, while the statement labels the reference period December. Publication and observation dates should be separate fields.[@M1|methodology/exemplars.md][@SRC-0200|USDL 23-2567, civilian sales and office occupations row][@SRC-0008|Item 12, compensation reference]

BLS NCS, the FCC satellite statement, SEC ADV-E, and EBSA settlement provide the source-specific methods summarized above. The examples do not warrant importing their assumptions unchanged into TSA models.[@SRC-0078|Item 12][@SRC-0068|Items 13-14][@SRC-0012|Items 12-15][@SRC-0086|Items 12-15]

# 12. Authoritative data source catalog

Source authority is necessary but not sufficient. A source can measure its own universe well while being an unsuitable proxy for a collection. For each observation retain publisher, dataset or series, table and row, reference period, release vintage, unit, geography, population, retrieval date, and transformation. Appendix D and the accompanying machine-readable catalog retain all 28 frozen entries.[@M1|data/data-sources.csv; methodology/canonical-data-dictionary.md]

| Analytical function | Useful source families | Appropriate use and transformation | Principal limitation |
|:--|:--|:--|:--|
| Occupations and wages | BLS OEWS | Annual SOC/NAICS wage observations; justify statistic and task mix | Wages exclude benefits; suppressed cells and role mismatch |
| Compensation and benefits | BLS ECEC | Quarterly group compensation or total/wage ratio | Match worker universe; do not add benefits twice |
| Wage/compensation updating | BLS ECI | Quarterly index ratio between stated periods | An index is not a wage level |
| Establishments and industry | Census CBP | Annual counts by industry, geography, and size | Establishment is not firm; exclusions and suppression |
| Employment and projections | BLS CES; Employment Projections | Monthly earnings/employment or annual projection releases | Earnings, net growth, and openings are different concepts |
| Asset/population proxies | EIA CBECS; MECS | Building/floorspace or manufacturing data with explicit mappings | Assets are not respondents; coverage and uncertainty |
| Price updating | BEA GDP price index; BLS PPI | Justified index ratio with price-year preservation | Broad prices may poorly match wages, IT, or equipment |
| Federal labor | OPM base/locality tables | Annual grade/step pay; published hourly rate or stated divisor | Benefits and contracts require separate evidence |
| Overhead | Historical Census ASM/SAS; EBSA method | Remove direct costs and retain occupation/industry allocation | Average expense is not necessarily marginal collection cost |
| Program workload | Dated administrative extracts | Counts, filters, coverage, and case stages | Restricted queries may not be independently reproducible |

The source families and transformations above are drawn from the frozen catalog, not a fresh market scan. OEWS, ECEC, ECI, CBP, OPM, EIA, CES, and price-index entries have distinct reference periods and update cycles. Appendix D supplies source-level citations and cautions, including archival-access limits.[@M1|data/data-sources.csv]

Administrative sources often provide the best population fit: RMP facility records in OSHA process safety, MISLE security-plan counts in Coast Guard analysis, and BSA E-Filing statistics in FinCEN. A published aggregate is usable evidence, but it does not make the underlying restricted query independently reproducible. Preserve extraction date and query definition, and label what remains inaccessible.[@SRC-0187|Item 12, March 2025 RMP coverage][@SRC-0174|Item 12, MISLE population description][@SRC-0185|Item 12, calendar 2022 submissions]

Future users should refresh inputs as part of a new model version. They should not silently replace historical values in the benchmark. A stale-source warning should distinguish an old but still justified observation from an unsupported carry-forward assumption.

# 13. Assumption and validation framework

The report recommends the following evidence hierarchy as a review aid, synthesized from the frozen assumption library. It is not a new empirical scoring scale. Fit to the modeled task and population can matter more than nominal rank.[@M1|data/assumptions.csv]

| Evidence level | Expected documentation |
|:--|:--|
| Directly measured activity | Task boundaries, mode, sample, date, active/elapsed time, distribution |
| Administrative program data | System, query filters, coverage, entity definition, extraction date |
| Authoritative external statistics | Universe, codes, geography, period, uncertainty, proxy transformation |
| Validated historical experience | Original basis, changed conditions, revalidation evidence |
| Structured expert judgment | Roles consulted, task decomposition, rationale, range, review date |
| Unsupported assumption | Explicit unresolved status and analyst decision needed |

Burden time, frequency, labor mix, manager or legal review, familiarization, and recordkeeping each need their own evidence boundaries. A management percentage should not duplicate hours already counted in preparation. Familiarization may be one-time for entrants and recurring only for changed material. Recordkeeping should distinguish creation from retention or retrieval. System costs need implementation scope and recurring operations; useful life needs replacement evidence; Federal workload needs an attributable activity or allocation driver.[@M1|data/assumptions.csv, ASM-0001 through ASM-0013 and ASM-0019 through ASM-0024]

Validation should distinguish four questions: Does the arithmetic reproduce? Are the inputs empirically plausible? Is the relevant scope complete without duplication? Do tables, narrative, and inventory agree? A model can pass one and fail another. The tool should expose this distinction and leave material unsupported inputs unresolved rather than replacing them with zeros.[@M1|methodology/canonical-model.md; methodology/tool-requirements.md, TR-20]

FinCEN illustrates a useful practice in responding to contrary evidence: it discusses a survey of 15 large banks yielding 21.41 hours per report against the retained 1.98-hour estimate and identifies coverage limitations. The transferable method is explicit assessment of conflicting evidence. Rejecting an unrepresentative alternative does not itself validate the retained mean.[@SRC-0185|Item 8, public comments and responses][@SRC-0191|85 FR 31605-31611]

Uncertainty analysis should be proportionate. A simple collection may need a documented timing check; a heterogeneous or consequential model may need ranges, scenarios, or calibration diagnostics. The frozen rubric does not require elaborate sensitivity analysis for every simple collection.[@M1|methodology/rubric.md]

# 14. Canonical Items 12-15 model

The frozen version 0.5.0 is a research reference architecture, not implemented software. It contains 27 entities spanning collection identity, scenarios, evidence, populations, activities, labor, purchases, Federal resources, assumptions, statistical models, formulas, validation, changes, and outputs. Appendix F preserves the entity-level contract.[@M1|methodology/canonical-data-dictionary.md]

## Relationships and core calculations

A **collection** owns versioned **scenarios**. A scenario identifies policy dates, price year, analysis horizon, and baseline. **Sources** and **evidence locators** support population observations, rates, prices, and assumptions. **Segments** define eligibility and overlap. **Obligations** link legal requirements to activities and owning control numbers. **Activities** link exposure/frequency, time estimates, and labor roles. Labor roles connect wage observations to compensation methods and separate overhead allocations.[@M1|methodology/canonical-data-dictionary.md, Collection through Price transformation]

**Purchased services** record quantities and unit prices; **capital cohorts** retain acquisition year, life, replacement, and annualization. **Federal activities** and **allocations** record attributable labor, contracts, and systems independently of fee offsets. **Statistical model** nodes permit calibrated predictions when a simple workload product is inadequate. **Validation observations** retain empirical scope, while **validation results** record model-check outcomes.[@M1|methodology/canonical-data-dictionary.md, Purchased service through Validation result]

For a bottom-up model, annual hours are the sum of eligible population × annual frequency × task time across applicable activities. Labor dollars sum role-hours × compensation plus justified nonoverlapping overhead. Item 13 combines scoped purchases and annualized capital. Item 14 combines attributable Federal labor and other resources. Item 15 compares named model versions and records quantified change events, including a declared convention for interactions.[@M1|methodology/canonical-model.md]

Every numeric input should retain a stable identifier, value, unit, period, source and locator, observation/assumption status, method, applicability, and review responsibility. Formula nodes retain their dependencies and full precision. Source-reported values and independent recomputations remain separate; a corrected scenario never overwrites source evidence.[@M1|methodology/canonical-model.md; methodology/canonical-data-dictionary.md]

## Model → Excel → Supporting Statement

The workbook should expose linked views for inputs and sources, assumptions, respondent activities and labor, purchases and capital, Federal costs, prior baselines, change bridges, validation, and output tables. It should preserve formulas rather than merely export calculated numbers. The narrative should bind to the same scenario and output identifiers, including source-aware footnotes and unresolved-input flags.[@M1|methodology/canonical-model.md, freeze note]

This design turns a renewal into an explicit input and requirement update. Analysts can identify what changed, recompute the effects, and regenerate the explanation. It also permits a reviewer to move backward from a sentence or table cell to the formula, assumption, and source that support it.

# 15. Requirements for a future ICR modeling and review tool

The priorities below are Mission 2 implementation judgments mapped to the frozen TR-01 through TR-20 specification. They organize development without changing the reference architecture. The proposed production flow is **structured model → validated calculations → defensible Excel model → Items 12-15 narrative**.[@M1|methodology/tool-requirements.md]

## Must have

| Requirement | Acceptance condition | Frozen basis |
|:--|:--|:--|
| Atomic, sourced inputs | Every material input has unit, period, source, locator, transformation, and observation/assumption flag | TR-01, 03, 18, 20 |
| Role and compensation metadata | Occupation choice, wage vintage, loading method, denominator, and overhead remain explicit | TR-06, 07 |
| Pathway and population validation | Exclusive shares reconcile; overlaps and unique respondents are handled explicitly | TR-04, 05 |
| Cost scope and capital | Internal work, services, fees, assets, life, and cohorts are distinct; no automatic division by approval years | TR-09, 10, 11 |
| Federal resource model | Workload, grades/pay, benefits, contracts, and allocation denominators reproduce | TR-12 |
| Versioned change bridges | Separate responses/hours/nonlabor bridges; named baselines and paired control transfers | TR-08, 13, 14, 17 |
| Arithmetic and dimensional QA | Formula evaluation independent of caches; unit, period, and total checks; tolerance and disposition retained | TR-03, 19 |
| Reproducible outputs | Excel formulas, tables, and narrative share one scenario; unsupported inputs cannot be invented | TR-02, 19, 20 |
| Review warnings | Missing/stale sources, unsupported assumptions, inconsistent totals, and unresolved classifications are visible | TR-01, 18, 20 |

## Should have

Store validation observations with task scope, samples, and statistics; produce source-refresh reports; support occupation-overhead allocation matrices where justified; expose alternate assumptions and interaction decompositions; and allow a reviewer to trace an output back through its complete dependency chain. Preserve statistical-model metadata and restricted-input status even when the first implementation cannot reproduce a particular calibrated model.[@M1|methodology/tool-requirements.md, TR-07, 15, 16, and 18; methodology/canonical-data-dictionary.md]

## Future / optional

Full calibrated-model execution, controlled-access replication workflows, and evidence-grounded comparison with analogous collections can follow the core deterministic model. A synthetic replication example for restricted models is a proposed capability, not an observed feature of the reviewed IRS package. None of these extensions is implemented in this report.[@M1|methodology/canonical-model.md, iteration 4 additions]

The tool should distinguish blocking arithmetic or identity defects from warnings requiring judgment. Exact thresholds and workflow permissions require later design. The report specifies necessary evidence and behavior, not a completed production system or settled policy interpretation.

# 16. Implications for future evidence-based review

The frozen corpus and report comparison tables can later support an evidence graph centered on internal TSA consistency. Comparable activities can be grouped by collection shape: enrollment paths, recordkeeping, review roles, security-plan amendments, case funnels, and shared system costs. Comparisons should retain units, periods, respondent scope, evidence quality, and source transformations before declaring an assumption an outlier.[@M1|data/model-sections.jsonl; data/assumptions.csv; methodology/canonical-data-dictionary.md]

An outlier is a review question, not an automatic error. Different legal scope, complexity, modes, or populations may justify different times or costs. External federal analogues should supply candidate methods and questions; they should not overwrite TSA-specific evidence simply because their scores are higher.

The accompanying normalized tables preserve ICR IDs, dimension rationales, source IDs, locators, risk classifications, action categories, and requirement mappings. They provide a starting point for later graph construction without re-extracting the reviewed corpus. Peripheral model rows still require semantic normalization before executable reuse. This report builds neither the graph nor the future review application.[@M1|research/limitations.md, limitation 7]

# 17. Conclusions

The observed federal frontier is a supported, publicly reconstructable chain linking requirements to populations, activities, resources, and changes. Its strongest elements are distributed across agencies. A defensible model combines explicit scope, task-matched evidence, transparent compensation, nonduplicative purchases, attributable Federal costs, and named-baseline reconciliation.[@M1|research/research-summary.md; methodology/exemplars.md]

TSA contributes valuable methods: atomic activities, operational segmentation, occupation metadata, cohorts, and workload equations. The principal observable risks arise when those elements are not consistently connected: pathway duplication, unmatched periods or units, weak task-weight evidence, conflicting displayed values, and incomplete change explanations. The evidence supports strengthening these controls, not drawing conclusions about undisclosed internal work.[@M1|methodology/tsa-comparison.md]

The reviewed sample does not establish unique TSA superiority, nor does it establish a government-wide agency ranking. The useful institutional response is to retain demonstrated strengths, improve public reconstruction, adopt complementary practices, and resolve disputed assumptions and cost conventions explicitly. A source-bound, versioned model can make those disciplines routine and produce a workbook and Supporting Statement that remain traceable through future renewals.[@M1|methodology/calibration.md; methodology/canonical-model.md]

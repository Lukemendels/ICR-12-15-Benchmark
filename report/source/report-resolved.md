# Executive summary

**Strong Items 12-15 analysis is a traceable model of obligations, people, activities, resources, and change.** The strongest observed practices make both the arithmetic and the reasons for the inputs visible. They distinguish unique respondents from repeated responses; support activity times and occupational choices; separate compensation, purchases, and Federal resources; and reconcile prior estimates to new estimates through quantified drivers. No single agency in the reviewed evidence supplies the complete model. The most useful benchmark combines complementary practices across collections.[^1]

**TSA demonstrates strong methods, but the evidence does not establish unique best-in-class performance.** The ten reviewed TSA collections span 50-76 points, with a descriptive mean of 67.4 under the study's 100-point rubric. Flight Training Security earns 52 of 60 points on the Item 12 composite, close to the highest observed 53 for two BLS collections. These are assessments of published reconstruction quality in a purposive sample, not estimates of institutional competence or government-wide performance.[^2]

**Federal frontier.** BLS illustrates obligation boundaries and phased burden; Census illustrates the importance of measuring preparation as well as questionnaire completion; FCC illustrates exact reconciliation from named baselines; OSHA and the Coast Guard offer useful regulatory and security comparators. Each example has limitations. FCC's precise bridge does not validate every time or wage assumption, and the selected FCC package was withdrawn. A method can be informative without being an endorsed current estimate.[^3]\textsuperscript{,}[^4]\textsuperscript{,}[^5]\textsuperscript{,}[^6]

**TSA observed practice.** Retain atomic activities, explicit occupation and wage metadata, year-specific cohorts, applicant/employer distinctions, and workload-based Federal costing. Strengthen the connection among these elements. Important published risks include a full-population enrollment calculation with an additional online-renewal subset, a monthly turnover proxy combined with annual mobility, wage-footnote and applied-rate conflicts, and table/narrative values that do not independently reconcile. These observations identify public reconstruction problems; they do not establish what happened in unavailable internal models.[^7]\textsuperscript{,}[^8]\textsuperscript{,}[^9]\textsuperscript{,}[^10]\textsuperscript{,}[^11]

**TSA opportunity.** The immediate priority is a common quantitative record that produces the workbook, tables, and narrative together. Pair it with explicit pathway tests, occupation-to-task justifications, cost-scope checks, and separate bridges for responses, hours, and nonlabor dollars. Adopt burden-validation records that retain measurement scope and a ledger assigning obligations to control numbers. Investigate unresolved cost-routing and allocation questions before setting universal defaults.[^12]

**Implication for the future tool.** The frozen canonical model provides a 27-entity reference architecture. It should support the sequence **structured model → validated calculations → defensible Excel model → Items 12-15 narrative**. Formula preservation, input-level sources, scenario identity, and documented assumptions are essential. Software can prevent avoidable inconsistencies and expose unresolved judgments; it cannot make an unsupported assumption defensible by calculating it precisely.[^13]

**Interpretive boundary.** The evidence comprises 73 unique recent controls across 38 agency/component labels. It is purposive, scored by one analyst, and based on public packages. Selected arithmetic was replayed; complete internal models were not independently replicated. Recent internal TSA process changes may not yet be visible in the public record, and their effects cannot be evaluated from this release.[^14]

\newpage

# 1. Research question and analytical context

TSA's use of burden and cost estimates in policy, program, and regulatory analysis creates a practical need for estimates that are reproducible, well sourced, internally consistent, and defensible. The institutional question is which observable federal practices meet that need, where reviewed TSA methods align with them, and what controls would improve future analysis. The objective is methodological learning with TSA as the principal application case.

Supporting Statement A separates four related outputs. Item 12 describes respondent burden hours and their labor valuation. Item 13 addresses non-hour respondent costs, including applicable capital, operations and maintenance, and purchased services. Item 14 addresses Federal Government costs. Item 15 explains changes in the collection's estimates. Together, these outputs should describe a coherent quantitative system rather than four independently maintained narratives.[^15]

The regulatory framework calls for an objectively supported burden estimate. The study treats empirical support as part of the analytical floor, while formula-preserving workbooks, detailed input lineage, and deterministic narrative generation are proposed improvements in reproducibility. It does not present a particular software format as a uniform legal requirement.[^16]\textsuperscript{,}[^17]

Provenance makes an estimate reviewable and renewable: a reviewer can identify the observed input, its period, its population, and the transformation producing the modeled value. Internal consistency allows downstream users to know which estimate they are reusing. An accurate multiplication cannot compensate for the wrong respondent universe, and a carefully sourced wage cannot resolve an unsupported task-time assumption.

PRA and downstream regulatory analysis may share inputs without sharing the same cost boundary. EBSA's labor methodology explicitly serves both purposes, and the CMMC final-rule analysis provides another concrete connection. The lesson is to preserve shared input lineage while making the scope mapping explicit; reuse alone does not distinguish one agency's methodological quality.[^18]\textsuperscript{,}[^19]

# 2. Methodology

## Evidence release and sample

The report uses only frozen evidence release **M1-1.0.0**, rubric **1.0.0**, and canonical model **0.5.0**, identified by repository commit `16aeb85d976eb3a89ecb3872d4dda94753e77cd3`. The package eligibility window is September 9, 2023-September 9, 2026, based on actual OIRA receipt/submission dates. Source upload dates, document dates, and conclusion status are separate. Historical methodological supplements inform the analysis but are not additional recent observations.[^20]

The 73 reviewed ICRs represent 73 unique controls and 38 agency/component labels, including ten TSA collections. The corpus spans statistical surveys, security and safety compliance, financial reporting, benefits, tax models, and environmental recordkeeping. Components within a department are retained as distinct labels; related controls are not treated as independent replications of agency quality. Appendix A provides the full sample.[^21]

Selection was purposive and directed toward information gain: seek methods, counterexamples, complex cost structures, and TSA-relevant comparators that could change the analytical architecture. This is not a random sample of federal ICRs. No score average, observed frequency, or dispersion estimate is interpreted as a population statistic.[^22]

## Review, scoring, and independent reconstruction

A collection counted as reviewed only after the Supporting Statement was inspected, its analytical structure extracted, and dimension scores assigned with rationale. Nine dimensions total 100 points: reproducibility (20), provenance (15), segmentation (15), labor compensation (10), each of Items 13, 14, and 15 (10 each), validation (5), and consistency (5). Appendix B gives the standards.[^23]

The **Independent Reconstruction Test**, as operationalized in this evidence base, asks whether a reader can move from disclosed populations, frequencies, activities, times, rates, and cost inputs to the reported outputs. It includes inspection of source transformations, scope, periods, and change baselines, plus performed arithmetic checks where recorded. It is a test of accessible reconstruction, not a certification that every internal agency workbook was independently rebuilt.[^24]

The freeze contains 267 performed checks: 133 labeled exact, 52 within display rounding, and 82 requiring interpretation. These are selected expressions with unequal coverage by collection, not 267 independent agency outcomes. The labels are numerical screening categories; the interpretation field remains necessary. One HME share check is labeled within rounding despite a semantic partition problem. Appendix E documents this frozen-record inconsistency; this report neither changes it nor treats the counts as an error rate.[^25]

## Saturation and challenge

After the sample crossed the minimum evidence gate, two successive strategic batches were classified as saturated at 61 and 69 reviews. The recorded tests covered new major methods, rubric changes, canonical-model changes, material leader changes, source categories, software requirements, and whether ordinary additional ICR reviews were likely to resolve remaining uncertainty. A separate four-collection challenge then examined FinCEN suspicious activity reports, OSHA process safety, EPA chemical reporting, and NASS agricultural surveys, bringing the total to 73.[^26]

Saturation means that these targeted searches stopped materially expanding the study's framework. It does not prove that all useful federal practices have been discovered. The remaining gaps chiefly concern unavailable inputs, independent scoring, representative sampling, and interpretive questions. Final validation covered identifiers, joins, source links and archive hashes, date eligibility, score bounds and sums, structured model presence, and replay of recorded arithmetic.[^27]

## Limitations affecting interpretation

Scores reflect one analyst's judgments; close differences are not established superiority. Complexity categories are qualitative rather than a statistical adjustment. Some current packages contain older analyses, and some were pending or withdrawn. Not every underlying administrative extract, quote, pay table, or model coefficient was available. The machine-readable extraction is a research record, not an executable replica of every collection. All these qualifications apply to both favorable and unfavorable examples.[^28]

# 3. Interpreting the benchmark

**Scores measure observable public reconstruction quality under the study rubric. They are not direct measures of all internal agency analytical work, institutional competence, or OMB approval quality.** A documentation gap may conceal a strong internal calculation; a detailed public statement may conceal a weak assumption. The evidence does not establish either possibility without further support.[^29]

A legitimate zero-cost case can earn full credit if the scope and rationale support it. Such a case is not an exemplar of estimating nonzero capital or Federal workload. Simple collections can expose their complete structure briefly. Conversely, extensive segmentation is valuable only when it captures meaningful variation. Document length is not analytical rigor.[^30]

The Item 12 composite combines the first four rubric dimensions for a maximum of 60 points. It is a useful lens on respondent architecture, provenance, segmentation, and compensation, not a separately validated index. A sensitivity view removes Items 13 and 14 and rescales the remaining 80 points to 100. TSA's descriptive mean becomes 68.375; the broader finding that TSA is not uniquely superior is unchanged. This does not eliminate all applicability or complexity differences.[^31]

The report therefore prioritizes three questions: What is the strongest observed method? What does TSA demonstrate publicly? What practical improvement follows? Scores help locate teaching examples; they do not settle whether a method fits a different collection.

# 4. What strong Items 12-15 analysis looks like

The federal frontier is best understood as a chain:

**Inputs → assumptions → calculations → validation → outputs → Supporting Statement.**

Each link has a distinct function. Inputs identify observed values. Assumptions explain judgments and proxies. Calculations preserve equations and units. Validation tests arithmetic, empirical plausibility, and scope. Outputs summarize a specific model version. The Supporting Statement explains that same version, including its limitations. The frozen model synthesizes these requirements from the reviewed methods and reconstruction risks.[^32]

| Analytical function | Federal frontier | TSA observed practice | TSA opportunity |
|:--|:--|:--|:--|
| Burden structure | Obligations, actors, activities, and cohorts are explicit | Detailed activities and enrollment pathways | Test partitions and unique-person counts |
| Labor valuation | Occupation, wage basis, benefits, and overhead are distinguishable | SOC/NAICS detail and explicit loading in several cases | Validate task weights and synchronize footnotes |
| Cost boundaries | Internal work, purchases, capital, and Federal resources are separated | Fees and workload equations are often explicit | Preserve gross costs and fee offsets separately |
| Changes | Named baselines and quantified driver bridges | Some old/new totals and described drivers | Generate complete bridges from model versions |
| Validation | Evidence has sample, task scope, period, and statistic | Administrative counts and selected proxies | Add proportionate empirical support for timing and mixes |

Table source: synthesis of the frozen exemplar and TSA comparison artifacts. This table describes transferable practices, not a claim that every federal exemplar satisfies every standard.[^33]

Reconstruction and empirical support are complementary. A precisely reproduced estimate can still be weak if its population proxy or time assumption is unsuitable. Likewise, well-supported assumptions lose public usefulness when displayed units or totals conflict. Quality assurance should test both, preserving the difference between an arithmetic defect and a substantive modeling judgment.

# 5. Item 12: respondent burden and labor cost

## Define who does what, how often

A useful starting equation is annual hours equal to eligible entities multiplied by events per entity per year and hours per event. Different respondent segments, activities, modes, and years require distinct rows when they change these terms. Event-based or statistically calibrated models may use a different structure; they should declare it rather than force a misleading population-times-frequency identity.[^34]

Unique respondents must be counted as the union of relevant populations, not the sum of every activity row. The same person can enroll, appeal, and answer a survey. An asset is not automatically a respondent, and a submission is not automatically a unique person. A model should distinguish mutually exclusive paths from additive tasks: an online renewal may replace in-person enrollment, while preparation and employer data entry may be additional activities.[^35]\textsuperscript{,}[^36]\textsuperscript{,}[^37]

BLS SOII distinguishes establishments already subject to OSHA recordkeeping from normally exempt establishments newly required to keep records for the survey. This makes the ownership of an obligation visible and avoids treating all recording as newly induced burden. TSA's flight-training model offers another useful structure: year-specific populations reflect transition to a multiyear security threat assessment rather than applying a flat average population before modeling the transition.[^38]\textsuperscript{,}[^39]

A complete activity model can include effort that does not result in a final submission. NASS separates 196,035 response hours and 10,924 nonresponse hours, totaling 206,959. FinCEN's historical method includes stages that end without filing. These examples suggest a case funnel for screening or compliance work: potential cases, assessments, qualifying cases, filings, and follow-up should have distinct populations and conversion assumptions.[^40]\textsuperscript{,}[^41]

## Match occupations to work

For each activity, record the role, occupation code, industry, geography, wage statistic, reference year, and selection rationale. Where several roles contribute, use role-specific hours or justified task shares. National employment shares describe a workforce distribution; they do not by themselves show who performs a collection's work.[^42]

TSA's flight-training statement explains an entry-career wage percentile and identifies wage and benefits sources. TWIC provides a transparent seven-occupation basket, but heavy and tractor-trailer truck drivers comprise about 96.7% of its employment weight. The published calculation supports reconstruction of the basket; it does not establish that the basket matches TWIC applicants or their relevant task mix. This is a representativeness question, separate from the calculation's arithmetic.[^43]\textsuperscript{,}[^44]

## Preserve compensation methods

| Method | Equation | Required distinction |
|:--|:--|:--|
| Direct compensation | $c=C$ | Do not add benefits already included in $C$ |
| Wage plus benefit dollars | $c=w+b$ | Match hourly units and worker universe |
| Wage markup | $c=w(1+m)$ | $m$ is benefits divided by wages |
| Compensation ratio | $c=w(C/W)$ | Preserve the source numerator and denominator |
| Benefit share | $c=w/(1-s)$ | $s$ is benefits divided by total compensation |
| Separate overhead | $l=c+o$ | Define components, allocation base, and nonoverlap |

Here $w$ is the selected hourly wage, $b$ hourly benefits, $C$ and $W$ source compensation and wages, and $o$ hourly overhead. These alternative equations belong in the frozen architecture; they are not interchangeable labels for one generic multiplier.[^45]\textsuperscript{,}[^46]

A matched source ratio does not automatically validate its application to a different occupation or sector. A price update also needs a rationale: an employment-cost index and a broad output-price index measure different changes. Store the original rate and every transformation; updating only the final loaded rate destroys the audit trail.[^47]\textsuperscript{,}[^48]\textsuperscript{,}[^49]

## Validate times as well as totals

The strongest validation evidence matches the population, task boundary, period, and statistic used in the model. Census AIES demonstrates why this matters. Its burden study compares respondent-reported estimates and paradata with different measurement scopes. The overall medians shown are 4.5 hours in the response-analysis survey, 4 hours in the instrument, and 1.1 hours in paradata; these are not three interchangeable estimates of the same mean.[^50]

Before multiplying a time by a population, identify whether it measures preparation, active completion, elapsed session time, or multiple contributors. A median should not be presented as expected total burden without a justified distributional relationship. Structured expert judgment remains usable when measurement is impractical, but its task assumptions and uncertainty should remain visible.[^51]

# 6. Item 13: non-labor respondent costs

A strong Item 13 begins with scope: which information-collection activities require purchases or capital beyond labor already counted? Distinguish equipment, software, systems, purchased professional services, and recurring operations and maintenance. Identify the payer, quantity, price, price year, and whether the cost is one-time or recurring. Explain exclusions and any supported zero.[^52]

OSHA's portable-extinguisher model offers a useful make-or-buy structure. It separates the portion treated as noncustomary from customary work, then divides that portion into in-house and outsourced activity. The observed shares are 15% noncustomary, with 10% in-house and 90% outsourced within that portion. This prevents charging the same work as both respondent employee time and purchased service. Its price and customary-share evidence still require scrutiny before reuse.[^53]

A supported zero is a scope conclusion, not missing data. Census and BLS provide useful zero-cost cases under the rubric, but they do not demonstrate capital annualization. Conversely, a large positive cost does not establish completeness. No recent case in the frozen sample is certified as a universally complete nonzero capital exemplar.[^54]

## Useful life is not the approval period

Capital modeling should retain asset principal, installation scope, purchase cohorts, useful life, replacement schedule, residual value where relevant, and the selected annualization convention. An annual purchase flow should not be divided by an approval horizon simply because approval lasts several years. The model needs separate fields for the service life of an asset and the time span summarized in the ICR.[^55]

The historical EPA continuous-emissions-monitoring material illustrates explicit capital recovery. For a principal $P$, rate $r$, and useful life $n$, the annuity is $P r/[1-(1+r)^{-n}]$. The frozen example uses $510,899, ten years, and 7%, with $72,752 reported annually. Recomputing the displayed annuity gives $72,740.52, a residual of $11.48; the report preserves both values. This is a teaching example of a specified method, not a recommended current price, discount rate, or complete PRA scope. Historical engineering costs include boundaries that must be mapped before reuse.[^56]\textsuperscript{,}[^57]\textsuperscript{,}[^58]

EPA chemical reporting offers a separate period lesson: its 36-month approval period spans 18 months of one four-year reporting cycle and 18 months of the next. The published analysis prorates those cycles rather than treating reporting periodicity and approval horizon as identical. Its useful method coexists with a summary-table discrepancy and a Federal unit-time mismatch.[^59]\textsuperscript{,}[^60]

Financing, respondent payments, and resource cost answer different questions. Keep cash flows, fee payments, and annualized resource estimates identifiable. Official instruction wording contains a purchased-service routing conflict, recorded in the frozen interpretation register. The recommended architecture records payer and economic type separately and requires agency PRA/OIRA resolution before hardcoding a disputed default.[^61]\textsuperscript{,}[^62]\textsuperscript{,}[^63]

# 7. Item 14: Federal Government cost

Federal cost should expose the workload and resources attributable to the collection. For labor, identify review activities, annual workload, time per case, grade or role, locality, pay year, benefits, and the annual-hours divisor if converting annual compensation. Add nonduplicative contractor, system, and operating costs with an allocation rationale. The full program budget is not automatically the collection cost.[^64]\textsuperscript{,}[^65]

TSA's aircraft-operator statement provides three explicit Federal workloads: large-operator verification, small-operator verification, and incidents. The disclosed hours reconstruct as $48\times25+586\times4+1{,}200\times0.25=3{,}844$. This is a useful retained practice even though internal pay components are not independently available and rounded rates leave small dollar residuals.[^66]\textsuperscript{,}[^67]

Airport security likewise discloses 435 airports, 28.5 hours each, annual compensation of $155,109, and a 2,087-hour denominator. Recalculation yields approximately $921,401 against $921,402 reported. The small residual is qualitatively different from the applicant wage-footnote conflict discussed later. It should prompt a precision check, not an allegation of material Federal cost error.[^68]\textsuperscript{,}[^69]

Federal zero-cost claims require the same scope discipline as Item 13 zeros. EBSA's settlement collection receives the highest observed Item 14 score for a justified incremental zero; it is not the strongest demonstrated nonzero workload model. Other useful nonzero examples include EPA CSAPR and FAA repair stations. These teach workload decomposition while retaining limitations in pay, contracts, or allocations.[^70]\textsuperscript{,}[^71]

Fee recovery does not reconstruct staff, contracts, or systems. TWIC equates the relevant Federal cost estimate with fee revenue, while flight training refers to fee-development analysis. Those links are useful, but a resource ledger is still needed to reproduce the Federal estimate. Store gross resource cost, fee offsets, and net budget effect as separate outputs.[^72]\textsuperscript{,}[^73]

Shared systems require an allocation driver and its complete denominator. CMMC and ETA provide relevant examples for further investigation, but equal shares, total budgets, productive-hour denominators, and vendor prices should not become universal defaults. A vendor price containing profit and an internal staff cost have different interpretations.[^74]\textsuperscript{,}[^75]\textsuperscript{,}[^76]

# 8. Item 15: change reconciliation

The strongest architecture is **old baseline → input or requirement change → reason → classification → quantified effect → new estimate**. Maintain separate bridges for responses, burden hours, and nonlabor cost; a labor-dollar bridge can separately explain rate and workload effects. An arithmetically correct total change is insufficient when the published explanation does not identify its drivers.[^77]

## An exact bridge with two named baselines

The FCC IPCS statement exposes an annual-hours bridge from 6,690 to 15,175: 5,900 hours for new rules, 1,760 for revised rules, and 825 for expanded population. The expansion is described as resulting from the broadened jurisdiction, so the report preserves the agency's program-change classification rather than relabeling every population change as an adjustment.[^78]\textsuperscript{,}[^79]

![Figure 1. FCC IPCS annual burden bridge: each driver connects the prior baseline to the new estimate. Source: frozen model extraction and calculation checks for one ICR, 202503-3060-020, SRC-0064, Item 15. Units are annual burden hours. The selected package was withdrawn and continued on July 8, 2025; the exhibit illustrates its published method, not an operative approval.](report/figures/fcc-change-bridge.pdf){width=95%}

A second bridge connects the public-notice estimate of 17,555 hours to 15,175. Reducing waiver time from 240 to 100 hours for seven respondents removes 980 hours; reducing one disability-access obligation from 80 to 40 hours for 35 respondents removes 1,400. Together these explain 2,380 hours. Both bridges are correct because they refer to different baselines. The exact arithmetic does not independently validate all underlying timing and wage assumptions.[^80]

## Classify the cause, preserve the lineage

A baseline can mean prior approved inventory, a prior analytical estimate, a regulatory-program baseline, or an earlier notice proposal. Its identity, date, scope, and status should be explicit. ROCIS classifications and an analyst's more detailed causal categories should be stored separately. The recorded guide distinguishes adjustments from changes resulting from deliberate Federal action; a model should retain the authority and reasoning behind each classification.[^81]\textsuperscript{,}[^82]

The Coast Guard provides a close security example: removing 980 two-minute addendum responses produces about 33 fewer annual hours. OSHA process safety provides a larger activity bridge from 2,325,294 to 2,269,066 hours, a decrease of 56,228. These examples link a requirement or population change to an interpretable effect.[^83]\textsuperscript{,}[^84]\textsuperscript{,}[^85]

Transfers between control numbers need paired source and destination entries to prevent omission or double counting. Where both time and population change, driver effects depend on decomposition order unless an interaction is shown explicitly. Statistical recalibration can change estimated hours and purchases without an equivalent change in real obligations; the IRS example makes preserving model version and analytical cause especially important.[^86]\textsuperscript{,}[^87]\textsuperscript{,}[^88]

# 9. How TSA compares

## Strong observable practice

TSA's strongest examples expose meaningful operational detail. Aircraft operators distinguish 18 activities and three Federal workloads. Airports separate applicant time from airport data entry. Flight training preserves transition cohorts and a career-stage wage rationale. TWIC separates enrollment, renewal modes, replacement, pickup, appeals, and survey effort. These practices make future refinement possible without rebuilding the model conceptually.[^89]\textsuperscript{,}[^90]\textsuperscript{,}[^91]\textsuperscript{,}[^92]

The ten TSA scores range from 50 to 76. The Item 12 composite mean is 46.2 of 60; flight training's 52 is near the observed maximum of 53. This supports recognizing strong methods in particular TSA collections. It does not establish that TSA is unusually rigorous across the full federal population, or that every TSA collection is comparably strong.[^93]

![Figure 2. TSA and relevant complex comparators show overlapping reconstruction scores. Source: M1-1.0.0, icrs.csv joined to scores.csv. Each point is one reviewed ICR; overlapping values are offset vertically. TSA: n=10. Other components: n=36, selected only for high TSA relevance and high/very-high complexity. This is a descriptive subset of the purposive sample, not matched estimation or an agency ranking. The scale is the complete 0-100 rubric.](report/figures/tsa-comparators.pdf){width=95%}

## Distinct risks require distinct responses

**Inconsistent displayed values.** The aircraft-operator first-flight checklist narrative gives $54,658 while Table 2 gives $20,165,327. The narrative amount also appears for the adjacent foreign-airport employee activity. That pattern is consistent with a copy or versioning issue; the published record establishes the conflict, not the internal editing history. The first-flight table and displayed-rate recomputation are close but not identical, so the report does not substitute a new exact total for the agency's table.[^94]

**Confirmed displayed arithmetic discrepancy.** The certified-cargo program subtotal is 4,451 hours although its displayed component values sum to 6,049, a difference of 1,598. This establishes a discrepancy in the published subtotal. It does not establish whether one component, the subtotal, or an underlying version is the intended estimate. Its fee passage also uses 6,959 assessments while the reported dollars reproduce with 6,859 from Item 12.[^95]\textsuperscript{,}[^96]

**Pathway and summary risk.** HME's Tables 5a and 5b allocate all agent applicants to in-person pathways, while Table 5c adds online renewal for a subset. The disclosed shares sum to $0.44+0.56+(0.52\times0.60)=1.312$. This is potential duplicated enrollment burden if those are alternative pathways. The report does not infer the correct replacement total without resolving the intended scope. Separately, roughly 519 survey hours become 5,187 in summary tables.[^97]

**Source-transformation risk.** Surface cybersecurity combines a monthly separations proxy with annual residential mobility for contact updates. The event definitions and periods differ; residential moves may not change professional contacts, and overlaps are not resolved. Its Federal displayed rows sum to 1,149 hours against a stated 881. Its package-level hour bridge does reconcile, but that alone does not reconcile the narrative classification and driver explanation.[^98]\textsuperscript{,}[^99]\textsuperscript{,}[^100]

**Rate/version ambiguity.** Airport applicant calculations use $34.48 per hour, while the stated footnote transformation yields about $50.19. These alternatives materially affect labor valuation, but the evidence does not establish which input was intended. The displayed CHRC fee multiplication produces $58,953,375 against $58,954,925 reported, a $1,550 residual. Keep the large rate conflict distinct from this much smaller displayed-fee residual, which needs a precision and source check.[^101]

**Assumption and scope risk.** TWIC's employment-weighted wage basket is calculable but not established as the relevant applicant mix. Fee revenue does not expose its Federal workload. Airport amendment times are attributed to program expertise, but the public record does not supply direct timing evidence. These are support and scope gaps, not arithmetic errors.[^102]\textsuperscript{,}[^103]

**Unit and rounding distinctions.** Secure Flight's Federal cost labels conflict, but the footnote and three-year inputs resolve the intended order of magnitude, approximately $156.875 million annually. Flight training's two-hour summary difference and TWIC's one-hour and one-dollar residuals should be treated as precision or reconciliation questions rather than grouped with material pathway or rate conflicts.[^104]\textsuperscript{,}[^105]\textsuperscript{,}[^106]

## Relative position and process-change limits

The evidence does not support calling TSA uniquely best-in-class. It also does not establish that TSA is typical or unusually weak government-wide. Methods worth adopting occur in statistical, regulatory, and security collections, including comparators with substantial complexity. Figure 3 shows why total scores alone are inadequate: strength in one dimension coexists with limits elsewhere.[^107]

![Figure 3. Selected exemplars offer complementary strengths across rubric dimensions. Source: M1-1.0.0, scores.csv and icrs.csv; ten selected teaching examples, not a representative subsample. Cells show raw points; color shows the fraction of each dimension's maximum. Brackets report complexity (L=low, M=medium, H=high, VH=very high) and TSA relevance. A high score for a justified zero does not demonstrate nonzero-cost methodology.](report/figures/dimension-profile.pdf){width=100%}

The two newest reviewed TSA packages were received August 21 and September 1, 2026, and were pending at retrieval. Those dates do not show that a particular internal process was used. Recent internal changes may not yet be visible in public packages, so their effect cannot be evaluated from this release. No before/after or causal conclusion is drawn.[^108]

# 10. TSA action framework

The framework below translates frozen findings into implementation priorities. It is a report recommendation, not an assessment of any office or individual. Preserve source-reported estimates; any proposed correction should be a separately identified analyst scenario.[^109]

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

Table source: the frozen TSA KEEP/IMPROVE/ADOPT/INVESTIGATE framework; the associated external sources and qualifications are discussed in Sections 5-9 and 11. Machine-readable action records accompany this report.[^110]

Begin with controls that prevent contradictions within a single package: scenario identity, unit checking, population partitioning, and synchronized outputs. Next, make the change bridge a required model view rather than a closing narrative exercise. Then improve recurring assumptions by collecting task-matched evidence. This order is an implementation judgment based on the observed failure mechanisms, not an estimated ranking of benefits or a quantified return on investment.

# 11. Federal exemplars

An exemplar teaches a bounded method. The following selections are deliberately broader than a list of the highest totals. The highest observed total is BLS SOII at 83, followed closely by EBSA settlement at 82 and OSHA process safety at 80; those differences do not establish meaningful superiority.[^111]

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

The examples and limits are retained from the frozen exemplar review. BLS's $32.91 compensation observation illustrates the need to inspect provenance even in a leading case: it matches September 2023 data released in December, while the statement labels the reference period December. Publication and observation dates should be separate fields.[^112]\textsuperscript{,}[^113]\textsuperscript{,}[^114]

BLS NCS, the FCC satellite statement, SEC ADV-E, and EBSA settlement provide the source-specific methods summarized above. The examples do not warrant importing their assumptions unchanged into TSA models.[^115]\textsuperscript{,}[^116]\textsuperscript{,}[^117]\textsuperscript{,}[^118]

# 12. Authoritative data source catalog

Source authority is necessary but not sufficient. A source can measure its own universe well while being an unsuitable proxy for a collection. For each observation retain publisher, dataset or series, table and row, reference period, release vintage, unit, geography, population, retrieval date, and transformation. Appendix D and the accompanying machine-readable catalog retain all 28 frozen entries.[^119]

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

The source families and transformations above are drawn from the frozen catalog, not a fresh market scan. OEWS, ECEC, ECI, CBP, OPM, EIA, CES, and price-index entries have distinct reference periods and update cycles. Appendix D supplies source-level citations and cautions, including archival-access limits.[^120]

Administrative sources often provide the best population fit: RMP facility records in OSHA process safety, MISLE security-plan counts in Coast Guard analysis, and BSA E-Filing statistics in FinCEN. A published aggregate is usable evidence, but it does not make the underlying restricted query independently reproducible. Preserve extraction date and query definition, and label what remains inaccessible.[^121]\textsuperscript{,}[^122]\textsuperscript{,}[^123]

Future users should refresh inputs as part of a new model version. They should not silently replace historical values in the benchmark. A stale-source warning should distinguish an old but still justified observation from an unsupported carry-forward assumption.

# 13. Assumption and validation framework

The report recommends the following evidence hierarchy as a review aid, synthesized from the frozen assumption library. It is not a new empirical scoring scale. Fit to the modeled task and population can matter more than nominal rank.[^124]

| Evidence level | Expected documentation |
|:--|:--|
| Directly measured activity | Task boundaries, mode, sample, date, active/elapsed time, distribution |
| Administrative program data | System, query filters, coverage, entity definition, extraction date |
| Authoritative external statistics | Universe, codes, geography, period, uncertainty, proxy transformation |
| Validated historical experience | Original basis, changed conditions, revalidation evidence |
| Structured expert judgment | Roles consulted, task decomposition, rationale, range, review date |
| Unsupported assumption | Explicit unresolved status and analyst decision needed |

Burden time, frequency, labor mix, manager or legal review, familiarization, and recordkeeping each need their own evidence boundaries. A management percentage should not duplicate hours already counted in preparation. Familiarization may be one-time for entrants and recurring only for changed material. Recordkeeping should distinguish creation from retention or retrieval. System costs need implementation scope and recurring operations; useful life needs replacement evidence; Federal workload needs an attributable activity or allocation driver.[^125]

Validation should distinguish four questions: Does the arithmetic reproduce? Are the inputs empirically plausible? Is the relevant scope complete without duplication? Do tables, narrative, and inventory agree? A model can pass one and fail another. The tool should expose this distinction and leave material unsupported inputs unresolved rather than replacing them with zeros.[^126]

FinCEN illustrates a useful practice in responding to contrary evidence: it discusses a survey of 15 large banks yielding 21.41 hours per report against the retained 1.98-hour estimate and identifies coverage limitations. The transferable method is explicit assessment of conflicting evidence. Rejecting an unrepresentative alternative does not itself validate the retained mean.[^127]\textsuperscript{,}[^128]

Uncertainty analysis should be proportionate. A simple collection may need a documented timing check; a heterogeneous or consequential model may need ranges, scenarios, or calibration diagnostics. The frozen rubric does not require elaborate sensitivity analysis for every simple collection.[^129]

# 14. Canonical Items 12-15 model

The frozen version 0.5.0 is a research reference architecture, not implemented software. It contains 27 entities spanning collection identity, scenarios, evidence, populations, activities, labor, purchases, Federal resources, assumptions, statistical models, formulas, validation, changes, and outputs. Appendix F preserves the entity-level contract.[^130]

## Relationships and core calculations

A **collection** owns versioned **scenarios**. A scenario identifies policy dates, price year, analysis horizon, and baseline. **Sources** and **evidence locators** support population observations, rates, prices, and assumptions. **Segments** define eligibility and overlap. **Obligations** link legal requirements to activities and owning control numbers. **Activities** link exposure/frequency, time estimates, and labor roles. Labor roles connect wage observations to compensation methods and separate overhead allocations.[^131]

**Purchased services** record quantities and unit prices; **capital cohorts** retain acquisition year, life, replacement, and annualization. **Federal activities** and **allocations** record attributable labor, contracts, and systems independently of fee offsets. **Statistical model** nodes permit calibrated predictions when a simple workload product is inadequate. **Validation observations** retain empirical scope, while **validation results** record model-check outcomes.[^132]

For a bottom-up model, annual hours are the sum of eligible population × annual frequency × task time across applicable activities. Labor dollars sum role-hours × compensation plus justified nonoverlapping overhead. Item 13 combines scoped purchases and annualized capital. Item 14 combines attributable Federal labor and other resources. Item 15 compares named model versions and records quantified change events, including a declared convention for interactions.[^133]

Every numeric input should retain a stable identifier, value, unit, period, source and locator, observation/assumption status, method, applicability, and review responsibility. Formula nodes retain their dependencies and full precision. Source-reported values and independent recomputations remain separate; a corrected scenario never overwrites source evidence.[^134]

## Model → Excel → Supporting Statement

The workbook should expose linked views for inputs and sources, assumptions, respondent activities and labor, purchases and capital, Federal costs, prior baselines, change bridges, validation, and output tables. It should preserve formulas rather than merely export calculated numbers. The narrative should bind to the same scenario and output identifiers, including source-aware footnotes and unresolved-input flags.[^135]

This design turns a renewal into an explicit input and requirement update. Analysts can identify what changed, recompute the effects, and regenerate the explanation. It also permits a reviewer to move backward from a sentence or table cell to the formula, assumption, and source that support it.

# 15. Requirements for a future ICR modeling and review tool

The priorities below are Mission 2 implementation judgments mapped to the frozen TR-01 through TR-20 specification. They organize development without changing the reference architecture. The proposed production flow is **structured model → validated calculations → defensible Excel model → Items 12-15 narrative**.[^136]

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

Store validation observations with task scope, samples, and statistics; produce source-refresh reports; support occupation-overhead allocation matrices where justified; expose alternate assumptions and interaction decompositions; and allow a reviewer to trace an output back through its complete dependency chain. Preserve statistical-model metadata and restricted-input status even when the first implementation cannot reproduce a particular calibrated model.[^137]

## Future / optional

Full calibrated-model execution, controlled-access replication workflows, and evidence-grounded comparison with analogous collections can follow the core deterministic model. A synthetic replication example for restricted models is a proposed capability, not an observed feature of the reviewed IRS package. None of these extensions is implemented in this report.[^138]

The tool should distinguish blocking arithmetic or identity defects from warnings requiring judgment. Exact thresholds and workflow permissions require later design. The report specifies necessary evidence and behavior, not a completed production system or settled policy interpretation.

# 16. Implications for future evidence-based review

The frozen corpus and report comparison tables can later support an evidence graph centered on internal TSA consistency. Comparable activities can be grouped by collection shape: enrollment paths, recordkeeping, review roles, security-plan amendments, case funnels, and shared system costs. Comparisons should retain units, periods, respondent scope, evidence quality, and source transformations before declaring an assumption an outlier.[^139]

An outlier is a review question, not an automatic error. Different legal scope, complexity, modes, or populations may justify different times or costs. External federal analogues should supply candidate methods and questions; they should not overwrite TSA-specific evidence simply because their scores are higher.

The accompanying normalized tables preserve ICR IDs, dimension rationales, source IDs, locators, risk classifications, action categories, and requirement mappings. They provide a starting point for later graph construction without re-extracting the reviewed corpus. Peripheral model rows still require semantic normalization before executable reuse. This report builds neither the graph nor the future review application.[^140]

# 17. Conclusions

The observed federal frontier is a supported, publicly reconstructable chain linking requirements to populations, activities, resources, and changes. Its strongest elements are distributed across agencies. A defensible model combines explicit scope, task-matched evidence, transparent compensation, nonduplicative purchases, attributable Federal costs, and named-baseline reconciliation.[^141]

TSA contributes valuable methods: atomic activities, operational segmentation, occupation metadata, cohorts, and workload equations. The principal observable risks arise when those elements are not consistently connected: pathway duplication, unmatched periods or units, weak task-weight evidence, conflicting displayed values, and incomplete change explanations. The evidence supports strengthening these controls, not drawing conclusions about undisclosed internal work.[^142]

The reviewed sample does not establish unique TSA superiority, nor does it establish a government-wide agency ranking. The useful institutional response is to retain demonstrated strengths, improve public reconstruction, adopt complementary practices, and resolve disputed assumptions and cost conventions explicitly. A source-bound, versioned model can make those disciplines routine and produce a workbook and Supporting Statement that remain traceable through future renewals.[^143]

\newpage

# Appendix A. Complete reviewed sample

All 73 observations are shown in agency/ICR order, not score order. Dates are actual OIRA receipt dates; the ICR reference prefix is not a submission date. Scores are within-sample public reconstruction judgments. Full titles, archetypes, complexity, relevance, and source IDs are preserved in `report/tables/benchmark-comparison.csv`.[^144]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.19\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.14\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.48\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.12\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.07\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{ICR reference} & \textbf{Component} & \textbf{Collection} & \textbf{Received} & \textbf{/\allowbreak{}100} \\
\midrule\endfirsthead
\toprule
\textbf{ICR reference} & \textbf{Component} & \textbf{Collection} & \textbf{Received} & \textbf{/\allowbreak{}100} \\
\midrule\endhead
\bottomrule\endfoot
202412-3170-001 & CFPB & Required Rulemaking on Personal Financial Data Rights & 12/\allowbreak{}06/\allowbreak{}2024 & 54 \\
202602-3170-003 & CFPB & Home Mortgage Disclosure Act (Regulation C) & 02/\allowbreak{}27/\allowbreak{}2026 & 46 \\
202306-3038-007 & CFTC & Swap Data Recordkeeping and Reporting Requirements & 09/\allowbreak{}13/\allowbreak{}2023 & 67 \\
202402-1652-002 & DHS/\allowbreak{}TSA & Air Cargo Security Requirements & 03/\allowbreak{}27/\allowbreak{}2024 & 64 \\
202405-1652-001 & DHS/\allowbreak{}TSA & Flight Training Security Program & 05/\allowbreak{}14/\allowbreak{}2024 & 74 \\
202406-1652-001 & DHS/\allowbreak{}TSA & Aircraft Operator Security, 49 CFR Part 1544 & 06/\allowbreak{}26/\allowbreak{}2024 & 76 \\
202408-1652-002 & DHS/\allowbreak{}TSA & Certified Cargo Screening Program & 09/\allowbreak{}06/\allowbreak{}2024 & 60 \\
202411-1652-007 & DHS/\allowbreak{}TSA & TSA Claims Application & 12/\allowbreak{}17/\allowbreak{}2024 & 68 \\
202412-1652-001 & DHS/\allowbreak{}TSA & Airport Security Part 1542 & 03/\allowbreak{}20/\allowbreak{}2025 & 71 \\
202504-1652-008 & DHS/\allowbreak{}TSA & Transportation Worker Identification Credential & 05/\allowbreak{}05/\allowbreak{}2025 & 75 \\
202508-1652-001 & DHS/\allowbreak{}TSA & Secure Flight Program & 12/\allowbreak{}11/\allowbreak{}2025 & 70 \\
202606-1652-001 & DHS/\allowbreak{}TSA & Cybersecurity Measures for Surface Modes & 09/\allowbreak{}01/\allowbreak{}2026 & 66 \\
202606-1652-002 & DHS/\allowbreak{}TSA & Security Threat Assessment for Individuals Applying for a Hazardous Materials Endorsement for a Commercial Driver's License & 08/\allowbreak{}21/\allowbreak{}2026 & 50 \\
202411-1651-004 & DHS/\allowbreak{}USCBP & Global Interoperability Standards (GIS) & 02/\allowbreak{}12/\allowbreak{}2025 & 57 \\
202408-1625-012 & DHS/\allowbreak{}USCG & Security Plan for Ports, Vessels, Facilities, Outer Continental Shelf Facilities and Other Security-Related Requirements & 09/\allowbreak{}30/\allowbreak{}2024 & 77 \\
202401-1615-055 & DHS/\allowbreak{}USCIS & Petition to Remove the Conditions on Residence & 02/\allowbreak{}08/\allowbreak{}2024 & 69 \\
202310-0607-003 & DOC/\allowbreak{}CENSUS & Annual Integrated Economic Survey & 10/\allowbreak{}31/\allowbreak{}2023 & 74 \\
202403-0607-001 & DOC/\allowbreak{}CENSUS & Quarterly Services Survey & 03/\allowbreak{}11/\allowbreak{}2024 & 74 \\
202602-0607-001 & DOC/\allowbreak{}CENSUS & Annual Business Survey & 02/\allowbreak{}17/\allowbreak{}2026 & 71 \\
202402-0648-005 & DOC/\allowbreak{}NOAA & NMFS Alaska Region Vessel Monitoring System (VMS) Program & 02/\allowbreak{}20/\allowbreak{}2024 & 70 \\
202504-1004-001 & DOI/\allowbreak{}BLM & Leasing of Solid Minerals Other Than Coal and Oil Shale (43 CFR 3500-3590) & 07/\allowbreak{}17/\allowbreak{}2025 & 73 \\
202310-1220-004 & DOL/\allowbreak{}BLS & National Compensation Survey & 01/\allowbreak{}31/\allowbreak{}2024 & 78 \\
202404-1220-001 & DOL/\allowbreak{}BLS & Survey of Occupational Injuries and Illnesses & 07/\allowbreak{}01/\allowbreak{}2024 & 83 \\
202405-1220-001 & DOL/\allowbreak{}BLS & Cognitive and Psychological Research & 06/\allowbreak{}10/\allowbreak{}2024 & 69 \\
202501-1210-006 & DOL/\allowbreak{}EBSA & Settlement Agreements Between a Plan and a Party in Interest & 04/\allowbreak{}14/\allowbreak{}2025 & 82 \\
202603-1210-004 & DOL/\allowbreak{}EBSA & Employee Benefit Plan Claims Procedure Under the Employee Retirement Income Security Act & 04/\allowbreak{}03/\allowbreak{}2026 & 71 \\
202412-1205-002 & DOL/\allowbreak{}ETA & Claims and Payment Activities & 01/\allowbreak{}15/\allowbreak{}2025 & 77 \\
202310-1219-001 & DOL/\allowbreak{}MSHA & Respirable Crystalline Silica Standard & 04/\allowbreak{}18/\allowbreak{}2024 & 73 \\
202403-1219-001 & DOL/\allowbreak{}MSHA & Respiratory Protection Program at Coal Mines & 08/\allowbreak{}15/\allowbreak{}2024 & 72 \\
202405-1218-005 & DOL/\allowbreak{}OSHA & Portable Fire Extinguishers Standard (Annual Maintenance Certification Record) (29 CFR 1910.157(e)(3)) & 07/\allowbreak{}09/\allowbreak{}2024 & 78 \\
202411-1218-005 & DOL/\allowbreak{}OSHA & Occupational Safety and Health Act Variance Regulations (29 CFR 1905.10, 1905.11 and 1905.12) & 01/\allowbreak{}16/\allowbreak{}2025 & 69 \\
202505-1218-008 & DOL/\allowbreak{}OSHA & Benzene Standard (29 CFR 1910.1028) & 01/\allowbreak{}26/\allowbreak{}2026 & 77 \\
202508-1218-005 & DOL/\allowbreak{}OSHA & Standard on Process Safety Management of Highly Hazardous Chemicals (29 CFR 1910.119, 29 CFR 1926.64) & 02/\allowbreak{}04/\allowbreak{}2026 & 80 \\
202404-1240-007 & DOL/\allowbreak{}OWCP & Claim for Medical Reimbursement Form & 05/\allowbreak{}30/\allowbreak{}2024 & 64 \\
202404-2120-002 & DOT/\allowbreak{}FAA & Certification and Operation of Repair Stations, 14 CFR Part 145 & 08/\allowbreak{}29/\allowbreak{}2024 & 69 \\
202409-2126-001 & DOT/\allowbreak{}FMCSA & Quantitative Data on Safety Belt Usage of Commercial Motor Vehicle Drivers & 11/\allowbreak{}22/\allowbreak{}2024 & 60 \\
202508-2126-007 & DOT/\allowbreak{}FMCSA & Hours of Service (HOS) of Drivers Regulations & 09/\allowbreak{}15/\allowbreak{}2025 & 61 \\
202506-2130-004 & DOT/\allowbreak{}FRA & Hours of Service Regulations & 07/\allowbreak{}09/\allowbreak{}2025 & 67 \\
202311-2137-001 & DOT/\allowbreak{}PHMSA & Hazardous Materials Security Plans & 11/\allowbreak{}14/\allowbreak{}2023 & 64 \\
202404-2137-003 & DOT/\allowbreak{}PHMSA & Approvals for Hazardous Materials & 04/\allowbreak{}12/\allowbreak{}2024 & 68 \\
202405-0704-001 & DOW/\allowbreak{}DODDEP & Cybersecurity Maturity Model Certification (CMMC) Enterprise Mission Assurance Support-Service (eMASS) Instantiation Information Collection & 06/\allowbreak{}26/\allowbreak{}2024 & 72 \\
202405-0704-002 & DOW/\allowbreak{}DODDEP & Cybersecurity Maturity Model Certification (CMMC) Program Reporting and Recordkeeping Requirements Information Collection & 06/\allowbreak{}25/\allowbreak{}2024 & 75 \\
202502-2060-039 & EPA/\allowbreak{}OAR & National Emission Standards for Hazardous Air Pollutants (NESHAP) from Manufacturing of Nutritional Yeast (40 CFR Part 60, CCCC) (Renewal) & 02/\allowbreak{}28/\allowbreak{}2025 & 67 \\
202504-2060-006 & EPA/\allowbreak{}OAR & Acid Rain Program under Title IV of the Clean Air Act Amendments (Renewal) & 05/\allowbreak{}30/\allowbreak{}2025 & 67 \\
202505-2060-004 & EPA/\allowbreak{}OAR & Cross-State Air Pollution Rule and Texas SO2 Trading Programs (Renewal) & 05/\allowbreak{}30/\allowbreak{}2025 & 73 \\
202509-2060-003 & EPA/\allowbreak{}OAR & NESHAP for Gasoline Distribution Bulk Terminals, Bulk Plants, Pipeline Facilities and Gasoline Dispensing Facilities (40 CFR part 63, subparts BBBBBB and CCCCCC) (Final Rule) & 09/\allowbreak{}30/\allowbreak{}2025 & 68 \\
202602-2060-006 & EPA/\allowbreak{}OAR & NESHAP for Hazardous Waste Combustors (40 CFR Part 63, Subpart EEE) (Proposed Rule) & 02/\allowbreak{}27/\allowbreak{}2026 & 74 \\
202401-2070-005 & EPA/\allowbreak{}OCSPP & Chemical Data Reporting under the Toxic Substances Control Act (TSCA) (Non-Substantive Change) & 02/\allowbreak{}01/\allowbreak{}2024 & 76 \\
202411-2070-003 & EPA/\allowbreak{}OCSPP & Toxic Chemical Release Reporting (Revision/\allowbreak{}Consolidation) & 11/\allowbreak{}27/\allowbreak{}2024 & 75 \\
202312-2050-001 & EPA/\allowbreak{}OLEM & Alternate PCB Extraction Methods and Amendments to PCB Cleanup and Disposal Regulations (Final Rule) & 01/\allowbreak{}10/\allowbreak{}2024 & 71 \\
202502-2040-002 & EPA/\allowbreak{}OW & 2022 National Pollutant Discharge Elimination System General Permit for Discharges from Construction Activities (Renewal) & 02/\allowbreak{}28/\allowbreak{}2025 & 71 \\
202503-3060-020 & FCC & Incarcerated People’s Communications Services (IPCS) Provider Annual Reporting, Certification, and Other Requirements, WC Docket Nos. 23-62, 12-375 & 04/\allowbreak{}01/\allowbreak{}2025 & 76 \\
202505-3060-038 & FCC & Part 25 of the Federal Communications Commission's Rules Governing the Licensing of, and Spectrum Usage By, Commercial Earth Stations and Space Stations & 05/\allowbreak{}28/\allowbreak{}2025 & 69 \\
202504-1902-007 & FERC & FERC Form No. 60 (Annual Reports Of Centralized Service Cos.), FERC-61 (Narrative Description Of Service Co, FERC-555A (Preservation of Records Companies \& Service Cos) & 05/\allowbreak{}16/\allowbreak{}2025 & 69 \\
202507-1902-004 & FERC & FERC-725A, RD25-5 Mandatory Reliability Standards for the Bulk-Power System & 07/\allowbreak{}30/\allowbreak{}2025 & 64 \\
202410-7100-005 & FRS & Recordkeeping and Disclosure Requirements Associated with CFPB's Regulation B & 01/\allowbreak{}24/\allowbreak{}2025 & 58 \\
202405-0938-022 & HHS/\allowbreak{}CMS & Proposed Prior Authorization Process and Requirements for Certain Hospital Outpatient Department (OPD) Services (CMS-10711) & 05/\allowbreak{}24/\allowbreak{}2024 & 65 \\
202506-0938-007 & HHS/\allowbreak{}CMS & Hospitals and Health Care Complex Cost Report (CMS-2552-10) & 06/\allowbreak{}11/\allowbreak{}2025 & 60 \\
202403-0910-005 & HHS/\allowbreak{}FDA & Premarket Tobacco Product Applications and Recordkeeping Requirements & 11/\allowbreak{}27/\allowbreak{}2024 & 60 \\
202410-0910-013 & HHS/\allowbreak{}FDA & Current Good Manufacturing Practice and Hazard Analysis and Risk-Based Preventive Controls For Human Food and Food for Animals & 10/\allowbreak{}29/\allowbreak{}2024 & 64 \\
202410-3150-005 & NRC & 10 CFR Part 50, Domestic Licensing of Production and Utilization Facilities & 10/\allowbreak{}24/\allowbreak{}2024 & 73 \\
202401-3235-005 & SEC & Form PF and Rule 204(b)-1 & 01/\allowbreak{}11/\allowbreak{}2024 & 61 \\
202409-3235-022 & SEC & Form ADV-E, cover sheet for each certificate of accounting of client securities and funds in the custody of an investment adviser & 12/\allowbreak{}13/\allowbreak{}2024 & 76 \\
202502-3235-014 & SEC & Interactive Data & 06/\allowbreak{}24/\allowbreak{}2025 & 53 \\
202504-3235-016 & SEC & Rule 206(4)-2, Custody of Funds or Securities of Clients by Investment Advisers & 08/\allowbreak{}01/\allowbreak{}2025 & 68 \\
202410-0960-002 & SSA & Disability Report-Appeal & 10/\allowbreak{}22/\allowbreak{}2024 & 62 \\
202502-0960-015 & SSA & Social Security Benefits Application & 03/\allowbreak{}18/\allowbreak{}2025 & 64 \\
202405-1506-005 & TREAS/\allowbreak{}FINCEN & FinCEN Form 111 - Suspicious Activity Report & 05/\allowbreak{}31/\allowbreak{}2024 & 68 \\
202511-1545-005 & TREAS/\allowbreak{}IRS & U.S. Business Income Tax Returns & 12/\allowbreak{}15/\allowbreak{}2025 & 73 \\
202506-0551-003 & USDA/\allowbreak{}FAS & Technical Assistance for Specialty Crops & 08/\allowbreak{}08/\allowbreak{}2025 & 70 \\
202409-0560-007 & USDA/\allowbreak{}FSA & Farm Loan Programs - Direct Loan Servicing - Special ( 7 CFR 766) & 10/\allowbreak{}08/\allowbreak{}2024 & 69 \\
202511-0583-005 & USDA/\allowbreak{}FSIS & Sanitation SOPs and Pathogen Reduction/\allowbreak{}HACCP & 07/\allowbreak{}20/\allowbreak{}2026 & 59 \\
202603-0535-001 & USDA/\allowbreak{}NASS & Agricultural Surveys Program & 03/\allowbreak{}17/\allowbreak{}2026 & 75 \\
\end{longtable}\endgroup



# Appendix B. Rubric and dimension scores

The frozen rubric retains nine dimensions and 100 total points. Full credit requires the standard below; approximate anchors are 25% for an asserted total, 50% for partial reconstruction with material gaps, and 75% for mostly reconstructable work with bounded gaps. Explicit justified zeros remain eligible for full credit.[^145]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.25\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.09\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.66\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Dimension} & \textbf{Max.} & \textbf{Full-credit standard} \\
\midrule\endfirsthead
\toprule
\textbf{Dimension} & \textbf{Max.} & \textbf{Full-credit standard} \\
\midrule\endhead
\bottomrule\endfoot
Reproducibility & 20 & Disclosed inputs, units, frequency, annualization, and rounding support total reconstruction. \\
Provenance & 15 & Material inputs identify source, dataset, codes, dates, geography, and transformations. \\
Segmentation & 15 & Meaningful respondent and task variation is represented without gratuitous complexity. \\
Labor & 10 & Occupation, wage, benefits, overhead bases, and transformations are defensible. \\
Item 13 & 10 & Applicable purchases and capital reconstruct; zero is justified where appropriate. \\
Item 14 & 10 & Attributable Federal workload and resources reconstruct, or zero is defensible. \\
Item 15 & 10 & Old/\allowbreak{}new bridge identifies changes, reasons, classifications, and effects. \\
Validation & 5 & Assumptions have proportionate empirical support or justified uncertainty. \\
Consistency & 5 & Tables, prose, package totals, and baseline agree within explained tolerances. \\
\end{longtable}\endgroup


## Full dimension scores

R=reproducibility; P=provenance; S=segmentation; L=labor; V=validation; C=consistency. Maxima: 20, 15, 15, 10, 10, 10, 10, 5, 5. Each row is one ICR. All 657 dimension rationales and locators are preserved in the accompanying scoring table.[^146]

\small


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.25\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.075\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{ICR} & \textbf{R} & \textbf{P} & \textbf{S} & \textbf{L} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{V} & \textbf{C} & \textbf{Total} \\
\midrule\endfirsthead
\toprule
\textbf{ICR} & \textbf{R} & \textbf{P} & \textbf{S} & \textbf{L} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{V} & \textbf{C} & \textbf{Total} \\
\midrule\endhead
\bottomrule\endfoot
202306-3038-007 & 16 & 9 & 14 & 6 & 5 & 5 & 8 & 2 & 2 & 67 \\
202310-0607-003 & 17 & 11 & 15 & 5 & 10 & 3 & 6 & 5 & 2 & 74 \\
202310-1219-001 & 17 & 11 & 15 & 4 & 7 & 5 & 8 & 4 & 2 & 73 \\
202310-1220-004 & 19 & 11 & 15 & 8 & 8 & 3 & 6 & 4 & 4 & 78 \\
202311-2137-001 & 18 & 8 & 14 & 4 & 5 & 2 & 8 & 2 & 3 & 64 \\
202312-2050-001 & 14 & 10 & 15 & 6 & 7 & 7 & 8 & 3 & 1 & 71 \\
202401-1615-055 & 19 & 6 & 13 & 4 & 7 & 5 & 9 & 2 & 4 & 69 \\
202401-2070-005 & 16 & 10 & 15 & 7 & 7 & 7 & 9 & 3 & 2 & 76 \\
202401-3235-005 & 14 & 9 & 15 & 4 & 6 & 2 & 7 & 3 & 1 & 61 \\
202402-0648-005 & 17 & 10 & 13 & 3 & 7 & 7 & 7 & 3 & 3 & 70 \\
202402-1652-002 & 14 & 11 & 13 & 5 & 8 & 6 & 4 & 2 & 1 & 64 \\
202403-0607-001 & 19 & 11 & 13 & 6 & 10 & 3 & 5 & 3 & 4 & 74 \\
202403-0910-005 & 16 & 9 & 13 & 4 & 3 & 5 & 6 & 3 & 1 & 60 \\
202403-1219-001 & 19 & 11 & 13 & 4 & 5 & 6 & 8 & 3 & 3 & 72 \\
202404-1220-001 & 19 & 12 & 15 & 7 & 10 & 5 & 8 & 3 & 4 & 83 \\
202404-1240-007 & 16 & 9 & 12 & 5 & 8 & 5 & 5 & 3 & 1 & 64 \\
202404-2120-002 & 16 & 10 & 14 & 6 & 6 & 8 & 4 & 3 & 2 & 69 \\
202404-2137-003 & 18 & 9 & 14 & 6 & 5 & 5 & 8 & 2 & 1 & 68 \\
202405-0704-001 & 17 & 10 & 12 & 6 & 8 & 6 & 7 & 3 & 3 & 72 \\
202405-0704-002 & 17 & 11 & 15 & 8 & 4 & 7 & 7 & 3 & 3 & 75 \\
202405-0938-022 & 17 & 10 & 12 & 6 & 7 & 3 & 5 & 2 & 3 & 65 \\
202405-1218-005 & 17 & 11 & 14 & 8 & 8 & 5 & 9 & 4 & 2 & 78 \\
202405-1220-001 & 17 & 10 & 12 & 6 & 8 & 4 & 6 & 3 & 3 & 69 \\
202405-1506-005 & 17 & 10 & 14 & 6 & 2 & 5 & 7 & 4 & 3 & 68 \\
202405-1652-001 & 17 & 12 & 15 & 8 & 7 & 5 & 6 & 2 & 2 & 74 \\
202406-1652-001 & 17 & 11 & 15 & 7 & 8 & 8 & 5 & 3 & 2 & 76 \\
202408-1625-012 & 18 & 10 & 14 & 6 & 8 & 6 & 8 & 3 & 4 & 77 \\
202408-1652-002 & 12 & 10 & 14 & 6 & 4 & 7 & 5 & 2 & 0 & 60 \\
202409-0560-007 & 18 & 10 & 14 & 5 & 3 & 7 & 6 & 3 & 3 & 69 \\
202409-2126-001 & 17 & 3 & 13 & 2 & 6 & 8 & 7 & 1 & 3 & 60 \\
202409-3235-022 & 20 & 9 & 14 & 4 & 8 & 4 & 9 & 3 & 5 & 76 \\
202410-0910-013 & 18 & 8 & 14 & 5 & 4 & 2 & 7 & 3 & 3 & 64 \\
202410-0960-002 & 15 & 8 & 15 & 4 & 7 & 4 & 4 & 4 & 1 & 62 \\
202410-3150-005 & 18 & 9 & 15 & 3 & 4 & 7 & 9 & 4 & 4 & 73 \\
202410-7100-005 & 16 & 9 & 13 & 5 & 2 & 3 & 5 & 2 & 3 & 58 \\
202411-1218-005 & 16 & 10 & 12 & 5 & 6 & 8 & 8 & 2 & 2 & 69 \\
202411-1651-004 & 16 & 11 & 10 & 8 & 1 & 2 & 7 & 2 & 0 & 57 \\
202411-1652-007 & 18 & 10 & 13 & 6 & 8 & 6 & 4 & 2 & 1 & 68 \\
202411-2070-003 & 18 & 10 & 14 & 8 & 6 & 7 & 6 & 3 & 3 & 75 \\
202412-1205-002 & 18 & 11 & 12 & 8 & 6 & 7 & 8 & 3 & 4 & 77 \\
202412-1652-001 & 18 & 11 & 15 & 5 & 6 & 8 & 4 & 2 & 2 & 71 \\
202412-3170-001 & 17 & 3 & 13 & 0 & 5 & 7 & 6 & 2 & 1 & 54 \\
202501-1210-006 & 19 & 11 & 12 & 7 & 9 & 9 & 7 & 4 & 4 & 82 \\
202502-0960-015 & 14 & 9 & 15 & 5 & 8 & 3 & 6 & 3 & 1 & 64 \\
202502-2040-002 & 16 & 11 & 15 & 7 & 5 & 6 & 6 & 4 & 1 & 71 \\
202502-2060-039 & 16 & 10 & 13 & 5 & 5 & 6 & 7 & 3 & 2 & 67 \\
202502-3235-014 & 18 & 5 & 10 & 0 & 5 & 0 & 9 & 2 & 4 & 53 \\
202503-3060-020 & 19 & 8 & 14 & 4 & 8 & 5 & 10 & 4 & 4 & 76 \\
202504-1004-001 & 16 & 10 & 14 & 7 & 7 & 5 & 9 & 3 & 2 & 73 \\
202504-1652-008 & 18 & 11 & 15 & 6 & 8 & 5 & 6 & 3 & 3 & 75 \\
202504-1902-007 & 18 & 8 & 13 & 5 & 6 & 7 & 8 & 2 & 2 & 69 \\
202504-2060-006 & 16 & 9 & 14 & 6 & 7 & 6 & 4 & 3 & 2 & 67 \\
202504-3235-016 & 15 & 11 & 14 & 5 & 7 & 5 & 7 & 3 & 1 & 68 \\
202505-1218-008 & 17 & 11 & 14 & 7 & 7 & 7 & 8 & 3 & 3 & 77 \\
202505-2060-004 & 17 & 9 & 14 & 6 & 7 & 8 & 5 & 3 & 4 & 73 \\
202505-3060-038 & 18 & 8 & 14 & 3 & 8 & 6 & 8 & 3 & 1 & 69 \\
202506-0551-003 & 18 & 9 & 12 & 5 & 7 & 8 & 6 & 2 & 3 & 70 \\
202506-0938-007 & 17 & 9 & 10 & 4 & 4 & 4 & 7 & 3 & 2 & 60 \\
202506-2130-004 & 13 & 9 & 14 & 5 & 6 & 7 & 9 & 3 & 1 & 67 \\
202507-1902-004 & 17 & 9 & 14 & 6 & 2 & 6 & 6 & 3 & 1 & 64 \\
202508-1218-005 & 17 & 11 & 15 & 7 & 8 & 8 & 9 & 3 & 2 & 80 \\
202508-1652-001 & 16 & 11 & 14 & 7 & 6 & 5 & 7 & 2 & 2 & 70 \\
202508-2126-007 & 13 & 10 & 13 & 4 & 6 & 6 & 6 & 3 & 0 & 61 \\
202509-2060-003 & 18 & 9 & 15 & 3 & 6 & 5 & 8 & 2 & 2 & 68 \\
202511-0583-005 & 14 & 8 & 15 & 4 & 3 & 5 & 6 & 3 & 1 & 59 \\
202511-1545-005 & 12 & 11 & 15 & 7 & 7 & 6 & 9 & 4 & 2 & 73 \\
202602-0607-001 & 18 & 9 & 14 & 4 & 10 & 4 & 6 & 3 & 3 & 71 \\
202602-2060-006 & 16 & 10 & 15 & 6 & 6 & 6 & 9 & 3 & 3 & 74 \\
202602-3170-003 & 15 & 5 & 9 & 3 & 6 & 3 & 4 & 1 & 0 & 46 \\
202603-0535-001 & 18 & 10 & 15 & 6 & 8 & 4 & 8 & 3 & 3 & 75 \\
202603-1210-004 & 16 & 10 & 15 & 7 & 8 & 4 & 6 & 3 & 2 & 71 \\
202606-1652-001 & 15 & 11 & 13 & 7 & 6 & 7 & 4 & 2 & 1 & 66 \\
202606-1652-002 & 10 & 8 & 11 & 6 & 5 & 4 & 3 & 3 & 0 & 50 \\
\end{longtable}\endgroup

\normalsize

# Appendix C. Descriptive summaries and sensitivity

Agency/component statistics describe only reviewed observations. A standard deviation of zero for n=1 contains no evidence about institutional consistency. Population-formula SD means division by the observed n, not a population inference. The sample is purposive and heterogeneous.[^147]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.34\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.08\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.15\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.15\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.15\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.13\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Component} & \textbf{n} & \textbf{Mean} & \textbf{Median} & \textbf{Range} & \textbf{SD} \\
\midrule\endfirsthead
\toprule
\textbf{Component} & \textbf{n} & \textbf{Mean} & \textbf{Median} & \textbf{Range} & \textbf{SD} \\
\midrule\endhead
\bottomrule\endfoot
CFPB & 2 & 50.00 & 50.0 & 46-54 & 4.00 \\
CFTC & 1 & 67.00 & 67.0 & 67-67 & 0.00 \\
DHS/\allowbreak{}TSA & 10 & 67.40 & 69.0 & 50-76 & 7.53 \\
DHS/\allowbreak{}USCBP & 1 & 57.00 & 57.0 & 57-57 & 0.00 \\
DHS/\allowbreak{}USCG & 1 & 77.00 & 77.0 & 77-77 & 0.00 \\
DHS/\allowbreak{}USCIS & 1 & 69.00 & 69.0 & 69-69 & 0.00 \\
DOC/\allowbreak{}CENSUS & 3 & 73.00 & 74.0 & 71-74 & 1.41 \\
DOC/\allowbreak{}NOAA & 1 & 70.00 & 70.0 & 70-70 & 0.00 \\
DOI/\allowbreak{}BLM & 1 & 73.00 & 73.0 & 73-73 & 0.00 \\
DOL/\allowbreak{}BLS & 3 & 76.67 & 78.0 & 69-83 & 5.79 \\
DOL/\allowbreak{}EBSA & 2 & 76.50 & 76.5 & 71-82 & 5.50 \\
DOL/\allowbreak{}ETA & 1 & 77.00 & 77.0 & 77-77 & 0.00 \\
DOL/\allowbreak{}MSHA & 2 & 72.50 & 72.5 & 72-73 & 0.50 \\
DOL/\allowbreak{}OSHA & 4 & 76.00 & 77.5 & 69-80 & 4.18 \\
DOL/\allowbreak{}OWCP & 1 & 64.00 & 64.0 & 64-64 & 0.00 \\
DOT/\allowbreak{}FAA & 1 & 69.00 & 69.0 & 69-69 & 0.00 \\
DOT/\allowbreak{}FMCSA & 2 & 60.50 & 60.5 & 60-61 & 0.50 \\
DOT/\allowbreak{}FRA & 1 & 67.00 & 67.0 & 67-67 & 0.00 \\
DOT/\allowbreak{}PHMSA & 2 & 66.00 & 66.0 & 64-68 & 2.00 \\
DOW/\allowbreak{}DODDEP & 2 & 73.50 & 73.5 & 72-75 & 1.50 \\
EPA/\allowbreak{}OAR & 5 & 69.80 & 68.0 & 67-74 & 3.06 \\
EPA/\allowbreak{}OCSPP & 2 & 75.50 & 75.5 & 75-76 & 0.50 \\
EPA/\allowbreak{}OLEM & 1 & 71.00 & 71.0 & 71-71 & 0.00 \\
EPA/\allowbreak{}OW & 1 & 71.00 & 71.0 & 71-71 & 0.00 \\
FCC & 2 & 72.50 & 72.5 & 69-76 & 3.50 \\
FERC & 2 & 66.50 & 66.5 & 64-69 & 2.50 \\
FRS & 1 & 58.00 & 58.0 & 58-58 & 0.00 \\
HHS/\allowbreak{}CMS & 2 & 62.50 & 62.5 & 60-65 & 2.50 \\
HHS/\allowbreak{}FDA & 2 & 62.00 & 62.0 & 60-64 & 2.00 \\
NRC & 1 & 73.00 & 73.0 & 73-73 & 0.00 \\
SEC & 4 & 64.50 & 64.5 & 53-76 & 8.50 \\
SSA & 2 & 63.00 & 63.0 & 62-64 & 1.00 \\
TREAS/\allowbreak{}FINCEN & 1 & 68.00 & 68.0 & 68-68 & 0.00 \\
TREAS/\allowbreak{}IRS & 1 & 73.00 & 73.0 & 73-73 & 0.00 \\
USDA/\allowbreak{}FAS & 1 & 70.00 & 70.0 & 70-70 & 0.00 \\
USDA/\allowbreak{}FSA & 1 & 69.00 & 69.0 & 69-69 & 0.00 \\
USDA/\allowbreak{}FSIS & 1 & 59.00 & 59.0 & 59-59 & 0.00 \\
USDA/\allowbreak{}NASS & 1 & 75.00 & 75.0 & 75-75 & 0.00 \\
\end{longtable}\endgroup


## Sensitivity definitions

The cost-exclusion view is `(total - Item13 - Item14) / 80 × 100`; Item 12 is the sum of reproducibility, provenance, segmentation, and labor. Neither replaces the rubric. The table below shows all ten TSA cases; the machine-readable sensitivity file retains all 73.[^148]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.28\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.18\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.32\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.22\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{TSA ICR} & \textbf{Original /\allowbreak{}100} & \textbf{Excluding 13-14 /\allowbreak{}100} & \textbf{Item 12 /\allowbreak{}60} \\
\midrule\endfirsthead
\toprule
\textbf{TSA ICR} & \textbf{Original /\allowbreak{}100} & \textbf{Excluding 13-14 /\allowbreak{}100} & \textbf{Item 12 /\allowbreak{}60} \\
\midrule\endhead
\bottomrule\endfoot
202402-1652-002 & 64 & 62.50 & 43 \\
202405-1652-001 & 74 & 77.50 & 52 \\
202406-1652-001 & 76 & 75.00 & 50 \\
202408-1652-002 & 60 & 61.25 & 42 \\
202411-1652-007 & 68 & 67.50 & 47 \\
202412-1652-001 & 71 & 71.25 & 49 \\
202504-1652-008 & 75 & 77.50 & 50 \\
202508-1652-001 & 70 & 73.75 & 48 \\
202606-1652-001 & 66 & 66.25 & 46 \\
202606-1652-002 & 50 & 51.25 & 35 \\
\end{longtable}\endgroup


Among components with at least three reviewed ICRs, BLS has the highest observed mean (76.67; n=3), while Census has the narrowest observed dispersion (SD 1.41; n=3; range 71-74). These are descriptive sample results, not agency quality or consistency rankings.[^149]



# Appendix D. Source and assumption catalogs

## Source catalog

These 28 entries preserve the frozen catalog's analytical coverage. Update frequencies are as recorded in the release, not newly verified publication schedules. Citations identify the selected sources; administrative entries may describe an unavailable underlying query. Exact original fields remain in `data/data-sources.csv`.[^150]


**Burden definitions.** As amended; Federal scope. Map obligations to included and excluded activities, documenting usual/customary treatment. Cite section and paragraph. The regulation does not supply response times.[^151]


**Agency estimation responsibilities.** As amended; Federal scope. Identify the evidence supporting the estimate. Cite section and paragraph. Compliance with a process is not an accuracy guarantee.[^152]


**JOLTS.** Monthly flows, with annual revisions; industry and selected geographic detail, not occupation-specific turnover. Preserve series, denominator, reference period, and vintage. Do not treat a monthly flow as a unique annual probability.[^153]


**OEWS.** Annual occupational wages and employment, with SOC/NAICS and geographic detail. Select mean, median, or percentile deliberately; retain codes, year, and table. Wages exclude benefits and may be suppressed.[^154]


**ECEC.** Quarterly wages, benefits, and compensation for broad worker groups. Use direct compensation or an explicit matched ratio. Cite reference quarter, publication date, table, and row. Benefits are not overhead.[^155]


**OPM 2025 DCB salary table.** Annual grade/step pay for the Washington locality. Cite year, locality, grade, and step; document benefits and any hourly divisor. Salary is not a contractor rate.[^156]


**CPS geographic mobility.** Annual mobility by demographic and labor-force characteristics. Preserve affected population and denominator. Residential movement is not necessarily professional contact change and may overlap other events.[^157]


**Employment Cost Index.** Quarterly wage/compensation indexes for broad groups. Update a level by the ratio of matched periods. Cite series, quarters, seasonal status, and vintage. The index is not itself a wage observation.[^158]


**County Business Patterns.** Annual establishment, employment, and payroll counts by NAICS, size, and geography. Map the legal respondent unit explicitly. Cite year, industry, geography, and table; account for exclusions and suppression.[^159]


**BEA GDP price index.** Quarterly broad output-price indexes with revisions. Preserve NIPA table, line, periods, and release. A general price ratio may not represent equipment, IT, or labor cost change.[^160]


**PRA burden guidance.** Updated guidance on activities, loaded wages, and cost categories. Cite heading, URL, and retrieval date; interpret alongside regulations and the frozen instruction-conflict register.[^161]


**EBSA overhead methodology.** June 2019 method; input updates are separate. Allocate selected industry expenses through occupational employment, then divide by employment and hours. Preserve matrices, exclusions, and price years. Worked-example inconsistencies and average/marginal cost interpretation require review.[^162]


**AIES burden measurement.** One-time research supplement, printed p. 19. Retain sample, segment, statistic, and preparation/completion scope. The response-analysis survey, instrument, and paradata are not interchangeable measures of mean total effort.[^163]


**Business taxpayer burden model.** Annual updates and periodic calibration; entity and industry characteristics generate time and purchases. Preserve model version, calibration years, legal cutoff, and prediction inputs. Public coefficients/microdata are unavailable in the selected package.[^164]


**EIA CBECS.** Periodic commercial-building survey; the selected vintage is 2018. National/regional building and floorspace data can support asset proxies with explicit coverage assumptions. Cite table, vintage, and uncertainty; buildings are not respondents.[^165]


**EIA MECS.** Quadrennial manufacturing survey program with industry and regional detail. Align manufacturing and nonmanufacturing universes to avoid overlap. Cite reference year, table, release, and transformation.[^166]


**BLS Employment Projections.** Annual projections releases with SOC and employment-matrix detail. Preserve base and horizon; annualize growth geometrically where appropriate. Openings differ from net growth and new regulated entrants.[^167]


**BLS CES.** Monthly employment, earnings, and hours with revisions. Cite series and seasonal status. Industry earnings are not occupation-specific pay or benefits, and employee coverage may differ from respondents.[^168]


**BLS PPI.** Monthly industry/commodity price indexes with revisions. Apply a matched index ratio and retain series and price years. Producer prices are not automatically the relevant purchased-service, consumer, or wage index.[^169]


**Historical Census ASM.** Historical annual manufacturing expenses, employment, and payroll by industry. Exclude direct inputs before overhead allocation. Check transition to AIES when refreshing. The source page was inaccessible at freeze; this entry is not a claim of independent table validation.[^170]


**Historical Census SAS.** Historical annual service-industry revenue and expenses. Preserve expense categories and allocation denominators. Industry averages need not represent marginal collection costs; check coverage changes and AIES transition. Source-page access was blocked at freeze.[^171]


**OPM salary tables.** Annual base/locality schedules; special rates separately. Use a published hourly rate or a stated annual divisor. Cite year, locality, grade, and step. Benefits require separate support.[^172]


**EPA CEMS cost workbook.** Historical engineering method, not current prices. Retain principal, life, discounting, installation, and recurring-cost scope. Cite workbook sheet/cells. Separate labor and wider regulatory costs before PRA use.[^173]


**RMP administrative population.** March 2025 extract described in OSHA process safety. Preserve facility filters, chemical/process scope, and coverage adjustments. PSM and RMP universes differ; the exact filtered extract is not public.[^174]


**MISLE security-plan population.** Program-specific administrative counts described by the Coast Guard. Preserve extraction date, vessel/facility definitions, and query. Published counts do not expose the underlying query.[^175]


**BSA E-Filing workload.** Calendar 2022 SAR submissions described by FinCEN. Preserve unique filers, reports, categories, and case stages. Restricted microdata prevent independent querying of published aggregates.[^176]


**ETA unemployment-insurance workload funding.** FY2025 workload/funding assumptions. Preserve pay, workload, and productive-hours allocation; the 1,711-hour denominator is program-specific, not a universal Federal conversion.[^177]


**CMMC system and vendor evidence.** Final-rule labor, contract, and system cost tables. Separate staged assessments, internal staff, vendor prices, implementation, and recurring systems. Retain allocation denominators and avoid duplicating labor embedded in capital.[^178]


## Assumption catalog

The 24 recurring types below are a review checklist, not default parameter values. Each requires a justification, applicability boundary, source or expert basis, and review date. The full original strong/weak evidence descriptions are retained in `data/assumptions.csv`.[^179]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.17\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.24\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.59\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{ID} & \textbf{Assumption} & \textbf{Evidence/\allowbreak{}control} \\
\midrule\endfirsthead
\toprule
\textbf{ID} & \textbf{Assumption} & \textbf{Evidence/\allowbreak{}control} \\
\midrule\endhead
\bottomrule\endfoot
ASM-0001 & Response time & Task-matched timing; mode, sample, date, and distribution. \\
ASM-0002 & Population & Dated count with filters, coverage, and unique entity definition. \\
ASM-0003 & Frequency & Events per eligible entity per defined period; overlap treatment. \\
ASM-0004 & Pathway share & Dated mutually exclusive modes or explicit additive stages. \\
ASM-0005 & Familiarization & Text/\allowbreak{}task boundary, role, and entrant/\allowbreak{}update cohort. \\
ASM-0006 & Labor mix & Observed task roles or justified role-hour shares. \\
ASM-0007 & Wage selection & Occupation, industry, geography, statistic, vintage, and rationale. \\
ASM-0008 & Benefits & Matching worker universe and explicit denominator. \\
ASM-0009 & Overhead & Components, allocation base, nonoverlap, and cost interpretation. \\
ASM-0010 & Outsourcing & Dated price evidence and contract scope; no duplicated internal labor. \\
ASM-0011 & Capital life & Asset inventory, service life, and replacement schedule. \\
ASM-0012 & Usual/\allowbreak{}customary & Evidence of existing practice and obligation ownership. \\
ASM-0013 & Federal review & Workload, task time, compensation, and contract evidence. \\
ASM-0014 & Inflation & Index identity, base/\allowbreak{}target periods, and economic rationale. \\
ASM-0015 & Nonreporter determination & Potentially affected nonfilers and screening tasks. \\
ASM-0016 & Change classification & Named baseline, changed input/\allowbreak{}requirement, reason, and effect. \\
ASM-0017 & Measurement scope & Sample design, active/\allowbreak{}elapsed time, preparation, and statistic. \\
ASM-0018 & Statistical calibration & Model version, coefficients/\allowbreak{}access limits, and diagnostics. \\
ASM-0019 & Manager/\allowbreak{}legal review & Observed routing and boundaries distinct from preparation. \\
ASM-0020 & IT implementation & Scoped build, recurring operations, payer, and asset treatment. \\
ASM-0021 & Federal allocation & Usage driver with numerator and complete denominator. \\
ASM-0022 & Discount/\allowbreak{}annualization & Principal, life, rate convention, and price basis. \\
ASM-0023 & Case conversion & Dated funnel including decisions that do not produce filings. \\
ASM-0024 & Cohort/\allowbreak{}horizon & Start/\allowbreak{}end dates, eligibility, replacement, and sunset. \\
\end{longtable}\endgroup



# Appendix E. Calculation checks and evidence qualifications

All 267 recorded expressions were replayed for this report. The table gives frozen numerical statuses, not defect prevalence. One collection can contribute multiple dependent checks, and some checks intentionally test a counterfactual or conflicting display. Read the interpretation and source before drawing a conclusion.[^180]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.5\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.5\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Frozen status} & \textbf{Expressions} \\
\midrule\endfirsthead
\toprule
\textbf{Frozen status} & \textbf{Expressions} \\
\midrule\endhead
\bottomrule\endfoot
Exact & 133 \\
Within display rounding & 52 \\
Difference requires interpretation & 82 \\
Total & 267 \\
\end{longtable}\endgroup


**Frozen-record qualification M2-OBS-001.** HME's pathway-share expression is 1.312 against 1, but the numerical label says within display rounding. The interpretation correctly flags apparent double counting. The report uses the semantic interpretation and does not alter the record or scores. Correcting the canonical status would require a new evidence version.[^181]


**Source-binding qualification M2-OBS-002.** The historical capital-recovery check is attached to SRC-0146 in the check table, while its inputs and method are documented in the frozen SRC-0162 extraction, with SRC-0161 providing related workbook methodology. This report cites those method sources directly and retains the reported $72,752 separately from $72,740.52 recomputed. It does not amend the frozen check binding. A canonical correction would require a new evidence version.[^182]


These issues limit automated interpretation of the status and citation fields; they do not change the reported score comparisons. The report's citation registry records the sources actually supporting its statements. No broad research was reopened, and no new evidence release was created.


## Selected numerical distinctions


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.21\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.37\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.42\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Case} & \textbf{Observed comparison} & \textbf{Interpretation} \\
\midrule\endfirsthead
\toprule
\textbf{Case} & \textbf{Observed comparison} & \textbf{Interpretation} \\
\midrule\endhead
\bottomrule\endfoot
Aircraft operators & Narrative \$54,658; Table 2 \$20,165,327 & Inconsistent displayed values; possible copy/\allowbreak{}version issue. \\
Certified cargo & Components 6,049 h; subtotal 4,451 h & Confirmed displayed subtotal discrepancy; intended value unresolved. \\
HME pathways & Shares 1.312; mutually exclusive target 1 & Potential scope duplication, not rounding. \\
Surface cybersecurity & Printed Federal rows 1,149 h; total 881 h & Displayed arithmetic discrepancy. \\
Airport applicant labor & \$34.48 used; footnote gives about \$50.19 & Transformation/\allowbreak{}version ambiguity; not a verified corrected estimate. \\
Airport Federal costs & \$921,400.97 recomputed; \$921,402 reported & Small precision/\allowbreak{}reconciliation residual. \\
TWIC totals & One-hour and one-dollar differences & Rounding/\allowbreak{}precision questions, not evidence of material scope error. \\
\end{longtable}\endgroup


Sources and locators for each row are cited in Sections 7 and 9 and preserved in `report/tables/reconstruction-risks.csv`. No corrected agency total is asserted.



# Appendix F. Canonical entity contract

Version 0.5.0 contains the following 27 entities. These summaries preserve the frozen relationships; the authoritative dictionary supplies full fields and constraints. The model is a research architecture, not a completed implementation.[^183]


\begingroup\fontsize{9.5}{11.8}\selectfont
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{\dimexpr 0.2\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.37\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr 0.43\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Entity} & \textbf{Principal fields} & \textbf{Relationship/\allowbreak{}control} \\
\midrule\endfirsthead
\toprule
\textbf{Entity} & \textbf{Principal fields} & \textbf{Relationship/\allowbreak{}control} \\
\midrule\endhead
\bottomrule\endfoot
Collection & collection\_\allowbreak{}id, OMB\_\allowbreak{}control, component, title, authority, approval\_\allowbreak{}lineage & Identity binds every table and narrative output. \\
Scenario & scenario\_\allowbreak{}id, collection\_\allowbreak{}id, baseline\_\allowbreak{}id, policy\_\allowbreak{}date, price\_\allowbreak{}year, first\_\allowbreak{}year, horizon, status & Approved, proposed and notice versions remain separate. \\
Source & source\_\allowbreak{}id, author, title, publication\_\allowbreak{}date, reference\_\allowbreak{}period, URL, retrieval\_\allowbreak{}date, hash, access\_\allowbreak{}status & Citation-ready metadata; publication date differs from data reference period. \\
Evidence locator & locator\_\allowbreak{}id, source\_\allowbreak{}id, page, table, row, cell, quoted\_\allowbreak{}value, extraction\_\allowbreak{}method & A transformed input links to the original observation and its locator. \\
Population & population\_\allowbreak{}id, unit\_\allowbreak{}type, count, period, query\_\allowbreak{}filters, source\_\allowbreak{}id, coverage, exclusions & Persons, firms, establishments, sites, assets and events are distinct types. \\
Segment & segment\_\allowbreak{}id, parent\_\allowbreak{}population\_\allowbreak{}id, eligibility\_\allowbreak{}rule, share/\allowbreak{}count, overlap\_\allowbreak{}type & Exclusive partitions sum to one; overlapping groups require an explicit union. \\
Obligation & obligation\_\allowbreak{}id, legal\_\allowbreak{}citation, activity\_\allowbreak{}id, owning\_\allowbreak{}control, exclusion/\allowbreak{}transfer\_\allowbreak{}reason & Cross-control movements have source and destination entries. \\
Activity & activity\_\allowbreak{}id, segment\_\allowbreak{}id, task, trigger, mode, role\_\allowbreak{}id, one\_\allowbreak{}time\_\allowbreak{}or\_\allowbreak{}recurring & Atomically priced work; a purchased activity is not also charged as internal time. \\
Exposure/\allowbreak{}frequency & frequency\_\allowbreak{}id, activity\_\allowbreak{}id, events\_\allowbreak{}per\_\allowbreak{}period, periods\_\allowbreak{}per\_\allowbreak{}year, eligibility\_\allowbreak{}share & Annualize rates only after reconciling periods and denominators. \\
Time estimate & time\_\allowbreak{}id, activity\_\allowbreak{}id, value, time\_\allowbreak{}unit, statistic, scope, assumption\_\allowbreak{}id & Mean, median, percentile and elapsed/\allowbreak{}active time cannot be interchanged. \\
Labor role & role\_\allowbreak{}id, task\_\allowbreak{}description, SOC, NAICS, locality, selection\_\allowbreak{}reason & Industry employment weights are not automatically task labor shares. \\
Wage observation & wage\_\allowbreak{}id, role\_\allowbreak{}id, source\_\allowbreak{}id, year, wage\_\allowbreak{}statistic, base\_\allowbreak{}rate, units & Preserve suppressed values and historical code changes. \\
Compensation method & compensation\_\allowbreak{}id, wage\_\allowbreak{}id, method\_\allowbreak{}enum, benefit\_\allowbreak{}value/\allowbreak{}share, denominator, reference\_\allowbreak{}period & Direct compensation, wage markup and wage/\allowbreak{}compensation-share use different equations. \\
Overhead allocation & overhead\_\allowbreak{}id, components, direct\_\allowbreak{}cost\_\allowbreak{}exclusions, industry\_\allowbreak{}matrix, occupation\_\allowbreak{}weights, annual\_\allowbreak{}hours & Monetary units, average/\allowbreak{}marginal interpretation and potential double counting are explicit. \\
Price transformation & transform\_\allowbreak{}id, input\_\allowbreak{}id, index\_\allowbreak{}series, base\_\allowbreak{}period, target\_\allowbreak{}period, ratio, rationale & Detect overlapping nominal updates; distinguish wage from output-price inflation. \\
Purchased service & service\_\allowbreak{}id, activity\_\allowbreak{}id, quantity, unit\_\allowbreak{}price, price\_\allowbreak{}scope, vendor\_\allowbreak{}evidence, payer & Outside professional hours are a service quantity, not necessarily Item12 respondent hours. \\
Capital asset/\allowbreak{}cohort & asset\_\allowbreak{}id, cohort\_\allowbreak{}year, quantity, price, useful\_\allowbreak{}life, replacement\_\allowbreak{}rule, residual\_\allowbreak{}value, annualization\_\allowbreak{}method, discount\_\allowbreak{}rate & Asset life, approval horizon and annual purchase flow are separate. \\
Federal activity & federal\_\allowbreak{}activity\_\allowbreak{}id, workload, time, grade/\allowbreak{}role, locality, benefits\_\allowbreak{}method & Include only attributable resource use; explain zero or allocation. \\
Federal allocation & allocation\_\allowbreak{}id, contract/\allowbreak{}system/\allowbreak{}budget\_\allowbreak{}line, gross\_\allowbreak{}cost, allocation\_\allowbreak{}driver, fraction, fee\_\allowbreak{}offset & Gross cost and net budget effect remain separate outputs. \\
Assumption & assumption\_\allowbreak{}id, estimate\_\allowbreak{}method, evidence\_\allowbreak{}ids, justification, applicability, uncertainty, review\_\allowbreak{}date & Unsupported does not mean zero; analyst judgment is identifiable. \\
Statistical model & model\_\allowbreak{}id, version, equation/\allowbreak{}algorithm, coefficients, calibration\_\allowbreak{}population, training\_\allowbreak{}period, legal\_\allowbreak{}cutoff, diagnostics, access\_\allowbreak{}status & Can generate time and purchases jointly; restricted data limit public replication. \\
Validation observation & observation\_\allowbreak{}id, target\_\allowbreak{}input, method, sample\_\allowbreak{}size, sample\_\allowbreak{}frame, segment, task\_\allowbreak{}scope, statistic, distribution & Distinguish empirical plausibility from spreadsheet arithmetic. \\
Formula & formula\_\allowbreak{}id, expression\_\allowbreak{}tree, input\_\allowbreak{}ids, output\_\allowbreak{}unit, rounding\_\allowbreak{}rule, source\_\allowbreak{}formula, observed\_\allowbreak{}cache & Acyclic dependencies; deterministic evaluation; independent result versus cached value. \\
Change event & change\_\allowbreak{}id, baseline\_\allowbreak{}id, proposed\_\allowbreak{}id, changed\_\allowbreak{}input/\allowbreak{}obligation, reason, analytical\_\allowbreak{}type, ROCIS\_\allowbreak{}type, delta\_\allowbreak{}by\_\allowbreak{}metric & Old + program changes + adjustments = new, separately for responses, hours and nonlabor dollars. \\
Interaction/\allowbreak{}decomposition & decomposition\_\allowbreak{}id, changed\_\allowbreak{}inputs, update\_\allowbreak{}order, interaction\_\allowbreak{}term, counterfactual\_\allowbreak{}values & Driver effects depend on order; store the convention rather than hiding interactions. \\
Validation result & check\_\allowbreak{}id, formula/\allowbreak{}model\_\allowbreak{}version, expected, actual, tolerance, status, severity, disposition & A known source defect is distinct from an extraction defect. \\
Output/\allowbreak{}narrative binding & output\_\allowbreak{}id, semantic\_\allowbreak{}item, table\_\allowbreak{}cell/\allowbreak{}sentence, formula\_\allowbreak{}ids, source\_\allowbreak{}ids, scenario\_\allowbreak{}id & Prose cannot invent numbers or inherit values from a different scenario. \\
\end{longtable}\endgroup


## Reproduction and navigation

Run `python report/scripts/analyze.py`, then `python report/scripts/publish.py`, from a checkout containing the pinned evidence and report source. The first script joins and checks the frozen tables and regenerates figure data and charts. The second resolves deterministic first-use footnotes and references, generates appendices, and renders the PDF with Pandoc and XeLaTeX. `report/audit` contains numerical, citation, argument, and visual review records. The report metadata records its evidence pin and output hash.


The report-specific comparison tables retain stable ICR and source IDs. They supplement the frozen release without replacing its extractions, scores, or research status. Future graph construction and modeling applications are separate work.

\newpage

# References

Only externally cited sources appear below. Display titles for supporting statements are editorial descriptions based on their registered collection titles; exact source titles, source IDs, dates, and URLs remain in the accompanying references registry. “n.d.” indicates that the frozen source registry has no publication year. Dates for statements may reflect recorded upload rather than authorship.



\small

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Economic Analysis. (n.d.). *Gross domestic product price index*. Bureau of Economic Analysis. <https://www.bea.gov/data/prices-inflation/gdp-price-index>. [SRC-0033]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Current Employment Statistics*. Bureau of Labor Statistics. <https://www.bls.gov/ces/>. [SRC-0195]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Employer Costs for Employee Compensation: June 2025*. Bureau of Labor Statistics. <https://www.bls.gov/news.release/archives/ecec_09122025.htm>. [SRC-0028]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Employment Cost Index*. Bureau of Labor Statistics. <https://www.bls.gov/eci/>. [SRC-0031]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Employment Projections: Occupational projections and characteristics*. Bureau of Labor Statistics. <https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm>. [SRC-0194]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Job Openings and Labor Turnover Survey: Frequently asked questions*. Bureau of Labor Statistics. <https://www.bls.gov/jlt/jltfaq.htm>. [SRC-0026]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *May 2023 occupational employment and wage estimates: Rail transportation (NAICS 482000)*. Bureau of Labor Statistics. <https://www.bls.gov/oes/2023/May/naics3_482000.htm>. [SRC-0027]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (n.d.). *Producer Price Indexes*. Bureau of Labor Statistics. <https://www.bls.gov/ppi/>. [SRC-0196]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (2023). *Employer Costs for Employee Compensation: September 2023*. BLS. <https://www.bls.gov/news.release/archives/ecec_12152023.pdf>. [SRC-0200]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (2024). *Supporting statement A: National Compensation Survey* (OMB Control No. 1220-0164). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139056101>. [SRC-0078]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Bureau of Labor Statistics. (2024). *Supporting statement A: Survey of Occupational Injuries and Illnesses* (OMB Control No. 1220-0045). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143710604>. [SRC-0008]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Department of Defense. (2024). *CMMC Program final rule, official PDF including quantitative tables*. GPO/Federal Register. <https://www.govinfo.gov/content/pkg/FR-2024-10-15/pdf/2024-22905.pdf>. [SRC-0164]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Eastern Research Group and US EPA. (2017). *Costs for the Manufacturing of Nutritional Yeast Source Category – Final Rule*. US EPA or GPO. <https://downloads.regulations.gov/EPA-HQ-OAR-2015-0730-0201/content.pdf>. [SRC-0162]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Employee Benefits Security Administration. (2019). *Labor Cost Inputs Used in EBSA OPR Regulatory Impact Analyses and Paperwork Reduction Act Burden Calculations*. US Department of Labor. <https://www.dol.gov/sites/dolgov/files/EBSA/laws-and-regulations/rules-and-regulations/technical-appendices/labor-cost-inputs-used-in-ebsa-opr-ria-and-pra-burden-calculations-june-2019.pdf>. [SRC-0102]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Employee Benefits Security Administration. (2025). *Supporting statement A: Settlement Agreements Between a Plan and a Party in Interest* (OMB Control No. 1210-0091). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=151812302>. [SRC-0086]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Employment and Training Administration. (2025). *Supporting statement A: Claims and Payment Activities* (OMB Control No. 1205-0010). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=150266202>. [SRC-0144]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Energy Information Administration. (n.d.). *Commercial Buildings Energy Consumption Survey: 2018 data*. Energy Information Administration. <https://www.eia.gov/consumption/commercial/data/2018/>. [SRC-0192]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Energy Information Administration. (n.d.). *Manufacturing Energy Consumption Survey*. Energy Information Administration. <https://www.eia.gov/consumption/manufacturing/>. [SRC-0193]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Federal Communications Commission. (2025). *Incarcerated People’s Communications Services (IPCS) Provider Annual Reporting, Certification, and Other Requirements, WC Docket Nos. 23-62, 12-375* (OMB Control No. 3060-1222). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202503-3060-020>. [SRC-0063]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Federal Communications Commission. (2025). *Supporting statement A: Incarcerated People’s Communications Services (IPCS) Provider Annual Reporting, Certification, and Other Requirements, WC Docket Nos. 23-62, 12-375* (OMB Control No. 3060-1222). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=155788401>. [SRC-0064]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Federal Communications Commission. (2025). *Supporting statement A: Part 25 of the Federal Communications Commission's Rules Governing the Licensing of, and Spectrum Usage By, Commercial Earth Stations and Space Stations* (OMB Control No. 3060-0678). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=158284001>. [SRC-0068]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Financial Crimes Enforcement Network. (2020). *Renewal of SAR reporting: expanded burden methodology* (OMB Control No. 1506-0065). GPO/Federal Register. <https://www.govinfo.gov/content/pkg/FR-2020-05-26/pdf/2020-11247.pdf>. [SRC-0191]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Financial Crimes Enforcement Network. (2024). *Supporting statement A: FinCEN Form 111 - Suspicious Activity Report* (OMB Control No. 1506-0065). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143239001>. [SRC-0185]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Internal Revenue Service. (n.d.). *2025 Technical, Legislative, and Agency Adjustments2* (OMB Control No. 1545-0123). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=164337801>. [SRC-0100]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Internal Revenue Service. (2025). *Supporting statement A: U.S. Business Income Tax Returns* (OMB Control No. 1545-0123). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=163490901>. [SRC-0094]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

National Agricultural Statistics Service. (2026). *Supporting statement A: Agricultural Surveys Program* (OMB Control No. 0535-0213). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=167082401>. [SRC-0189]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Occupational Safety and Health Administration. (2024). *Supporting statement A: Portable Fire Extinguishers Standard (Annual Maintenance Certification Record) (29 CFR 1910.157(e)(3))* (OMB Control No. 1218-0238). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143525202>. [SRC-0060]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Occupational Safety and Health Administration. (2026). *Supporting statement A: Standard on Process Safety Management of Highly Hazardous Chemicals (29 CFR 1910.119, 29 CFR 1926.64)* (OMB Control No. 1218-0200). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=161728301>. [SRC-0187]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Information and Regulatory Affairs. (n.d.). *Creating a Supporting Statement Part A*. General Services Administration, PRA guide. <https://pra.digital.gov/uploads/supporting-statement-a-instructions.pdf>. [SRC-0001]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Information and Regulatory Affairs. (n.d.). *Estimating burden*. Office of Information and Regulatory Affairs. <https://digital.gov/guides/pra/estimate-burden>. [SRC-0034]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Management and Budget. (n.d.). *5 CFR 1320.3: Definitions*. Office of Management and Budget. <https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.3>. [SRC-0024]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Management and Budget. (n.d.). *5 CFR 1320.8: Agency collection responsibilities*. Office of Management and Budget. <https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.8>. [SRC-0025]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Personnel Management. (n.d.). *Salaries and wages: Salary tables*. Office of Personnel Management. <https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/>. [SRC-0199]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Office of Personnel Management. (n.d.). *Salary Table 2025-DCB*. Office of Personnel Management. <https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/salary-tables/pdf/2025/DCB.pdf>. [SRC-0029]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Regulatory Information Service Center. (2026). *ROCIS PRA Module User Guide*. RISC/OIRA. <https://www.rocis.gov/rocis/downloadResourceDocument.do?uuid=632c6a25-57d2-45f3-84d7-701437f7c73a>. [SRC-0002]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Securities and Exchange Commission. (2024). *Supporting statement A: Form ADV-E, cover sheet for each certificate of accounting of client securities and funds in the custody of an investment adviser* (OMB Control No. 3235-0361). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=146738601>. [SRC-0012]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2024). *Supporting statement A: Aircraft Operator Security, 49 CFR Part 1544* (OMB Control No. 1652-0003). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143967301>. [SRC-0038]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2024). *Supporting statement A: Certified Cargo Screening Program* (OMB Control No. 1652-0053). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=145598901>. [SRC-0040]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2024). *Supporting statement A: Flight Training Security Program* (OMB Control No. 1652-0021). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=142748301>. [SRC-0036]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2025). *Supporting statement A: Airport Security Part 1542* (OMB Control No. 1652-0002). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=150317001>. [SRC-0176]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2025). *Supporting statement A: Transportation Worker Identification Credential* (OMB Control No. 1652-0047). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=156989403>. [SRC-0180]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2026). *Supporting statement A: Cybersecurity Measures for Surface Modes* (OMB Control No. 1652-0074). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=169398300>. [SRC-0022]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2026). *Supporting statement A: Secure Flight Program* (OMB Control No. 1652-0046). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=161038202>. [SRC-0048]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

Transportation Security Administration. (2026). *Supporting statement A: Security Threat Assessment for Individuals Applying for a Hazardous Materials Endorsement for a Commercial Driver's License* (OMB Control No. 1652-0027). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=169514100>. [SRC-0054]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Census Bureau. (n.d.). *Annual Survey of Manufactures*. U.S. Census Bureau. <https://www.census.gov/programs-surveys/asm.html>. [SRC-0197]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Census Bureau. (n.d.). *Attachment N - AIES Dress Rehearsal Preliminary Findings and Recommendations* (OMB Control No. 0607-1024). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139566701>. [SRC-0099]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Census Bureau. (n.d.). *County Business Patterns*. U.S.Census Bureau. <https://www.census.gov/programs-surveys/cbp.html>. [SRC-0032]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Census Bureau. (n.d.). *Geographic mobility: 2023 tables*. U.S.Census Bureau. <https://www.census.gov/data/tables/2023/demo/geographic-mobility/cps-2023.html>. [SRC-0030]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Census Bureau. (n.d.). *Service Annual Survey*. U.S. Census Bureau. <https://www.census.gov/programs-surveys/sas.html>. [SRC-0198]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Coast Guard. (n.d.). *Security-plan burden calculation supplement: Appendices A-B* (OMB Control No. 1625-0077). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=162617501>. [SRC-0181]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Coast Guard. (2025). *Supporting statement A: Security Plan for Ports, Vessels, Facilities, Outer Continental Shelf Facilities and Other Security-Related Requirements* (OMB Control No. 1625-0077). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=145780303>. [SRC-0174]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

U.S. Environmental Protection Agency. (2023). *Supporting statement A: Chemical Data Reporting under the Toxic Substances Control Act (TSCA) (Non-Substantive Change)* (OMB Control No. 2070-0162). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139435801>. [SRC-0183]

\par\endgroup

\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1

US EPA. (2007). *CEMS Cost Model*. US EPA or GPO. <https://www.epa.gov/sites/default/files/2020-08/19-cems.xls>. [SRC-0161]

\par\endgroup

\normalsize


[^1]: *Federal ICR benchmark evidence release M1-1.0.0*. (2026). Rubric 1.0.0; canonical model 0.5.0. Repository commit `16aeb85d976eb3a89ecb3872d4dda94753e77cd3`. research/research-summary.md; methodology/exemplars.md. <https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/research-summary.md>.

[^2]: *Federal ICR benchmark*, M1-1.0.0. [data/scores.csv; data/score-sensitivity.csv; methodology/calibration.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/scores.csv).

[^3]: Bureau of Labor Statistics. (2024). *Supporting statement A: Survey of Occupational Injuries and Illnesses* (OMB Control No. 1220-0045). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143710604>. Item 12, recording burden and Table 9.

[^4]: U.S. Census Bureau. (n.d.). *Attachment N - AIES Dress Rehearsal Preliminary Findings and Recommendations* (OMB Control No. 0607-1024). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139566701>. printed p. 19, burden measurement comparison.

[^5]: Federal Communications Commission. (2025). *Supporting statement A: Incarcerated People’s Communications Services (IPCS) Provider Annual Reporting, Certification, and Other Requirements, WC Docket Nos. 23-62, 12-375* (OMB Control No. 3060-1222). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=155788401>. Item 15 and paragraph 18.

[^6]: Federal Communications Commission. (2025). *Incarcerated People’s Communications Services (IPCS) Provider Annual Reporting, Certification, and Other Requirements, WC Docket Nos. 23-62, 12-375* (OMB Control No. 3060-1222). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202503-3060-020>. OIRA conclusion action, July 8, 2025.

[^7]: Transportation Security Administration. (2024). *Supporting statement A: Flight Training Security Program* (OMB Control No. 1652-0021). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=142748301>. Item 12, cohorts and wage footnotes.

[^8]: Transportation Security Administration. (2026). *Supporting statement A: Security Threat Assessment for Individuals Applying for a Hazardous Materials Endorsement for a Commercial Driver's License* (OMB Control No. 1652-0027). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=169514100>. Item 12, Tables 5a-5c.

[^9]: Transportation Security Administration. (2026). *Supporting statement A: Cybersecurity Measures for Surface Modes* (OMB Control No. 1652-0074). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=169398300>. Item 12, coordinator updates; Item 14.

[^10]: Transportation Security Administration. (2025). *Supporting statement A: Airport Security Part 1542* (OMB Control No. 1652-0002). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=150317001>. Item 12, applicant wage footnote.

[^11]: Transportation Security Administration. (2024). *Supporting statement A: Aircraft Operator Security, 49 CFR Part 1544* (OMB Control No. 1652-0003). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143967301>. Item 12, first-flight checklist and Table 2.

[^12]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tsa-comparison.md; methodology/tool-requirements.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tsa-comparison.md).

[^13]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md; methodology/canonical-model.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^14]: *Federal ICR benchmark*, M1-1.0.0. [research/final-validation.json; research/limitations.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/final-validation.json).

[^15]: Office of Information and Regulatory Affairs. (n.d.). *Creating a Supporting Statement Part A*. General Services Administration, PRA guide. <https://pra.digital.gov/uploads/supporting-statement-a-instructions.pdf>. Items 12-15, pp. 2-3.

[^16]: Office of Management and Budget. (n.d.). *5 CFR 1320.8: Agency collection responsibilities*. Office of Management and Budget. <https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.8>. 5 CFR 1320.8(a)(4).

[^17]: *Federal ICR benchmark*, M1-1.0.0. [methodology/requirements-floor.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/requirements-floor.md).

[^18]: Employee Benefits Security Administration. (2019). *Labor Cost Inputs Used in EBSA OPR Regulatory Impact Analyses and Paperwork Reduction Act Burden Calculations*. US Department of Labor. <https://www.dol.gov/sites/dolgov/files/EBSA/laws-and-regulations/rules-and-regulations/technical-appendices/labor-cost-inputs-used-in-ebsa-opr-ria-and-pra-burden-calculations-june-2019.pdf>. p. 1, purpose and labor-cost definition.

[^19]: Department of Defense. (2024). *CMMC Program final rule, official PDF including quantitative tables*. GPO/Federal Register. <https://www.govinfo.gov/content/pkg/FR-2024-10-15/pdf/2024-22905.pdf>. 89 FR 83177-83192 and 83211-83213.

[^20]: *Federal ICR benchmark*, M1-1.0.0. [research/mission-2-handoff.md; research/research-state.json](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/mission-2-handoff.md).

[^21]: *Federal ICR benchmark*, M1-1.0.0. [data/icrs.csv; research/limitations.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/icrs.csv).

[^22]: *Federal ICR benchmark*, M1-1.0.0. [methodology/sampling-strategy.md; research/research-plan.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/sampling-strategy.md).

[^23]: *Federal ICR benchmark*, M1-1.0.0. [AGENTS.md; methodology/rubric.md; data/scores.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/AGENTS.md).

[^24]: *Federal ICR benchmark*, M1-1.0.0. [methodology/rubric.md; research/final-validation.json; data/calculation-checks.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/rubric.md).

[^25]: *Federal ICR benchmark*, M1-1.0.0. [research/final-validation.json; data/calculation-checks.csv, HME Agentpathway share](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/final-validation.json).

[^26]: *Federal ICR benchmark*, M1-1.0.0. [research/saturation-log.md; logs/iteration-007-results.md; logs/iteration-008-results.md; logs/iteration-009-results.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/saturation-log.md).

[^27]: *Federal ICR benchmark*, M1-1.0.0. [research/final-validation.json; research/open-questions.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/final-validation.json).

[^28]: *Federal ICR benchmark*, M1-1.0.0. [methodology/calibration.md; research/limitations.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/calibration.md).

[^29]: *Federal ICR benchmark*, M1-1.0.0. [methodology/rubric.md; research/limitations.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/rubric.md).

[^30]: *Federal ICR benchmark*, M1-1.0.0. [methodology/calibration.md; methodology/exemplars.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/calibration.md).

[^31]: *Federal ICR benchmark*, M1-1.0.0. [data/score-sensitivity.csv; methodology/calibration.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/score-sensitivity.csv).

[^32]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^33]: *Federal ICR benchmark*, M1-1.0.0. [methodology/exemplars.md; methodology/tsa-comparison.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/exemplars.md).

[^34]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^35]: Transportation Security Administration. (2025). *Supporting statement A: Transportation Worker Identification Credential* (OMB Control No. 1652-0047). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=156989403>. Item 12, Tables 1-9.

[^36]: Transportation Security Administration, *Security Threat Assessment for Individuals Applying for a Hazardous...*. Item 12, Tables 5a-5c.

[^37]: Transportation Security Administration, *Airport Security Part 1542*. Item 12, STA applicant and airport data-entry activities.

[^38]: Bureau of Labor Statistics, *Survey of Occupational Injuries and Illnesses*. Item 12, recording burden and Table 9.

[^39]: Transportation Security Administration, *Flight Training Security Program*. Item 12, candidate and provider cohort tables.

[^40]: National Agricultural Statistics Service. (2026). *Supporting statement A: Agricultural Surveys Program* (OMB Control No. 0535-0213). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=167082401>. Item 12, Tables 1-2.

[^41]: Financial Crimes Enforcement Network. (2020). *Renewal of SAR reporting: expanded burden methodology* (OMB Control No. 1506-0065). GPO/Federal Register. <https://www.govinfo.gov/content/pkg/FR-2020-05-26/pdf/2020-11247.pdf>. 85 FR 31605-31611, including Tables 21-22.

[^42]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv, ASM-0006 and ASM-0007](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^43]: Transportation Security Administration, *Flight Training Security Program*. Item 12, wage selection footnotes.

[^44]: Transportation Security Administration, *Transportation Worker Identification Credential*. Item 12, weighted wage table.

[^45]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md, compensation alternatives](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^46]: Employee Benefits Security Administration, *Labor Cost Inputs Used in EBSA OPR Regulatory Impact Analyses and...*. pp. 1-3, compensation and overhead methods.

[^47]: Bureau of Labor Statistics. (n.d.). *Employment Cost Index*. Bureau of Labor Statistics. <https://www.bls.gov/eci/>. Employment Cost Index, source catalog entry.

[^48]: Bureau of Economic Analysis. (n.d.). *Gross domestic product price index*. Bureau of Economic Analysis. <https://www.bea.gov/data/prices-inflation/gdp-price-index>. GDP price index, source catalog entry.

[^49]: *Federal ICR benchmark*, M1-1.0.0. [data/data-sources.csv; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/data-sources.csv).

[^50]: U.S. Census Bureau, *Attachment N - AIES Dress Rehearsal Preliminary Findings and...*. printed p. 19, burden table.

[^51]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv, ASM-0001 and ASM-0017; methodology/canonical-model.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^52]: Office of Information and Regulatory Affairs, *Creating a Supporting Statement Part A*. Item 13, pp. 2-3.

[^53]: Occupational Safety and Health Administration. (2024). *Supporting statement A: Portable Fire Extinguishers Standard (Annual Maintenance Certification Record) (29 CFR 1910.157(e)(3))* (OMB Control No. 1218-0238). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143525202>. Items 12-13, annual maintenance and purchased-service calculations.

[^54]: *Federal ICR benchmark*, M1-1.0.0. [methodology/exemplars.md; research/limitations.md, limitation 10](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/exemplars.md).

[^55]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md; data/assumptions.csv, ASM-0011 and ASM-0022](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^56]: US EPA. (2007). *CEMS Cost Model*. US EPA or GPO. <https://www.epa.gov/sites/default/files/2020-08/19-cems.xls>. Costs sheet, rows 152 and 181-184; Summary Info rows 44-47.

[^57]: Eastern Research Group and US EPA. (2017). *Costs for the Manufacturing of Nutritional Yeast Source Category – Final Rule*. US EPA or GPO. <https://downloads.regulations.gov/EPA-HQ-OAR-2015-0730-0201/content.pdf>. pp. 2-5, Tables 2-1 through 4-1.

[^58]: *Federal ICR benchmark*, M1-1.0.0. [data/claims.jsonl, CLM-FINDING-017](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/claims.jsonl).

[^59]: U.S. Environmental Protection Agency. (2023). *Supporting statement A: Chemical Data Reporting under the Toxic Substances Control Act (TSCA) (Non-Substantive Change)* (OMB Control No. 2070-0162). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139435801>. Tables 3-4 and 6.

[^60]: *Federal ICR benchmark*, M1-1.0.0. [logs/iteration-009-results.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/logs/iteration-009-results.md).

[^61]: Office of Information and Regulatory Affairs, *Creating a Supporting Statement Part A*. Items 12-13.

[^62]: Regulatory Information Service Center. (2026). *ROCIS PRA Module User Guide*. RISC/OIRA. <https://www.rocis.gov/rocis/downloadResourceDocument.do?uuid=632c6a25-57d2-45f3-84d7-701437f7c73a>. pp. 120-121, supporting-statement appendix.

[^63]: *Federal ICR benchmark*, M1-1.0.0. [methodology/requirements-floor.md, instruction defects](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/requirements-floor.md).

[^64]: Office of Information and Regulatory Affairs, *Creating a Supporting Statement Part A*. Item 14.

[^65]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md, Federal activity and Federal allocation](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^66]: Transportation Security Administration, *Aircraft Operator Security, 49 CFR Part 1544*. Item 14, workload tables.

[^67]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, aircraft-operator Federal hours and dollars](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^68]: Transportation Security Administration, *Airport Security Part 1542*. Item 14.

[^69]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, Airport Security Federal check](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^70]: *Federal ICR benchmark*, M1-1.0.0. [methodology/exemplars.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/exemplars.md).

[^71]: Employee Benefits Security Administration. (2025). *Supporting statement A: Settlement Agreements Between a Plan and a Party in Interest* (OMB Control No. 1210-0091). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=151812302>. Item 14.

[^72]: Transportation Security Administration, *Transportation Worker Identification Credential*. Item 14.

[^73]: Transportation Security Administration, *Flight Training Security Program*. Item 14.

[^74]: Department of Defense, *CMMC Program final rule, official PDF including quantitative tables*. 89 FR 83177-83192, cost analysis.

[^75]: Employment and Training Administration. (2025). *Supporting statement A: Claims and Payment Activities* (OMB Control No. 1205-0010). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=150266202>. Item 14.

[^76]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv, ASM-0020 and ASM-0021](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^77]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md, Item 15; methodology/tool-requirements.md, TR-13 and TR-14](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^78]: Federal Communications Commission, *Incarcerated People’s Communications Services (IPCS) Provider Annual...*. Item 15.

[^79]: Federal Communications Commission, *Incarcerated People’s Communications Services (IPCS) Provider Annual...*. OIRA conclusion action and date.

[^80]: Federal Communications Commission, *Incarcerated People’s Communications Services (IPCS) Provider Annual...*. paragraph 18; Items 12 and 15.

[^81]: Regulatory Information Service Center, *ROCIS PRA Module User Guide*. pp. 49-51.

[^82]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md, Change event](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^83]: U.S. Coast Guard. (2025). *Supporting statement A: Security Plan for Ports, Vessels, Facilities, Outer Continental Shelf Facilities and Other Security-Related Requirements* (OMB Control No. 1625-0077). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=145780303>. Item 15, removal of CG-6025A.

[^84]: U.S. Coast Guard. (n.d.). *Security-plan burden calculation supplement: Appendices A-B* (OMB Control No. 1625-0077). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=162617501>. revised calculation supplement, annual responses.

[^85]: Occupational Safety and Health Administration. (2026). *Supporting statement A: Standard on Process Safety Management of Highly Hazardous Chemicals (29 CFR 1910.119, 29 CFR 1926.64)* (OMB Control No. 1218-0200). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=161728301>. Table 3 and Item 15.

[^86]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md, baseline and interaction requirements](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^87]: Internal Revenue Service. (2025). *Supporting statement A: U.S. Business Income Tax Returns* (OMB Control No. 1545-0123). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=163490901>. Items 12-15.

[^88]: Internal Revenue Service. (n.d.). *2025 Technical, Legislative, and Agency Adjustments2* (OMB Control No. 1545-0123). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=164337801>. change supplement.

[^89]: Transportation Security Administration, *Aircraft Operator Security, 49 CFR Part 1544*. Items 12 and 14.

[^90]: Transportation Security Administration, *Airport Security Part 1542*. Item 12.

[^91]: Transportation Security Administration, *Flight Training Security Program*. Item 12.

[^92]: Transportation Security Administration, *Transportation Worker Identification Credential*. Item 12, Tables 1-9.

[^93]: *Federal ICR benchmark*, M1-1.0.0. [data/scores.csv; data/score-sensitivity.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/scores.csv).

[^94]: Transportation Security Administration, *Aircraft Operator Security, 49 CFR Part 1544*. Item 12, first-flight checklist, foreign-airport employees, and Table 2.

[^95]: Transportation Security Administration. (2024). *Supporting statement A: Certified Cargo Screening Program* (OMB Control No. 1652-0053). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=145598901>. Item 12, Table 7; Item 13.

[^96]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, Program subtotal and Fee using Item12](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^97]: Transportation Security Administration, *Security Threat Assessment for Individuals Applying for a Hazardous...*. Item 12, Tables 5a-5c, 7, 8, and 10.

[^98]: Transportation Security Administration, *Cybersecurity Measures for Surface Modes*. Item 12, coordinator update assumptions; Items 14-15.

[^99]: Bureau of Labor Statistics. (n.d.). *Job Openings and Labor Turnover Survey: Frequently asked questions*. Bureau of Labor Statistics. <https://www.bls.gov/jlt/jltfaq.htm>. JOLTS FAQ, reference periods.

[^100]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, surface cybersecurity Federal table hours and ROCIS hour bridge](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^101]: Transportation Security Administration, *Airport Security Part 1542*. Item 12, applicant wage footnote; Item 13, Table 11.

[^102]: Transportation Security Administration, *Transportation Worker Identification Credential*. Items 12 and 14.

[^103]: Transportation Security Administration, *Airport Security Part 1542*. Item 12, amendment-time assumptions.

[^104]: Transportation Security Administration. (2026). *Supporting statement A: Secure Flight Program* (OMB Control No. 1652-0046). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=161038202>. Item 14, Federal cost table and footnote.

[^105]: Transportation Security Administration, *Flight Training Security Program*. Item 12, summary hours.

[^106]: Transportation Security Administration, *Transportation Worker Identification Credential*. Items 12-13, totals.

[^107]: *Federal ICR benchmark*, M1-1.0.0. [methodology/calibration.md; methodology/tsa-comparison.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/calibration.md).

[^108]: *Federal ICR benchmark*, M1-1.0.0. [research/limitations.md, limitation 5; icrs/202606-1652-001/extraction.json; icrs/202606-1652-002/extraction.json](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/limitations.md).

[^109]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tsa-comparison.md; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tsa-comparison.md).

[^110]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tsa-comparison.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tsa-comparison.md).

[^111]: *Federal ICR benchmark*, M1-1.0.0. [methodology/exemplars.md; data/scores.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/exemplars.md).

[^112]: *Federal ICR benchmark*, M1-1.0.0. [methodology/exemplars.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/exemplars.md).

[^113]: Bureau of Labor Statistics. (2023). *Employer Costs for Employee Compensation: September 2023*. BLS. <https://www.bls.gov/news.release/archives/ecec_12152023.pdf>. USDL 23-2567, civilian sales and office occupations row.

[^114]: Bureau of Labor Statistics, *Survey of Occupational Injuries and Illnesses*. Item 12, compensation reference.

[^115]: Bureau of Labor Statistics. (2024). *Supporting statement A: National Compensation Survey* (OMB Control No. 1220-0164). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=139056101>. Item 12.

[^116]: Federal Communications Commission. (2025). *Supporting statement A: Part 25 of the Federal Communications Commission's Rules Governing the Licensing of, and Spectrum Usage By, Commercial Earth Stations and Space Stations* (OMB Control No. 3060-0678). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=158284001>. Items 13-14.

[^117]: Securities and Exchange Commission. (2024). *Supporting statement A: Form ADV-E, cover sheet for each certificate of accounting of client securities and funds in the custody of an investment adviser* (OMB Control No. 3235-0361). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=146738601>. Items 12-15.

[^118]: Employee Benefits Security Administration, *Settlement Agreements Between a Plan and a Party in Interest*. Items 12-15.

[^119]: *Federal ICR benchmark*, M1-1.0.0. [data/data-sources.csv; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/data-sources.csv).

[^120]: *Federal ICR benchmark*, M1-1.0.0. [data/data-sources.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/data-sources.csv).

[^121]: Occupational Safety and Health Administration, *Standard on Process Safety Management of Highly Hazardous Chemicals...*. Item 12, March 2025 RMP coverage.

[^122]: U.S. Coast Guard, *Security Plan for Ports, Vessels, Facilities, Outer Continental Shelf...*. Item 12, MISLE population description.

[^123]: Financial Crimes Enforcement Network. (2024). *Supporting statement A: FinCEN Form 111 - Suspicious Activity Report* (OMB Control No. 1506-0065). Reginfo.gov, OMB/GSA. <https://www.reginfo.gov/public/do/DownloadDocument?objectID=143239001>. Item 12, calendar 2022 submissions.

[^124]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^125]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv, ASM-0001 through ASM-0013 and ASM-0019 through ASM-0024](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^126]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md; methodology/tool-requirements.md, TR-20](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^127]: Financial Crimes Enforcement Network, *FinCEN Form 111 - Suspicious Activity Report*. Item 8, public comments and responses.

[^128]: Financial Crimes Enforcement Network, *Renewal of SAR reporting: expanded burden methodology*. 85 FR 31605-31611.

[^129]: *Federal ICR benchmark*, M1-1.0.0. [methodology/rubric.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/rubric.md).

[^130]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^131]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md, Collection through Price transformation](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^132]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md, Purchased service through Validation result](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

[^133]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^134]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^135]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md, freeze note](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^136]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tool-requirements.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tool-requirements.md).

[^137]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tool-requirements.md, TR-07, 15, 16, and 18; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tool-requirements.md).

[^138]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-model.md, iteration 4 additions](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-model.md).

[^139]: *Federal ICR benchmark*, M1-1.0.0. [data/model-sections.jsonl; data/assumptions.csv; methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/model-sections.jsonl).

[^140]: *Federal ICR benchmark*, M1-1.0.0. [research/limitations.md, limitation 7](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/limitations.md).

[^141]: *Federal ICR benchmark*, M1-1.0.0. [research/research-summary.md; methodology/exemplars.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/research/research-summary.md).

[^142]: *Federal ICR benchmark*, M1-1.0.0. [methodology/tsa-comparison.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/tsa-comparison.md).

[^143]: *Federal ICR benchmark*, M1-1.0.0. [methodology/calibration.md; methodology/canonical-model.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/calibration.md).

[^144]: *Federal ICR benchmark*, M1-1.0.0. [data/icrs.csv; data/scores.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/icrs.csv).

[^145]: *Federal ICR benchmark*, M1-1.0.0. [methodology/rubric.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/rubric.md).

[^146]: *Federal ICR benchmark*, M1-1.0.0. [data/scores.csv; icrs/*/extraction.json](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/scores.csv).

[^147]: *Federal ICR benchmark*, M1-1.0.0. [data/agency-summary.csv; methodology/calibration.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/agency-summary.csv).

[^148]: *Federal ICR benchmark*, M1-1.0.0. [data/score-sensitivity.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/score-sensitivity.csv).

[^149]: *Federal ICR benchmark*, M1-1.0.0. [data/agency-summary.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/agency-summary.csv).

[^150]: *Federal ICR benchmark*, M1-1.0.0. [data/data-sources.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/data-sources.csv).

[^151]: Office of Management and Budget. (n.d.). *5 CFR 1320.3: Definitions*. Office of Management and Budget. <https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.3>. Definitions,burden andscope.

[^152]: Office of Management and Budget, *5 CFR 1320.8: Agency collection responsibilities*. Agency collection responsibilities.

[^153]: Bureau of Labor Statistics, *Job Openings and Labor Turnover Survey: Frequently asked questions*. FAQ questions7,8,14.

[^154]: Bureau of Labor Statistics. (n.d.). *May 2023 occupational employment and wage estimates: Rail transportation (NAICS 482000)*. Bureau of Labor Statistics. <https://www.bls.gov/oes/2023/May/naics3_482000.htm>. May2023 RailTransportationNAICS482000.

[^155]: Bureau of Labor Statistics. (n.d.). *Employer Costs for Employee Compensation: June 2025*. Bureau of Labor Statistics. <https://www.bls.gov/news.release/archives/ecec_09122025.htm>. June2025 ECEC Tables1–4.

[^156]: Office of Personnel Management. (n.d.). *Salary Table 2025-DCB*. Office of Personnel Management. <https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/salary-tables/pdf/2025/DCB.pdf>. SalaryTable2025-DCB.

[^157]: U.S. Census Bureau. (n.d.). *Geographic mobility: 2023 tables*. U.S.Census Bureau. <https://www.census.gov/data/tables/2023/demo/geographic-mobility/cps-2023.html>. 2023 geographicmobility,Table2.

[^158]: Bureau of Labor Statistics, *Employment Cost Index*. EmploymentCostIndex.

[^159]: U.S. Census Bureau. (n.d.). *County Business Patterns*. U.S.Census Bureau. <https://www.census.gov/programs-surveys/cbp.html>. CountyBusinessPatterns.

[^160]: Bureau of Economic Analysis, *Gross domestic product price index*. NIPA priceindexes.

[^161]: Office of Information and Regulatory Affairs. (n.d.). *Estimating burden*. Office of Information and Regulatory Affairs. <https://digital.gov/guides/pra/estimate-burden>. Burden estimation guidance.

[^162]: Employee Benefits Security Administration, *Labor Cost Inputs Used in EBSA OPR Regulatory Impact Analyses and...*. Tables1–3; Census ASM/SAS and BLS employment matrix.

[^163]: U.S. Census Bureau, *Attachment N - AIES Dress Rehearsal Preliminary Findings and...*. Printed page19.

[^164]: Internal Revenue Service, *U.S. Business Income Tax Returns*. Items12–15; taxpayer burden survey andmodel.

[^165]: Energy Information Administration. (n.d.). *Commercial Buildings Energy Consumption Survey: 2018 data*. Energy Information Administration. <https://www.eia.gov/consumption/commercial/data/2018/>. 2018 Table B1 and detailed building characteristics.

[^166]: Energy Information Administration. (n.d.). *Manufacturing Energy Consumption Survey*. Energy Information Administration. <https://www.eia.gov/consumption/manufacturing/>. Manufacturing Energy Consumption Survey.

[^167]: Bureau of Labor Statistics. (n.d.). *Employment Projections: Occupational projections and characteristics*. Bureau of Labor Statistics. <https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm>. Table1.2 occupational projections and National Employment Matrix.

[^168]: Bureau of Labor Statistics. (n.d.). *Current Employment Statistics*. Bureau of Labor Statistics. <https://www.bls.gov/ces/>. Current Employment Statistics earnings series.

[^169]: Bureau of Labor Statistics. (n.d.). *Producer Price Indexes*. Bureau of Labor Statistics. <https://www.bls.gov/ppi/>. Producer Price Index industry and commodity series.

[^170]: U.S. Census Bureau. (n.d.). *Annual Survey of Manufactures*. U.S. Census Bureau. <https://www.census.gov/programs-surveys/asm.html>. Annual Survey of Manufactures historical tables.

[^171]: U.S. Census Bureau. (n.d.). *Service Annual Survey*. U.S. Census Bureau. <https://www.census.gov/programs-surveys/sas.html>. Service Annual Survey historical expense tables.

[^172]: Office of Personnel Management. (n.d.). *Salaries and wages: Salary tables*. Office of Personnel Management. <https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/>. Annual GS base and locality pay tables.

[^173]: US EPA, *CEMS Cost Model*. 2007 CEMS cost workbook; Costs/Activities/SummaryInfo.

[^174]: Occupational Safety and Health Administration, *Standard on Process Safety Management of Highly Hazardous Chemicals...*. March2025 RMP facility extract.

[^175]: U.S. Coast Guard, *Security Plan for Ports, Vessels, Facilities, Outer Continental Shelf...*. Security-plan population counts.

[^176]: Financial Crimes Enforcement Network, *FinCEN Form 111 - Suspicious Activity Report*. Calendar2022 SAR submissions.

[^177]: Employment and Training Administration, *Claims and Payment Activities*. FY2025 UIPL19-24 allocation assumptions.

[^178]: Department of Defense, *CMMC Program final rule, official PDF including quantitative tables*. RIA cost tables and eMASS historical budgets.

[^179]: *Federal ICR benchmark*, M1-1.0.0. [data/assumptions.csv](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/assumptions.csv).

[^180]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv; research/final-validation.json](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^181]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, HME Agentpathway share](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^182]: *Federal ICR benchmark*, M1-1.0.0. [data/calculation-checks.csv, Capital recovery exemplar; raw/methods/epa-yeast-2017-extraction.json](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/data/calculation-checks.csv).

[^183]: *Federal ICR benchmark*, M1-1.0.0. [methodology/canonical-data-dictionary.md](https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/16aeb85d976eb3a89ecb3872d4dda94753e77cd3/methodology/canonical-data-dictionary.md).

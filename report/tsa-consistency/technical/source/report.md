# Consistency and Defensibility of Burden and Cost Estimation Across TSA Information Collections

Technical analytical report | September 9, 2026

## Executive summary

TSA's published estimation methods show substantial coherence in the activities and components that this study could compare. The more consequential observed control risks arise within individual Supporting Statements, where population definitions, calculations, tables, source transformations, and narrative do not always reconcile. This distinction supports an institutional response that preserves useful analytical methods while strengthening the connection between the quantitative model and its published representations.

The study examines the public evidence for Information Collection Requests (ICRs) submitted by the Transportation Security Administration (TSA), focusing on Supporting Statement A Items 12–15: respondent burden and its labor valuation, nonlabor costs, Federal costs, and changes from the applicable baseline. The evidence covers 90 recent package versions received from September 9, 2021, through September 9, 2026; 48 assigned TSA control histories; 468 normalized activity representations; 162 reviewed assumption observations; and 341 quantitative checks. The 90 packages include historical versions, proposals, and pending submissions. They are not 90 independent, currently approved collections.

The task/method comparison register contains 32 adjudicated records: 15 consistent, 8 different with an observable explanation, 6 unresolved, and 3 not comparable. None remains potentially inconsistent after adjudication. The register combines comparisons across collections, across renewal versions, and among selected comparable components within a package. Its distribution describes these selected tests; it does not estimate TSA-wide consistency or validate every underlying assumption.

Several recurring analytical components are coherent. Carrier and cargo security-program requests retain a one-hour documentation coefficient. Surface security-training amendments retain an eight-hour coefficient, and training record entry retains one minute per record. Cybersecurity plan review retains eight manager hours plus 24 analyst hours per plan. Consistency here means agreement in the specified published component, with actor and task boundaries preserved. A stable coefficient across renewals is evidence of continuity, not independent confirmation of actual task time. [[CMP-01,CMP-02,CMP-03,CMP-16]]

Observable differences often reflect different work. Examples include initial applications versus incremental resubmissions, security-threat triage versus contractor response handling, and pathways that add fingerprinting and travel. Other changes have a documented basis in online migration, user-experience feedback, employee universe, source vintage, or who pays for an examination. Such explanations justify distinguishing estimates; they do not establish that every proxy is optimal or that unpublished timing evidence has been independently validated. [[CMP-07,CMP-11,CMP-12,CMP-13,CMP-15,CMP-22,CMP-24,CMP-25]]

Six task/method comparisons remain unresolved. The public evidence does not align all relevant task bundles, denominators, travel measures, renewal boundaries, or calibration evidence. Airport and carrier amendment preparation, for example, cannot be interpreted as an efficiency comparison merely because the published times differ. These cases warrant targeted analyst and program review, rather than a finding of established methodological error. [[CMP-04,CMP-05,CMP-09,CMP-10,CMP-14,CMP-21]]

The separate within-ICR review retains seven potentially inconsistent findings and one unresolved finding. The seven concern: Hazardous Materials Endorsement (HME) enrollment-path overlap in a pending package; Maryland Three cost products; a generic-clearance table and narrative; Exercise Information System (EXIS) stock versus new-user definitions; an annual Federal-cost column that contains a three-year-scale value; a monthly separation-rate proxy applied annually in a pending surface-cyber package; and a cybersecurity Federal-cost product that does not reproduce the displayed total. These findings identify public reconciliation risks. They do not establish corrected official burden, actual expenditure, or the internal causes of the discrepancies. [[FIND-HME,FIND-MD3,FIND-GENERIC,FIND-EXIS,FIND-LEO,FIND-TURNOVER,FIND-CYBER-COST]]

Counterevidence is central to the conclusion. Prior HME and Transportation Worker Identification Credential (TWIC) pathway partitions reconcile. The law enforcement officer (LEO) annual-cost narrative is coherent even though its table heading conflicts with the magnitude in the cell. PreCheck's difference between total hours and monetized hours is explained arithmetically by separately identified correction and survey activities; the unresolved question is their exclusion from valuation. These observations narrow the findings and prevent overgeneralization. [[FIND-HME,FIND-LEO,FIND-PRECHECK]]

The principal institutional implication is to distinguish **method governance**, which concerns the suitability and consistency of analytical choices, from **representation governance**, which concerns synchronization of calculations, tables, footnotes, summaries, and narrative. The evidence provides a more direct basis for strengthening the latter than for imposing a single time coefficient or compensation factor across unlike activities. Some risks, especially turnover calibration and population definitions, require both forms of governance.

The recommended architecture retains source-bound inputs, explicit units and periods, versioned assumptions, formulas, population partitions, and baseline/change ledgers. Deterministic checks should precede generation of output tables and draft Items 12–15 language from the same approved quantitative model. Analysts and program specialists remain responsible for task definition, proxy selection, scope exceptions, and final review. No estimate of implementation savings is made.

## 1. Purpose and scope

### 1.1 The analytical question

This report asks how consistently TSA estimates burden and cost for analytically similar information-collection activities, where variation has an observable justification, and what analytical-control risks remain within published ICRs. It is an empirical examination of public estimation evidence, intended for economic analysts, program and policy partners, Paperwork Reduction Act (PRA) practitioners, and reviewers.

Consistency matters because an estimate may be reused for renewal, policy design, program analysis, or review long after its original preparation. A later analyst needs to know what activity was timed, whose time was valued, which population was counted, and which approval or prior estimate supplies the baseline. Reproducibility means another analyst can reconstruct a result from its stated inputs and operations. Auditability adds the ability to trace those inputs and operations to their sources and explanations. Defensibility requires both, together with a justified fit between the model and the collection activity.

These are related but separate properties. A formula can reproduce exactly and still use an unsuitable proxy. A task-time coefficient can remain consistent across programs while a published cost total fails to use it correctly. Conversely, different coefficients can be defensible when they describe different actors, tasks, or lifecycle stages. The study tests these distinctions rather than treating numerical uniformity as the objective.

### 1.2 Evidence and administrative scope

The recent-package window is defined by actual receipt dates, September 9, 2021, through September 9, 2026, rather than by the date-like characters in a package reference number. The archived official search produced 92 rows: 90 TSA ICR packages and two Office of Personnel Management (OPM) common-form requests excluded from TSA-authored statement comparison. The inventory also identifies 48 assigned TSA control histories and five packages with unassigned control numbers. A blank control number does not create a new independent collection identity. [[INVENTORY]]

All 42 packages returned by the active search and all seven returned by the pending search appear within the 90-package recent corpus. Active-search membership is distinct from a historical approval conclusion. A package approved earlier can be a predecessor rather than the currently active version. Proposed-rule and improperly submitted packages provide evidence of published analytical constructs, but not evidence that their workloads were implemented. Status descriptions throughout this report refer to the September 9, 2026 evidence snapshot. [[INVENTORY]]

Prior versions are used to test continuity, identify changed task boundaries, and challenge apparent discrepancies. Of the 90 recent packages, 84 have explicit previous-package links that reach usable Supporting Statements; six lack such a link. The broader evidence represents 135 package versions and 134 archived statement versions, including one administrative predecessor without a statement. Retrieval of a predecessor does not itself verify its numerical use as an Item 15 baseline.

### 1.3 What this report measures

The Office of Management and Budget (OMB), including its Office of Information and Regulatory Affairs (OIRA), provides the public package records used here. The unit of comparison is ordinarily a source-defined activity or analytical component, not the whole collection. An activity representation is a structured record of a task as described in a table, narrative, or other source representation. Several representations can describe the same underlying task. They must not be added as if they were distinct burdens.

The report uses the completed TSA evidence register as its empirical basis and selectively draws on four already-reviewed Federal comparators. It does not extend the source corpus or conduct a new Federal benchmarking exercise. Recommendations are a synthesis of the documented risks and existing analytical architecture; they are not additional empirical findings about TSA operations.

Public documents cannot reveal all internal workbooks, subject-matter judgments, timing samples, or production procedures. The absence of a published explanation does not establish that no internal rationale exists. Accordingly, the report neither attributes discrepancies to particular analysts or offices nor asserts that manual processing, internal procedures, or a particular technology caused them.

## 2. Analytical method

### 2.1 Normalize the task before comparing the number

The analysis preserves the original statement and values, then records structured fields for the activity, actor, population, task scope, unit, period, lifecycle, and evidence basis. A collection shape describes its broad operational structure, such as security-program compliance, credentialing or security threat assessment, operational reporting, claims, or cybersecurity compliance. An activity shape describes a task within that structure, such as application, enrollment, renewal, amendment, review, recordkeeping, appeal, or verification.

A shared activity label identifies a candidate comparison. It does not establish that the work is equivalent. For example, an annual school recordkeeping bundle and entry of one employee training record can both involve records, but their denominators differ. A Federal reviewer processing an electronic submission may perform different work from a reviewer verifying substantive eligibility. The analysis retains these failed matches rather than forcing a numerical comparison. [[CMP-23,CMP-28]]

Normalization converts hours to minutes by multiplying by 60 when a common time unit is useful. It does not convert an annual bundle to a per-event mean without a defensible event denominator. It preserves a maximum as a maximum, rather than treating it as a mean. It also preserves unknown active-versus-elapsed time, one-time versus recurring work, and source precision. Unknown information is not zero and does not count as evidence that two cases match.

For labor valuation, the comparison retains occupation, wage statistic, employee universe, geography where documented, source vintage, and loading base. Direct total compensation, total-compensation-to-wage ratios, benefit shares, and overhead are different constructs. For nonlabor and Federal costs, the analysis preserves payer identity, resource cost versus transfer, recurring versus one-time treatment, and relevant cost period. For Item 15, it preserves baseline identity rather than relying only on subtraction of displayed totals.

### 2.2 Similarity, explanation testing, and classification

A strong match has the same substantive actor and task boundary without a known material scope conflict. A moderate match permits a bounded methodological comparison with stated differences or incomplete scope. A weak match is useful for discovery only. Similarity is evaluated before interpreting numerical differences.

The sequence is: define the component; establish similarity; observe agreement or difference; test observable explanations; then classify. Relevant explanations include legal or operational requirements, complexity, actor, population, frequency, technology, source vintage, and implementation versus steady state. The comparison remains unresolved when those features cannot be aligned sufficiently.

@table definitions

The classifications concern the tested component and named versions. They are not grades for entire packages. The task/method register includes cross-collection, lineage, and within-package component comparisons; the separate within-ICR findings register contains the eight challenged reconstruction and reconciliation cases. A within-package methodological comparison, such as training record entry across surface modes, is therefore distinct from a within-document discrepancy finding. This distinction preserves the two reported denominators without relabeling the adjudications.

### 2.3 Evidence status and confidence

The analysis distinguishes five evidence labels. **Published** denotes what the source states. **Calculated** denotes a reproduced arithmetic result. **Normalized** denotes a transparent unit or representation transformation. **Inferred** denotes an analytical judgment, such as the comparability classification. **Unresolved** denotes a question that available evidence does not settle. A record can contain published inputs and an inferred conclusion; one label must not erase the other.

Confidence describes confidence in the bounded public-evidence classification. High confidence that a table and its stated formula conflict is not high confidence that the analyst has identified the correct replacement model. Likewise, agreement between two printed coefficients does not independently validate the actual time respondents require.

### 2.4 Challenge and prior-version falsification

Every adjudicated comparison and finding has a challenge record. The 41 challenge records cover all 40 adjudications and one rejected foreign-air-carrier rounding candidate. Challenges test whether an apparent discrepancy can be explained by source extraction or table geometry, hidden precision, different actors, task bundles, populations, periods, source vintages, prior versions, or a legitimate interpretation.

Prior-version falsification asks whether earlier evidence contradicts a proposed generalization. It is especially useful when an apparent defect in one recent version might otherwise be attributed to an entire collection family. The HME predecessor and TWIC partitions constrain the current HME finding. The LEO narrative constrains the cost-table finding. PreCheck's named subtotals constrain its valuation question. A repeated total in an earlier version establishes historical recurrence; it does not identify the internal mechanism that produced it. [[FIND-HME,FIND-LEO,FIND-PRECHECK,FIND-CYBER-COST]]

### 2.5 Deterministic quantitative review

The quantitative review contains 341 checks across 40 versions: 41 checks reused from the Federal benchmark's TSA cases, 23 source-specific checks, and 277 activity-row screens. A deterministic check applies the same explicit rule to the same inputs and produces the same result. Checks include count-by-time products, role-specific cost construction, population partitions, component sums, annualization, and cross-representation agreement.

Arithmetic dispositions remain distinct from final findings. A row flagged for source precision or scope review is not automatically an error. The analysis tests whether display rounding could explain a difference and whether the compared numbers actually refer to the same quantity. Period and population mismatches can require analytical judgment even when multiplication is straightforward.

The review does not divide flagged checks by 341 to estimate an error rate. Checks are heterogeneous, correlated, and unevenly distributed across packages. Principal-task normalization across all 90 recent packages is broader than quantitative testing across 40 versions, and neither constitutes full-model validation of the entire portfolio.

## 3. TSA portfolio and evidence coverage

### 3.1 The evidence base and its denominators

@figure classification

@table coverage

The evidence base is broad enough to identify recurring task structures and to test selected comparable methods. It is not designed as a probability sample of independent estimation decisions. Serial renewals, transfers between controls, and multiple representations create dependence. The analysis therefore reports counts of evidence records and explicit cases instead of confidence intervals or agency-wide defect rates.

@table portfolio

The portfolio groups in Table 3 are descriptive coverage groupings. They cover security programs; credentialing, redress, and vetting; cyber and surface assessment; operational, fee, and system activities; and other collections. They are not rankings of offices or quality. The large credentialing group is especially rich in pathway and formula-header evidence, which influences the composition of the assumption register.

### 3.2 Approval status and version coverage

@table status

The 76 packages with approval conclusions in Table 4 include historical versions; only 42 packages are in the active-search snapshot. The seven pending packages are not final approved estimates. Four proposed-rule comment outcomes and three improperly submitted outcomes remain analytically distinguishable from approvals. These status counts are mutually exclusive conclusion categories; active membership is a separate attribute. [[INVENTORY]]

This distinction affects interpretation of the case studies. The HME package received August 21, 2026, and the surface-cyber package received September 1, 2026, were pending in the evidence snapshot. The Maryland Three, generic-clearance, EXIS, LEO, PreCheck, and pipeline plan-review packages used in the principal cases were active. Status establishes the administrative context, not the arithmetic quality or empirical validity of a statement. [[INVENTORY]]

### 3.3 Coverage is not validation

Every recent package has Items 12–15 section coverage and principal-task normalization. That means its principal activity is represented in an inspectable form. It does not mean that all secondary activities, cohort relationships, formulas, or cost allocations have been independently reconstructed and validated.

The 468 normalized activity representations exclude 25 additional activity-context records used to connect assumptions. The register explicitly identifies 27 representation-overlap groups. Its 97-row consistency matrix is a member-observation view of comparisons, not 97 independent findings. The 162 reviewed assumptions comprise 69 scalar or categorical observations and 93 formula-header coefficients. Discovery searches cover 17 families, while reviewed assumption observations cover 16; Item 15 is handled through baseline/change records.

These distinctions matter for institutional reuse. A reviewed coefficient may be a candidate input to a new model only after its applicability is checked. A normalized row may supply a reconstruction starting point without establishing that its population can be added to another row. A source link supplies provenance without validating a behavioral assumption.

## 4. Cross-ICR methodological consistency

### 4.1 What the positive findings establish

The 15 consistent task/method comparisons show that several source-defined analytical components recur coherently across programs, modes, or renewal versions. The evidence supports preserving those components and their task definitions. It does not support describing all TSA methods as uniform or fully validated.

The main examples span security-program work, administrative record entry, compensation, applicant time, Federal plan review, fee financing, familiarization, legal review, appeals, incident reporting, and applications. Appendix A provides the complete 32-comparison register, including the scope limitations that govern use of each conclusion.

### 4.2 Security-program amendments and record entry

Domestic carrier, foreign carrier, and indirect air carrier statements each identify one hour for industry-requested security-program documentation. The useful match is an operator preparing a request to change an existing program. TSA-issued directives, initial program development, and Federal review are separate tasks. The indirect air carrier description emphasizes approval of existing business practices, which may be narrower than other requests. The consistent classification is therefore local to the published one-hour component. [[CMP-01]]

Surface security-training program amendments retain eight hours and a 10 percent annual amendment share across modes and the receiving collection after consolidation. The transfer preserves a recognizable analytical structure, but it does not create independent empirical replications. The appropriate reusable object is a defined amendment activity with a time coefficient, frequency assumption, applicability conditions, and lineage. [[CMP-02]]

Training record entry is separately estimated at one minute per record for freight rail, public transportation/passenger railroad, and over-the-road bus activities. The coefficient concerns an administrative record entry, not attendance at training. It illustrates why a well-bounded activity can support comparison across modes while a broad label such as training burden cannot. [[CMP-03]]

### 4.3 Compensation and applicant-time components

Two pipeline packages use compensation-loading ratios of 1.467370066 and 1.467370 with aligned source period and employee universe. Their difference is displayed precision. This supports a common treatment of the formula and precision convention, not a requirement that the same ratio apply to different years or worker populations. [[CMP-06]]

The Federal Air Marshal Service (FAMS) and Transportation Security Officer (TSO) medical applicant statements share a $32.66 mean wage, a 1.4582 loading factor, and an 11-minute waiting assumption for the compared applicant component. Provider compensation and incumbent Federal employee travel have different actor boundaries. The agreement does not resolve the separate travel-proxy questions discussed in Section 6. [[CMP-08]]

HME and TWIC describe fee financing, and TWIC explicitly distinguishes excess revenue as a transfer. The consistency finding concerns that financing convention. It does not show that fee-funded activities have no resource cost or that fees should be added to underlying Federal costs to estimate total social cost. Gross resource use, fee receipts, and net budget effects remain different quantities. [[CMP-18]]

### 4.4 Federal review and recurring components

Cybersecurity implementation-plan reviews retain eight manager hours and 24 analyst hours per plan across surface and pipeline packages and their versions. This is one of the clearest examples of a reusable role-based activity structure. It is also the clearest demonstration that method consistency and output consistency are separate: the plan-review staffing component is consistent, while a later pipeline cost total does not reproduce from its displayed wages and workload. [[CMP-16,FIND-CYBER-COST]]

Maryland Three familiarization remains a distinct half-hour step across renewal versions, separate from travel and the complete 5.75-hour process. Proposed cybersecurity operational implementation-plan legal review retains a four-hour Federal component across submissions; the 50 percent eligibility coefficient is separate. Those proposed submissions are not two implemented programs. The first had an improperly submitted outcome, and the later assigned-control submission had a proposed-rule comment outcome. [[CMP-19,CMP-20]]

Other stable components include an eight-hour Law Enforcement Officers Safety Act (LEOSA) rejection-review request, a 30-minute maximum for pipeline physical-incident reporting, a one-hour Ronald Reagan Washington National Airport (DCA) Access Standard Security Program (DASSP) initial operator application coefficient, claim filing, a 130-second Secure Flight identity-transmission component, and a 10-minute canine adoption application. The incident-reporting statistic is a maximum, not a measured mean. DASSP field scope is not proven identical across versions, and neighboring armed-security-officer nomination work is excluded. Secure Flight resolution calls and visitor applications are outside the identity-transmission comparison. [[CMP-26,CMP-27,CMP-29,CMP-30,CMP-31,CMP-32]]

### 4.5 Implications for reuse

The positive evidence supports reusable activity archetypes: structured definitions of a task, its actor, population unit, time statistic, frequency, and associated cost construction. A coefficient should travel with that definition and its evidence. Reusing the number without its scope would discard the feature that made the comparison defensible.

A consistent published coefficient may be retained as a candidate institutional default within a documented applicability domain. It should still have a review trigger when technology, form content, population, legal requirements, or timing evidence changes. Continuity should make an assumption easier to review, not exempt it from review.

## 5. Explainable variation

### 5.1 Different estimates can be appropriate

Eight comparisons are classified different with an observable explanation. They illustrate why standardization should govern definitions, evidence, and transformations while allowing substantively different inputs. A published explanation can establish why two estimates differ without independently proving the accuracy of both.

@table explained

### 5.2 Task scope, actor, and lifecycle

Comment-card processing distinguishes Federal security-threat triage, at 0.5 minute, from contractor reading and response selection, at five minutes. These are sequential functions performed by different actors. A ratio between their times would obscure the workflow rather than measure inconsistency. [[CMP-11]]

The mobile driver's license (mDL) application example distinguishes 20 hours of initial work from five hours for resubmission of an insufficient application. The latter is an incremental 25 percent of initial effort. It is not an alternative that replaces all initial work. By contrast, credentialing pathways can be mutually exclusive when the source says online renewal avoids an in-person visit. A common architecture must express both additive follow-up work and exclusive alternatives. [[CMP-22,FIND-HME]]

For bidders seeking Sensitive Security Information (SSI) access, the path with a criminal history records check (CHRC) includes fingerprinting and travel/wait activities that the no-CHRC path omits. Published totals of 116 and 15 minutes therefore have an observable scope explanation. Uniformity would be inappropriate if it removed work that one pathway actually includes. [[CMP-25]]

### 5.3 Technology and documented experience

The Federal Flight Deck Officer (FFDO) statement removes a 10-minute verbal interview because certification questions move online and duplicative questions are removed. This supports the explanation for deleting that task. It does not by itself verify the entire Item 15 numerical change bridge. [[CMP-12]]

The LEO checkpoint-login estimate increases from one to four minutes, while the Traveler Redress Inquiry Program (TRIP) form estimate decreases from 60 to 30 minutes. The respective recent statements cite user experience as the basis. These are observable explanations for changed estimates. The timing samples and their representativeness are not publicly established in this evidence, so the report does not describe the new times as independently measured universal completion times. [[CMP-13,CMP-24]]

### 5.4 Source choice and payer boundaries

An airport compensation factor of 1.454667 uses full-time private-industry workers and a June 2024 source period, while the domestic carrier factor of 1.4582 uses production, transportation, and material-moving workers from March 2023. The differing universe and vintage explain unequal ratios. A month-label ambiguity in the carrier paragraph remains, and an explained difference does not establish optimal proxy selection. [[CMP-07]]

The TSO medical examination statement moves payment from Federal contractor funding to candidates, using $150 for each of 18,000 examinations. The payer change explains movement between cost categories. It is not evidence of an equivalent reduction in resources consumed. A governed estimate should identify the examination as the same resource activity while separately recording the party that pays. [[CMP-15]]

## 6. Unresolved cross-ICR questions

### 6.1 Why these questions remain open

The six unresolved task/method comparisons are candidates for targeted analytical review. Each has enough relationship to make a question useful, but insufficient published evidence to settle the relevant scope or methodological explanation. None is a surviving potentially inconsistent cross-ICR finding.

@table unresolved

### 6.2 Amendment preparation and Federal review

Airport amendment preparation is estimated at 25 hours, compared with one hour for carrier request documentation. The airport obligation includes development, submission, and implementation, but its timed paragraph does not decompose the preparation bundle. Equal case complexity and complete task boundaries are not established. The appropriate question is what work each estimate contains, not whether one program is 25 times less efficient. [[CMP-04]]

The Federal amendment-review comparison is similarly constrained. The indirect air carrier statement converts 15 days to 120 hours and pools TSA-issued and industry-requested amendments. The foreign carrier statement describes four hours of field work and 6.75 hours of headquarters review. The evidence does not establish identical amendment types, staffing, or complexity. It also does not establish that the 15-day quantity is elapsed rather than active time. Analysts would need a task and role decomposition for aligned case types before a useful numerical comparison could be made. [[CMP-14]]

### 6.3 Coordinator updates and turnover

Surface-cyber updates use five minutes for a new coordinator or alternate. Pipeline updates use 30 minutes for an operator's coordinator and/or alternate update. One event may contain different numbers of people, fields, or verification steps. The six-to-one displayed-time ratio is not a defensible measure of methodological inconsistency until that cardinality is aligned. [[CMP-05]]

The associated frequency models also have different constructs: a four-percent annual substitution proxy versus one operator update per year. No common person-stock denominator or shared calibration is established. The comparison therefore remains a method-selection question. Separately, the surface statement's own source-to-period transformation is a within-ICR finding; the unresolved comparison does not dilute or expand that narrower finding. [[CMP-21,FIND-TURNOVER]]

### 6.4 Travel and online renewal

FAMS medical applicant travel uses 20 minutes each way, while the TSO statement uses 34 minutes each way. Different cited studies visibly explain the source selection, but the archived primary-source review does not establish an aligned travel quantity or applicant population. The Altarum brief describes diary-day travel rather than explicitly one-way travel, and the FAMS source concerns adults aged 50 or older. The evidence therefore leaves both the TSO doubling and applicant-population fit open. No corrected travel total is selected. [[CMP-09]]

TWIC and HME use 10 minutes for online renewal, while PreCheck uses 1.8 minutes and separately models conditional biometric submission. TWIC reports pilot completion faster than its retained conservative estimate. These distinctions prevent treating all three published figures as interchangeable measured means. Closure would require aligned form content, conditional-task definitions, and timing evidence. Conditional biometrics must not be labeled duplicate renewal burden merely because it is an additional row. [[CMP-10]]

The unresolved questions should be maintained as a small, explicit review agenda. Resolving them requires program knowledge, model access, or task-specific timing and calibration evidence. Repeatedly searching unrelated public collections would not supply those missing facts.

## 7. Within-ICR consistency and reconstruction

### 7.1 What the eight findings mean

The within-ICR review asks whether a published statement's own definitions, inputs, formulas, tables, and narrative can be reconciled. Seven findings remain potentially inconsistent after challenge; one remains unresolved. The seven are not interchangeable failure modes. Some concern arithmetic, some concern the meaning of a population or period, and one concerns transformation of an external statistic into a model coefficient.

@table findings

The designation potentially inconsistent reflects an unresolved material conflict in the published evidence after challenge. It does not mean that every aspect of the package is suspect, that actual burden has been measured incorrectly by a known amount, or that the correct underlying model can be reconstructed without further information. Table 7 identifies the package context; the cases below explain the specific observation and its limits.

### 7.2 HME: potential overlap between enrollment pathways

The Hazardous Materials Endorsement (HME) package, reference 202606-1652-002, control 1652-0027, was pending at the evidence cutoff. The statement describes online renewal as avoiding an enrollment-center visit. However, the in-person rows already exhaust the TSA-agent applicant population before online renewals are added. [[FIND-HME]]

For 2026, the two in-person counts are 75,000 and 95,454, which sum to the parent cohort of 170,454. Adding 53,182 online renewals produces a partition residual of 53,182. The corresponding residuals are 54,840 in 2027 and 53,816 in 2028, exactly the displayed online-renewal counts. These are residuals in an analyst's exclusive-pathway identity; zero is the expected identity result, not a published source value. [[FIND-HME]]

@table hme

The challenge tested whether table extraction had displaced merged headers or whether in-person and online activities were deliberately additive. Original cell origins were verified. The narrative's avoidance of an in-person visit does not support charging the full parent population for that visit and then adding online renewal as another complete pathway. A documented rule requiring both activities, or evidence of a different parent cohort, could change the interpretation; neither is established in the reviewed paragraphs. [[FIND-HME]]

The finding is deliberately narrow. The prior HME statement partitions its populations coherently, and TWIC partitions also reconcile. The evidence does not support a general claim that credentialing models duplicate pathways. Nor can the residual counts simply be multiplied by a selected time or wage to produce an official corrected burden: the authoritative eligibility and activity rules must first be established. The recommended control is a declared exclusive/additive relationship for every pathway and a population-partition check against its parent cohort. [[FIND-HME]]

### 7.3 Maryland Three: displayed inputs do not reproduce cost totals

The Maryland-3 Airports package, reference 202501-1652-002, control 1652-0029, was active and approved with change. Its stated annual population is 262 applicants, its task bundle totals 5.75 hours, and its displayed loaded wage is $98.37 per hour. Their product is $148,194.405, compared with the published annual figure of $208,718. The displayed per-person product is $565.6275, compared with the published $563.63. [[FIND-MD3]]

The large annual discrepancy is not explained by display rounding. The review also tested a three-year interpretation, additional tasks, a different actor or wage boundary, and prior-version values. The source separately reports a three-year narrative amount of $626,155. The predecessor has 369 applicants and a different wage, which cannot substitute for the current inputs without an explicit model explanation. [[FIND-MD3]]

This is a cost-product reconstruction finding. The independently calculated products show what the displayed operands yield, not what the official estimate should necessarily become. A different eligible population, additional priced task, or different annual time basis would need to be documented and reconciled across the table and narrative. A deterministic control should require every reported cost total and per-person amount to resolve to the same approved inputs and rounding rules. [[FIND-MD3]]

### 7.4 Generic clearance: arithmetic, totals, and scope conflict

The Generic Clearance for the Collection of Qualitative Feedback on Agency Service Delivery, reference 202504-1652-003, control 1652-0058, was active and approved without change. Its feedback row specifies 589,066 respondents and 45 minutes. The product is 441,799.5 hours, whereas the table publishes 589,066.43 hours. The five displayed respondent rows sum to 4,149,166, compared with a table total of 7,094,500. The annual narrative gives 13,383 hours while the table's displayed total is 1,180,050 hours. [[FIND-GENERIC]]

These are three related reconciliation problems within one finding, not three independent package defects. Even a half-minute allowance around the displayed feedback duration does not explain the row-product difference. Recovered table geometry confirms the minutes column and row identities. The preceding version repeats table values, which demonstrates recurrence but does not resolve the arithmetic or validate the totals. [[FIND-GENERIC]]

A generic clearance establishes a ceiling rather than observed realized collections. That qualification prevents claims about actual respondent hours or realized overstatement. It does not make incompatible annual table and narrative values reconcile. The appropriate response is to identify the authoritative ceiling, the scope of each table, and the column units, then bind all summaries to the same selected calculation. Neither published total is adopted here as the corrected official ceiling. [[FIND-GENERIC]]

### 7.5 EXIS: stock and new-user flows are not interchangeable

The Exercise Information System (EXIS) package, reference 202411-1652-004, control 1652-0057, was active and approved without change. Table 3 estimates exercisers from five percent of new limited users. Table 4 instead applies 95 percent to the entire limited-user stock, although the narrative describes subtracting Table 3 exercisers. [[FIND-EXIS]]

For 2025, the limited-user stock is 12,654 and Table 3 exercisers are 90. Following the stated subtraction yields 12,564, while Table 4 gives 12,021.3. The respective differences are 542.7, 632.7, and 702.2 responses across the three modeled years. These differences exceed rounding. [[FIND-EXIS]]

There is a plausible alternative model: if five percent of the entire user stock exercises annually, then a 95-percent stock calculation could be appropriate. But that model would depart from the stated new-user-based Table 3 subtraction. The evidence does not select which participation behavior is correct. It identifies a mismatch between the narrative operation and the table's denominator. A control should require every stock, inflow, subset, and subtraction to use an explicit population identity. [[FIND-EXIS]]

### 7.6 LEO: annual heading versus three-year magnitude

The Law Enforcement Officers Flying Armed package, reference 202509-1652-001, control 1652-0072, was active and approved with change. Its annual Federal task inputs are 83,749 responses, 0.025 hour per response, and $75.94 per hour. The annual product is $158,997.4765, which is consistent with the narrative's rounded annual figure of $158,997. The table's annual-cost column contains $476,990.86. [[FIND-LEO]]

Multiplying the displayed annual product by three yields $476,992.4295, within wage-rounding tolerance of the table cell. A three-year interpretation therefore explains the magnitude but not the annual heading. The source excludes other Federal entities from the described cost, and the review did not identify an additional annual task that would account for the cell under its heading. [[FIND-LEO]]

This is a period-label and representation conflict, not evidence that all Federal costs in the package are wrong. The coherent annual narrative is affirmative counterevidence against a broader conclusion. A governed output should inherit both the amount and its period from the same result object, so that an annual column cannot be populated with a three-year result without an explicit transformation. [[FIND-LEO]]

### 7.7 Surface cybersecurity: a source-period and event-definition problem

The Cybersecurity Measures for Surface Modes package, reference 202606-1652-001, control 1652-0074, was pending at the evidence cutoff. Its coordinator update model uses a four-percent coefficient annually, while the source footnote describes an average of monthly separation rates. The model also combines the coefficient with nine-percent residential mobility to represent contact changes. [[FIND-TURNOVER]]

The arithmetic representation of four percent as 0.04 is unproblematic. The issue is the mapping from a monthly event-rate statistic to an annual coordinator-stock assumption, and from separation or residential movement to required contact updates. The public evidence does not supply an annual calibration or an overlap rule for those mechanisms. A deliberate four-percent annual proxy could be defensible, but the cited monthly statistic does not establish it by itself. [[FIND-TURNOVER]]

The report does not multiply the monthly rate by 12 or compound it into an annual probability. Separations are events; they are not automatically a validated individual hazard for a stable coordinator population. Residential mobility also need not be disjoint from job separation or correspond one-for-one with a required update. Closure requires a documented population, event definition, annual calibration, and overlap mapping. This case requires substantive assumption governance as well as unit-aware calculation controls. [[FIND-TURNOVER]]

### 7.8 PreCheck: a valuation-scope question, not an arithmetic error

The TSA PreCheck Application Program package, reference 202605-1652-002, control 1652-0059, was active and approved with change. It reports 4,339,658 annual all-activity hours, while 4,286,341 enrollment hours are used in respondent valuation. Their difference is 53,317 hours. Table 15 separately identifies 7,149 correction-of-record hours and 46,167 survey hours, totaling 53,316 hours, within one hour of the displayed gap. [[FIND-PRECHECK]]

Those named components explain the arithmetic within rounding. The retained classification is unresolved because the reviewed evidence does not explain the valuation rule that excludes correction and survey hours. The report therefore rejects an arithmetic-error interpretation. It also does not automatically value the gap using the enrollment wage: the relevant actor, activity scope, and valuation rule require confirmation. [[FIND-PRECHECK]]

A useful control would show, for every burden activity, whether it is monetized, which rate applies, and why any exclusion exists. The sum of valued and explicitly excluded hours should reconcile to the all-activity total. Human review must establish the appropriateness of the exclusion; arithmetic can only verify that the partition is complete. [[FIND-PRECHECK]]

### 7.9 Pipeline cybersecurity: coherent staffing, unreconciled cost

The Pipeline Corporate Security Reviews and TSA Security Directive Pipeline–2021–02 Series package, reference 202512-1652-001, control 1652-0056, was active and approved with change. Its Federal plan-review paragraph uses 100 reviews, eight manager hours at $122.27, and 24 analyst hours at $104.17. The grouped per-plan product is:

> 100 × [(8 × $122.27) + (24 × $104.17)] = $347,824.

The published total is $290,825.84. The difference between the displayed-input product and the published amount is $56,998.16. Wage rounding across the 3,200 review hours cannot reconcile that difference; neither does the literal unparenthesized printed expression. [[FIND-CYBER-COST]]

The earlier version reports the same total with lower wages and one-time review wording. This historical continuity does not establish why the later total remained unchanged. It also does not establish which recurrence convention should govern the current activity. A different reviewer count, effective rate, or explicit annualization convention would have to reproduce the amount and be documented consistently. [[FIND-CYBER-COST]]

This case brings the principal thesis into focus. The eight-manager-hour and 24-analyst-hour components are consistent in the comparative method review, while the cost representation remains unreconciled. An institution can preserve a useful role-based method and still need a deterministic control that requires reported costs to use the displayed workload, rates, and period. The recomputed value is not an estimate of actual spending or a replacement official total. [[CMP-16,FIND-CYBER-COST]]

### 7.10 Item 15: a verified bridge and a bounded conclusion

The registered Transportation Worker Identification Credential (TWIC) bridge links the prior annualized baseline of 430,317 hours to 510,471 hours. Six displayed component changes sum to 80,154 hours, with zero residual. The prior baseline is independently matched to the predecessor statement and to the current Item 15 narrative. [[BASELINE-TWIC-2025]]

@table twic

@figure twic

The bridge verifies the named annualized component reconciliation. It does not isolate causal contributions from population growth, time changes, pathway shares, or other factors within a component. That requires a declared decomposition model, including treatment of interactions. It also does not verify other portfolio baselines merely because prior statements have been retrieved. The practical lesson is to retain baseline identity and a component ledger as explicit model objects, then add causal driver attribution where supported. [[BASELINE-TWIC-2025]]

## 8. Recurring assumption families

### 8.1 What the 162 observations represent

The reviewed assumption register contains 162 observations in 16 families: 69 scalar or categorical assumptions and 93 formula-header coefficients. Pathway shares and task durations account for much of this evidence. The distribution reflects the reviewed documents and extraction depth, particularly credentialing formulas; it is not a measure of the frequency of each assumption across TSA operations.

@figure assumptions

@table assumptions

The broader discovery catalog searches 17 families. Its lexical hits include narrative context, zero statements, bundled tasks, and citations, and must not be counted as reviewed assumptions. Item 15 has discovery coverage but no reviewed assumption node; its relevant evidence is the baseline/change register. This structural distinction does not mean that TSA lacks Item 15 assumptions.

### 8.2 Candidates for governed reuse

Task duration, management review, legal review, familiarization, recordkeeping, and renewal supply recurring building blocks. The evidence supports retaining a defined per-plan manager/analyst review structure, a bounded training-record entry task, and stable within-lineage familiarization or appeal components. It does not support one universal review time, recordkeeping coefficient, or renewal duration. [[CMP-03,CMP-16,CMP-19,CMP-20,CMP-26]]

A reusable default should include its source, date, actor, task boundaries, time statistic, population unit, recurrence, rationale, confidence, and applicable collection conditions. Its status should distinguish an observed recurring coefficient from an institutionally adopted default. Adoption requires analytical approval; recurrence alone is insufficient.

Compensation is suitable for standardizing the transformation contract. If total compensation is C and wages are W, a loading factor C/W can be applied to a compatible wage input. A benefit share of total compensation requires a different transformation from a benefit-to-wage markup. Direct compensation must not be loaded again without a separately justified component. The choice of worker universe, occupation, vintage, and any overhead remains case-specific. [[CMP-06,CMP-07,ANALOGUE-202310-1220-004,CANONICAL]]

### 8.3 Assumptions requiring case-specific justification

Pathway shares require explicit eligibility and overlap rules. An initial application plus a conditional resubmission is an additive sequence; an online alternative that avoids an in-person visit may be an exclusive partition. Renewal duration requires a known form and conditional-task boundary. Turnover requires a population and annual event calibration. Source authority does not replace these mappings. [[CMP-10,CMP-22,FIND-HME,FIND-TURNOVER]]

Occupational assignment and wage statistic require an explanation of whose time is valued and whether a mean, median, or other statistic serves the intended purpose. Federal grade/pay requires an identified role, pay basis, effective period, and compensation treatment. Federal review time requires the case type and whether the time is active work, elapsed time, or a bundle of reviewers. Unknown distinctions should remain visible. [[CMP-08,CMP-14,CMP-16]]

Fee treatment, purchased services, and capital/system costs require payer, resource, and period boundaries. An examination paid by a candidate and an examination paid through a Federal contractor should not be treated as different resource activities solely because the payer changes. A capital life should not be equated with the approval horizon. The sparse reviewed capital evidence does not support a general default life or annualization method for TSA assets. [[CMP-15,CMP-18,CANONICAL]]

### 8.4 A practical assumption-library policy

The recommended library should have three states: candidate evidence, approved default within a defined domain, and case-specific override. A reviewer should be able to see which source supports a value, why its population and task fit, when it was last assessed, and what would trigger reconsideration. Overrides should record a reason and source rather than silently replacing an institutional value.

This policy would preserve strong recurring practice while making exceptions reviewable. It would also prevent an unsupported assumption from becoming authoritative merely because it appears repeatedly in prior documents. Evidence quality and frequency of reuse should remain separate fields.

## 9. Relationship to the Federal benchmark

### 9.1 Selective methodological lessons

The prior Federal benchmark found useful practices distributed across agencies and dimensions rather than a single uniformly superior exemplar. This report uses four selected cases already linked to the TSA evidence. They illustrate methods or analogous risks; they do not provide replacement TSA coefficients or a prevalence comparison. [[BENCHMARK]]

@table analogues

### 9.2 Timing evidence must match the modeled quantity

The Census Annual Integrated Economic Survey (AIES) distinguishes respondent research and paradata measures. The reviewed evidence records medians of 4.5 hours in a response-analysis survey, four hours in the instrument, and 1.1 hours in paradata, with different samples and measurement scopes. These numbers are not interchangeable measures or means. The relevant lesson for TSA amendment, travel, and renewal questions is to preserve preparation time, active versus elapsed scope, respondent segment, and statistic type before applying a timing estimate. No AIES duration is proposed as a TSA default. [[ANALOGUE-202310-0607-003]]

### 9.3 Baseline identity precedes decomposition

The FCC Incarcerated People's Communications Services (IPCS) example distinguishes a prior-approved burden baseline from a public-notice estimate. The approved-baseline bridge is 6,690 + 5,900 + 1,760 + 825 = 15,175 hours. The notice estimate is 17,555 hours, with a 2,380-hour reduction to the same 15,175-hour endpoint. Both deltas can be meaningful because their starting points differ. [[ANALOGUE-202503-3060-020]]

The relevance to TSA is the structure: identify the baseline, retain component changes, and reconcile the endpoint. The FCC values do not substitute for a TSA baseline. The verified TWIC bridge is a TSA example of component reconciliation, while most other numerical baselines remain outside the scope of verified bridges in this study. [[BASELINE-TWIC-2025]]

### 9.4 Compensation alternatives and non-TSA reconstruction risks

The BLS National Compensation Survey uses direct total compensation and an occupational mix. Its reviewed rates of $63.45 and $33.01, weighted 70 and 30 percent, produce a displayed weighted rate of $54.32. This illustrates an observable alternative to separately loading a wage. It does not establish an optimal TSA proxy, and its rates should not be transplanted to unrelated tasks or vintages. [[ANALOGUE-202310-1220-004]]

The CBP Global Interoperability Standards example illustrates a related reconstruction problem rather than a best-practice cost total. Its Federal inputs of 288 responses and two hours per response imply 576 hours, while the statement reports 10 hours and about $702 using a $70.19 rate. The example also raises a boundary issue between collection costs and broader claimed savings. It shows that this type of public reconstruction risk is not unique to TSA, without establishing relative frequency or severity across agencies. [[ANALOGUE-202411-1651-004]]

## 10. Institutional implications

### 10.1 Method governance

Method governance asks whether analytical choices fit their purpose and are applied coherently when the relevant conditions match. It includes defining tasks, choosing populations, selecting time evidence and wage proxies, distinguishing alternative from additive pathways, and deciding which prior baseline applies.

The comparative evidence supports preserving several existing methods. It also identifies targeted questions that common metadata and analyst review could make easier to resolve. The appropriate response is selective standardization of definitions and evidence requirements, coupled with explicit room for justified variation. The evidence does not support replacing every program-specific coefficient with a common value.

### 10.2 Representation governance

Representation governance asks whether the same approved analytical result is represented consistently in a calculation, table, footnote, narrative summary, and renewal explanation. Maryland Three, generic clearance, LEO, and pipeline plan review provide direct examples of why this matters. The HME and EXIS cases add population relationships; the turnover case adds source-period mapping. [[FIND-MD3,FIND-GENERIC,FIND-LEO,FIND-CYBER-COST,FIND-HME,FIND-EXIS,FIND-TURNOVER]]

The evidence supplies a stronger direct basis for tightening these controls than for claiming broad cross-ICR methodological inconsistency. That is an inference about the documented cases, not a measured ranking of all institutional risks. More intensive within-ICR testing might reveal different patterns, and public evidence cannot observe the full internal production process.

### 10.3 One quantitative source of truth

A single approved quantitative model should determine all published numerical outputs for a scenario. This does not mean that all source material must be stored in one file, or that every estimate should use one methodology. It means that each output value has one identified calculation, input set, period, and version, and that all representations refer to that result.

This arrangement would address the observed class of synchronization risks directly. A wage update would flow to the role-cost calculation, table, and narrative. An annual result would carry an annual label. An excluded valuation activity would remain visible in the reconciliation. A changed pathway share would be tested against its parent cohort before output generation.

### 10.4 Human judgment remains essential

Deterministic controls can verify multiplication, addition, units, periods, and declared partitions. They cannot establish that a 10-minute renewal coefficient fits a new form, that an occupation adequately represents the respondent, or that a monthly event statistic is a valid annual proxy. Those are analytical decisions requiring program context and evidence.

Generated tables and draft narrative should therefore express approved model content and flag unresolved inputs. They should not supply missing assumptions, invent explanations, or convert unresolved differences into settled findings. Final analyst and PRA review should consider whether the model represents the obligation and whether the statement communicates its scope faithfully.

## 11. Recommended analytical architecture

### 11.1 Source-to-output design

The recommended architecture connects sources, structured inputs, assumptions, calculations, validation, output tables, and Items 12–15 narrative. It combines the prior Federal model architecture with the specific controls motivated by the TSA findings. This is a proposed design, not a claim about TSA's current internal systems. [[CANONICAL]]

@figure architecture

Sources should retain document identity, package/control identity, issue or reference period, source locator, and the original observed value. Structured inputs should retain units, population identity, and evidence status. Assumptions should record the rationale and applicability of any selected coefficient or proxy. Calculations should preserve formulas and full precision. Validation should compare declared relationships before outputs are approved.

@table architecture

### 11.2 Calculations and scope relationships

For a recurring respondent activity, the common structure is eligible population multiplied by responses per person or entity per year and time per response. Event-based models can use events per year directly. The model should not silently equate unique respondents with summed activity counts, because one person can perform multiple activities.

Role-based labor cost is the sum of hours by role multiplied by the applicable loaded hourly rate. Each transformation should retain its formula and base. Nonlabor purchases, capital/system costs, fees, Federal resource use, and net budget effects should be separate objects with declared relationships, so that the same expenditure or transfer is not counted twice.

An exclusive pathway should reconcile to its parent population within an explicit tolerance. Additive activities should instead declare their triggering relationship and conditional frequency. A stock-minus-subset formula should identify the same stock and subset used by its narrative. These controls operationalize the HME and EXIS lessons without choosing their unresolved behavioral inputs. [[FIND-HME,FIND-EXIS,CMP-22]]

### 11.3 Baselines and renewals

An Item 15 ledger should identify the applicable prior approval, prior statement, public notice, or transferred requirement. It should preserve previous values, current values, quantified changes, and classification of changes. A component bridge should reconcile independently for responses, hours, and relevant cost categories. A driver decomposition should document its order or an interaction term when multiple factors change simultaneously. [[BASELINE-TWIC-2025,ANALOGUE-202503-3060-020,CANONICAL]]

Renewal should begin by carrying forward the prior approved model with explicit version lineage, then changing supported inputs or scope. An unchanged coefficient should retain its rationale and review status; a changed coefficient should retain the evidence and explanation for the change. A prior-package link alone is insufficient to certify a numerical bridge.

### 11.4 Validation and publication

Validation results should identify the rule, inputs, independent result, published or proposed output, tolerance, and disposition. Arithmetic failures should be distinguished from missing evidence and analyst-review warnings. Any unresolved material issue should have an owner, a reason, and a publication disposition rather than disappearing into a summary indicator.

Output tables should obtain values and labels from validated results. Draft Supporting Statement language should obtain numerical claims from those same results and source references. Analytical explanations should be reviewed by humans, especially when task boundaries, burden exclusions, or changes in payer are involved. The final document should be checked against the approved model after any editorial revision that can affect numbers or scope.

## 12. Recommendations

The recommendations below are proportional to the evidence. They prioritize inspectable model-to-output controls while preserving sound recurring methods. Suggested responsibilities are implementation proposals, not findings about existing organizational assignments.

### 12.1 Preserve strong recurring practice

Retain activity segmentation, source-based compensation transformations, role-based Federal review structures, and explicit pathway or fee boundaries where supported. Preserve the task definitions and caveats with the coefficients. Economic analysts, program specialists, and PRA reviewers should jointly determine whether a recurring component is suitable as a default within a defined domain. Completion would be demonstrated by a reviewed archetype record with source, scope, and applicability conditions, rather than by a list of unqualified numbers. [[CMP-01,CMP-03,CMP-06,CMP-16,CMP-18]]

### 12.2 Standardize the analytical contract

Adopt common fields for activity, actor, population unit, response/event definition, time statistic, period, lifecycle, source vintage, and evidence status. Require compensation inputs to disclose occupation, statistic, worker universe, loading base, and transformations. Require exceptions and proxy choices to include a rationale and review trigger.

Start the assumption library with the recurring structures supported here. Treat turnover calibration, travel interpretation, renewal boundaries, and heterogeneous capital assumptions as case-specific until their evidence supports broader reuse. Completion would be demonstrated when a reviewer can determine whether two similarly named inputs are actually comparable without reconstructing their meanings from scattered prose. [[CMP-04,CMP-05,CMP-09,CMP-10,CMP-14,CMP-21]]

### 12.3 Make reconciliation controls deterministic

@table controls

Implement these controls in a bounded model and validate them against both positive and negative cases. A control should detect the documented risk while accepting valid alternatives, such as incremental resubmission work or a coherent prior pathway partition. A failed check should show its operands and scope, enabling an analyst to distinguish a real conflict from rounding or a justified difference.

Completion would be demonstrated by reproducible pass/fail results, an explicit disposition for unresolved items, and tables and draft language generated from the same approved model. The record should retain the original published values alongside recomputed values so that review does not erase the source evidence.

### 12.4 Investigate the bounded open questions

For the six unresolved task/method comparisons, request the specific missing evidence in Table 6: decomposed tasks, aligned person/operator denominators, timing measures, form boundaries, reviewer bundles, or annual calibration. For PreCheck, establish the valuation inclusion rule. For the seven potentially inconsistent within-ICR cases, obtain authoritative model inputs or scope/output corrections that reconcile the documented conflict.

The purpose is resolution, not reassignment of a label based on preference. New evidence should document what changed and why it supports a different interpretation. Until then, preserve the current classifications and avoid circulating a corrected official aggregate that the available evidence cannot establish.

### 12.5 Sequence implementation around observable outcomes

First, establish the minimal activity/input/result contract and the reconciliation controls listed above. Second, implement one role-based Federal-cost example and one branching respondent model, because those structures exercise different observed risks. Third, connect output tables and draft narrative to their validated results. Fourth, test a renewal with an explicit baseline/change ledger, using the verified TWIC bridge as a reconciliation reference rather than a general behavioral template.

A useful acceptance standard is reproducibility: a second analyst can trace each material output to its sources and formulas; explain every pathway relationship; reproduce each check; and distinguish an approved assumption from an unresolved input. No cost savings, staffing reduction, or universal improvement rate is estimated from the present evidence.

## 13. Limitations

The report assesses public published estimation evidence. It cannot observe undocumented internal rationale, model files, timing samples, or production procedures. An omission from a Supporting Statement does not prove that the corresponding internal analysis does not exist.

The 90 recent packages are versions in a defined receipt window, not 90 independent active collections. Approval conclusions, active membership, pending status, and proposed-rule outcomes are distinct. Five unassigned-control packages do not constitute five additional independent histories. Findings about pending or proposed submissions must not be represented as findings about implemented workloads.

Principal-task normalization does not imply complete reconstruction or validation of every model. Quantitative checks cover 40 versions and include heterogeneous row screens and reused checks. Activity representations, serial versions, and member observations overlap. None of these denominators supports a portfolio error prevalence, office ranking, or statistical comparison of TSA with other agencies.

Not all normalized activities are comparable. Similarity is bounded to the tested component. Unknown task scope, actor, period, statistic, or denominator prevents automatic numerical interpretation. Agreement between published coefficients is not empirical validation of actual burden, and repeated values across renewals are not independent observations.

Some source models and timing evidence are unavailable. The public material does not establish the optimality of all compensation proxies, travel assumptions, or renewal coefficients. The absence of an explanation preserves uncertainty rather than establishing an error.

Prior-version retrieval is broader than numerical baseline verification. Only the registered TWIC baseline and displayed component bridge are fully verified here. The report does not certify all Item 15 baselines or provide a causal factor decomposition of the TWIC change.

Calculated discrepancies reproduce specified public inputs; they do not establish corrected official totals or actual respondent burden and spending. The LEO narrative, PreCheck subtotals, prior HME partition, and TWIC evidence materially constrain the conclusions. A study that omitted these counterexamples would overstate the findings.

Source locators resolve to the archived evidence reviewed for this study. Public URLs may subsequently change, and source-provenance verification does not establish that every underlying behavioral assumption is true. The four Federal analogues are selective methodological examples, not a representative comparison group.

The proposed architecture and recommendations are analytical design judgments derived from observed risks. Their operational performance, resource requirements, and institutional adoption have not been measured in this study. Human review remains necessary for methodological choices and publication decisions.

## 14. Conclusion

TSA's published estimation evidence contains coherent recurring methods across comparable activities and renewal versions. Several differences have observable explanations in task scope, lifecycle, source selection, technology, or payer. The six unresolved task/method questions warrant targeted review, but none of the 32 task/method adjudications remains potentially inconsistent.

The more direct observed control risk lies within individual published Supporting Statements. Seven challenged cases retain potentially inconsistent relationships among calculations, tables, population definitions, source periods, and narrative. The eighth within-ICR case, PreCheck, remains an unresolved valuation-scope question. These findings establish bounded public reconstruction risks without identifying undocumented internal causes or corrected portfolio totals.

The institutional response most directly supported by this evidence is to preserve useful analytical structures while making model-to-output reconciliation explicit and deterministic. Source-bound inputs, formulas, population and period identities, baseline/change ledgers, and generated tables and draft narrative can keep representations synchronized. Analysts and program specialists must continue to decide what the model should represent and whether its assumptions are justified.

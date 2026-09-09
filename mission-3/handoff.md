# Mission 4 handoff — TSA internal consistency and defensibility report

Mission 3 release **M3-1.0.0**, graph **1.0.0**, schema **0.1.0**. The release is authorized only with `MISSION_STATUS = EVIDENCE_GRAPH_FROZEN` and final-validation PASS in this same committed tree. This is a public-evidence report-writing handoff; no broad new research, application/UI building, or changes to Mission 1, the technical benchmark, or leadership brief.

## Evidence base

| Measure | Frozen count |
|---|---:|
| Recent TSA ICR packages | 90 |
| Assigned TSA control histories | 48 |
| Unassigned-control packages, separately retained | 5 |
| Graph package versions including lineage | 135 |
| Archived statement versions | 134 |
| Normalized activity representations | 468 |
| Assumption-context activity nodes, additional | 25 |
| Reviewed assumption observations | 162 |
| Scalar/categorical observations / formula-header coefficients | 69 / 93 |
| Task/method comparisons | 32 |
| Within-ICR adjudicated findings | 8 |
| Quantitative checks / versions with checks | 341 / 40 |

The 90 packages occupy the fixed 2021-09-09 to 2026-09-09 recent window and include status-distinct proposals and prior versions. They are not 90 independent active collections. Graph totals are 2,546 nodes and 4,077 edges; 493 ACTIVITY nodes include the 468 representations plus 25 context nodes. The 97-row consistency matrix is a member-observation view, not 97 independent findings. Keep the 27 explicit representation-overlap groups nonadditive.

| Classification | Task/method comparisons | Within-ICR findings | Combined adjudicated records |
|---|---:|---:|---:|
| CONSISTENT | 15 | 0 | 15 |
| DIFFERENT_EXPLAINED | 8 | 0 | 8 |
| POTENTIALLY_INCONSISTENT | 0 | 7 | 7 |
| NOT_COMPARABLE | 3 | 0 | 3 |
| UNRESOLVED | 6 | 1 | 7 |

## Method

Read normalization, shape and similarity rules with the canonical comparability contract. Original text/numbers remain separate from transformations: hours to minutes multiply by 60; annual/person/event denominators, maximum versus mean, one-time versus recurring, payer/resource/transfer boundaries and source precision remain explicit. Compensation comparison retains occupation, employee universe, source vintage and loading base. Unknown fields never count as matching evidence.

Collection shapes include security-program compliance, credentialing/STA, operational reporting, claims and cybersecurity compliance. Activities include application, enrollment, renewal, amendment, review, recordkeeping, data entry, appeal, coordinator update, assessment, reporting and verification. A shared label discovers candidates; it does not establish comparable scope.

Strong similarity matches substantive actor/task boundaries; moderate permits a bounded method comparison with scope caveats; weak is discovery only. CONSISTENT describes the tested published component; DIFFERENT_EXPLAINED requires observable explanation; POTENTIALLY_INCONSISTENT retains an unexplained material conflict after challenge; NOT_COMPARABLE rejects a match; UNRESOLVED preserves insufficient evidence. These are analytical inferences, not whole-package grades.

Epistemic labels are PUBLISHED, CALCULATED, NORMALIZED, INFERRED and UNRESOLVED. Preserve field-level published versus calculated values in mixed records; a node-level inference does not turn a quoted observation into an inferred source fact.

Adversarial review tests source/geometry, rounding, actor/task scope, population and period, wages, prior-version continuity, related-task counterexamples and possible legitimate explanations. Forty-one challenge records cover all 40 adjudicated records and the rejected FAC rounding candidate. Prior HME and TWIC partitions supply counterexamples to broad credentialing claims; PreCheck was retained as a valuation-scope question, and LEO's coherent narrative limits its table finding. Batches F and G are durably recorded successive stable reviews without material framework or major-finding change.

## Principal findings

### Strongest observed consistencies

- CMP-01: industry-requested carrier/cargo amendment documentation retains one hour per request; cargo scope may be narrower.
- CMP-02/03: surface STP amendment assumptions retain eight hours and a 10% annual share; record entry retains one minute. Consolidation is continuity, not independent replication.
- CMP-06: pipeline loading ratios align at the same source vintage, differing only in displayed precision.
- CMP-16: cybersecurity plan reviews retain eight manager hours plus 24 analyst hours. Cost products and recurrence are separately evaluated.
- CMP-29–32: held-out application/claim/adoption coefficients and the 130-second Secure Flight identity-transmission component remain stable, with DASSP field-scope and unrelated processing components excluded.

### Strongest explainable variations

- CMP-07: loading factors differ with documented employee universe and source period; proxy optimality is not established.
- CMP-11/22/25: threat triage versus contractor response handling, initial versus incremental resubmission, and CHRC versus non-CHRC pathways contain different work.
- CMP-12/13/24: online migration or published user-experience explanations support removed/revised tasks; underlying timing samples remain unavailable.
- CMP-15: moving medical examination payment from Federal contractor funding to candidates explains cost-category movement, not net resource savings.

### Potentially inconsistent patterns and within-ICR QA

No cross-ICR task/method comparison is classified POTENTIALLY_INCONSISTENT. The seven retained potential conflicts are the within-ICR findings below. Do not turn unresolved cross-program differences into inconsistency claims.

- **FIND-HME — POTENTIALLY_INCONSISTENT**: In-person rows already exhaust parent cohort before online renewals are added; residual equals53182/54840/53816 online renewals. Original OOXML cell origins verified. Narrative avoidance of visit contradicts full-cohort in-person charging. Prior HME partitions reconcile and TWIC partitions reconcile; reject generalization to all credentialing. Missing workbooks prevent corrected cost estimate.
- **FIND-MD3 — POTENTIALLY_INCONSISTENT**: Annual published208718 differs from displayed product148194.405; per-person product565.6275 differs from563.63. Rounding insufficient; table specifies same five tasks and annual population. Three-year narrative separately626155. Do not infer mechanism of mismatch.
- **FIND-GENERIC — POTENTIALLY_INCONSISTENT**: Feedback45minutes does not reproduce published hours; table population sum and annual narrative also disagree. Merged grid confirms minutes and row identities. Ceiling scope prevents actual-impact claim, but does not reconcile internal arithmetic or totals. Earlier version repeats table values; repetition is not independent corroboration.
- **FIND-EXIS — POTENTIALLY_INCONSISTENT**: Table4 uses95%of all limited users, whereas Table3 applies5%to new users. Alternative all-user exercising might justify95%stock but contradicts explicit subtraction of Table3. Residuals far exceed rounding. Retain formulation mismatch without selecting correct behavior.
- **FIND-LEO — POTENTIALLY_INCONSISTENT**: Annual-column476990.86 aligns with three-year product; narrative annual158997 is coherent. Narrative excludes other Federal entities. Three-year interpretation explains cell magnitude and correct narrative supplies counterevidence against agency-wide cost error; annual table label remains conflicting.
- **FIND-TURNOVER — POTENTIALLY_INCONSISTENT**: Monthly-average4%is used annually and combined with9%residential mobility as contact changes. Footnote explicitly averages monthly rates; no annual conversion or overlap treatment is visible. Could be deliberate proxy choice, but no calibration justifies period substitution. Do not annualize mechanically: separations are events, not a validated individual hazard.
- **FIND-PRECHECK — UNRESOLVED**: 4339658all-activity hours versus4286341enrollment hours monetized. Table15 explicitly separates7149correction and46167survey hours, summing within rounding to53317gap. Reject arithmetic-error claim. Why these public hours are excluded from valuation is not explained here.
- **FIND-CYBER-COST — POTENTIALLY_INCONSISTENT**: Published290825.84 versus component product347824; the earlier version reports the same total with different wages. Neither grouped per-plan product nor literal printed expression reproduces total; wage rounding is insufficient. Earlier repeated total supports historical continuity of the number but does not prove copy/paste cause.

### Unresolved comparison questions

CMP-04 (airport/carrier amendments), CMP-05 (coordinator update cardinality), CMP-09 (medical travel proxy interpretation), CMP-10 (renewal scope), CMP-14 (Federal amendment-review bundle) and CMP-21 (turnover denominators) remain UNRESOLVED. See the evidence-needed register for precise closure evidence. CMP-17/23/28 are rejected matches, not open inconsistency allegations.

### Recurring assumption families and Item 15

The discovery catalogue covers 17 families; reviewed assumption nodes cover 16, including task duration, pathway share, Federal grade/pay, manager/Federal/legal review, purchases, loading, wages/occupation, fees, turnover, recordkeeping, renewal, familiarization and capital life. Item 15 is represented by baseline/change records rather than a reviewed ASSUMPTION node. Discovery counts are not reviewed counts.

The registered TWIC bridge starts at 430,317 hours; six displayed component changes sum to 80,154, reaching 510,471 hours. This verifies the specified prior baseline and aggregate components, not a causal factor decomposition or every portfolio Item 15 baseline.

## Federal comparator opportunities

Use only `analysis/federal-analogues.jsonl` and its existing frozen Mission 1 references:

| Frozen example | Specific TSA use | Boundary |
|---|---|---|
| Census AIES, 202310-0607-003 | CMP-04/09/10: timing scope, preparation and timing-statistic distinctions | Do not transfer survey times to TSA tasks |
| FCC IPCS, 202503-3060-020 | TWIC baseline bridge: prior approval versus public-notice baseline and component changes | Method example, not a TSA baseline substitute |
| BLS National Compensation Survey, 202310-1220-004 | CMP-06/07/08: direct compensation and occupational mixes | Does not prove an optimal TSA loading proxy |
| CBP GIS, 202411-1651-004 | FIND-CYBER-COST/CMP-18: Federal workload reconstruction and gross-cost/transfer boundaries | Shows risk is not uniquely TSA; not a prevalence comparison |

## Reporting boundaries

### Claims Mission 4 may make

- Specific published TSA statements show the source-backed consistency and reconstruction risks retained in the adjudicated ledgers.
- Several coefficients and methods recur consistently within source-defined boundaries; observable task, lifecycle, payer and source-vintage differences explain other variation.
- Stronger model-to-output controls could prevent the documented arithmetic, period, pathway and provenance conflicts. Present this as a control recommendation tied to observed output risks.
- Report exact ledger counts and the bounded TWIC reconciliation, keeping comparison, finding, check, package and representation denominators separate.

### Claims Mission 4 should qualify

- Potential inconsistency describes published evidence after challenge, not proof of the correct underlying model or actual respondent burden.
- A repeated coefficient is continuity, not independent empirical validation; a published explanation may lack a public supporting timing sample.
- Missing public rationale, scope fields or prior administrative evidence limits adjudication; it does not establish absence of internal reasoning.
- Proposed/pending/improperly submitted packages must be identified by inventory and record status and distinguished from approved final estimates.
- Source-locator validation concerns frozen archived content; external URLs may later change availability.

### Claims Mission 4 must not make

- Attribute undocumented internal causes, copying practices, software use, analyst intent, review failures or program-office behavior.
- Rank analysts or program offices, infer agency-wide performance/prevalence, or present this corpus as a statistical sample of errors.
- Treat unlike normalized tasks as comparable, missing evidence as zero, discovery hits as reviewed assumptions, or inherited versions/transfers as independent observations.
- Publish an aggregate corrected burden, cost savings estimate, or universal preferred coefficient unsupported by the adjudicated evidence.
- State that all 90 packages received full-model quantitative validation or that all 341 checks are errors.

## Recommended visuals

- Consistency matrix: use the 97 member rows, grouped under the 40 distinct adjudications with visible scope/classification caveats.
- Assumption-family heatmap: unique reviewed assumption IDs by exact version and family; distinguish discovery coverage and missing reviewed evidence.
- Task-time comparison: only registered comparable components with identical units/denominators/statistics; show unresolved cases as annotated rows without ratios.
- Compensation-method comparison: method, source universe/vintage and ratio precision; do not combine nominal dollar rates across years.
- Item 15 reconciliation view: the single verified TWIC prior/components/current bridge.
- Source-to-assumption provenance diagram: use actual SUPPORTED_BY, MEMBER_OF and USES_ASSUMPTION edges; mark inferred relations and missing links explicitly.

## Exact Mission 4 inputs

Start with the following files; full source-corpus rereading is unnecessary. Canonical adjudications already contain source observations, explanation tests and provenance. Open an individual original locator only for a quotation or specific ambiguity.

- `mission-3/research-state.json`
- `mission-3/release-counts.json`
- `mission-3/freeze-gates.json`
- `mission-3/validation/final-validation.json`
- `mission-3/handoff.md`
- `mission-3/limitations.md`
- `mission-3/open-questions.md`
- `mission-3/inventory.json`
- `mission-3/control-histories.json`
- `mission-3/lineage-resolved.json`
- `mission-3/stability-batches.json`
- `evidence-graph/manifest.json`
- `evidence-graph/schema.json`
- `evidence-graph/normalization-rules.md`
- `evidence-graph/shape-taxonomy.md`
- `evidence-graph/similarity-rules.md`
- `evidence-graph/representation-overlap.json`
- `evidence-graph/query-catalog.json`
- `analysis/comparability-protocol.md`
- `analysis/comparison-groups.jsonl`
- `analysis/adjudicated-comparisons.jsonl`
- `analysis/adjudicated-findings.jsonl`
- `analysis/consistency-matrix.jsonl`
- `analysis/adversarial-challenge.jsonl`
- `analysis/review-questions.jsonl`
- `analysis/within-icr-qa.jsonl`
- `analysis/qa-summary.json`
- `analysis/qa-coverage.jsonl`
- `analysis/item15-bridges.jsonl`
- `analysis/federal-analogues.jsonl`
- `mission-3/assumptions/family-catalog.json`
- `mission-3/assumptions/reviewed.jsonl`
- `mission-3/assumptions/reviewed-review-and-fees.jsonl`
- `mission-3/extractions/07-cohort-formula-assumptions.jsonl`
- `mission-3/external-sources/external-source-review.json`
- `mission-3/validation/provenance-validation.json`
- `mission-3/validation/graph-validation.json`
- `mission-3/validation/unit-period-register.json`
- `report/leadership/source/citation-registry.json`
- `report/source/citation-registry.json`
- `icrs/202310-0607-003/extraction.json`
- `icrs/202503-3060-020/extraction.json`
- `icrs/202310-1220-004/extraction.json`
- `icrs/202411-1651-004/extraction.json`

For graph-driven visuals, consume exactly the node_files and edge_files arrays in `evidence-graph/manifest.json`; the machine-readable handoff input list below expands every shard path. Do not glob stale/unlisted shards or run corpus-building scripts during report writing.

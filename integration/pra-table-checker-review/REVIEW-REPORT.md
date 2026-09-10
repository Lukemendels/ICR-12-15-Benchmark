# PRA Q12–15 table checker logic review and reuse assessment

## Executive Summary

**TABLE_CHECKER_REVIEW_STATUS = COMPLETE. Preserve the checker as a narrow prototype/reference; reimplement selected review concepts, not its JavaScript.** It is a six-table LEOFA/413A audit with fixed captions, columns, rates, durations and three positional cross-table years. It is not a general Supporting Statement parser, narrative/formula checker, quantitative model, or Item 15 reconciliation engine.

Useful concepts are explicit carried-value links between tables; an audit record showing formula, observed value, recomputation, residual and tolerance; year-by-year output reconciliation; and visible parsing/coverage diagnostics. The sample-specific implementation should not become production defaults. Basic arithmetic and rounding largely duplicate stronger typed functions in Jay's application. No component merits literal migration into Svelte/TypeScript.

Execution covered 44 complete inputs, 26 focused probes, 11 direct Jay comparisons, all 14 internal comparison sites through target mutations, and report/event smoke tests. A coherent synthetic fixture passes all50 numerical comparisons. Counterexamples expose false matches, false mismatches, missing coverage and misleading summaries. Pipeline and TWIC are unsupported: neither is meaningfully reconstructed or diagnosed by this checker.

The prior integration recommendation is unchanged: retain separate repositories, conditionally use icr-tool as the drafting/review foundation, and preserve frozen evidence as a separate read-only authority. Resolve lossless persistence and portable provenance before evidence adoption into working drafts; resolve model/output semantics before treating exported estimates as authoritative. The first PR should fix lossless draft persistence as one bounded unit. Defer evidence integration, broader reconciliation and Item 15 to later separately reviewed work. No PR or implementation was created.

## Inspection basis

| Repository/artifact | Exact inspected SHA |
|---|---|
| Benchmark HEAD and checker-introducing commit | `dc818c0a31177aed36ebd3881a559a113447bce5` |
| icr-tool | `e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e` |

Local benchmark initially stood at clean `50420c47714efa918a660d27908f1b496a322c9a`; fetch and fast-forward obtained the user-specified commit before checker inspection. Jay remained at its expected prior-validation baseline. The closeout commit adds only review artifacts; it does not redefine the code baseline reviewed.

Read and reused the complete [prior comparison report](../icr-tool-comparison/CODEBASE-COMPARISON-REPORT.md), [evidence log](../icr-tool-comparison/evidence-log.md), [validation report](../icr-tool-validation/VALIDATION-REPORT.md), [reproduction log](../icr-tool-validation/reproduction-log.md) and [validation state](../icr-tool-validation/validation-state.json). Existing validation findings are identified as prior execution; new checker/Jay executions are in [test-results.md](test-results.md). No research, dependency installation or evidence regeneration occurred.

Direct current Jay inspection covered `app/src/lib/review/parse/{parse,normalize}.ts`, `review/rules/{math,tablemodel,types,xcomp,req,src}.ts`, `review/{index,score,passport}.ts`, `calc/{burden,govcost,annualize,dollars,round}.ts`, and export Markdown/XLSX paths. Prior page/schema/DB/source-proof reproductions remain valid because that repository SHA is unchanged. All checker functions and packaging ranges are covered by [logic-inventory.md](logic-inventory.md).

## Tool Architecture

Lines1–322 contain CSS and UI with a second nested doctype/html/head/body shell. Lines323–344 contain Paperclip portable-tool metadata, STICKSHIFT_TOOL and generated launch-skill text. These identify packaging, not analytical capability; prompts/capabilities arrays are empty. ANVIL generation provenance supplied by the user does not imply an embedded reusable ANVIL reasoning engine. No external runtime dependency is loaded.

The final script, lines345–796, has one global state object, a sample and six captions, numeric/parser helpers, hard-coded calculations, finding/report helpers and event wiring. Analytical operations are synchronous JavaScript. Many helpers are pure, but check runners append to global state and runChecks reads the DOM and immediately renders. Clipboard/report generation and filters are presentation. Generated skill registration was read as code-review material, not activated as an instruction.

## Parsing Model

getSection searches for the exact phrase “Provide estimates of hour and cost burdens” and optionally cuts at “For collections of information whose results will be published.” If the first phrase is absent, it uses the whole pasted text. There is no independent Q12/Q13/Q14/Q15 recognition, section number map, heading normalization or semantic item routing.

buildTables searches six exact, case-sensitive caption substrings. extractRows uses the first occurrence, then captures pipe-delimited lines; alignment rows are removed. It accepts outer pipes or none, but no HTML tables, merged cells, escaped pipes or native spreadsheet formulas. The first captured row becomes headers; headers never determine calculation roles. Rows whose first cell is not exactly1,2,3 orAverage are dropped. Rows can be duplicated or reordered without validation. Blank/nonpipe lines terminate a populated block. Average rows use a compact layout unlike ordinary full-width rows.

parseNumber strips dollar signs, commas and percent signs and applies Number. Missing/blank/n/a and nonfinite numbers becomeNaN; ASCII minus works. It returns5 for5%, leaving percentage division to fixed formulas. There are no typed currency, hour, minute, population, period or magnitude units. Numeric text with units is rejected, malformed comma groups are silently concatenated, and exponent/hex syntax is accepted. No prose values or formulas are extracted; repeated values are not generally indexed.

## Calculation/Reconciliation Model

The complete formula and tolerance register is in [logic-inventory.md](logic-inventory.md). Implemented relationships are:

- Table 1 population growth, seeded at 83749 and chained through displayed rows; LEO population×use share; means of the parsed finite annual LEO/response values.
- Table 2 responses×row time in hours; displayed hours×$62.36.
- Table 3 population×share and Table 4 occurrences×registration portion, rounded to integer counts.
- Table 5 registrations×.0833hours and flight occurrences×.0333hours; each displayed hour result×$62.36.
- Federal table responses×row time and displayed hours×$70.35.
- Four fixed cross-table equality relationships for three row positions.

No general population×frequency×duration relationship, subtotal/total engine, role summation, capital annualization, wage loading, inflation, unit conversion or Item 15 difference engine is implemented. The two Table 1 means are the only annualization-like checks. All other averages, totals, fourth years and causal relationships are untested.

PASS means equality after hard-coded display rounding, including when raw values differ outside a zero tolerance. Otherwise finite residuals within the absolute tolerance areWARNING and larger onesISSUE. Missing operands also generateWARNING; INFO covers scope/parser metadata. There is no confidence model or separate unassessed status. Money rounds to whole dollars in findings; raw operands/residuals are discarded from the result object. diffText can suppress a nonzero difference to0. A $2 tolerance is not a source-specific rounding derivation; production comparisons need declared precision and units.

## Cross-Table and Narrative Logic

The four explicit edges are T1LEOs→T3LEOs, T1responses→T2responses, T3occurrences→T4occurrences, and T4registrations→T5registrations. This is valuable relationship intent but fragile implementation: matches use array index, not year labels, row names, learned numeric equality or explicit model IDs. Reordering Table 3 alone creates four false issues. Missing tables still produce12 attempted comparisons. No averages, Table 5 occurrence propagation or Federal response propagation are connected.

checkNarrative contains only two rules: warn if both literal1.6265 and1.6266 occur; warn about a Table 4 reference if two fixed strings occur. It does not read a wage formula, compare prose amounts to table totals, or identify compensation denominators. Unrelated identifiers containing those substrings trigger; other conflicting factors are ignored. A “Narrative Issues” counter exists but no current narrative rule emitsISSUE.

Jay's MATH-004 is more general but still matches numerical presence, not meaning. Fresh mutation of a100-hour table total to999 correctly fails MATH-001, yet100-hour prose still passes MATH-004 because the respondent count is100. A future synchronization layer needs bound quantities, not repetition of strings or numbers.

## Item 12–15 Coverage

| Requirement | Actual checker coverage | Benchmark alignment / reuse value |
|---|---|---|
| Item 12 respondent burden | Selected responses×hours, hard-coded activity shares/times | Consistent arithmetic shape but much narrower; no activity eligibility, frequency contract or distinct respondent/event unit |
| Respondent labor valuation | Hours×fixed 62.36 | Narrow product; incompatible as general wage authority, no source/vintage/role/loading method |
| Item 13 nonhour/capital/O&M | None | No payer, useful life, timing, exclusions or missing-vs-zero semantics |
| Item 14 Federal costs | One fixed response/time/rate workflow | Narrow useful product; no multi-role sums, operating allocations, gross/fee/net distinction |
| Item 15 change bridges | None | No baseline identity, signed components, current total, residual or causal decomposition |
| Population relationships | Fixed growth/share products and two linked population columns | No overlap/partition sum, parent-unit identity or out-of-range share validation |
| Frequency/time | Assumes response counts and hour units already resolved | No minutes conversion, annual/monthly period, recurrence or unique population reconciliation |
| Wage transformations | None; fixed rate and literal factor warning | Cannot distinguish benefit share from markup, inflation or overhead base |
| Period/unit reconciliation | None | Labels do not establish unit compatibility; year indices are not period keys |
| Subtotals/totals | Two finite-subset means only | Omits total/component reconciliation; incomplete years can be averaged as complete |
| Table/narrative synchronization | Two literals only | Prototype warning examples; not an implementation seed for semantic binding |
| Cross-table propagation | Four hard-coded relationships | Best conceptual seed, replace indices with quantity/period identities |
| Rounding/tolerance | Display match plus fixed absolute thresholds | Useful audit dimensions; incompatible as universal precision policy |
| Missing versus zero | ScalarNaN versus0, then finite-only means and generic warnings | Preserve initial distinction; reject omission and misleading completion claims |
| Provenance/source binding | Human table/row labels only | No input locator, raw quote, file hash, observation ID, source release or assumption applicability |

Requirements above derive from frozen [canonical-model.md](../../methodology/canonical-model.md), [canonical dictionary](../../methodology/canonical-data-dictionary.md), [requirements floor](../../methodology/requirements-floor.md) and existing QA/bridge records. These are requirements references, not new research or claims that the full canonical model is implemented.

## Executed Test Results

The unchanged final script ran in a disposable Node VM with minimal DOM/clipboard adapters; real rendering and report functions executed. Full browser parsing/layout, real clipboard, Anvil and WebView2 were not exercised. [Exact inputs/output receipts](execution-results.json) and the [reproduction harness](reproduce.mjs) are durable review artifacts; generated Jay bundles stay in/tmp.

The embedded sample yields38 calculation checks plus12 cross-table checks,48 passes, two numerical warnings and one duplicate-table warning. An independently constructed coherent fixture yields50 numerical passes. Each of14 target perturbations produces a calculation issue. These results establish narrow arithmetic execution, not document validity.

Renaming captions removes all supported tables; changing header semantics does not change results. Calendar years and a fourth year disappear. A missing annual value is dropped from a reported three-year mean. Full-width average rows are misread. Incorrect Table 2 averages and an unpropagated Federal response count escape checks. Nonempty unrelated text reports six detected tables although all six parsed tables are empty: counts includes both “found” and “not found.” The conclusion counts12 missing-operand warnings as numerical checks that “ran with no issues.” Coverage should instead be reported as unsupported/incomplete.

## Benchmark Case Results

**Pipeline Federal mismatch: NOT DETECTED / UNSUPPORTED.** Tested the unchanged frozen 202512 source and its exact L216 paragraph with a synthetic numberedQ14 heading. The checker finds none of the relevant inputs, reconstructs no multi-role calculation, and supplies no meaningful explanation. Generic parse warnings are not mismatch detection.

The independent diagnostic is100×(8×122.27+24×104.17)=347824, versus published paragraph290825.84; calculated minus published is56998.16. Literal printed grouping gives100316.08 and also fails. The frozen source has a distinct Table 8 displayed amount347836.86; we preserve that distinction. Jay's explicit govCostRow/govCostTotal, given800manager hours and2400analyst hours, returns347824. Its Q14 text review emits only the broad MATH-006 “no hours×rate product matches” failure after a heading is supplied. That is not the required reconstruction. **347824 is a calculated diagnostic, not an official correction or spending estimate.** The checker makes no correction claim because it produces no substantive result.

**TWIC bridge: NOT RECONCILED / UNSUPPORTED.** The frozen bridge has430317 baseline plus deltas153985,1906,−78815,−5175,9497,−1244, totaling80154, equals510471 with residual 0. Tested a faithful signed readable serialization, a wrong-current-total mutation, and current/prior frozen full texts. Checker identifies no baseline/component/current roles and returns the same irrelevant checks for correct and incorrect serialized totals. Its scalar parser can retain ASCII minus, but never applies it to bridge prose. Jay recognizesQ15 only with a numbered heading; negative figure signs are lost and noQ15 finding appears. The independently recomputed residual confirms displayed component reconciliation only; growth/time/share/fee causal attribution remains outside that evidence.

An additional frozen Pipeline compliance paragraph is a rounding control:4800×88.39=424272 versus424261.04 differs10.96, compatible with cent-rate rounding across4800hours. Checker performs no check; Jay's much broader5% any-product rule passes. The reasoned precision control, not that heuristic pass, supports treating this as a negative control for unwarranted mismatch claims. All source paths and observed outputs are in [test-results.md](test-results.md).

## Comparison with icr-tool

[reuse-matrix.md](reuse-matrix.md) classifies every meaningful capability with the requested comparison vocabulary. The checker is stronger only within its configured sample: it recognizes its pipe tables without standard Markdown separators, checks specific sequential growth/means, carries four known fields between tables, and flags duplicate table numbers. Jay needs numbered headings and its header patterns do not activate math on even the headed, normalized sample's six tables.

Jay is stronger in generic parsing, semantic item recognition, unit/magnitude tokens, line/footnote locations, typed calculations, tested rounding modes, sums, projection/price helpers, source/requirements review, passports and exports. Its11 freshly compared documents show correct general100×2×.5 burden arithmetic, but no bridge and no automatic Pipeline role reconstruction. Unnumbered frozen source headings defeat Jay's sectionizer; changing input format for diagnostic tests is disclosed, never silently treated as original source execution.

Jay's architecture is extensible and testable: parseSupportingStatement→CheckableDoc→25 typed rules→findings, score, passports. The checker is global-state orchestration and string-formatting of numbers. Jay scoring deducts10/3/1 by severity, excludesPASS/EXPLAINED from deductions and has SRC-201/202 auto-fail behavior. Those gates measure rule findings, not complete semantic validity. Passports retain value/expected/rawQuote/sourceLocation for Q12–14 but are not portable evidence observations. XCOMP context is cross-corpus practice, not the checker's within-document propagation; existing incorrect context wiring is not solved by merging them.

## Reuse Assessment

Reimplement explicit relationship validation and a typed audit envelope, eventually supporting output/model reconciliation. Retain source-reported and recalculated values separately with operands, units, year, locator, precision and applicability. Feed bound inputs to existing Jay calculation functions; do not copy rates 83749/62.36/70.35 or durations. Rebuild duplicate/reference and coverage diagnostics on parsed document identities. These are later review enhancements, not authority to alter project assumptions.

Use the sample and adversarial mutations as parser/review regression fixtures only. Use independently calculated Pipeline and frozen TWIC bridge expectations as future validator fixtures, retaining limitations and signs. Do not use checker output as the correctness oracle. Reject exact-caption general parsing, finite-only averaging, positional links, literal factor warnings and misleading summary/severity logic. Trivial pure utilities have no compelling architectural advantage over existing code.

### Relevance to the nine confirmed icr-tool gaps

| Confirmed gap | Helps? | Exact contribution / limit |
|---|---|---|
|1. Rich draft loss through UI roundtrip | NO | No draft schema, form serialization, storage or field merge; use prior reproduction and Jay model |
|2. Growth/projection not driving export | YES_CONCEPTUALLY | Yearly chained-population checks and Table 1 means illustrate output reconciliation; no export wiring or general projection code to reuse |
|3. Dollar-year conversion not driving export | NO | No indices, price periods or deflator transformation |
|4. Item 13 output semantics | NO | No Item 13 model, cost-boundary rule or exporter |
|5. Weak source-proof/locator preservation | NO | Audit labels help humans read arithmetic but are not source locators/proof; no raw quote or observation identity |
|6. Nonportable integer source IDs | NO | No source identity/registry/interchange logic |
|7. Incorrect/incomplete XCOMP context | NO | Within-document fixed links are unrelated to measured corpus statistics and rule applicability |
|8. No Item 15 engine | NO | Scalar ASCII sign preservation is a tokenizer test case only; no bridge or baseline/change roles to leverage |
|9. Incomplete XLSX Sources | NO | No workbook or citation traversal |

There are no YES_DIRECTLY findings. The checker contributes useful review ideas, not a patch for any confirmed persistence/provenance/export defect. PARTIALLY is not assigned merely because a generic arithmetic helper could be used somewhere in a larger solution.

## Risks / Limitations

The largest risk is false confidence from specialized checks presented as a Q12–15 review. Exact captions can match narrative mentions rather than table starts. Row positions, silent filtering and ignored headers break traceability. Hard-coded rates and times masquerade as recomputations from the document. Finite-only means can erase unknown data. Rounded equality hides residuals and currency cents; formatted results are insufficient for independent replay. The sameWARNING class covers missing input and minor numerical disagreement. Unsupported content is described as a completed numerical review.

Neither numeric equality nor Jay's broader heuristic source tests establishes assumption validity, causal explanation or official correction. No new security, performance, host compatibility or production certification is claimed. The embedded sample's original source/version and the rationale for fixed coefficients/tolerances are not bound in code. Frozen substantive uncertainties remain unchanged.

## Implications for the first icr-tool pull request

### Must fix before evidence integration

Scope matters: read-only evidence browsing does not itself require a scenario calculator. **Before evidence adoption into editable drafts**, two actual blockers are lossless supported draft persistence and portable source/observation identity with supporting locator/proof preservation. Otherwise adoption can lose rich fields or silently resolve to another local source. **Before relying on generated evidence-backed estimates**, projection/price-year/output semantics and complete citation propagation must also be correct or explicitly unsupported. These are gates for their affected workflows, not grounds for one omnibus PR. Incorrect XCOMP context must be fixed before representing its findings as corpus evidence.

### Appropriate for the first PR

Proposed title: **Preserve supported draft data across load, edit and save**. This coherent unit fixes an executed data-loss defect without importing benchmark evidence or creating a new model. No checker runtime code belongs in it.

| Proposed change | Current behavior / evidence | Desired behavior and source of logic | Required proving tests | Project-file compatibility |
|---|---|---|---|---|
| Preserve rich schema fields when rebuilding form state | Prior reproductionA:23 changed paths; growth defaults flat, notes/capital/frozen/narratives/SOC/quotes disappear and createdDate changes | Merge edited supported fields into the validated loaded project; retain untouched metadata and supported fields. Source: Jay schema and executed failure, benchmark stable-state requirement, not HTML | Rich schema fixture load→one supported edit→save→parse: only intended edit differs; preserve createdDate, growth, all optional fields and arrays; repeat save stable | Retain schemaVersion 1 and supported values; no new field format needed. Unknown future-schema input must fail or preserve under declared policy, not be silently truncated |
| Preserve input-level locator/quote and source-selection metadata through form conversion | PriorA/D:all rawQuote lost; Federal locators lost; some activity locators already survive | Preserve full supported SourcedValue payload unless user edits its relevant field. Do not imply this alone fixes export proof or integer portability | Sourced and unverified variants across activities and Federal costs; no-edit roundtrip; source change test defines which old proof is invalidated | Existing fields retained; no portable-ID migration in this PR |
| Handle perResponse Federal items without destructive conversion | PriorA:valid perResponse becomes blank fixed item, build returnsnull | Preserve typed perResponse unchanged if no editing UI yet, or support its existing fields; any unsupported operation visibly blocked before mutation. Source: existing discriminated union and govcost.ts | Load/save a project containing labor/fixed/perResponse together; edit unrelated activity; assert all Federal variants and calculations preserved; malformed input leaves loaded project unchanged | Existing schema union preserved; no new kind or version |

Tests must exercise the actual form conversion/save boundary, not just Zod or export→review. Use a portable self-contained synthetic fixture; avoid the existing missing absolute Windows golden path. Appropriate validation is focused conversion/save tests plus existing frontend checks/build and available regression tests. Keep unrelated missing-fixture failures explicitly identified. Jay should understand the bug from a small fixture and before/after field differences without reading this benchmark repository.

### Defer to later PRs

1. Portable evidence/source references and observation proof, including migration/remapping decisions, export locator/quote propagation and complete XLSX source traversal. This is a separately versioned compatibility contract.
2. Correct Item 12 labor/Item 13 nonhour outputs and missing-versus-zero declarations; then wire per-year projection and declared dollar conversion into a shared calculation-to-output contract with fixtures. Split further as needed for reviewability.
3. Repair XCOMP context definitions/wiring and visible unevaluated states. Separately add typed cross-table relationships, coverage diagnostics and raw-residual audit results; these are the checker-inspired enhancements.
4. Add explicit role-bound Federal reconciliation and Item 15 baseline/components/current validation from benchmark requirements, including negative signs, units, period/baseline identity, residuals and causal boundaries. TWIC success and wrong-total/sign mutations are required; Pipeline remains a diagnostic discrepancy, not a prescribed official total.
5. Only after relevant gates, implement verified read-only evidence consumption and deliberate adoption. Do not merge frozen public evidence, TSA-local overlays and working state.

## Recommended Direction

Preserve this artifact as a prototype with the narrow scope documented here. Decompose its useful ideas conceptually into later typed/pure review and output validators. Keep its layouts and defects as tests/reference, with independent expected results. No partial source migration or HTML refactor is recommended now; retirement as an operational aid can be considered after typed replacements cover its useful cases.

Unresolved decisions are the source/version and rationale behind sample constants/tolerances; the portable identity/migration contract; analyst-confirmed quantity binding and baseline/causal policies; and eventual host/deployment validation. None requires more inspection to classify this checker. Reuse findings have saturated.

Closeout is documented in [LOOP.md](LOOP.md) and [review-state.json](review-state.json). Only this new review folder is committed/pushed to benchmark origin/main; Jay, the checker, applications and frozen evidence remain unchanged. No PR, integration or CI polling follows.

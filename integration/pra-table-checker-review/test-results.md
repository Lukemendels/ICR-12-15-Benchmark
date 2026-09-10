# Executed test results

Fresh Linux execution on 2026-09-10, Node v24.21.0, locale en-US. **Harness completed successfully; this is not certification of the checker.** There are 44 full-run input cases, 26 scalar/scope/format probes, 11 fresh Jay document comparisons, and event/report smoke checks. Fourteen target-cell mutations cover all 14 internal comparison call sites. The coherent fixture checks all 50 numerical comparisons and the mutations exercise all four cross-table edge families. Baseline application tests were not rerun: the prior completed validation is retained.

Reproduce from benchmark root (uses already installed Jay esbuild; no dependency installation):

```sh
node integration/pra-table-checker-review/reproduce.mjs /home/luke/Projects/icr-tool /tmp/pra-review-results.json
```

[reproduce.mjs](reproduce.mjs) reads the last inline script directly from the unchanged authoritative HTML and evaluates it in Node vm. DOM elements, listeners, clipboard and prompt are minimal adapters; real runChecks, parsing, comparisons, rendering and report generation run. Jay modules are bundled read-only into a fresh `/tmp/pra-review-*` directory. No extracted application code is committed. This is not browser layout, actual clipboard, DOMContentLoaded timing, WebView2, Tauri or Anvil host validation. No full code-coverage percentage is claimed.

[execution-results.json](execution-results.json) preserves **exact input text, parsed tables, every finding and detail, complete plain-text report and conclusion for every case** under `cases[id]`; `micro` contains exact evaluated expressions and results; `jayComparisons[id]` includes exact text, sections/figures, findings/passports and scores. NaN is serialized as the explicit string “NaN.” The run includes assertions for coherent/sample check counts, target perturbations, the table-count defect, report copying/reset, repository SHA, Pipeline calculation and TWIC residual. Remaining exploratory probes record observed behavior rather than pretending every output is an expected-correct assertion.

One harness setup run failed on a newline embedded in a vm expression string, before any result artifact was written. The harness expression quoting was fixed; the HTML was unchanged. A successful initial 40-case run was broadened to 44 only to test comparable headed/standard Markdown inputs and a frozen rounding control. The retained JSON is the final successful run.

## Full-run receipt

C = calculation issues, X = cross-table issues, N = narrative issues, W = all warnings, P = numeric passes. “Detected” is the checker's defective summary, not verified table count. Rows are actual parsed annual rows.

| Case ID | C/X/N | W | P | Detected / rows | Input/intent |
|---|---|---|---|---|---|
| sample | 0/0/0 | 3 | 48 | 6 / 18 | Exact embedded prototype sample, not separately verified frozen evidence. |
| empty | 0/0/0 | 1 | 0 | 0 / 0 | Empty input branch. |
| unrelated | 0/0/0 | 18 | 0 | 6 / 0 | Out-of-scope handling. |
| narrative-literals | 0/0/0 | 6 | 48 | 6 / 18 | Both hard-coded narrative predicates. |
| narrative-unrelated | 0/0/0 | 4 | 48 | 6 / 18 | Substring false positive, no semantic relation. |
| narrative-other-factors | 0/0/0 | 3 | 48 | 6 / 18 | Other inconsistent factors ignored. |
| renamed-captions | 0/0/0 | 18 | 0 | 6 / 0 | Case-sensitive captions fail. |
| changed-headers | 0/0/0 | 3 | 48 | 6 / 18 | Headers ignored; same arithmetic despite changed meaning. |
| calendar-years | 0/0/0 | 15 | 0 | 6 / 0 | Year labels outside 1/2/3 ignored. |
| reordered-one-table | 0/4/0 | 3 | 44 | 6 / 18 | Same year values, different order creates false cross-links. |
| fourth-year | 0/0/0 | 3 | 48 | 6 / 18 | Fourth year silently discarded. |
| missing-average-term | 1/0/0 | 7 | 43 | 6 / 18 | Finite-only mean omits missing term. |
| padded-average | 1/0/0 | 4 | 46 | 6 / 18 | Ordinary full-width average misaligned to compact fixed layout. |
| unchecked-averages | 0/0/0 | 3 | 48 | 6 / 18 | Table 2 average not checked. |
| unchecked-federal-link | 0/0/0 | 3 | 48 | 6 / 18 | Federal responses not linked to Table 1. |
| changed-prose-rate | 0/0/0 | 3 | 48 | 6 / 18 | Hard-coded $62.36 and 83749 unchanged. |
| aligned-pipes | 0/0/0 | 3 | 48 | 6 / 18 | Optional outer pipes and Markdown alignment accepted. |
| blank-mid-table | 0/0/0 | 7 | 38 | 6 / 16 | Blank line terminates populated table. |
| caption-only | 0/0/0 | 17 | 0 | 6 / 0 | Presence pass with no parsed rows. |
| coherent | 0/0/0 | 1 | 50 | 6 / 18 | Independent arithmetic control; duplicate numbering remains a warning. |
| perturb-table1-1-2 | 4/1/0 | 1 | 45 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table1-1-4 | 2/1/0 | 1 | 47 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table1-4-1 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table1-4-2 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table2-1-3 | 2/0/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table2-1-4 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table3-1-3 | 1/1/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table4-1-3 | 1/1/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table5-1-2 | 2/0/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table5-1-3 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table5-1-5 | 2/0/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-table5-1-6 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-federal-1-3 | 2/0/0 | 1 | 48 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| perturb-federal-1-4 | 1/0/0 | 1 | 49 | 6 / 18 | Increase one target cell by 1000; may trigger dependent checks. |
| pipeline-paragraph | 0/0/0 | 18 | 0 | 6 / 0 | Verbatim source L216 with explicit synthetic Q14 heading. |
| pipeline-full | 0/0/0 | 18 | 0 | 6 / 0 | Unmodified frozen text; path mission-3/sources/202512-1652-001/e21e863d84c9cbf0.txt |
| twic-bridge | 0/0/0 | 18 | 0 | 6 / 0 | Synthetic readable serialization of frozen BASELINE-TWIC-2025, signs retained. |
| twic-wrong-total | 0/0/0 | 18 | 0 | 6 / 0 | One-hour mutation of frozen bridge serialization. |
| twic-current-full | 0/0/0 | 22 | 0 | 6 / 0 | Unmodified current frozen statement. |
| twic-prior-full | 0/0/0 | 23 | 0 | 6 / 0 | Unmodified predecessor frozen statement. |
| headed-sample | 0/0/0 | 3 | 48 | 6 / 18 | Synthetic Q12 heading plus standard Markdown formatting; same sample values. |
| generic-hour-pass | 0/0/0 | 18 | 0 | 6 / 0 | Independent standard burden table control. |
| generic-hour-fail | 0/0/0 | 18 | 0 | 6 / 0 | Wrong total should fail row arithmetic. |
| pipeline-compliance | 0/0/0 | 18 | 0 | 6 / 0 | Additional frozen bounded case: 4800 × 88.39 = 424272 vs 424261.04, compatible with cent-rate rounding; original paragraph. |

## Exact scalar probes

| Expression | Observed output |
|---|---|
| `parseNumber("-$1,234.50")` | `-1234.5` |
| `parseNumber("(123)")` | `"NaN"` |
| `parseNumber("−10")` | `"NaN"` |
| `parseNumber("10 hours")` | `"NaN"` |
| `parseNumber("5%")` | `5` |
| `parseNumber("0")` | `0` |
| `parseNumber("")` | `"NaN"` |
| `parseNumber("n/a")` | `"NaN"` |
| `parseNumber("1,2")` | `12` |
| `parseNumber("1e3")` | `1000` |
| `parseNumber("0x10")` | `16` |
| `average([100,NaN,300])` | `200` |
| `average([])` | `"NaN"` |
| `roundForDisplay(-1.5,0)` | `-1` |
| `roundForDisplay(1.005,2)` | `1.01` |
| `classify(100,100,0,0)` | `"pass"` |
| `classify(100.4,100.1,0,0)` | `"pass"` |
| `classify(101,100,1,0)` | `"warning"` |
| `classify(102,100,1,0)` | `"issue"` |
| `classify(NaN,100,1,0)` | `"warning"` |
| `diffText(100.4,100.1,"number",0)` | `"0"` |
| `diffText(100.51,100.49,"number",0)` | `"0.02"` |
| `diffText(99,100,"money",0)` | `"-$1"` |
| `getSection("before Provide estimates of hour and cost burdens KEEP For collections of information whose results will be published after")` | `"Provide estimates of hour and cost burdens KEEP "` |
| `getSection("12. Burden\nALL\n16. Publication")` | `"12. Burden\nALL\n16. Publication"` |
| `escapeHtml("<script>\"&")` | `"&lt;script&gt;&quot;&amp;"` |

## Significant findings

- Embedded sample: 38 calculation + 12 cross-table checks; 48 numeric passes, two numerical warnings (Table 5 flight hours Years 2/3), one duplicate-number warning. No ISSUE. This does not establish accuracy of the sample assumptions or its untested average rows.
- Coherent synthetic control: 50 numerical passes. Each of 14 separate +1000 target mutations produces at least one calculation ISSUE. These are independent expected-arithmetic controls, not a promise that all arbitrary document changes are detected.
- Unsupported nonempty text: zero parsed tables, 12 unavailable cross-comparisons, six missing-caption warnings. Summary incorrectly says six tables and conclusion says “12 numeric/prose checks ran with no issues” plus 18 warnings. `endsWith("found")` includes `not found`.
- Exact captions and positions dominate semantics: changing headers to Wage/Minutes/Dollars leaves results unchanged. Calendar years and year4 are dropped. Reordering only Table 3 creates four false cross-table issues although year-keyed values are unchanged.
- Finite-only average with missing Year 2 reconstructs 118557 from Years 1/3 while claiming “Average of Years 1–3.” The bad mean becomes an ISSUE, although the underlying problem is incomplete input. A conventional padded average row shifts fields and creates a false comparison.
- Changing Table 2 average to 1/1/$1 produces the original findings unchanged. Table 3 average 119171 versus Table 1 119168 is also unchecked. Federal response count can change to 100 with coherent local arithmetic without a propagation issue; Table 5 occurrences likewise have no link from Table 3/4.
- New prose rate $100 and population90000 are ignored; constants remain $62.36 and83749. Two arbitrary factor substrings produce a warning; a genuine-looking 1.5/1.6 contradiction does not. “Table 4 summarizes” is itself picked up by the generic duplicate-number scan as a caption.
- Display-equal values pass even with tolerance0 and raw difference0.3; diffText reports0. Decimal precision and tolerance must remain separate in a future validator. Missing and zero parse distinctly, but finite-only averaging undermines that distinction.
- Real registered load/run/filter/clear handlers execute under shim. Clipboard success/fallback both preserve the complete report. Attention filter retains INFO despite its warnings/issues label. Escaping probe passes; no security or browser compatibility certification follows.

## Frozen benchmark cases

**Pipeline:** unmodified full source and exact L216 paragraph with an added Q14 heading both produce zero recognized tables, zero calculation findings and zero meaningful mismatch findings. The paragraph run gives 18 warnings and the erroneous six-table summary. No operands are extracted; no $347824 is calculated by the checker; no explanation or official-correction claim is generated.

Independent control and Jay's explicit Federal labor rows calculate manager800h ×122.27 =97816; analyst2400h ×104.17 =250008; sum347824. Displayed/public paragraph amount290825.84 is lower by56998.16. Literal printed grouping instead gives100316.08 and also fails. The original source Table 8 separately states347836.86 and a113.22 rate: that separate representation is not the paragraph total and was not silently substituted. The frozen `QA-CYBER-COST` / `FIND-CYBER-COST` classify the discrepancy as requiring interpretation / potentially inconsistent, not an official correction or proof of internal cause.

**TWIC:** frozen BASELINE-TWIC-2025 serializes to prior430317, signed changes153985,1906,-78815,-5175,9497,-1244, and current510471. Independent sum80154 yields residual 0. Checker never recognizes those roles, adds the changes or produces a bridge result. Changing current to510472 produces the same generic findings. Current and predecessor full source texts are also unsupported (extra structure warnings arise from their table references). parseNumber's ASCII sign support is not bridge parsing.

**Additional negative/rounding control:** verbatim Pipeline compliance paragraph has4800 ×88.39 =424272 against424261.04, a10.96 difference within ±24 from cent-rate rounding across4800h. Checker performs no meaningful check. Jay MATH-006 passes its much looser any-product5% criterion; that pass alone does not establish rounding explanation, intended pairing or combined total. No source adjudication is changed.

Frozen source locators:

- [Pipeline current text L216](../../mission-3/sources/202512-1652-001/e21e863d84c9cbf0.txt), plus L218 compliance paragraph; original full text retained as input.
- [Pipeline QA register](../../analysis/within-icr-qa.jsonl), ID QA-CYBER-COST; [adjudication](../../analysis/adjudicated-findings.jsonl), FIND-CYBER-COST.
- [TWIC bridge](../../release/icr-evidence/v1.0.0/tsa/item15-bridges.json), BASELINE-TWIC-2025, including baseline identity/provenance and causal limitation.
- [TWIC current](../../mission-3/sources/202504-1652-008/ec91651842d62d7c.txt), Table 10 annualized row and Item 15 prose; [predecessor](../../mission-3/sources/202502-1652-004/4639c859f157e253.txt), Table 10.

## Fresh Jay comparison

| Input | Parsed sections/tables | Meaningful observed result |
|---|---|---|
| sample | None | No MATH finding; 10 total findings |
| aligned-pipes | None | No MATH finding; 10 total findings |
| pipeline-paragraph | Q14: 0 tables | MATH-006 FAIL; 12 total findings |
| pipeline-full | None | No MATH finding; 10 total findings |
| twic-bridge | Q15: 0 tables | No MATH finding; 10 total findings |
| twic-wrong-total | Q15: 0 tables | No MATH finding; 10 total findings |
| twic-current-full | None | No MATH finding; 10 total findings |
| headed-sample | Q12: 6 tables | No MATH finding; 12 total findings |
| generic-hour-pass | Q12: 1 tables | MATH-001 PASS, MATH-004 PASS; 13 total findings |
| generic-hour-fail | Q12: 1 tables | MATH-001 FAIL, MATH-004 PASS; 13 total findings |
| pipeline-compliance | Q14: 0 tables | MATH-006 PASS; 14 total findings |

Raw frozen texts have unnumbered headings; Jay recognizes no sections. The synthetic Q14 heading isolates rule behavior: Pipeline MATH-006 FAIL means no simple hours×rate pair matches, not reconstruction of the multi-role formula. The checker is stronger for its own exact-caption sample: Jay parses six tables after adding a numbered Q12 heading and normalizing Markdown, but no math rule fires for those column layouts. On a standard independent 100×2×.5=100 hour table, Jay MATH-001 correctly passes and fails a changed999 total; the checker does neither. Jay MATH-004 still passes the inconsistent100-hour prose because another table cell is the respondent count100: numerical coincidence is not semantic reconciliation.

For TWIC, Jay preserves Item 15 text but tokenizes negative changes as positive figures; neither total produces a Q15 rule. Jay's explicit typed Federal calculation, unlike either text-review path, returns347824. Prior nine confirmed UI/export/context gaps are historical executed evidence from the same Jay SHA; they were not rerun in this review.

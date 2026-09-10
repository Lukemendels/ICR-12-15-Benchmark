# Targeted reproduction log

Status: COMPLETE. All executions use icr-tool `e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e`. **Product code modified: no, for every reproduction.** Fixtures are synthetic diagnostics, not sourced estimates; references to real source #1 intentionally demonstrate the absence of observation-level verification.

## Reproduction mechanism

From the benchmark repository, after the authorized npm install in icr-tool:

```sh
node integration/icr-tool-validation/reproduce.mjs /home/luke/Projects/icr-tool
```

Requires the captured Node version with `node:sqlite` and target-declared esbuild, TypeScript, ExcelJS and other installed packages. No new test framework is installed. [reproduce.mjs](reproduce.mjs) creates a fresh `/tmp/icr-reproduce-*` directory on each run. It imports baseline engine modules and uses the TypeScript AST to extract page function declarations directly from source. No copied application function is maintained in the evidence repository.

Dialog open/save are deterministic temporary paths; filesystem APIs use Node files; `@tauri-apps/plugin-sql` is replaced at the module boundary by a thin adapter executing **actual `db.ts` SQL** with Node SQLite. Page scalar/array state is supplied as ordinary JavaScript variables. The one textual expression substitution evaluates the Svelte-derived analysisYears from yearsText at build time using the same expression. Svelte effects/DOM reactivity, IPC, permissions, host database initialization and dialogs are not executed. This isolates serialization/context behavior without claiming full UI testing.

The harness writes [fixture.icrdraft.json](fixture.icrdraft.json), [fixture-export.md](fixture-export.md) and [reproduction-results.json](reproduction-results.json). The latter contains original schema/index records, workbook sheet values, review findings, source-vintage rows and exact field differences. Binary workbooks, disposable databases and generated bundles remain in `/tmp`; Jay can regenerate them with the command above. The fixture export visibly uses contrived numeric claims with a real source ID: it is reproduction evidence only.

Diagnostic setup iterations are retained in command/log receipts: initial CommonJS bundle rejected top-level await (changed harness format to ESM); an unsupported fixture series kind was correctly rejected (changed to declared `other`); the first Item 15 replacement did not match the fixture end (corrected injection and added an assertion that 999 is present). The final run includes numerical and finding assertions and exits zero. None of these setup corrections changed product code or converted a product failure into a pass.

## A — UI/schema roundtrip: CONFIRMED

**Hypothesis:** valid rich schema data cannot survive the form load/build/save path.

**Setup/input:** fixture has 100 respondents, two responses, 30 minutes, $20 wage × 1.5, 10% growth, notes, wage SOC and vintage, input locators/quotes, frozen parameter, $200 startup/$100 O&M, fixed/labor Federal costs and Q12–14 narratives. `createdDate=2024-01-02`.

**Path:** `parseDraft` → file → extracted `loadProject` → `saveProject/buildProject` → file → `parseDraft`. Control: JSON serialize/parse without the form.

**Expected:** preservation of all supported fields; unsupported cases explicitly rejected before destructive editing.

**Observed:** JSON-only control is lossless; form has 23 changed paths. Growth resets to flat, activity notes and narratives empty, frozen/capital arrays empty, SOC and all rawQuote fields disappear. Activity input locators and wage series references survive; Federal input locators do not. Creation date changes to 2026-09-10. Exact before/after values are under `roundtrip.differences`.

**Per-response fixture:** replace governmentCosts with `{kind:'perResponse',responses:100,minutesPerResponse:6,hourlyWage:40}` using sourced values. Load represents it as a blank fixed item; build returns null with `Federal cost "Federal responses": value + source required.` This is save blockage rather than silent numeric conversion. No full browser used.

**Files:** `app/src/routes/draft/+page.svelte` (`loadProject`, `buildProject`, `sv`, `blankGov`), `app/src/lib/model/draft.ts`.

## B — Projection/annualization/dollar year: CONFIRMED

**Hypothesis:** implemented helpers do not drive real export projections or price conversion.

**Input:** base population 100 in 2026, growth 10%, years 2026–2028, two responses × 0.5 hours. Deflator indices 100 and 120 with $3,000 labor.

**Path:** `projectPopulation`, `threeYearAverage`, `toDollarYear`; `exportDraft` and `exportXlsx` on the same validated rich project, bypassing the form loss.

**Expected:** populations/hours 100,110,121, mean 110.333333 (display 110); conversion helper $3,600. An export claiming those semantics should use them or reject them.

**Observed:** helper values correct up to normal floating-point representation; Markdown states 100 hours and trace `(100 + 100 + 100) ÷ 3`; XLSX contains only base 100-hour row. Changing dollarYear from 2026 to 2028 changes the Markdown label only, byte-for-byte otherwise identical. `threeYearAverage([100,200])=150`: function accepts arbitrary nonempty length, not exactly three years. Export modules have no calls to projection or deflator helpers. Direct helper correctness does not establish export behavior.

**Files:** `app/src/lib/calc/{annualize,dollars}.ts`, `app/src/lib/export/{markdown,xlsx}.ts`.

## C — Item 13: CONFIRMED

**Hypothesis:** both formats place respondent labor in Q13 alongside nonhour costs.

**Input/path:** same fixture exported directly. Labor = 100 hours × $30 = $3,000; other = 100 × $5 = $500; annualized capital/O&M = $200+$100.

**Expected comparison contract:** benchmark `methodology/requirements-floor.md` and `canonical-model.md` distinguish Item 12 labor valuation from Item 13 nonhour costs. This is a comparison to the existing canonical contract, not newly adjudicated policy.

**Observed:** Q13 activity table has labor $3,000, other $500, total $3,500. Separate capital/O&M section adds $300, not included in that activity total. Markdown provides a capital subtotal; XLSX lists capital rows without a combined all-cost total. Both formats distinguish labor/other/capital columns or rows, but the Q13 placement conflicts with its own “Do not include” wording. Empty capital array emits “There are no capital, start-up, operation, or maintenance costs beyond the hour burden reflected in Question 12,” even while $500 activity other cost remains. The absence of entries is being treated as affirmative no-cost prose.

**Files:** `app/src/lib/export/{markdown,xlsx}.ts`, `app/src/lib/calc/burden.ts`, `app/src/lib/model/draft.ts`.

## D — Source proof: CONFIRMED

**Hypothesis:** source identity is sufficient to look sourced without locator, quote or observation.

**Input/path:** `{value:100,sourceId:1}` passed to `sourcedValue`, inserted into fixture and exported through `sourcesById` and `exportDraft`. Separately export the original fixture carrying `locator='Table X row Y'` and `rawQuote='Fixture supporting quote'`.

**Expected:** stated strict sourcing convention requires source ID + locator + raw supporting quote or explicit UNVERIFIED; observation identity should survive adoption/export.

**Observed:** ID-only accepted; unverifiedCount=0. Footnote identifies OEWS publication/year/URL/access date without the input locator, quote, original observation or linkage to the claimed 100. Even supplied input locators/quotes do not enter Markdown or XLSX Sources sheet. Numeric outputs survive; evidence connecting source to supporting value does not. This fixture intentionally attributes arbitrary counts to a wage publication and is accepted. Unknown IDs do throw in the Markdown citation registry, as passing baseline tests verify; existence is weaker than proof.

**Files:** `app/src/lib/model/draft.ts`, `app/src/routes/draft/+page.svelte`, `app/src/lib/db/db.ts` (`sourcesById`), `app/src/lib/cite/footnotes.ts`, export modules.

## E — Source ID portability: CONFIRMED

**Hypothesis:** independent local source records can share an integer ID.

**Setup/path:** copy tracked database to local-a.db and local-b.db. Use `insertSource` to add `Context A source` and `Context B source`, respectively; never write original DB. Both receive ID 8. Export identical parsed draft with respondent sourceId 8 using each `sourcesById` map.

**Expected:** portable draft reference should resolve to same identity or fail visibly.

**Observed:** same numeric draft silently exports citation “Context A source” versus “Context B source”. Both references exist and no missing-ID error occurs. `portability` records both footnote blocks. A database-relative integer is not a portable identity.

**Files:** `app/src/lib/db/db.ts` (`insertSource`, `sourcesById`), `app/src/lib/model/draft.ts`, `app/src/lib/export/markdown.ts`; schema from `data/icr.db` copies.

## F — Review context: CONFIRMED

**Hypothesis:** XCOMP-301 receives a current reference factor rather than an actual corpus mode, and XCOMP-302 gets no counts.

**Input/path:** `MINI_SS` has load factor 1.42 and footnote NAICS 481100. Execute extracted review-page `runReview` with real copied database query. Then review identical text with absent context and explicit diagnostic `{ececFactorMode:1.42,wageSeriesCounts:{'99-9999':1}}`.

**Expected:** a rule declaring corpus practice should receive corpus statistics of that meaning, and missing context should remain identifiable as unevaluated.

**Observed:** page SQL supplies latest active private-industry ECEC value 1.4294. XCOMP-301 FAILs the 1.42 fixture and says most TSA ICRs use 1.4294; the query establishes no such frequency. Explicit mode 1.42 passes. XCOMP-302 emits no finding with page or absent context; with synthetic counts it executes and FAILs unfamiliar NAICS 481100. Neither dependent rule emits anything when context is absent. Page result score 98 versus clean baseline tests reflects this minor factor deduction, not a reconciliation of source methodology.

**Files:** `app/src/routes/review/+page.svelte` (`runReview`), `app/src/lib/review/rules/{xcomp,types}.ts`, `review/index.ts`.

## G — Item 15: CONFIRMED

**Hypothesis:** heading recognition does not provide baseline/change/reconciliation/output capability.

**Input/path:** replace Item 15 text with `Prior baseline: 100 hours. Program change: 20 hours. Adjustment: -10 hours. New burden: 999 hours.` Execute parser and all 25 rules. Add candidate priorBaseline/componentChanges/newBurden fields to draft input and parse; inspect export.

**Expected:** if a bridge engine exists, 100+20−10=110 differs from 999 and should be diagnosed with baseline/component roles.

**Observed:** section heading and raw text preserved; quantities recognized, but `-10 hours` is tokenized as positive 10. No Q15 finding. Extra baseline/change fields stripped by schema. No Item 15 export.

| Capability | Observed classification |
|---|---|
| Identify Item 15 | Supported, executed |
| Parse heading/text/figures | Partially supported; no typed bridge; negative sign lost in normalized figure |
| Validate baseline bridge | Not implemented in executed rule set |
| Represent prior baseline as project field | Not implemented; candidate extra fields stripped |
| Represent typed component changes | Not implemented |
| Reconcile old + changes = new | Not implemented; deliberate mismatch unflagged |
| Classify program change versus adjustment | Text preserved only; no structured distinction or rule |
| Generate Item 15 draft content | Not implemented |

**Files:** `app/src/lib/review/parse/{parse,normalize}.ts`, `review/index.ts`, review rules, `app/src/lib/model/draft.ts`, export modules.

## H — Representative workflows and additional export gap

**Source workflow:** real FTS queries return 60 capped section hits and two wage sources. Active management wage is 68.15. Insert old/new fixture vintages via `insertSeriesVintage` and `importSeriesVintages`; rows 4480/4481 retain 20/25, old row points to new. Execute `checkPropagation` and `applyPrompt`; new wage 25 explicitly adopted, sourceId 8, vintage/year 2027, quote placed in locator. Save/reload the supported subset and execute both page export functions; updated labor $3,750 verified. Expected calculation and actual output agree.

**Review workflow:** real page functions review `MINI_SS`, create one audit row and 26 finding rows, and SQL readback matches. Existing seeded declarations produce 13/13 detected IDs, score 50, auto-fail. Corpus sections for 1652-0001 separately review as 18 sections, 43 findings, 24 passports, score 62, auto-fail. This is not the absent original external golden file. No application review-reload UI exists in the inspected route/API; SQL readback does not establish one.

**Import workflow:** temporary ExcelJS workbook with OCC_CODE/OCC_TITLE/H_MEAN parses 11-0000/Management/68.15. ECEC Table 4 fixture with 46.60 total compensation and 32.60 wages yields 1.4294. Feeding ECEC to OEWS throws missing OCC_CODE. Synthetic fixtures prove small parser cases, not real workbook compatibility.

**XLSX citation completeness hypothesis:** all used source records should appear in Sources. Assign ID 8 only to other cost and Federal cost; export and reopen. ID 8 absent from Sources despite Federal row naming it. CONFIRMED. Affected `app/src/lib/export/xlsx.ts` usedIds collection.

**Database initialization/migration:** integrity, FK checks, table/index inventory and copy-based SQL executed. Rust `ensure_db` not testable in current environment; no emulation represented as actual first launch. Inspection-only copy-if-absent behavior and absent corpus merge remain explicitly unvalidated at host level.

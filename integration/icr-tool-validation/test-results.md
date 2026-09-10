# Test and build execution results

Status: COMPLETE. Baselines are in [validation-state.json](validation-state.json). All application commands run without tracked source changes. Command receipts contain exact argv, cwd, exit and duration; wrapper exit 0 means the recorder wrote its receipt, not that the recorded command passed.

## Dependency and prerequisite commands

| Command | Working directory | Exit | Result / duration |
|---|---|---:|---|
| `npm ci` | `/home/luke/Projects/icr-tool/app` | 226 | FAIL: default ~/.npm cache read-only; extraction/cleanup warnings; duration not recorded |
| `npm ci --cache /tmp/icr-validation-npm-cache` | same | 0 | PASS: 255 packages, 256 audited, 6 seconds reported |
| `node --version`, `npm --version`, `python3 --version` | icr-tool root | 0 each | v24.21.0, 11.19.0, 3.12.3 |
| `rustc --version`, `cargo --version` | icr-tool root | 127 each | Executables missing |
| `pkg-config --modversion gtk+-3.0 webkit2gtk-4.1` | icr-tool root | 1 | Both required pkg-config entries unavailable |
| Git status/diff, SHA-256 checks | both repositories | 0 | Initial clean; target remains unchanged; final receipt in cleanliness.json |

Installation warnings: six deprecated transitive package notices; five audit entries (3 low, 2 moderate); esbuild postinstall outside npm allowScripts. esbuild binary works without overriding this policy. Lockfile hashes unchanged. No dependency fix applied. Raw install logs are bounded and retained in logs/npm-ci*.log.

## Recorded executions

Commands below are reproduced exactly as argument strings; shell quoting is represented with backticks for readability. Working directories are absolute in commands.jsonl.

| Label | Command | Cwd suffix | Exit | Seconds |
|---|---|---|---:|---:|
| cargo | `bash -c cargo fetch --locked; cargo check --locked; cargo test --locked` | `/home/luke/Projects/icr-tool/app/src-tauri` | 127 | 0.011 |
| host | `npm run tauri build --no-bundle` | `/home/luke/Projects/icr-tool/app` | 1 | 0.5 |
| vitest | `./node_modules/.bin/vitest run src/lib --reporter=verbose` | `/home/luke/Projects/icr-tool/app` | 1 | 6.604 |
| check | `npm run check` | `/home/luke/Projects/icr-tool/app` | 0 | 12.884 |
| build | `npm run build` | `/home/luke/Projects/icr-tool/app` | 0 | 20.188 |
| reproductions | `node integration/icr-tool-validation/reproduce.mjs /home/luke/Projects/icr-tool` | `/home/luke/Projects/ICR-12-15-Benchmark` | 1 | 1.135 |
| host-no-bundle | `npm run tauri -- build --no-bundle` | `/home/luke/Projects/icr-tool/app` | 1 | 0.276 |
| reproductions | `node integration/icr-tool-validation/reproduce.mjs /home/luke/Projects/icr-tool` | `/home/luke/Projects/ICR-12-15-Benchmark` | 0 | 1.363 |
| npm-audit | `npm audit --json --cache /tmp/icr-validation-npm-cache` | `/home/luke/Projects/icr-tool/app` | 1 | 1.244 |
| reproductions-final | `node integration/icr-tool-validation/reproduce.mjs /home/luke/Projects/icr-tool` | `/home/luke/Projects/ICR-12-15-Benchmark` | 0 | 1.339 |

## Interpretation and test counts

Vitest exits 1: **11 passed files / 1 failed file; 89 passed tests / 2 skipped tests**. `review/golden.test.ts` fails before its six test declarations register because `GOLDEN_PATH` is `C:\Users\jpadd\Documents\Claude\ICR\corpus\md\1652-0001\1652-0001 911PassFee SS.md`. This is a repository fixture-portability failure, not a math assertion failure. The documented 97 total comprises 91 collected cases plus those six unregistered cases.

`import/xlsximport.test.ts` skips two real-workbook cases under absent `data/manual/`; its third test “rejects a non-OEWS workbook” returns early with no assertion. Therefore 88 of 89 reported passes actually reach assertions. The missing external inputs were not downloaded or fabricated to relabel baseline results green.

All other collected calculation, schema, rounding, citation, parser, review/seeded and Markdown cases pass. The seed gate requires at least 12/13 detections; the diagnostic replay reports 13/13, no missed IDs, auto-fail, score 50. Six real-document golden cases remain TEST_PRESENT_BUT_NOT_EXECUTED; database-sourced review in the harness is separate execution evidence.

Svelte check passes with zero errors/warnings. The production build passes, writing static output. Warnings: initial generated tsconfig missing (fresh/concurrent check/build startup), two removable Zod pure-comment annotations, ~940 kB minified chunk. These did not fail compilation. No separate lint command exists. Schema, import/export and calculation tests are subgroups of the same Vitest invocation; no invented npm test/lint scripts were used.

Cargo fetch/check/test each cannot start (exit 127). The initial Tauri invocation loses --no-bundle to npm, so it attempts the documented default build; corrected flag forwarding still fails cargo metadata. Both host attempts exit 1 before frontend pre-build/Rust compilation/packaging. PLATFORM_BLOCKED is the matrix interpretation, not product compilation failure. Windows NSIS/WebView2 tests were not attempted via emulation.

npm audit exits 1 for five reported dependency entries, no high/critical; see logs/npm-audit.log. No exploitability claim or forced remediation.

Diagnostic harness iterations: initial CJS format rejected top-level await (unrecorded preliminary local setup log in /tmp); first recorded ESM run rejects an invalid fixture series kind. That log is retained as reproductions-fixture-error.log. Next run executes but its Item15 fixture replacement did not insert the bridge, so it was corrected and asserted. `reproductions-final` is authoritative: exit 0, 1.339 seconds, field-diff and numerical expectations pass. These are diagnostic expectations of observed defects, not an application acceptance PASS. No product source was changed.

The final harness executes read-only integrity/FK/schema/count checks, actual db.ts SQL on disposable copies, page serialization/context functions with I/O adapters, synthetic workbook parsers, export/reopen checks, seeded review replay, and Item15 mismatch. No browser DOM, first-launch resource copy, SQL IPC, Tauri permissions, Rust host or Windows deployment is proved. Expected/observed details and repeat command are in reproduction-log.md.

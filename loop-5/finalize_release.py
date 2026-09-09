#!/usr/bin/env python3
"""Assemble candidate docs, runtime and manifest. Refuses a previously frozen target."""
import argparse,json,pathlib,hashlib,shutil
from build_release import encode,HEAD,M3,M4,VERSION
ROOT=pathlib.Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('release',type=pathlib.Path);ap.add_argument('--freeze',action='store_true');args=ap.parse_args();r=args.release
manifest=r/'release-manifest.json'
if manifest.exists() and json.load(open(manifest)).get('status')=='ICR_EVIDENCE_RELEASE_FROZEN':raise SystemExit('Already frozen; create a new release version.')
def put(p,o):f=r/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(encode(o))
def doc(p,s):f=r/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s.strip()+'\n')
doc('README.md','''# ICR Evidence Release 1.0.0

Portable public evidence for a local ICR Workbench. JSON is authoritative. This release contains the 73-ICR federal benchmark and models, 200 federal sources, 389 federal claims, federal method assumptions and the frozen 27-entity canonical model; TSA portfolio, graph, reviewed assumptions, comparisons, within-ICR findings, quantitative checks, predecessor bridge, excerpts, and bounded retrieval indexes. It includes 90 recent TSA packages and 48 assigned control histories. Recency is not approval status.

The original evidence states are M1-1.0.0 and M3-1.0.0; graph 1.0.0; canonical model 0.5.0; rubric 1.0.0. Mission 4 and the completed EAB brief supply the analytical snapshot. Exact commits and input hashes are in the manifest and provenance/input-inventory.json. No new research was conducted.

Start with release-manifest.json, CONTRACTS.md and LOOP-5.2-HANDOFF.md. The graph and indexes are projections; complete adjudication registers govern analytical meaning. Source evidence, normalization, inference, calculated results, unresolved questions and reusable method guidance retain distinct labels. Numeric assumptions are observations, not approved TSA defaults.

## Validation and offline loading

Unzip to a new directory. Obtain the expected manifest SHA-256 from the separately committed freeze receipt. On a machine with Node, run `node runtime/verify.mjs . EXPECTED_MANIFEST_SHA256` from this directory. No package installation, Python, network or repository is needed. Omit the hash only for exploratory loading; a trusted external hash is needed to verify the expected identity. The validator does not write into the release.

For an offline HTML/WebView2 application, include runtime/consumer.mjs in the application build and supply `readBytes(relativePath)` from user-selected files or the host file bridge. Call `loadRelease(readBytes, {expectedManifestHash, listPaths})`. It uses native UTF-8, JSON and Web Crypto only. A File/ArrayBuffer adapter avoids file:// fetch restrictions. Nothing here requires an HTTP server. Consumer returns structured data; it does not render source text as HTML or execute stored formulas.

Validation checks the complete artifact inventory, SHA-256, every listed JSON contract, IDs, provenance, graph endpoints, claim sources, comparison evidence, counts, bridge arithmetic and indexes. The runtime intentionally supports only the JSON Schema keywords used by this release and rejects unsupported keywords. The repository build audit additionally verifies input fingerprints, frozen-tree preservation and lossless reproduction of canonical registers. The clean-load report records isolated release-only retrieval tests.

## Scope and limitations

This is not a Workbench UI, approved ICR model, legal guidance, official correction, internal TSA dataset, or complete archive of publication binaries. Source excerpts and registered analytical evidence are available offline; clicking an external publication requires connectivity. Public links are preserved as frozen locators and were not newly tested for availability. Full reports and original documents remain outside the distribution.

There are 468 principal activity representations and 25 assumption-context activity nodes. Repeated table/narrative, year/annualized and predecessor representations must not be summed. There are 32 task/method adjudications and a separate eight-record within-ICR register. Six unresolved task/method questions are not the seven combined unresolved records. Neither register supports a portfolio inconsistency rate.

Only 40 versions have registered quantitative checks. Row screening does not mean full-model assurance. Null/absent means unobserved, not zero. The federal sample is purposive. Source metadata review flags can predate completed review; canonical analytical registers govern. See KNOWN-ISSUES.md and provenance/limitations.json.

Base evidence remains immutable. Layer TSA-local evidence and project models in separate stores using the overlay contract. Human approval controls applicability, comparability, new assumptions, official corrections, Item 15 cause/classification, and narrative adoption.
''')
doc('CONTRACTS.md','''# Software contracts — schema 1.0.0

All files are UTF-8 JSON or text; JSON numbers preserve the frozen values, including IEEE-754 representation limits. Historical CSV numeric strings remain strings. Never convert missing strings/nulls to zero. Freeze original and computed values separately. JSON Schema dialect is 2020-12; the used subset is type, required, properties, additionalProperties, items, enum, const, minimum, maximum, minItems, minLength and pattern, plus documentation keywords. runtime/consumer.mjs validates this entire used subset, not arbitrary third-party schemas.

## Manifest and integrity

release_id identifies the institutional product; version and schema_version are 1.0.0. source_commits distinguish the frozen evidence snapshot, report completion and final editorial source. Each inventory row declares relative path, byte length, SHA-256, schema and schema mode for JSON. record_counts reproduce the registered TSA counts, including separate classification ledgers. dependency_groups give the load dependencies.

The manifest inventories every file under this directory except itself. Its exact byte SHA-256 is pinned externally in the repository freeze receipt; that receipt also records the release commit. This avoids circular self-hashing and commit self-reference. Reports inside the inventory describe checks and results without containing the final manifest hash. The ZIP and its SHA-256 are outside the canonical directory. A trusted hash verifies expected content, not publisher authentication by itself.

## Identities and relationships

Existing SRC-*, M3-SRC-*, M3-META-*, VER-*, CONTROL-*, activity, ASSUM-*, CMP-*, FIND-*, QA-*, BASELINE-* and CLM-* identities are preserved verbatim. Federal package refs and OMB controls remain source identities. New PROV-<sha256> IDs intern previously anonymous provenance objects; their hash is over canonical sorted-key UTF-8 JSON plus newline. New analysis IDs are release interpretations, never substitutes for original evidence IDs.

Graph nodes: id, type, epistemic_status, data, provenance_refs. Edges: id, type, source, target, epistemic_status, provenance_refs. Nodes and edges are authoritative JSON projections of graph 1.0.0, consolidated without batch mechanics. Hydrating provenance_refs through provenance/observations.json restores the original provenance arrays exactly. `hydrate` is supplied. Original paths inside payloads are supplemental provenance, not runtime dependencies.

Graph evidence categories PUBLISHED, NORMALIZED, CALCULATED, INFERRED and UNRESOLVED are retained. Source records include source ID, agency, control, package, document ID, public URL, dates/period when known, source type, evidence status and original_record. The raw original metadata is preserved. Federal sources shared by the TSA graph resolve to the federal source registry; indexes/sources.json is the definitive citation lookup.

Activities use graph ACTIVITY.data: ref, activity, actor where observed, period, lifecycle/lifecycle_scope, unit/population_unit, frequency where explicit, source boundary fields, original and normalized values. `record_kind` separates normalized_activity_representation from assumption_task_context. Actor/task/shape facets preserve frozen labels; no new synonym equivalence is asserted. Missing lifecycle, actor or frequency is not filled. The source-defined field details remain in data and linked excerpts.

Assumption observations use graph ASSUMPTION.data: family, original_value, original_unit, normalized_value or formula/value, unit, period, vintage where known, actor, scope and evidence status. A formula-header observation is not the same as a reviewed scalar default. `provenance_refs` preserves original, extraction_method, transformation and status. Direct relationships use USES_ASSUMPTION. Same-package retrieval is context only. Federal assumption-library.json describes reusable methods/applicability and example ICRs; the TSA library is the original discovery-family catalog, not an approved numeric default library. Actual reviewed TSA observations are ASSUMPTION nodes.

Comparisons: tsa/comparisons.json contains complete task/method adjudications, compared observations, normalization dimensions, family, rationale, limitations, source refs and challenge results. tsa/within-icr-findings.json contains the separate reconstruction register, linked check IDs and adjudications. Preserve CONSISTENT, DIFFERENT_EXPLAINED, POTENTIALLY_INCONSISTENT, NOT_COMPARABLE, UNRESOLVED. The task/method register includes some within-package pathway and lineage comparisons; its conceptual scope differs from the reconstruction register regardless of the legacy `level` label.

Claims in federal/claims.json retain observed evidence, interpretation, confidence, locator and source_ids. Extractions in federal/models.json preserve every reviewed model, formula, check, score rationale, method and reconstruction limitation. No generic prose is promoted to an observed fact. Every analysis/findings.json conclusion has evidence_refs, origin, kind and limitations.

Item 15 bridges: prior_ref/current_ref, verified baseline_identity, components, prior/current component values, deltas, net_change, residual, unit, period, classification and provenance. Check every component delta, component sums and old + changes + residual = new. The TWIC bridge validates displayed component reconciliation; it does not estimate causal driver effects or assign program-change/adjustment labels.

Canonical ICR model: federal/canonical-model.json transcribes the frozen 27-entity dictionary and full model 0.5.0 specification. This is an architectural contract, not a newly implemented scenario schema. Population, activities, frequency, labor, nonlabor, Federal costs, sources, assumptions, formulas, periods, baselines, change events and narrative bindings are retained. Loop 5.2 must not pretend packaging implemented formulas or resolved ambiguous field choices.

## Retrieval

indexes/addresses.json maps qualified retrieval keys to file#JSON-pointer addresses. Qualified keys are addresses, not new analytical identities. indexes/facets.json maps exact facet/value pairs to those keys: dataset, type, control, package, activity/shape, actor, population/event unit, assumption family, source, comparator family, adjudication status, federal category and Item 12–15. Intersect facets; sort qualified keys; page with limit 1–100 and exclusive after key. Unknown fields/operators are rejected. Unknown values return no records. See contracts/query-contract.json and `query` in the runtime.

indexes/adjacency.json preserves typed outgoing edges. A missing edge does not prove absence of a relationship. indexes/locators.json resolves archived locator strings to release-contained excerpt provenance; original document locators remain visible. There is no broad language search or automatic comparability decision. Item tags are incomplete: explicit source item fields, federal model sections and validated bridges are indexed; do not infer irrelevance from missing tags. No schema uses external resolvers or runtime databases.

Recommended sequence: trusted manifest hash → inventory integrity → schemas → provenance and source registries → graph and complete registers → indexes → project overlays. `loadRelease` implements this with full validation before returning queryable data. Rebuild indexes from canonical JSON if optimizing later, and verify their projection equivalence. Any SQLite database is disposable and must contain no evidence absent from JSON.
''')
doc('KNOWN-ISSUES.md','''# Known issues and mechanical normalization

No new substantive evidence or adjudication was introduced. The packaging source state matched every blob present at the Mission 3 freeze. Full frozen limitations are in provenance/limitations.json.

1. Source review_status may say NOT_YET_REVIEWED because it is historical retrieval metadata. Preserve it in original_record; completed reviewed registers and epistemic labels govern analytical state. Do not mechanically relabel the original metadata.
2. One administrative-only 2019 LEOSA package has no Supporting Statement. Its existing package URL is exposed as the source URL; the separate usable predecessor and source lineage remain in the graph. Package metadata is not task evidence.
3. Graph ACTIVITY count 493 includes 25 assumption-context nodes. Principal representations total 468 and include overlapping representations. No deduplication or numeric aggregation is implied.
4. TSA assumption discovery families and observed graph families are different layers. Only 162 reviewed ASSUMPTION nodes are assumption observations; keyword discovery is not reviewed numerical evidence.
5. Detailed Item 12–15, lifecycle, frequency and actor fields are incomplete in frozen records. Indexes preserve available explicit values; absent tags are documented coverage limits. No packaging inference fills them.
6. Canonical model 0.5.0 is a research dictionary/specification. A scenario implementation schema remains future work. Some peripheral federal rows require human semantic interpretation.
7. Public publication links are preserved, not newly fetched. Offline use includes excerpts and analytical records, not original publication binaries or report PDFs.
8. Legacy source/working paths remain as supplemental historical provenance. Their excerpt content resolves through indexes/locators.json; consumers use manifest files and JSON pointers, never those historical paths. Control-history refs older than represented versions are metadata-only historical references, not unresolved internal graph links.
9. Graph FINDING projections are secondary to the separate complete comparison and within-ICR ledgers. A task comparison can have legacy level within_ICR while still belonging to the task/method register. Classification counts must use register membership.
10. Floating-point artifacts and CSV numeric strings are preserved. Display rounding must not overwrite evidence. Formulas are inert strings, not executable JavaScript. Future deterministic calculation engines require a bounded formula grammar.

Mechanical changes: concatenate graph shards; parse CSV/JSONL into JSON; intern repeated provenance arrays using content-addressed PROV IDs; transcribe the canonical Markdown entity table without changing fields; expose administrative package URL from its existing nested record; retain original source metadata. No authoritative identity was replaced. New analysis summaries point to completed registered evidence and retain applicability boundaries.
''')
doc('CHANGELOG.md','''# Changelog and version policy

## 1.0.0 — 2026-09-09
First portable JSON evidence release from completed federal benchmark, frozen TSA evidence graph, consistency report and EAB leadership brief. Includes schemas, provenance, distinct adjudication registers, exact retrieval indexes, dependency-free consumer, integrity validation and clean-load evidence.

Patch: metadata/provenance correction with unchanged analytical meaning and compatible identities/contracts. Minor: additive evidence, indexes or compatible schema extension. Major: incompatible schema, changed identity meaning or incompatible analytical interpretation. Corrected substantive evidence must be reviewed, identified and versioned; never use a metadata patch to conceal a changed conclusion.

All published versions are immutable, including patches. Every correction creates a new directory, manifest, hashes, validation results and release identity. Never silently replace v1.0.0. A derived SQLite cache may be regenerated from canonical JSON and discarded; its generation must declare the source manifest digest.
''')
doc('LOOP-5.2-HANDOFF.md','''# Loop 5.2 — consume ICR-EVIDENCE-1.0.0

Repository path: release/icr-evidence/v1.0.0. Entry point: release-manifest.json. Portable/schema version: 1.0.0; graph: 1.0.0; M1-1.0.0 and M3-1.0.0; canonical model 0.5.0; rubric 1.0.0. The externally committed loop-5/freeze-state.json identifies the exact manifest digest and release commit. Distribution ZIP has the same canonical directory contents.

Read README.md, CONTRACTS.md, schemas/, contracts/query-contract.json and contracts/overlay-contract.json. No broad repository inspection is necessary. Implement local file selection or a WebView2 host adapter, pin the expected manifest hash, pass readBytes and listPaths to runtime/consumer.mjs, and enable evidence querying only after loadRelease succeeds. Run runtime/verify.mjs with Node as a development smoke test; production browser use does not require Node, Python, a package manager or a server. Bundle the supplied module with the Anvil project and preserve the base files unchanged.

Use tsa/nodes.json plus tsa/edges.json for exploration. Resolve citations through indexes/sources.json and provenance/observations.json. `hydrate` restores full original provenance arrays. The separate full task/method, within-ICR, QA, challenge and Item 15 registers govern findings; graph projections do not replace them. Federal comparator records link to all 73 available federal models and their claim/source registries. Original documents remain public click-through links; excerpts are offline.

Use exact address/facet indexes for bounded queries. Supported facets include OMB control, package, activity/shape, actor, population unit, assumption family, source, comparator family, adjudication status, federal category and explicit item relationship. query returns bounded records and stable pagination, rejects unknown fields/operators, and does not infer matches. Future DHSChat query packets may select this contract; they must not execute arbitrary code or mutate adjudications. A2UI displays must render data as text and approved components, never arbitrary HTML from evidence or packets.

The clean-load examples cover portfolio/version selection, activities, package-associated assumptions, adjudications, public sources, QA-CYBER-COST/FIND-CYBER-COST, BASELINE-TWIC-2025, six unresolved task/method questions, federal comparators, Federal review-time assumptions and CMP-01 carrier amendments. Reuse validation/clean-load-report.json as the fixture and runtime acceptance function as executable acceptance checks.

Layer base release + separate TSA-local overlay + separate project model. An overlay pins the base release ID and manifest digest, uses local:<organization>:<uuid> identities, records explicit references/proposed overrides, and never overwrites base objects. Keep restricted content out of the public base and future public exports. Conflicts are review records, not silent last-write-wins merges. See overlay schema and contract for deterministic envelope validation.

Human decisions: applicability/transfer of assumptions; whether tasks are truly comparable; missing inputs and proxy selection; economic scope and interpretation; official corrections; program changes versus adjustments; causal driver decomposition; approval of narrative and publication. The UI may explain or flag these decisions but must not automatically close unresolved questions.

Known limits include 468 overlapping principal representations, 25 contextual activity nodes, source review metadata predating completed review, incomplete item/actor/frequency tags, 40 quantitatively checked versions, and a frozen architectural model that still needs an implementation schema. No internal-process attribution, agency ranking or portfolio inconsistency rate is authorized. No Workbench UI or DHSChat bus was built in Loop 5.1.
''')
put('contracts/overlay-contract.json',{'version':'1.0.0','base':'immutable public release','required_base_pin':['base_release_id','base_manifest_sha256'],'namespace':'local:<organization>:<uuid>; project:<uuid> for project model identities','references':'base:<release_id>:<existing_id>, with dataset where identity is shared by projections','extensions':'namespaced extension object; never add local fields to base files','conflicts':'retain all competing proposals; require human disposition; no silent last-write-wins','compatibility':'exact base digest required; schema major must match; migration to another release requires explicit validated remap and human acceptance','export':'base files never incorporate local evidence; local classification/access controls and export review belong to overlay host','record_fields':['id','references','proposed_changes','provenance','owner','review_status'],'human_control':['applicability','comparability','official_correction','causal_decomposition','item15_classification','publication']})
put('schemas/overlay.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['schema_version','base_release_id','base_manifest_sha256','namespace','records'],'additionalProperties':False,'properties':{'schema_version':{'const':'1.0.0'},'base_release_id':{'const':'ICR-EVIDENCE-1.0.0'},'base_manifest_sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'},'namespace':{'type':'string','pattern':'^local:[A-Za-z0-9_-]+$'},'records':{'type':'array','items':{'type':'object','required':['id','references','proposed_changes','provenance','owner','review_status'],'properties':{'id':{'type':'string','pattern':'^local:[A-Za-z0-9_-]+:[A-Za-z0-9-]+$'},'references':{'type':'array','items':{'type':'string'}},'proposed_changes':{'type':'object'},'provenance':{'type':'array','items':{'type':'object'}},'owner':{'type':'string'},'review_status':{'enum':['PROPOSED','APPROVED','REJECTED','CONFLICT']}}}}}})
manifest_schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['release_id','name','version','schema_version','created_at','source_repository','source_commits','evidence_versions','graph_version','canonical_model_version','rubric_version','schemas','files','record_counts','dependency_groups','compatibility','provenance_notes','known_limitations','status'],'properties':{'release_id':{'const':'ICR-EVIDENCE-1.0.0'},'version':{'const':'1.0.0'},'schema_version':{'const':'1.0.0'},'status':{'enum':['CANDIDATE','ICR_EVIDENCE_RELEASE_FROZEN']},'files':{'type':'array','minItems':1,'items':{'type':'object','required':['path','bytes','sha256'],'properties':{'path':{'type':'string','minLength':1},'bytes':{'type':'integer','minimum':0},'sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'}}}}}}
put('schemas/manifest.schema.json',manifest_schema)
(r/'runtime').mkdir(exist_ok=True)
for file in ['consumer.mjs','verify.mjs']:shutil.copyfile(ROOT/'loop-5'/file,r/'runtime'/file)
put('validation/compatibility-report.json',{'status':'PASS','canonical_format':'UTF-8 JSON','schema_version':'1.0.0','runtime':'ECMAScript module + native JSON/TextDecoder/WebCrypto; File or host bridge adapter','external_runtime_dependencies':[],'requires_python':False,'requires_network':False,'requires_repository':False,'requires_database':False,'sqlite':'Not included; JSON size and exact indexes suffice','browser_ui_test':'No UI in scope; isolated release-only Node execution tests the same dependency-free consumer core.'})
if args.freeze:
    for p in ['validation/source-preservation-report.json','validation/validation-report.json','validation/clean-load-report.json','validation/integrity-report.json']:
        if json.load(open(r/p)).get('status')!='PASS':raise SystemExit('Freeze gate failed: '+p)
mapping=json.load(open(r/'contracts/schema-map.json'))
inventory=[]
for f in sorted(r.rglob('*')):
    if not f.is_file() or f==manifest:continue
    p=str(f.relative_to(r));b=f.read_bytes();entry={'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    if p.endswith('.json'):
        entry.update({'schema':mapping.get(p,{}).get('schema','schemas/object.schema.json'),'schema_mode':mapping.get(p,{}).get('mode','document')})
        parsed=json.loads(b);entry['record_count']=len(parsed) if isinstance(parsed,list) else None
    inventory.append(entry)
state=json.load(open(r/'provenance/frozen-state.json'))
put('release-manifest.json',{'release_id':'ICR-EVIDENCE-1.0.0','name':'Portable ICR Evidence Release','version':'1.0.0','schema_version':'1.0.0','created_at':'2026-09-09T21:42:00Z','source_repository':'https://github.com/Lukemendels/ICR-12-15-Benchmark','source_commits':{'completed_editorial_state':HEAD,'mission1_frozen_snapshot':M3,'mission3_freeze':M3,'mission4_completion':M4},'evidence_versions':{'federal':'M1-1.0.0','tsa':'M3-1.0.0'},'graph_version':'1.0.0','canonical_model_version':'0.5.0','rubric_version':'1.0.0','schemas':{'portable':'1.0.0','frozen_graph_ontology':'0.1.0','contract_map':'contracts/schema-map.json','manifest':'schemas/manifest.schema.json','typed_graph_payloads':{'ACTIVITY':'schemas/activity-data.schema.json','ASSUMPTION':'schemas/assumption-data.schema.json'}},'files':inventory,'record_counts':state['mission3_counts'],'dependency_groups':{'provenance':[],'federal':['provenance'],'tsa':['provenance','federal/source-registry.json'],'analysis':['federal','tsa'],'indexes':['federal','tsa','provenance'],'runtime':['schemas','release-manifest.json','indexes']},'compatibility':{'consumer_schema_major':1,'canonical':'JSON','offline':True,'required_runtime_packages':[],'overlay_contract':'contracts/overlay-contract.json','query_contract':'contracts/query-contract.json'},'provenance_notes':['Mission 1 original evidence versions preserved; its exact source snapshot is pinned at the unchanged Mission 3 freeze.','Original source/claim/graph IDs retained; anonymous provenance interned with reversible content-addressed IDs.','Graph projections and complete analytical registers remain distinct.','Manifest excludes itself; pin exact SHA-256 and release commit in external freeze receipt.'],'known_limitations':'KNOWN-ISSUES.md; provenance/limitations.json','status':'ICR_EVIDENCE_RELEASE_FROZEN' if args.freeze else 'CANDIDATE'})
print(hashlib.sha256(manifest.read_bytes()).hexdigest())

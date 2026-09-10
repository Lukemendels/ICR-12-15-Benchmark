"""Loop 5.2 repository closeout gate; portable transfer checks live in package.py."""
import json
from pathlib import Path
import subprocess
import sys
from importlib.util import spec_from_file_location, module_from_spec

sys.dont_write_bytecode = True

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parent
spec = spec_from_file_location('transfer', PROJECT / 'tests/package.py')
pkg = module_from_spec(spec)
spec.loader.exec_module(pkg)
B = '328fc916d451f9b98670f9bb7906cb4e56b5fc56'
A = 'f70a521'
WINDOWS = 'WINDOWS_WEBVIEW2_DEPLOYMENT_VALIDATION_PENDING'
ANVIL = 'ANVIL_RUNTIME_IMPORT_NOT_EXECUTED'

def read(name):
    return json.loads((PROJECT / name).read_text())

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def main():
    if not (ROOT / '.git').exists():
        raise SystemExit('Closeout requires repository history; use build.mjs, foundation.test.mjs and package.py for portable transfer validation.')
    # Remove stale success attestations before starting validation.
    for name in ['loop-5.2-acceptance.json', 'loop-5.2-terminal.json', 'compatibility-report.json']:
        (PROJECT / 'validation' / name).unlink(missing_ok=True)
    (PROJECT / 'validation/foundation-tests.json').unlink(missing_ok=True)
    pkg.run('node', '--test', 'tests/foundation.test.mjs')
    pkg.run(sys.executable, 'tests/package.py')
    tests = read('validation/foundation-tests.json')
    build = read('validation/build-report.json')
    transfer = read('validation/transfer-package-report.json')
    manifest = read('paperclip.tool.json')
    pin = read('assets/evidence-pin.json')
    checkpoint = read('validation/checkpoint-b.json')
    passed = {x['id'] for x in tests['tests'] if x['status'] == 'PASS'}
    criteria = []
    def check(id, condition, evidence):
        criteria.append({'id': id, 'status': 'PASS' if condition else 'FAIL', 'evidence': evidence})
    def tested(id, *names):
        check(id, all(n in passed for n in names), {'report': 'validation/foundation-tests.json', 'tests': names})
    frozen_diff = git('diff', '007abaf', '--', 'release/icr-evidence/v1.0.0', 'loop-5/freeze-state.json')
    untracked = git('ls-files', '--others', '--exclude-standard', '--', 'release/icr-evidence/v1.0.0')
    check('frozen_loop_5_1_unchanged', not frozen_diff and not untracked, 'Git comparison to frozen Loop 5.1 commit 007abaf; exact payload also verified by build and transfer')
    ancestry = subprocess.run(['git', 'merge-base', '--is-ancestor', A, B], cwd=ROOT).returncode == 0
    protected = ['src', 'assets', 'paperclip.tool.json', 'ARCHITECTURE.md', 'SKILL.md', 'skills', 'prompts']
    unchanged = not git('diff', B, '--', *['icr-workbench/' + p for p in protected])
    check('checkpoint_a_architecture_preserved', ancestry and unchanged, 'Checkpoint A is ancestor of B; architecture/source/pins remain byte-unchanged from completed B')
    check('checkpoint_b_working_shell_complete', checkpoint['status'] == 'WORKING_SHELL_COMPLETE' and not git('diff', B, '--', 'icr-workbench/validation/checkpoint-b.json'), 'validation/checkpoint-b.json unchanged')
    check('modular_source_authoritative', manifest['source'] == {'html':'src/index.html','css':'src/style.css','javascript':'src/app.js'} and build['source_validation']['status'] == 'PASS', 'paperclip.tool.json and build source validation')
    for name in ['ARCHITECTURE.md', 'SKILL.md']:
        check(name + '_exists', (PROJECT / name).is_file(), name)
    check('paperclip_manifest_valid', build['anvil_contract'] == 'PASS', 'Pinned upstream manifest and project closure validation')
    check('evidence_release_pinned', pin['release_id'] == 'ICR-EVIDENCE-1.0.0', 'assets/evidence-pin.json')
    check('exact_manifest_digest_pinned', pin['manifest_sha256'] == pkg.DIGEST, 'assets/evidence-pin.json')
    tested('correct_evidence_loads', 'correct_release_and_exact_manifest_load')
    tested('wrong_identity_digest_fails_closed', 'wrong_manifest_hash_fails_closed', 'wrong_release_identity_fails_closed')
    tested('public_base_deeply_immutable', 'public_base_recursively_immutable', 'forged_base_rejected_by_provider_and_stores')
    tested('tsa_overlay_separate', 'independent_overlay_project_import_export_and_no_base_replacement', 'overlay_identity_collision_bad_pin_reference_and_duplicate_rejected')
    tested('working_project_separate', 'independent_overlay_project_import_export_and_no_base_replacement', 'project_rejects_base_identity_calculation_extra_keys_and_preserves_prior')
    tested('bounded_provider', 'bounded_exact_paging_and_unknown_operators', 'provenance_hydration_and_typed_neighbors')
    tested('safe_rendering', 'stored_text_and_source_links_safe_by_construction', 'source_validation_and_modular_navigation')
    check('foundation_tests', tests['status'] == 'PASS' and tests['test_count'] == 26, 'validation/foundation-tests.json: 26 tests')
    tested('deterministic_build', 'clean_build_standalone_static_and_repeat_deterministic')
    standalone = PROJECT / 'dist/icr-workbench.html'
    check('standalone_exists', standalone.is_file() and pkg.sha(standalone.read_bytes()) == build['standalone']['sha256'], 'validation/build-report.json')
    tested('offline_core_no_cdn_server_package_manager_model_api', 'clean_build_standalone_static_and_repeat_deterministic', 'source_validation_and_modular_navigation')
    check('transfer_zip_exists', pkg.ZIP.is_file() and pkg.sha(pkg.ZIP.read_bytes()) == transfer['sha256'], 'validation/transfer-package-report.json')
    check('transfer_zip_validates', transfer['status'] == 'PASS', 'validation/transfer-package-report.json')
    check('transfer_frozen_identity', transfer['frozen_evidence_byte_identity'] == 'PASS' and transfer['manifest_sha256'] == pkg.DIGEST, 'Every archive and extracted byte compared to canonical input; extracted build verifies pinned release')
    check('extracted_transfer_reproduces_standalone', transfer['extracted_package_reproducibility'] == 'PASS' and transfer['standalone_sha256'] == build['standalone']['sha256'], 'Extracted HTML deleted before ordinary rebuild; exact output SHA-256 matches')
    tested('anvil_paperclip_linux_contract', 'upstream_anvil_closure_candidate_isolation_and_context')
    check('capability_pins_locks', build['status'] == 'PASS' and manifest['dependencies'][0]['version'] == '1.0.1' and transfer['capability'] == 'icr-evidence-foundation@1.0.1', 'Ordinary build validates source inputs, governed digests and capability set lock')
    check('windows_pending_recorded', WINDOWS == 'WINDOWS_WEBVIEW2_DEPLOYMENT_VALIDATION_PENDING', 'compatibility-report.json and loop-5.2-terminal.json; Linux cannot execute deployment host')
    check('anvil_import_not_executed_recorded', ANVIL == 'ANVIL_RUNTIME_IMPORT_NOT_EXECUTED', 'No supported Anvil runtime exercised; upstream source-contract validation only')
    check('loop_5_3_handoff_exists', (PROJECT / 'LOOP-5.3-HANDOFF.md').is_file(), 'LOOP-5.3-HANDOFF.md')
    limitations = ['Windows/WebView2 deployment-device validation pending.', 'Actual Anvil runtime import not executed; Linux validation covers the shared compiler and project contract only.', 'No browser DOM execution; safe rendering validated by construction and foundation tests.', 'Modern Web Crypto and DecompressionStream required; opening external source links needs connectivity.', 'Overlay/project envelopes are in memory with independent JSON APIs; no durable persistence or calculation model.', 'Graph visualization, DHSChat bus, data packets, A2UI and later modeling/production workflows are not implemented.']
    common = {'schema_version':'1.0.0', 'application_version':'0.1.0', 'foundation_capability_version':'1.0.1', 'foundation_capability':'icr-evidence-foundation@1.0.1', 'project_root':'icr-workbench', 'evidence_release_id':pin['release_id'], 'evidence_manifest_sha256':pin['manifest_sha256'], 'standalone_html':build['standalone'], 'transfer_zip':{'path':transfer['path'],'sha256':transfer['sha256']}, 'loop_5_3_handoff':'icr-workbench/LOOP-5.3-HANDOFF.md', 'linux_platform_independent_validation':'PASS' if all(c['status']=='PASS' for c in criteria) else 'FAIL', 'windows_webview2_status':WINDOWS, 'anvil_runtime_status':ANVIL, 'remaining_non_blocking_limitations':limitations}
    compatibility = {**common, 'foundation_test_status':tests['status'], 'foundation_test_count':tests['test_count'], 'deterministic_build_status':'PASS' if 'clean_build_standalone_static_and_repeat_deterministic' in passed else 'FAIL', 'transfer_package_validation':transfer['status'], 'extracted_package_reproducibility':transfer['extracted_package_reproducibility'], 'anvil_paperclip_project_contract':build['anvil_contract'], 'capability_pins_locks':build['status']}
    pkg.write('compatibility-report.json', compatibility)
    provisional = all(c['status']=='PASS' for c in criteria)
    terminal = {**common, 'terminal_state':'ANVIL_ICR_WORKBENCH_FOUNDATION_COMPLETE' if provisional else 'IN_PROGRESS', 'final_acceptance_result':'PASS' if provisional else 'FAIL'}
    pkg.write('loop-5.2-terminal.json', terminal)
    for criterion in criteria:
        if criterion['id'] in {'windows_pending_recorded', 'anvil_import_not_executed_recorded'}:
            key, expected = ('windows_webview2_status', WINDOWS) if criterion['id'] == 'windows_pending_recorded' else ('anvil_runtime_status', ANVIL)
            criterion['status'] = 'PASS' if all(read('validation/' + name)[key] == expected for name in ['compatibility-report.json', 'loop-5.2-terminal.json']) else 'FAIL'
    check('machine_readable_terminal_exists', read('validation/loop-5.2-terminal.json') == terminal, 'validation/loop-5.2-terminal.json parsed and compared')
    overall = 'PASS' if all(c['status']=='PASS' for c in criteria) else 'FAIL'
    pkg.write('loop-5.2-acceptance.json', {'schema_version':'1.0.0','checkpoint':'C','overall_result':overall,'criteria':criteria,'platform_deferrals_non_blocking':True})
    print(json.dumps({'final_acceptance':overall,'criteria':len(criteria),'terminal_state':terminal['terminal_state']}))
    if overall != 'PASS':
        raise SystemExit(1)

if __name__ == '__main__':
    main()

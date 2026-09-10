"""Deterministic three-root transfer; reports deliberately remain outside the ZIP."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parent
DIGEST = '572e8a414c5867e75a5d24eb4d5e939a475969c92bb1d81b3f183f436b4663a9'
RELEASE = ROOT / ('release/icr-evidence/v1.0.0' if (ROOT / 'release').exists() else 'evidence/icr-evidence/v1.0.0')
ZIP = PROJECT / 'dist/ICR-Workbench-Anvil-Project.zip'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def run(*args, cwd=PROJECT):
    subprocess.run(args, cwd=cwd, check=True)

def write(name, value):
    target = PROJECT / 'validation' / name
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(value, indent=2) + '\n')

def inventory():
    entries = {}
    def add(root, prefix, allowed=lambda p: True):
        for p in sorted(root.rglob('*')):
            rel = p.relative_to(root)
            if not allowed(rel):
                continue
            if p.is_symlink():
                raise ValueError(f'Symlink forbidden: {p}')
            if p.is_file():
                entries[f'{prefix}/{rel.as_posix()}'] = p.read_bytes()
    # Explicit source contract: no reports, caches, recovery files or nested ZIPs.
    docs = {'README.md', 'ARCHITECTURE.md', 'SKILL.md', 'LOOP-5.3-HANDOFF.md', 'paperclip.tool.json'}
    def project_file(p):
        return (p.as_posix() in docs or p.as_posix() == 'dist/icr-workbench.html' or
                (p.parts[0] in {'assets', 'src', 'skills', 'prompts', 'tests'} and
                 not any(x.startswith('.') or x in {'__pycache__', 'node_modules', 'cache', 'recovery'} for x in p.parts) and
                 p.suffix not in {'.pyc', '.bak', '.tmp', '.zip'}))
    add(PROJECT, 'icr-workbench', project_file)
    dep = json.loads((PROJECT / 'paperclip.tool.json').read_text())['dependencies'][0]
    assert (dep['id'], dep['version']) == ('icr-evidence-foundation', '1.0.1')
    folder = Path(dep['path']).parent
    add(ROOT / 'governed-library' / folder, 'governed-library/' + folder.as_posix())
    add(RELEASE, 'evidence/icr-evidence/v1.0.0')
    assert sha((RELEASE / 'release-manifest.json').read_bytes()) == DIGEST
    for p in docs | {'tests/build.mjs', 'tests/foundation.test.mjs', 'tests/package.py', 'tests/acceptance.py', 'src/index.html', 'src/style.css', 'src/app.js'}:
        assert 'icr-workbench/' + p in entries, p
    return dict(sorted(entries.items()))

def archive(entries):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as z:
        for name, data in entries.items():
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    return output.getvalue()

def main():
    run('node', 'tests/build.mjs')
    entries = inventory()
    packed = archive(entries)
    assert packed == archive(entries), 'Non-deterministic ZIP'
    ZIP.write_bytes(packed)
    expected = sha((PROJECT / 'dist/icr-workbench.html').read_bytes())
    with tempfile.TemporaryDirectory(prefix='icr-transfer-') as temp:
        destination = Path(temp)
        with zipfile.ZipFile(ZIP) as z:
            assert z.testzip() is None
            assert z.namelist() == list(entries)
            for name in z.namelist():
                assert not name.startswith('/') and '..' not in Path(name).parts
                assert z.read(name) == entries[name], name
            z.extractall(destination)
        for name, data in entries.items():
            assert (destination / name).read_bytes() == data, name
        extracted = destination / 'icr-workbench'
        (extracted / 'dist/icr-workbench.html').unlink()
        run('node', 'tests/build.mjs', cwd=extracted)
        assert sha((extracted / 'dist/icr-workbench.html').read_bytes()) == expected
    report = {'status': 'PASS', 'path': 'icr-workbench/dist/' + ZIP.name,
              'sha256': sha(packed), 'entries': len(entries), 'zip_determinism': 'PASS',
              'required_files': 'PASS', 'safe_extraction_paths': 'PASS',
              'source_authority': 'modular icr-workbench/',
              'excluded': ['validation reports (avoid artifact digest cycles)', 'other dist outputs', 'caches', 'recovery artifacts', 'unselected capability versions'],
              'capability': 'icr-evidence-foundation@1.0.1', 'evidence_release_id': 'ICR-EVIDENCE-1.0.0',
              'manifest_sha256': DIGEST, 'all_archive_and_extracted_bytes_match': 'PASS',
              'frozen_evidence_byte_identity': 'PASS', 'extracted_package_reproducibility': 'PASS',
              'standalone_sha256': expected, 'anvil_paperclip_contract': 'PASS'}
    write('transfer-package-report.json', report)
    print(json.dumps(report))

if __name__ == '__main__':
    main()

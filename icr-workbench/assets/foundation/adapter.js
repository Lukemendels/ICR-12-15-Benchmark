// Included inside the governed foundation closure; Consumer and PIN are pinned inputs.
function deepFreeze(value) {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    Object.values(value).forEach(deepFreeze);
    Object.freeze(value);
  }
  return value;
}
const administrative = new Set(['FREEZE-RECEIPT.json', 'validation/final-acceptance-gate.json']);
function safePath(path) {
  if (typeof path !== 'string' || !path || path.includes('\\') || path.startsWith('/') || path.includes(':') || path.split('/').some(p => !p || p === '.' || p === '..')) throw Error('Unsafe release path');
  return path;
}
function requirePin(manifest, pin = PIN) {
  if (pin.schema_major !== 1 || pin.consumer_major !== 1) throw Error('Incompatible consumer/schema major');
  if (manifest.release_id !== pin.release_id || Number(manifest.schema_version.split('.')[0]) !== pin.schema_major) throw Error('Unexpected evidence identity/schema');
}
async function loadAdapter(adapter) {
  if (!adapter || typeof adapter.readBytes !== 'function' || typeof adapter.listPaths !== 'function') throw Error('A read-only byte adapter with actual listPaths is required');
  const actual = [...await adapter.listPaths()];
  actual.forEach(safePath);
  if (new Set(actual).size !== actual.length) throw Error('Duplicate release paths');
  const loaded = await Consumer.loadRelease(p => adapter.readBytes(safePath(p)), {
    expectedManifestHash: PIN.manifest_sha256,
    listPaths: async () => actual.filter(p => !administrative.has(p))
  });
  requirePin(loaded.manifest);
  const frozen = loaded.files['provenance/frozen-state.json'];
  // Version metadata is also byte-bound by the manifest; explicit expectations are checked at build.
  if (!frozen || loaded.manifestHash !== PIN.manifest_sha256) throw Error('Missing frozen identity');
  return deepFreeze(loaded);
}
function bytesAdapter(entries) {
  const map = new Map();
  for (const [path, bytes] of entries) {
    safePath(path);
    if (map.has(path)) throw Error('Duplicate release path');
    map.set(path, new Uint8Array(bytes));
  }
  return Object.freeze({
    listPaths: async () => [...map.keys()],
    readBytes: async path => {
      if (!map.has(safePath(path))) throw Error('Missing release artifact: ' + path);
      return map.get(path).slice();
    }
  });
}
function fileAdapter(files) {
  const map = new Map(); let root = null;
  for (const file of files) {
    const raw = file.webkitRelativePath || file.name;
    const slash = raw.indexOf('/');
    if (slash < 0) throw Error('Select the release directory, not individual files');
    const prefix = raw.slice(0, slash);
    if (root !== null && prefix !== root) throw Error('Select exactly one release root');
    root = prefix;
    const path = safePath(raw.slice(slash + 1));
    if (map.has(path)) throw Error('Duplicate release path');
    map.set(path, file);
  }
  return Object.freeze({listPaths: async () => [...map.keys()], readBytes: async path => {
    const file = map.get(safePath(path));
    if (!file) throw Error('Missing release artifact: ' + path);
    return new Uint8Array(await file.arrayBuffer());
  }});
}
async function bundledAdapter() {
  const compressed = Uint8Array.from(atob(PAYLOAD), c => c.charCodeAt(0));
  const stream = new Blob([compressed]).stream().pipeThrough(new DecompressionStream('gzip'));
  const unpacked = JSON.parse(await new Response(stream).text());
  return bytesAdapter(Object.entries(unpacked).map(([p, b]) => [p, Uint8Array.from(atob(b), c => c.charCodeAt(0))]));
}

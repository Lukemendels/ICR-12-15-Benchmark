const clone = value => JSON.parse(JSON.stringify(value));
const uuid = '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}';
function assertEnvelopePin(value) {
  if (value.base_release_id !== PIN.release_id || value.base_manifest_sha256 !== PIN.manifest_sha256) throw Error('Local state has a different base evidence pin');
}
function createStores(base) {
  if (!verifiedBases.has(base)) throw Error('Verified immutable base required');
  const files = base.files;
  const ids = new Set(files['tsa/nodes.json'].map(r => r.id));
  for (const id of Object.keys(files['indexes/sources.json'])) ids.add(id);
  for (const address of Object.values(files['indexes/addresses.json'])) {
    const r = Consumer.resolve(files, address);
    if (r && typeof r === 'object') for (const field of ['id', 'claim_id', 'icr_id', 'ref']) if (typeof r[field] === 'string') ids.add(r[field]);
  }
  const referencePrefix = 'base:' + PIN.release_id + ':';
  function checkReferences(refs) {
    if (!Array.isArray(refs)) throw Error('References must be an array');
    for (const ref of refs) {
      if (typeof ref !== 'string' || !ref.startsWith(referencePrefix) || !ids.has(ref.slice(referencePrefix.length))) throw Error('Unresolved base reference');
    }
  }
  function store(validate) {
    let value = null;
    return Object.freeze({
      snapshot: () => value,
      importJSON: text => {
        const candidate = JSON.parse(text);
        validate(candidate); // Validate completely before replacing mutable working state.
        value = deepFreeze(clone(candidate));
        return value;
      },
      exportJSON: () => value === null ? null : JSON.stringify(value, null, 2) + '\n',
      clear: () => { value = null; }
    });
  }
  const overlay = store(value => {
    Consumer.schemaValidate(value, files['schemas/overlay.schema.json']);
    assertEnvelopePin(value);
    const seen = new Set();
    for (const record of value.records) {
      if (!new RegExp('^' + value.namespace + ':' + uuid + '$').test(record.id) || seen.has(record.id)) throw Error('Overlay namespace/UUID collision');
      seen.add(record.id); checkReferences(record.references);
      // Dataset qualification is retained inside provenance for identities shared across projections.
      // proposed_changes are proposals only; no application to base takes place.
    }
  });
  const project = store(value => {
    const keys = ['schema_version','id','title','base_release_id','base_manifest_sha256','references','workspace'];
    if (!value || typeof value !== 'object' || Array.isArray(value) || Object.keys(value).some(k => !keys.includes(k)) || keys.some(k => !Object.hasOwn(value,k))) throw Error('Invalid project envelope');
    assertEnvelopePin(value);
    if (value.schema_version !== '0.1.0' || !new RegExp('^project:' + uuid + '$').test(value.id) || typeof value.title !== 'string') throw Error('Invalid project identity');
    checkReferences(value.references);
    if (!value.workspace || typeof value.workspace !== 'object' || Array.isArray(value.workspace) || Object.keys(value.workspace).length) throw Error('Project calculations are not implemented; workspace must be empty');
  });
  return Object.freeze({overlay, project});
}

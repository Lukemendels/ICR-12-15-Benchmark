function createQueryProvider(base) {
  if (!Object.isFrozen(base) || base.manifestHash !== PIN.manifest_sha256) throw Error('Verified immutable base required');
  const files = base.files;
  const query = request => deepFreeze(Consumer.query(files, request));
  const source = id => {
    const address = files['indexes/sources.json'][id];
    if (!address) throw Error('Unknown source identity');
    return Consumer.resolve(files, address);
  };
  return Object.freeze({
    id: 'icr-json-index-provider', version: '1.0.0', query,
    portfolio: () => files['tsa/portfolio.json'],
    activities: (ref, page = {}) => query({...page, filters: {package: ref, type: 'ACTIVITY'}}),
    source,
    sourcesFor: record => deepFreeze([...new Set((record.provenance_refs || []).map(id => {
      const observation = files['provenance/observations.json'][id];
      if (!observation) throw Error('Unknown provenance identity');
      return observation.source_id;
    }))].map(source)),
    hydrate: record => deepFreeze(Consumer.hydrate(record, files['provenance/observations.json'])),
    neighbors: (id, type) => files['indexes/adjacency.json'][id]?.[type] || Object.freeze([])
  });
}

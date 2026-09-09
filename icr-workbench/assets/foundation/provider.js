function createQueryProvider(base) {
  if (!verifiedBases.has(base)) throw Error('Verified immutable base required');
  const files = base.files;
  const query = request => deepFreeze(Consumer.query(files, request));
  const source = id => {
    const address = files['indexes/sources.json'][id];
    if (!address) throw Error('Unknown source identity');
    return Consumer.resolve(files, address);
  };
  const sourcesForRecord = record => deepFreeze([...new Set((record.provenance_refs || []).map(id => {
    const observation = files['provenance/observations.json'][id];
    if (!observation) throw Error('Unknown provenance identity');
    return observation.source_id;
  }))].map(source));
  return Object.freeze({
    id: 'icr-json-index-provider', version: '1.0.1', query,
    selectPackage: ref => {
      const record = files['tsa/portfolio.json'].find(p => p.ref === ref);
      if (!record) throw Error('Unknown package/version');
      return record;
    },
    findings: (ref, page = {}) => query({...page, filters: {package: ref, dataset: 'tsa/comparisons.json'}}),
    sourceLinks: record => deepFreeze(sourcesForRecord(record).map(s => ({id: s.id, url: safeSourceURL(s.url)}))),
    portfolio: () => files['tsa/portfolio.json'],
    activities: (ref, page = {}) => query({...page, filters: {package: ref, type: 'ACTIVITY'}}),
    source,
    sourcesFor: sourcesForRecord,
    hydrate: record => deepFreeze(Consumer.hydrate(record, files['provenance/observations.json'])),
    neighbors: (id, type) => files['indexes/adjacency.json'][id]?.[type] || Object.freeze([])
  });
}

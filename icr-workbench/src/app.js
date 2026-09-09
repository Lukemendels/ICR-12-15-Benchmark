(async function () {
  'use strict';
  const F = globalThis.ICRFoundation;
  const main = document.getElementById('workspace');
  const nav = [...document.querySelectorAll('[data-route]')];
  const session = {route: 'home', packageRef: '202406-1652-001', after: null};
  let base, provider, stores;
  const el = (tag, text, cls) => F.textNode(document, tag, text, cls);
  const add = (parent, ...children) => { parent.append(...children); return parent; };
  const section = title => add(el('section', ''), el('h2', title));
  const message = text => el('p', text, 'muted');
  function facts(parent, entries) {
    const dl = el('dl', '');
    entries.forEach(([key, value]) => add(dl, el('dt', key), el('dd', value, key.includes('SHA') ? 'digest' : '')));
    parent.append(dl);
  }
  function details(parent, title, record) {
    parent.append(add(el('details', ''), el('summary', title), el('pre', JSON.stringify(record, null, 2))));
  }
  function status() {
    const s = section('Evidence is ready');
    add(s, el('span', 'Integrity verified · Read only', 'badge'), message('The packaged release passed its pinned digest, inventory, schema and reference checks.'));
    facts(s, [['Workbench version', F.appVersion], ['Evidence release', F.pin.release_id], ['Manifest SHA-256', base.manifestHash], ['Graph version', base.manifest.graph_version], ['TSA packages / recent versions', provider.portfolio().length], ['TSA-local overlay', stores.overlay.snapshot() ? 'Loaded separately' : 'Empty · in memory'], ['Working ICR project', stores.project.snapshot() ? 'Loaded separately' : 'Empty · in memory']]);
    main.append(s);
    main.append(message('Begin in Evidence to select a package, inspect its activity records and follow registered sources. Create / Model and Review are future modules.'));
  }
  function evidence() {
    const s = section('Inspect a TSA package');
    const label = el('label', 'Package / version'); label.htmlFor = 'package-select';
    const select = el('select', ''); select.id = 'package-select';
    provider.portfolio().forEach(p => { const opt = el('option', p.ref + ' · ' + (p.title || p.control || 'Untitled package')); opt.value = p.ref; opt.selected = p.ref === session.packageRef; select.append(opt); });
    select.addEventListener('change', () => {session.packageRef = select.value; session.after = null; render();});
    add(s, label, select);
    const selected = provider.selectPackage(session.packageRef);
    facts(s, [['Selected version', selected.ref], ['Collection', selected.title], ['OMB control', selected.control]]);
    add(s, message('Exact frozen relationships only. Activity representations can overlap; do not sum these records. Missing information is not zero.'));
    main.append(s);
    const page = provider.activities(session.packageRef, {limit: 10, after: session.after});
    const activities = section('Activity records');
    activities.append(message(page.total + ' matching records · up to 10 per page'));
    page.records.forEach(({record}) => {
      const card = el('article', '', 'card');
      add(card, el('h3', record.data.activity || record.id), el('span', record.epistemic_status, 'badge'));
      facts(card, [['Record ID', record.id], ['Representation', record.data.record_kind], ['Actor', record.data.actor], ['Unit', record.data.unit || record.data.population_unit]]);
      provider.sourcesFor(record).forEach(source => add(card, el('p', ''), F.sourceLink(document, source)));
      details(card, 'Normalized record and provenance references', record);
      details(card, 'Resolved provenance', provider.hydrate(record));
      activities.append(card);
    });
    if (!page.records.length) activities.append(message('No matching activity records.'));
    const controls = el('div', '', 'row');
    const first = el('button', 'First page'); first.disabled = session.after === null; first.addEventListener('click', () => {session.after = null; render();});
    const next = el('button', 'Next page'); next.disabled = !page.next; next.addEventListener('click', () => {session.after = page.next; render();});
    add(controls, first, next); activities.append(controls); main.append(activities);
    const findings = section('Published evidence · adjudication register');
    const result = provider.findings(session.packageRef, {limit: 10});
    result.records.forEach(({record}) => {
      const card = el('article', '', 'card');
      add(card, el('h3', record.id), el('span', record.classification, 'badge'));
      details(card, 'Frozen adjudication and limitations', record);
      provider.sourcesFor(record).forEach(source => card.append(F.sourceLink(document, source)));
      findings.append(card);
    });
    if (!result.records.length) findings.append(message('No task/method adjudications indexed for this package. This does not establish consistency or absence of other findings.'));
    findings.append(message(result.total + ' indexed task/method adjudications; showing up to 10.'));
    main.append(findings);
    // Loop 5.3: mount graph visualization here, using provider pages and registered IDs.
  }
  function settings() {
    const s = section('Settings / Release');
    facts(s, [['Application version', F.appVersion], ['Pinned release', F.pin.release_id], ['Pinned manifest SHA-256', F.pin.manifest_sha256], ['Schema / consumer major', F.pin.schema_major + ' / ' + F.pin.consumer_major], ['Graph version', F.pin.tsa_graph], ['Foundation capability', F.capabilityVersion], ['Overlay store', stores.overlay.snapshot() ? 'Loaded' : 'Empty'], ['Project store', stores.project.snapshot() ? 'Loaded' : 'Empty']]);
    add(s, message('Requires a modern browser with Web Crypto and DecompressionStream. Evidence is bundled; opening a public document link uses your network connection.'), message('Overlay and project import/export are separate foundation APIs. No persistence or evidence mutation controls are exposed in this shell.'));
    details(s, 'Evidence pin and compatibility', F.pin); main.append(s);
  }
  function render() {
    main.replaceChildren(); main.setAttribute('aria-busy', 'false');
    nav.forEach(button => {if (button.dataset.route === session.route) button.setAttribute('aria-current', 'page'); else button.removeAttribute('aria-current');});
    if (session.route === 'home') status();
    else if (session.route === 'evidence') evidence();
    else if (session.route === 'settings') settings();
    else {
      const s = section(session.route === 'create' ? 'Create / Model' : 'Review');
      add(s, el('span', 'Module boundary · Not implemented', 'badge'), message(session.route === 'create' ? 'The separate working-project store is ready for a future typed ICR calculation module. No calculations or Items 12–15 text are generated.' : 'A future review module will use explicit evidence and human dispositions. This foundation does not perform comprehensive QA or approve analytical conclusions.'));
      main.append(s);
    }
  }
  nav.forEach(button => {button.disabled = true; button.addEventListener('click', () => {session.route = button.dataset.route; render();});});
  try {
    if (!globalThis.crypto?.subtle || typeof DecompressionStream !== 'function') throw Error('This browser lacks Web Crypto or DecompressionStream. Open the standalone file in a supported modern browser.');
    base = await F.loadAdapter(await F.bundledAdapter());
    provider = F.createQueryProvider(base); stores = F.createStores(base);
    nav.forEach(button => {button.disabled = false;}); render();
  } catch (error) {
    main.replaceChildren(el('h2', 'Evidence unavailable'), el('p', error.message, 'error'), message('No evidence has been exposed. Restore the original pinned package or use a compatible browser.'));
    main.setAttribute('aria-busy', 'false');
  }
})();

# TSA evidence graph schema

JSONL nodes and edges are deterministic projections of reviewed source evidence. Schema enums are in `schema.json`. Stable IDs use entity type plus control/version and source-location identity; content-hashed edges use relationship, endpoints and analytical scope. IDs never depend on extraction order. `ASSUMPTION_FAMILY` and `MEMBER_OF` support recurring family queries.

Every substantive node/edge contains `provenance`: source ID, public document identity, exact text-line or table/row/paragraph locator, original evidence, extraction method, transformation and epistemic status. `data` retains normalized value, unit, period, vintage and scope; unknowns are null with a reason. SOURCE records may reference unchanged Mission 1 sources and canonical paths. Administrative metadata is not evidence of activity methods.

`PUBLISHED` means directly transcribed source content; `NORMALIZED` means an explicit unit or vocabulary transformation; `CALCULATED` means a replayable expression; `INFERRED` means analytical judgment; `UNRESOLVED` means the public evidence does not settle the assertion. These are independent of classification and confidence. A retrieved row is not automatically a validated model.

Reserved ontology entries are permitted but are instantiated only for observed distinctions. Shape comparison edges require shared/differing features, purpose, strength and caveats. A future tool must filter by document version and query completeness; it must never treat absent extracted evidence as a published zero.

# Decision Log

## D-001 Preserve exact requested plant inventory
Status: ACCEPTED
Reason: user explicitly wants this exact garden rather than a generic optimized replacement.

## D-002 Do not lock physical coordinates before site geometry
Status: ACCEPTED
Reason: exact layout without dimensions/sun map would create false precision.

## D-003 Separate permanent crops
Status: ACCEPTED
Applies to: asparagus, rhubarb, roses, durable perennial ornamentals.
Reason: avoid disrupting annual rotation and reconfiguration.

## D-004 Split herbs by water/drainage need
Status: ACCEPTED
Reason: “herbs” are not a valid irrigation hydrozone.

## D-005 Keep software optional and portable
Status: ACCEPTED
Canonical truth starts in human-readable files + structured CSV/JSON. Automation layers must be detachable.

## D-006 Red rose theme remains dominant
Status: ACCEPTED
One optional white backyard rose is allowed; no other rose color creep without explicit user change.

## D-007 Do not build a monolithic custom garden application yet
Status: ACCEPTED
Reason: open-source tools already cover much of mapping, journaling, tasks, inventory, exports, weather, APIs, and automation. The project should validate those tools against the real garden before paying the complexity cost of custom software.

## D-008 Jninty becomes the leading operations-layer candidate
Status: PROVISIONAL ACCEPTED
Reason: current local-first/offline PWA architecture covers journal, task rules, planting calendar, seed bank, expenses, maps, season comparison, ZIP backup/restore and optional sync under an MIT license.
Gate before adoption: test real Garden OS data portability and workflow friction.

## D-009 Open Garden Planner becomes the leading precision-map candidate
Status: PROVISIONAL ACCEPTED
Reason: calibrated CAD-like geometry, garden-specific objects, standard exports, plant metadata and MCP integration map closely to site-layout requirements.
Gate before adoption: actual property dimensions/photos and a sample scaled plan.

## D-010 OpenPlantDB may seed generic machine-readable plant fields, but not override local evidence
Status: ACCEPTED
Reason: CC0 flat-file data is highly reusable, but generic ranges vary by cultivar, region, and microclimate. Kentucky Extension/cultivar-specific evidence and actual garden observations remain higher authority.

## D-011 Cultivars are shortlisted, not locked
Status: ACCEPTED
Reason: cultivar decisions require exact site conditions, availability and user flavor/style preferences. `31_CULTIVAR_MATRIX_PROVISIONAL.md` records candidates without falsifying certainty.

## D-012 Daily operation becomes reason-exposing, not schedule-obeying
Status: ACCEPTED
Reason: watering/treatment tasks must explain biological evidence such as soil moisture, weather, plant stage or observed disease rather than asserting that elapsed time alone creates a need.

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
Reason: open-source tools already cover much of mapping, journaling, tasks, inventory, exports, weather, APIs, and automation.

## D-008 Jninty becomes the leading operations-layer candidate
Status: PROVISIONAL ACCEPTED
Reason: current local-first/offline PWA architecture covers journal, task rules, planting calendar, seed bank, expenses, maps, season comparison, ZIP backup/restore and optional sync under an MIT license.

## D-009 Open Garden Planner becomes the leading precision-map candidate
Status: PROVISIONAL ACCEPTED
Reason: calibrated CAD-like geometry, garden-specific objects, standard exports, plant metadata and MCP integration map closely to site-layout requirements.

## D-010 OpenPlantDB may seed generic machine-readable plant fields, but not override local evidence
Status: ACCEPTED
Reason: CC0 flat-file data is highly reusable, but generic ranges vary by cultivar, region, and microclimate.

## D-011 Cultivars are shortlisted, not locked
Status: ACCEPTED
Reason: cultivar decisions require exact site conditions, availability and user flavor/style preferences.

## D-012 Daily operation becomes reason-exposing, not schedule-obeying
Status: ACCEPTED
Reason: watering/treatment tasks must explain biological evidence such as soil moisture, weather, plant stage or observed disease rather than elapsed time alone.

## D-013 Site location becomes Richmond, Kentucky / Madison County
Status: SITE CONFIRMED
Date: 2026-09-05
Reason: user directly confirmed Richmond, Kentucky.
Consequence: northern-Kentucky assumptions are superseded.

## D-014 Property scale becomes approximately two acres
Status: SITE CONFIRMED
Date: 2026-09-05
Reason: user directly confirmed a two-acre yard.

## D-015 Do not cultivate the whole two acres by default
Status: SUPERSEDED BY D-019
Reason: this was the first safeguard against over-expansion. The user later specified a quarter-acre garden, which is now the stronger boundary.

## D-016 Use a maintenance-gradient masterplan
Status: MODIFIED BY D-019
Reason: the useful principle remains compact daily walking, but the old multi-ring two-acre architecture is superseded. The new design concentrates nearly all managed garden functions inside one quarter-acre campus.

## D-017 Design perennials conservatively across the Richmond 6b–7a transition until parcel location is pinned
Status: ACCEPTED
Reason: city/ZIP-scale sources place Richmond/Madison County across USDA 2023 Zones 6b and 7a.

## D-018 Exploit Madison County soil-testing capacity
Status: ACCEPTED
Reason: Madison County Extension currently advertises free soil testing for residents, up to 10 samples per home/farm per calendar year.

## D-019 Garden footprint becomes approximately one quarter acre
Status: SITE/DESIGN CONFIRMED
Date: 2026-09-05
Reason: user explicitly requested an average-scale garden using approximately one quarter acre rather than treating the 2-acre yard as the garden.
Locked area: **10,890 sq ft**.
Consequence: all primary garden functions should fit within this envelope unless expansion is explicitly requested later.

## D-020 Remaining property is ordinary yard/open space
Status: ACCEPTED
Date: 2026-09-05
Reason: the user asked not to make the full two acres garden.
Consequence: approximately 1.75 acres remain outside the Garden OS cultivated footprint by default.

## D-021 Add an enclosed greenhouse inside the quarter-acre garden
Status: ACCEPTED
Date: 2026-09-05
Reason: user explicitly requested a decent-size inside greenhouse.
Interpretation: a real enclosed greenhouse located within the quarter-acre garden footprint, not merely a temporary row cover or distant accessory.

## D-022 Default greenhouse size is 16 × 24 ft
Status: PROVISIONAL DESIGN LOCK
Date: 2026-09-05
Reason: this provides a substantial but still normal residential greenhouse (~384 sq ft), suitable for propagation, season extension, protected crops, potting, and overwintering experiments without consuming an excessive share of the quarter acre.
Consequence: exact model/materials/orientation remain site-dependent, but planning should reserve this footprint.

## D-023 Greenhouse is not assumed to be fully heated year-round
Status: ACCEPTED
Date: 2026-09-05
Reason: Kentucky greenhouse heating can be costly while summer ventilation/cooling is also critical.
Consequence: prioritize excellent ventilation, sun, water, drainage, and optional frost-protection heating; full winter heating requires a crop/use justification.

## D-024 Use a hybrid bed system
Status: ACCEPTED
Date: 2026-09-05
Reason: building the entire quarter acre as raised beds would be expensive and unnecessary.
Consequence: use raised beds selectively for high-frequency/access/drainage/soil-control areas and in-ground beds for potatoes, pumpkins/squash, large cutting-flower blocks, and broader rotations where appropriate.

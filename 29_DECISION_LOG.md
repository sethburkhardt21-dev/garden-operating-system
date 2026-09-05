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

## D-013 Site location becomes Richmond, Kentucky / Madison County
Status: SITE CONFIRMED
Date: 2026-09-05
Reason: user directly confirmed Richmond, Kentucky.
Consequence: northern-Kentucky assumptions are superseded. Future local research should prioritize Madison County Extension and Central/Eastern Kentucky guidance.

## D-014 Property scale becomes approximately two acres
Status: SITE CONFIRMED
Date: 2026-09-05
Reason: user directly confirmed a two-acre yard.
Consequence: the design no longer needs to solve every conflict by extreme spatial compression. Permanent crops, pumpkins, rotation blocks, roses, and flower areas can receive dedicated space.

## D-015 Do not cultivate the whole two acres by default
Status: ACCEPTED
Reason: land availability is not the same as maintainable garden capacity. High-maintenance crops should stay in a compact core near house/water; lower-frequency/permanent/sprawling features may sit farther out.

## D-016 Use a maintenance-gradient masterplan
Status: ACCEPTED
Architecture:
- Ring 0: near-house herbs/containers/high-frequency convenience
- Ring 1: kitchen garden / daily harvest
- Ring 2: permanent edible + ornamental garden rooms
- Ring 3: potatoes, garlic, pumpkins/squash, rotation/expansion
- Ring 4: low-frequency ecological/visual edge
Reason: this preserves two-acre capability without creating excessive daily walking and hose friction.

## D-017 Design perennials conservatively across the Richmond 6b–7a transition until parcel location is pinned
Status: ACCEPTED
Reason: city/ZIP-scale sources place Richmond/Madison County across USDA 2023 Zones 6b and 7a. Exact parcel and microclimate remain unknown.
Consequence: prefer permanent plants hardy to 6b where practical; zone is not used as a substitute for frost/planting-date data.

## D-018 Exploit Madison County soil-testing capacity
Status: ACCEPTED
Reason: Madison County Extension currently advertises free soil testing for residents, up to 10 samples per home/farm per calendar year.
Consequence: sample candidate vegetable, perennial, rose/flower, dry-herb, and problem drainage zones separately rather than averaging the two-acre property into one sample.

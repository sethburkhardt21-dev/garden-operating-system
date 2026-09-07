# Decision Log

## D-001 Preserve exact requested plant inventory
Status: ACCEPTED
Reason: user explicitly wants this exact garden rather than a generic optimized replacement.

## D-002 Do not lock physical coordinates before site geometry
Status: MODIFIED BY D-025
Reason: false precision is still prohibited for the real parcel, but an average normalized design coordinate system is now intentionally allowed so the project can continue without waiting for a survey.

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

## D-025 Adopt a normalized 90 × 121 ft default quarter-acre blueprint
Status: ACCEPTED DEFAULT
Date: 2026-09-07
Reason: the user asked for an average design rather than waiting for exact property geometry.
Consequence:
- Garden OS now has a canonical design canvas of exactly 10,890 sq ft.
- southwest is `(0,0)`; east is +x; north is +y.
- the blueprint may be rotated, mirrored, or translated onto the actual property later.
- real parcel coordinates remain provisional until surveyed.

## D-026 Place the greenhouse toward the north side of the default blueprint
Status: ACCEPTED DEFAULT
Date: 2026-09-07
Reason: this preserves convenient access while reducing avoidable shade over primary outdoor production areas.
Default design coordinates: approximately `x=6–22`, `y=93–117`.
Consequence: actual property sun/wind/water conditions may move it, but north-side siting is the baseline.

## D-027 Greenhouse propagation outranks permanent protected production
Status: ACCEPTED
Date: 2026-09-07
Reason: the greenhouse exists primarily to support the entire quarter-acre garden.
Priority order:
1. propagation
2. transplant staging/hardening support
3. shoulder-season production
4. selected protected crops
5. overwintering experiments
6. storage
Consequence: do not fill February–May bench space with permanent fruiting crops or clutter.

## D-028 Use normal first-year crop quantities despite available space
Status: ACCEPTED DEFAULT
Date: 2026-09-07
Reason: the user requested an average garden rather than maximum quarter-acre production.
Examples:
- 6 tomatoes total
- 6 bell peppers
- 3 jalapeños
- 3 eggplants
- 2–3 English cucumbers
- 2 pumpkin plants/hills
- modest squash allocation
- 6–8 spring + 6–8 fall cabbage
- 40–80 garlic cloves
- 15–24 asparagus crowns
- 2–3 rhubarb crowns
Consequence: unused capacity is reserve/airflow/succession/beauty, not an error.

## D-029 Use four annual rotation blocks plus high-frequency kitchen beds
Status: MODIFIED BY D-031
Date: 2026-09-07
Reason: this balances easy daily access with useful crop-family history.
Original default used conceptual ~12 × 24 ft rotation blocks, but v0.6 reconciles their geometry.

## D-030 Build infrastructure in dependency order
Status: ACCEPTED
Date: 2026-09-07
Canonical sequence:
`SITE → WATER/DRAINAGE → GREENHOUSE → PRIMARY PATHS → PERMANENT BEDS → IRRIGATION → ANNUAL BEDS → TRELLISES → FLOWERS/ROSES → POLISH`
Reason: minimize expensive rework and avoid burying utilities after finished beds/paths are installed.

## D-031 Reconcile the rotation field as four 16 × 16 ft blocks
Status: ACCEPTED DEFAULT
Date: 2026-09-07
Reason: v0.5's four ~12 × 24 ft blocks exceeded the previously assigned single rotation-zone geometry. The average garden does not need oversized rotation blocks for the normal first-year crop quantities.
Consequence:
- R1–R4 are each 16 × 16 ft.
- total active rotation soil = 1,024 sq ft.
- the combined east-middle rotation/flex field is approximately `x=47–86`, `y=37–77`.
- `45_VISUAL_MASTERPLAN_AND_BED_GRID.md` is the bed-level geometry authority.

## D-032 Use a matched red-rose entrance pair plus one red transition focal by default
Status: ACCEPTED DEFAULT
Date: 2026-09-07
Reason: this satisfies the user's classic red-rose direction while creating formal structure without turning the garden into a rose collection.
Consequence:
- default minimum = 3 red roses
- up to 5 red roses may be used through repetition
- optional white rose remains 0–1 and backyard only
- cultivar remains provisional pending current/local performance and availability review

## D-033 Treat historical Kentucky rose resistance lists as candidate evidence, not guarantees
Status: ACCEPTED
Date: 2026-09-07
Reason: older Kentucky/multi-state trials provide useful candidate names, but black-spot reactions vary by location/pathogen population and rose rosette can affect highly resistant roses.
Consequence:
- classic red historical candidates such as Mister Lincoln and Olympiad may be shortlisted
- no cultivar is labeled disease-proof or no-spray solely from older data
- actual Richmond performance becomes `OBSERVED IN THIS GARDEN` evidence after planting

## D-034 Size greenhouse summer ventilation from greenhouse volume, not floor area alone
Status: ACCEPTED DESIGN METHOD
Date: 2026-09-07
Reason: current UK guidance uses approximately one greenhouse volume per minute at an effective 8–10 ft height for summer ventilation.
Consequence for 16 × 24 ft structure:
- planning target ≈ 3,100–3,900 CFM effective installed summer exhaust capacity
- final fans/intakes must be verified against selected structure, free-air intake, screens/shutters, and manufacturer system losses
- circulation fans are separate from exhaust capacity

## D-035 Use independently controllable irrigation hydrozones and measured source hydraulics
Status: ACCEPTED
Date: 2026-09-07
Reason: the quarter-acre plan contains incompatible water needs and Kentucky drip guidance emphasizes filtration, pressure regulation, zoning, and real system sizing.
Default zones:
- Z1 kitchen Solanaceae
- Z2 cucumber/cabbage/moist herbs
- Z3 rotation blocks
- Z4 permanent moist edibles
- Z5 dry herbs
- Z6 roses/flowers
- Z7 greenhouse
- Z8 sprawling/flex
Consequence: runtime is calibrated from soil wetting and weather/plant evidence; a timer schedule never proves water is biologically needed.

## D-036 Create a bed-level machine-readable and visual masterplan
Status: ACCEPTED
Date: 2026-09-07
Reason: the project now has enough normalized geometry to support exact default modules without pretending the real parcel has been surveyed.
Canonical companions:
- `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
- `data/bed_inventory_v0_6.csv`
- `docs/default_quarter_acre_masterplan.svg`
Consequence: later site fitting should transform these coordinates rather than rebuild the garden architecture from zero.

# Garden Operating System — v0.5

**Status:** RICHMOND SITE CONFIRMED / QUARTER-ACRE GARDEN LOCKED / GREENHOUSE LOCKED / DEFAULT BLUEPRINT + 2027 OPERATING PLAN CREATED  
**Updated:** 2026-09-07  
**Purpose:** Turn the exact requested plant list into a living, research-backed system for planning, growing, maintaining, diagnosing, harvesting, beautifying, and improving this specific Richmond, Kentucky garden year after year.

## Site truth now locked

- **Location:** Richmond, Kentucky / Madison County
- **Yard:** approximately 2 acres
- **Actual Garden OS footprint:** approximately **1/4 acre = 10,890 sq ft**
- **Remaining ~1.75 acres:** ordinary yard/open space unless explicitly expanded later
- **Default garden blueprint:** **90 × 121 ft** normalized rectangle
- **Greenhouse:** real enclosed greenhouse inside the quarter-acre footprint
- **Default greenhouse:** **16 × 24 ft = 384 sq ft**
- Requested plant inventory remains preserved.
- Red roses remain the dominant rose theme; one optional white backyard rose remains the only exception.
- Wildflower tub remains separate.
- Asparagus/rhubarb remain permanent edible infrastructure.
- Herbs remain split by moisture/drainage need.
- Canonical garden truth remains portable Markdown + CSV + JSON.

## What v0.5 adds

The project no longer stops at an area budget. It now has a default buildable blueprint and a first-year operating model.

### Physical blueprint
`40_DEFAULT_QUARTER_ACRE_LAYOUT.md`
- exact 90 × 121 ft normalized coordinate system
- north-up default plan
- greenhouse placed toward the north side
- central cart spine
- kitchen garden
- permanent edible/herb areas
- rotation blocks
- flex pumpkin/squash/potato/garlic zone
- cutting/rose garden
- machine-readable coordinates in `data/default_layout_zones.csv`

The whole plan can later be rotated, mirrored, or translated onto the best real part of the yard.

### Greenhouse operating system
`41_GREENHOUSE_OPERATING_SYSTEM.md`
- propagation-first mission hierarchy
- ventilation/cooling sequence
- frost-protection modes
- humidity/condensation logic
- watering
- summer/winter operating modes
- hardening workflow
- greenhouse pest/disease biosecurity
- power/fan/heater/water failure playbooks

### 2027 propagation calendar
`42_2027_SEED_START_AND_SUCCESSION.md`
- peppers/eggplant: late Feb–early Mar default
- tomatoes: mid/late March
- cucumber/squash/pumpkin: short April starts if not direct-sown
- spring/fall cabbage timing
- herbs and flower starts
- greenhouse bench-capacity logic
- succession rules

### 2027 bed + rotation plan
`43_2027_BED_ASSIGNMENT_AND_ROTATION.md`
- normal first-year crop quantities
- kitchen-bed assignments
- four annual rotation blocks
- 2027–2030 family-rotation framework
- permanent asparagus/rhubarb/herb areas
- pumpkin/squash/potato/garlic flex plan
- flower/rose groupings
- machine-readable crop plan in `data/2027_crop_plan.csv`

### Infrastructure sequence
`44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md`

Build order is now:

**SITE → WATER/DRAINAGE → GREENHOUSE → PRIMARY PATHS → PERMANENT BEDS → IRRIGATION → ANNUAL BEDS → TRELLISES → FLOWERS/ROSES → POLISH**

This prevents buried utilities, greenhouse service, or paths from being added after finished beds are already in the way.

## Quarter-acre area budget

See `39_QUARTER_ACRE_GARDEN_PROGRAM.md`.

Planning allocation:
- greenhouse — 384 sq ft
- annual edible production — ~2,700 sq ft
- permanent edible + herbs — ~1,200 sq ft
- roses + flowers — ~1,800 sq ft
- pumpkin/squash/potato/garlic/flex — ~1,200 sq ft
- paths/work/compost/irrigation — ~1,800 sq ft
- buffer/pollinator/future adjustment — ~1,806 sq ft

Total = **10,890 sq ft**.

These are planning envelopes, not density targets. Airflow, reserve ground, succession, paths, and work space are legitimate uses of the quarter acre.

## Default 2027 crop scale

The first year stays intentionally normal rather than exploiting every available square foot:
- tomatoes: 6 total across heirloom/beefsteak/cherry
- bell peppers: 6
- jalapeños: 3
- eggplant: 3
- English cucumber: 2–3
- squash: 2 summer or 1–2 winter until type resolved
- pumpkin: 2 plants/hills
- cabbage: 6–8 spring + 6–8 fall
- garlic: 40–80 cloves
- potatoes: two modest 20–30 ft row allocations
- asparagus: 15–24 crowns
- rhubarb: 2–3 crowns
- red roses: 3–5
- dahlias: 8–12
- other flowers: grouped/drifted rather than one-of-each

The greenhouse does **not** automatically double outdoor plant counts.

## Greenhouse direction

The 16 × 24 ft greenhouse remains a propagation/work/season-extension structure first.

Default mission order:
1. propagation for outdoor garden
2. transplant staging/hardening support
3. shoulder-season crops
4. selected protected crops
5. overwintering experiments
6. storage

It is not assumed to be fully heated all winter.

## Richmond-specific research integrated

- Madison County Extension is the primary local Extension reference.
- Madison County currently advertises free resident soil testing, up to 10 samples per home/farm per calendar year.
- Richmond/Madison sits around the USDA 2023 6b–7a transition at coarse scale; exact parcel half-zone remains to be pinned.
- Kentucky Central/Eastern planting windows replace the superseded northern-Kentucky assumption.
- Kentucky greenhouse guidance informs heating/ventilation/cooling design.

## What remains provisional

The project now has an average blueprint, so work can continue without waiting. The real-world plan can later improve when these are known:
- exact quarter-acre placement within the property
- house/driveway geometry
- north on the real parcel
- mature trees/shade
- slopes/wet areas
- water/hose locations
- septic/utilities/no-dig zones
- wildlife pressure
- soil-test results

Until then, **90 × 121 ft north-up** is the canonical design canvas.

## Start here

1. `00_START_HERE.md` — current state and execution order.
2. `40_DEFAULT_QUARTER_ACRE_LAYOUT.md` — default physical blueprint.
3. `39_QUARTER_ACRE_GARDEN_PROGRAM.md` — scale/area program.
4. `38_GREENHOUSE_PLAN.md` — greenhouse structure/role.
5. `41_GREENHOUSE_OPERATING_SYSTEM.md` — greenhouse daily control logic.
6. `42_2027_SEED_START_AND_SUCCESSION.md` — first full propagation calendar.
7. `43_2027_BED_ASSIGNMENT_AND_ROTATION.md` — first-year crop/rotation plan.
8. `44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md` — build order and infrastructure.
9. `37_FALL_2026_RICHMOND_ACTION_PLAN.md` — current implementation work.
10. `02_SITE_PROFILE.md` — confirmed site truth.
11. `34_RICHMOND_KY_SITE_BASELINE.md` — local climate/Extension baseline.
12. `36_2027_PLANT_COUNT_AND_SPACE_MODEL.md` — sizing rationale.
13. `04_PLANT_MASTER_LEDGER.csv` — canonical requested inventory.
14. `05_PLANT_PROFILES/` — care profiles.
15. `06_ANNUAL_CALENDAR_PROVISIONAL.md` — Richmond calendar.
16. `31_CULTIVAR_MATRIX_PROVISIONAL.md` — cultivar shortlist.
17. `32_TODAY_ENGINE.md` — daily operating logic.
18. `09_SOIL_PLAN.md` / `10_IRRIGATION_PLAN.md` — soil/water infrastructure.
19. `12_PEST_IPM.md` / `13_DISEASE_PLAYBOOK.md` — health management.
20. `25_STYLE_UPGRADES.md` — visual system.
21. `27_GITHUB_REUSE_AUDIT.md` — software reuse.
22. `28_RESEARCH_LEDGER.md` — evidence ledger.
23. `29_DECISION_LOG.md` — accepted/superseded decisions.
24. `30_OPEN_QUESTIONS.md` — remaining refinements.

## Human operating principle

Deep detail belongs in the repository. Daily operation collapses to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Hard boundary rule

Do not let future work quietly turn the remaining 1.75 acres into more garden. Expansion requires an explicit user decision.

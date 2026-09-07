# Garden Operating System — v0.6

**Status:** RICHMOND SITE CONFIRMED / QUARTER-ACRE GARDEN LOCKED / GREENHOUSE LOCKED / BED-LEVEL BLUEPRINT + SYSTEM SPECS CREATED  
**Updated:** 2026-09-07  
**Purpose:** Turn the exact requested plant list into a living, research-backed system for planning, building, growing, maintaining, diagnosing, harvesting, beautifying, and improving this specific Richmond, Kentucky garden year after year.

## Site truth now locked

- **Location:** Richmond, Kentucky / Madison County
- **Yard:** approximately 2 acres
- **Actual Garden OS footprint:** approximately **1/4 acre = 10,890 sq ft**
- **Remaining ~1.75 acres:** ordinary yard/open space unless explicitly expanded later
- **Default garden blueprint:** **90 × 121 ft** normalized rectangle
- **Greenhouse:** enclosed 16 × 24 ft greenhouse inside the quarter-acre footprint
- Requested plant inventory remains preserved.
- Red roses remain the dominant rose theme; one optional white backyard rose remains the only exception.
- Wildflower tub remains separate.
- Asparagus/rhubarb remain permanent edible infrastructure.
- Herbs remain split by moisture/drainage need.
- Canonical garden truth remains portable Markdown + CSV + JSON.

## What v0.6 adds

v0.5 established the average blueprint and first-year operating plan. v0.6 resolves the geometry down to beds and turns several design concepts into engineering/procurement specifications.

### 1. Bed-level masterplan
`45_VISUAL_MASTERPLAN_AND_BED_GRID.md`

Adds:
- exact default K01–K08 kitchen-bed coordinates
- exact P01/P02/P03 permanent areas
- exact R1–R4 rotation block coordinates
- exact FL01–FL03 flower blocks
- pumpkin/flex geometry
- default red-rose focal positions
- path relationships

Companions:
- `data/bed_inventory_v0_6.csv`
- `docs/default_quarter_acre_masterplan.svg`

### 2. Rotation geometry corrected
v0.5's conceptual four ~12 × 24 ft rotation blocks did not fit the earlier single rotation envelope.

v0.6 makes the actual canonical rotation field:
- **four 16 × 16 ft blocks**
- **1,024 sq ft total active rotation soil**
- inside the combined east-middle rotation/flex field

This is ample for the intentionally normal first-year crop scale.

### 3. Rose + flower design
`46_ROSE_AND_FLOWER_DESIGN.md`

Adds:
- matched red-rose entrance pair + one red transition focal as the default structure
- 3–5 red roses total, not a giant rose garden
- historical Kentucky black-spot-resistance evidence treated as candidate evidence rather than guarantees
- classic-red candidates such as Mister Lincoln/Olympiad for further current/local validation
- dahlia/zinnia/cosmos/perennial drift composition
- cool-season and warm-season flower sequence
- conditional handling for lupines, daisies, geraniums, and impatiens

### 4. Greenhouse equipment specification
`47_GREENHOUSE_EQUIPMENT_SPEC.md`

The 16 × 24 ft greenhouse now has a real functional specification:
- structure/anchoring requirements
- ventilation/intake design
- circulation fans
- shade strategy
- heating modes
- electrical/water requirements
- benches and interior zones
- propagation capacity
- failure playbooks

Current UK greenhouse guidance supports a summer ventilation planning target of roughly one greenhouse volume per minute. For this greenhouse, that yields approximately **3,100–3,900 CFM effective installed exhaust capacity**, subject to final structure and system-loss verification.

### 5. Irrigation hydraulics
`48_IRRIGATION_ZONE_SIZING.md`

Adds:
- source GPM/pressure measurement gate
- filter/regulator/gauge/manifold architecture
- eight default hydrozones
- emitter/dripline flow formulas
- commissioning by observed wetting depth/width
- greenhouse and dry-herb independent zones
- rain override and flow-anomaly logic

Worksheet:
- `data/irrigation_zone_template.csv`

### 6. Procurement control
`49_MATERIALS_AND_PROCUREMENT_REGISTER.md`

Separates:
- BUY NOW
- BUY AFTER SITE FIT
- BUY AFTER MODEL SELECTED
- WINTER ORDER
- SPRING BUY
- OPTIONAL
- DO NOT BUY YET

The goal is to prevent high-cost rework from premature greenhouse, irrigation, path, or bed purchases.

### 7. Master implementation checklist
`50_2026_2027_MASTER_CHECKLIST.md`

Single dependency-ordered checklist from September 2026 through first-season commissioning in 2027.

---

## Canonical physical design

The default canvas is 90 × 121 ft, north-up:

**south entrance / red roses → flower foreground → rotation/flex → kitchen garden → greenhouse/work hub**

The entire design may later be rotated, mirrored, or translated onto the best real quarter-acre part of the 2-acre yard.

Do not quietly expand beyond the quarter acre.

---

## Default 2027 crop scale

The first year remains intentionally normal:
- tomatoes: 6 total across heirloom/beefsteak/cherry
- bell peppers: 6
- jalapeños: 3
- eggplant: 3
- English cucumber: 2–3
- squash: 2 summer or 1–2 winter until resolved
- pumpkin: 2 plants/hills
- cabbage: 6–8 spring + 6–8 fall
- garlic: 40–80 cloves
- potatoes: two modest cultivar allocations
- asparagus: 15–24 crowns
- rhubarb: 2–3 crowns
- red roses: 3–5
- dahlias: 8–12
- zinnias: roughly 24–36 across one or two successions
- cosmos: roughly 10–16

Reserve soil, airflow, access, flower massing, and succession space are intentional uses of the quarter acre.

---

## Greenhouse direction

Default mission order:
1. propagation for the outdoor garden
2. transplant staging/hardening support
3. shoulder-season production
4. selected protected crops
5. overwintering experiments
6. storage

The greenhouse is **not** assumed to be fully heated all winter.

Summer overheating is treated as a first-order design risk, not an afterthought.

---

## Irrigation direction

Default independent hydrozones:
- Z1 kitchen Solanaceae
- Z2 cucumber/cabbage/moist herbs
- Z3 rotation blocks
- Z4 permanent moist edibles
- Z5 dry herbs
- Z6 roses/flowers
- Z7 greenhouse
- Z8 sprawling/flex

A timer schedule does not prove plants need water. Source hydraulics are measured; runtime is calibrated from soil wetting, weather, and plant stage.

---

## Richmond-specific research integrated

Primary evidence remains University of Kentucky / Madison County Extension where available.

Integrated topics include:
- Richmond/Madison hardiness context
- Kentucky planting windows
- garlic
- asparagus/rhubarb
- tomato/pepper/cucurbit disease pressure
- rose black spot and rose rosette
- greenhouse structure/heating/cooling/ventilation
- drip irrigation architecture
- open-source garden software/data reuse

See `28_RESEARCH_LEDGER.md`.

---

## What remains provisional

The system can continue without these, but real-world siting improves when known:
- exact quarter-acre placement within the 2-acre property
- mature-tree shade
- water-source flow/pressure and route
- slopes/wet areas
- septic/utilities/no-dig zones
- soil-test results
- wildlife pressure
- final greenhouse manufacturer/model
- several plant cultivar/type choices

Until then, the normalized v0.6 design is the current source of truth.

---

## Start here

1. `00_START_HERE.md`
2. `50_2026_2027_MASTER_CHECKLIST.md`
3. `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
4. `docs/default_quarter_acre_masterplan.svg`
5. `40_DEFAULT_QUARTER_ACRE_LAYOUT.md`
6. `39_QUARTER_ACRE_GARDEN_PROGRAM.md`
7. `38_GREENHOUSE_PLAN.md`
8. `41_GREENHOUSE_OPERATING_SYSTEM.md`
9. `47_GREENHOUSE_EQUIPMENT_SPEC.md`
10. `48_IRRIGATION_ZONE_SIZING.md`
11. `49_MATERIALS_AND_PROCUREMENT_REGISTER.md`
12. `42_2027_SEED_START_AND_SUCCESSION.md`
13. `43_2027_BED_ASSIGNMENT_AND_ROTATION.md`
14. `46_ROSE_AND_FLOWER_DESIGN.md`
15. `44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md`
16. `37_FALL_2026_RICHMOND_ACTION_PLAN.md`
17. `04_PLANT_MASTER_LEDGER.csv`
18. `05_PLANT_PROFILES/`
19. `31_CULTIVAR_MATRIX_PROVISIONAL.md`
20. `06_ANNUAL_CALENDAR_PROVISIONAL.md`
21. `32_TODAY_ENGINE.md`
22. `09_SOIL_PLAN.md`
23. `10_IRRIGATION_PLAN.md`
24. `12_PEST_IPM.md`
25. `13_DISEASE_PLAYBOOK.md`
26. `25_STYLE_UPGRADES.md`
27. `27_GITHUB_REUSE_AUDIT.md`
28. `28_RESEARCH_LEDGER.md`
29. `29_DECISION_LOG.md`
30. `30_OPEN_QUESTIONS.md`

## Human operating principle

Deep detail belongs in the repository. Daily operation collapses to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Hard boundary rule

The Garden OS stops at approximately one quarter acre unless the user explicitly changes that decision.

# Garden Operating System — START HERE — v0.6

**Status:** RICHMOND CONFIRMED / QUARTER-ACRE GARDEN LOCKED / BED-LEVEL MASTERPLAN + GREENHOUSE/IRRIGATION SPECS CREATED  
**Updated:** 2026-09-07

## Current truth

Site-confirmed:
- Richmond, Kentucky / Madison County
- approximately 2-acre residential yard
- actual Garden OS limited to approximately **1/4 acre = 10,890 sq ft**
- decent-size enclosed greenhouse inside the garden

Canonical normalized design:
- **90 × 121 ft** quarter-acre rectangle
- southwest origin `(0,0)`
- north-up default
- entire design can later be rotated/mirrored onto the real parcel

Default greenhouse:
- **16 × 24 ft = 384 sq ft**
- north-side operational hub by default

Remaining ~1.75 acres stay ordinary yard/open space unless explicitly expanded later.

The exact requested plant list remains preserved in `04_PLANT_MASTER_LEDGER.csv`.

---

# What changed in v0.6

## Exact default bed map now exists
Open:
- `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
- `docs/default_quarter_acre_masterplan.svg`
- `data/bed_inventory_v0_6.csv`

The garden now has default coordinates for:
- K01–K08 kitchen beds
- R1–R4 rotation blocks
- P01/P02/P03 permanent areas
- FL01–FL03 flower blocks
- F01 pumpkin/flex area
- rose entrance/focal points
- primary paths

## Rotation geometry corrected
The four old conceptual ~12 × 24 ft rotation blocks are superseded.

Current default:
- four **16 × 16 ft** blocks
- total active rotation soil = **1,024 sq ft**

## Rose/flower composition now exists
`46_ROSE_AND_FLOWER_DESIGN.md`

Default structure:
- matched red entrance pair
- one red transition/path focal
- 3–5 red roses total
- optional white rose remains 0–1, backyard only
- flowers are massed/drifted rather than one-of-each

## Greenhouse equipment specification now exists
`47_GREENHOUSE_EQUIPMENT_SPEC.md`

Current summer exhaust planning target:
- approximately **3,100–3,900 CFM effective installed capacity**
- final hardware still depends on selected structure/intake/system losses

## Irrigation is now hydraulically designable
`48_IRRIGATION_ZONE_SIZING.md`

Eight default hydrozones exist, plus:
- source GPM/pressure measurement
- filter/regulator/gauge/manifold architecture
- commissioning by observed wetting depth/width
- greenhouse and dry-herb independent zones

Worksheet:
- `data/irrigation_zone_template.csv`

## Procurement is staged
`49_MATERIALS_AND_PROCUREMENT_REGISTER.md`

Do not buy greenhouse foundations, final fans, bulk irrigation tubing, roses, or path materials before their dependency gates close.

## One implementation checklist now controls the build
`50_2026_2027_MASTER_CHECKLIST.md`

Use it as the top-level execution list from now through first-season commissioning.

---

# Execute in this order

1. `50_2026_2027_MASTER_CHECKLIST.md`
2. `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
3. `docs/default_quarter_acre_masterplan.svg`
4. `40_DEFAULT_QUARTER_ACRE_LAYOUT.md`
5. `39_QUARTER_ACRE_GARDEN_PROGRAM.md`
6. `47_GREENHOUSE_EQUIPMENT_SPEC.md`
7. `38_GREENHOUSE_PLAN.md`
8. `41_GREENHOUSE_OPERATING_SYSTEM.md`
9. `48_IRRIGATION_ZONE_SIZING.md`
10. `49_MATERIALS_AND_PROCUREMENT_REGISTER.md`
11. `44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md`
12. `37_FALL_2026_RICHMOND_ACTION_PLAN.md`
13. `42_2027_SEED_START_AND_SUCCESSION.md`
14. `43_2027_BED_ASSIGNMENT_AND_ROTATION.md`
15. `46_ROSE_AND_FLOWER_DESIGN.md`
16. `02_SITE_PROFILE.md`
17. `34_RICHMOND_KY_SITE_BASELINE.md`
18. `36_2027_PLANT_COUNT_AND_SPACE_MODEL.md`
19. `04_PLANT_MASTER_LEDGER.csv`
20. `05_PLANT_PROFILES/`
21. `31_CULTIVAR_MATRIX_PROVISIONAL.md`
22. `06_ANNUAL_CALENDAR_PROVISIONAL.md`
23. `32_TODAY_ENGINE.md`
24. `09_SOIL_PLAN.md`
25. `10_IRRIGATION_PLAN.md`
26. `12_PEST_IPM.md`
27. `13_DISEASE_PLAYBOOK.md`
28. `25_STYLE_UPGRADES.md`
29. `27_GITHUB_REUSE_AUDIT.md`
30. `28_RESEARCH_LEDGER.md`
31. `29_DECISION_LOG.md`
32. `30_OPEN_QUESTIONS.md`

---

# Immediate September 2026 work

## URGENT / highest value
- secure garlic planting stock
- walk/stake the 90 × 121 ft garden footprint or equivalent transformed shape
- identify greenhouse position, sun, drainage, water route, and cart approach
- measure water-source flow/pressure
- submit separate soil samples

## THIS WEEK
- compare greenhouse models against `47_GREENHOUSE_EQUIPMENT_SPEC.md`
- mark main north–south and east–west paths on the ground
- verify the v0.6 bed arrangement does not collide with real trees/utilities/septic
- photograph fixed viewpoints
- tag dahlias before frost

## OPTIONAL
- test rose entrance spacing with temporary stakes
- mock up bench/wildflower-tub location
- choose trellis material language

## DO NOT TOUCH YET
- do not bulk-buy soil amendments before soil results
- do not buy final exhaust fan before greenhouse model/intake design
- do not install permanent path aggregate before buried services are resolved
- do not order a large rose collection; current default is only 3–5 red roses

---

# 2027 first-year scale remains normal

- 6 tomatoes
- 6 bell peppers
- 3 jalapeños
- 3 eggplants
- 2–3 English cucumbers
- 2 pumpkins
- modest squash
- 6–8 spring + 6–8 fall cabbage
- 40–80 garlic cloves
- 15–24 asparagus crowns
- 2–3 rhubarb crowns
- 3–5 red roses
- 8–12 dahlias

Unused capacity is reserve, airflow, successions, flowers, and comfort—not a mistake.

---

# Still not allowed to fake

Unknown until observed/measured:
- exact real-parcel placement
- mature-tree shade
- water-source flow/pressure until tested
- drainage/low spots
- soil chemistry
- wildlife pressure
- utilities/septic/no-dig zones
- exact greenhouse model
- several cultivar/type choices

These do not block default planning, but they can override local details when real evidence arrives.

---

# Human operating principle

Every daily brief collapses to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Evidence states

Use only:
- `PROVISIONAL`
- `RESEARCHED`
- `SITE CONFIRMED`
- `OBSERVED IN THIS GARDEN`
- `SUPERSEDED`

## Hard boundary

The Garden OS stops at approximately one quarter acre unless the user explicitly changes that decision.

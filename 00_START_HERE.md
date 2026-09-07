# Garden Operating System — START HERE — v0.7

**Status:** RICHMOND CONFIRMED / QUARTER-ACRE GARDEN LOCKED / BED-LEVEL MASTERPLAN / SELF-VALIDATING LIVING REPO  
**Updated:** 2026-09-07

## Current truth

- Richmond, Kentucky / Madison County
- ~2-acre residential property context
- actual Garden OS cultivated footprint = **1/4 acre / 10,890 sq ft**
- remaining ~1.75 acres are ordinary yard unless explicitly expanded
- default design canvas = **90 × 121 ft**
- default greenhouse = **16 × 24 ft / 384 sq ft** inside the quarter-acre garden
- exact requested plant list = 38 canonical entries
- red roses dominate; optional white rose maximum = 1, backyard/interior only
- wildflower feature = separate tub

## Before doing any major work

Run:

```bash
python scripts/validate_garden_data.py
```

The GitHub workflow `.github/workflows/validate-garden-data.yml` runs the same validation on pushes and pull requests.

If an AI is continuing this project, read:

`51_AI_CONTINUATION_PROTOCOL.md`

before changing architecture or canonical data.

---

# Canonical geometry now in force

## Macro
`40_DEFAULT_QUARTER_ACRE_LAYOUT.md`

## Bed-level
`45_VISUAL_MASTERPLAN_AND_BED_GRID.md`

## Machine-readable / visual
- `data/default_layout_zones.csv`
- `data/bed_inventory_v0_6.csv`
- `docs/default_quarter_acre_masterplan.svg`

Current rotation backbone:
- R1–R4
- each **16 × 16 ft**
- 1,024 sq ft total active rotation soil

Do not reintroduce the superseded 12 × 24 ft rotation-block geometry.

---

# Immediate execution order

1. `50_2026_2027_MASTER_CHECKLIST.md`
2. `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
3. `47_GREENHOUSE_EQUIPMENT_SPEC.md`
4. `48_IRRIGATION_ZONE_SIZING.md`
5. `49_MATERIALS_AND_PROCUREMENT_REGISTER.md`
6. `44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md`
7. `37_FALL_2026_RICHMOND_ACTION_PLAN.md`
8. `42_2027_SEED_START_AND_SUCCESSION.md`
9. `43_2027_BED_ASSIGNMENT_AND_ROTATION.md`
10. `46_ROSE_AND_FLOWER_DESIGN.md`
11. `31_CULTIVAR_MATRIX_PROVISIONAL.md`
12. task-specific plant/soil/IPM/disease files

---

# Immediate September 2026 work

### URGENT
- secure garlic planting stock
- preserve photos of existing pest/disease evidence
- identify/mark actual standing-water zones after rain

### THIS WEEK
- walk/stake a 90 × 121 ft quarter-acre footprint or equivalent transformed shape
- confirm greenhouse sun/drainage/access/water route
- measure source water flow and pressure
- submit separate soil samples
- tag dahlias intended for storage
- check real site for utilities/septic/no-dig conflicts

### OPTIONAL
- mock up red entrance rose pair with temporary stakes
- mock up bench/wildflower-tub position
- choose trellis material language

### DO NOT TOUCH YET
- do not cultivate the rest of the ~2-acre property
- do not bulk-buy amendments before soil results
- do not buy final greenhouse fan before model/intake design
- do not install final path aggregate before buried services are resolved
- do not buy a large rose collection; current default is 3–5 red roses

---

# Greenhouse current design

Mission order:
1. propagation
2. transplant staging/hardening
3. shoulder-season production
4. selected protected crops
5. overwintering experiments
6. storage

Current Kentucky-based summer exhaust planning target:
- **~3,100–3,900 CFM effective installed capacity**
- final hardware remains model/intake/system-loss dependent

Files:
- `38_GREENHOUSE_PLAN.md`
- `41_GREENHOUSE_OPERATING_SYSTEM.md`
- `47_GREENHOUSE_EQUIPMENT_SPEC.md`

---

# Irrigation current design

Default zones:
- Z1 kitchen Solanaceae
- Z2 cucumber/cabbage/moist herbs
- Z3 rotation blocks
- Z4 permanent moist edibles
- Z5 dry herbs
- Z6 roses/flowers
- Z7 greenhouse
- Z8 sprawling/flex

Final sizing requires actual source GPM/pressure.

Files:
- `48_IRRIGATION_ZONE_SIZING.md`
- `data/irrigation_zone_template.csv`

A timer never proves the plants need water.

---

# Rose / flower current design

Default rose geometry:
- matched red entrance pair
- one red transition/path focal
- total 3–5 red roses
- optional white rose 0–1 only

Classic-red candidate names from older Kentucky resistance evidence remain **candidates**, not guarantees.

File:
- `46_ROSE_AND_FLOWER_DESIGN.md`

---

# Current unresolved cultivar/type choices

These do not block architecture:
- squash = summer / winter / both
- daisy type
- geranium type
- eggplant form
- pumpkin purpose
- cherry tomato color preference
- final rose cultivar mix

File:
- `31_CULTIVAR_MATRIX_PROVISIONAL.md`

---

# Human operating principle

Every daily brief collapses to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

Every task should expose its reason.

---

# Evidence states

Use only:
- `PROVISIONAL`
- `RESEARCHED`
- `SITE CONFIRMED`
- `OBSERVED IN THIS GARDEN`
- `SUPERSEDED`

When a conclusion changes, update the current canonical document and preserve history in `29_DECISION_LOG.md` rather than leaving contradictory instructions active.

## Hard boundary

The Garden OS stops at approximately one quarter acre unless the user explicitly changes that decision.

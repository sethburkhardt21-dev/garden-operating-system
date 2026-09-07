# Garden Operating System — v0.7

**Status:** RICHMOND SITE CONFIRMED / QUARTER-ACRE GARDEN LOCKED / GREENHOUSE LOCKED / BED-LEVEL BLUEPRINT / SELF-VALIDATING LIVING REPO  
**Updated:** 2026-09-07

## Purpose

Turn the exact requested plant list into a living, research-backed system for planning, building, growing, maintaining, diagnosing, harvesting, beautifying, and improving one specific residential garden in Richmond, Kentucky.

## Locked site truth

- **Location:** Richmond, Kentucky / Madison County
- **Property context:** approximately 2 acres
- **Garden OS cultivated footprint:** approximately **1/4 acre = 10,890 sq ft**
- **Remaining ~1.75 acres:** ordinary yard/open space unless explicitly expanded later
- **Default garden canvas:** **90 × 121 ft** normalized rectangle
- **Greenhouse:** enclosed **16 × 24 ft = 384 sq ft** greenhouse inside the quarter-acre garden
- exact requested plant inventory: 38 canonical entries
- red roses dominate; optional white rose maximum = 1, backyard/interior only
- wildflower feature remains a separate tub
- asparagus/rhubarb remain permanent edible infrastructure
- dry herbs remain a separate moisture/drainage zone

## v0.7 milestone

The repository is now **self-validating** rather than relying only on human memory.

### Validator
Run:

```bash
python scripts/validate_garden_data.py
```

It checks high-value invariants including:
- 90 × 121 ft = 10,890 sq ft quarter-acre math
- area-budget math
- 16 × 24 ft greenhouse geometry
- canonical 38 plant IDs/count
- full 2027 crop-plan coverage
- coordinate bounds for zones/beds
- four 16 × 16 ft rotation blocks
- presence of canonical files

### Continuous validation
GitHub Actions workflow:
- `.github/workflows/validate-garden-data.yml`

The validator runs on pushes and pull requests so future AI/human edits cannot silently break core data as easily.

### AI handoff protocol
`51_AI_CONTINUATION_PROTOCOL.md`

This tells another AI exactly how to continue the project without:
- expanding the garden beyond 1/4 acre
- deleting requested plants
- reintroducing stale two-acre-garden assumptions
- changing geometry in only one file
- treating old cultivar claims as guarantees
- replacing Kentucky/local evidence with generic advice
- creating contradictory `FINAL_v2` document sprawl

---

# Canonical physical design

## Macro layout
`40_DEFAULT_QUARTER_ACRE_LAYOUT.md`

## Bed-level layout
`45_VISUAL_MASTERPLAN_AND_BED_GRID.md`

Companions:
- `data/default_layout_zones.csv`
- `data/bed_inventory_v0_6.csv`
- `docs/default_quarter_acre_masterplan.svg`

The normalized design can later be rotated, mirrored, or translated onto the real property.

## Canonical circulation
South to north:

**matched red rose entrance → flower garden → rotation/flex field → kitchen garden → greenhouse/work hub**

Default style:

**formal bones + cottage abundance**

---

# Canonical bed system

## Kitchen beds
- K01 — 2 heirloom tomatoes
- K02 — 2 beefsteak tomatoes
- K03 — 2 cherry tomatoes
- K04 — 6 bell peppers
- K05 — 3 jalapeños + 3 eggplants
- K06 — 2–3 English cucumbers on trellis
- K07 — 6–8 spring + 6–8 fall cabbage
- K08 — basil / parsley / cilantro succession

## Rotation blocks
The superseded conceptual 12 × 24 ft blocks are gone.

Current:
- R1–R4
- each **16 × 16 ft**
- **1,024 sq ft** total active rotation soil

2027:
- R1 — Solanaceae / potatoes
- R2 — Cucurbitaceae / squash
- R3 — garlic + brassica shoulder-season flex
- R4 — reset / flowers / trial / reserve

## Permanent
- P01 — asparagus
- P02 — rhubarb
- P03 — lavender / thyme / rosemary

## Flowers
- FL01 — dahlias
- FL02 — zinnias + cosmos
- FL03 — perennial pollinator drift
- dedicated sweet-pea support
- separate morning-glory structure

## Roses
Default:
- matched red entrance pair
- one red path/flower-transition focal
- total 3–5 red roses
- optional white rose 0–1 only

See `46_ROSE_AND_FLOWER_DESIGN.md`.

---

# Greenhouse system

Core files:
- `38_GREENHOUSE_PLAN.md`
- `41_GREENHOUSE_OPERATING_SYSTEM.md`
- `47_GREENHOUSE_EQUIPMENT_SPEC.md`

Mission priority:
1. propagation
2. transplant staging/hardening support
3. shoulder-season production
4. selected protected crops
5. overwintering experiments
6. storage

Current Kentucky-based summer exhaust planning target for the 16 × 24 structure:
- approximately **3,100–3,900 CFM effective installed capacity**
- final fan/intake package must be verified against selected greenhouse/model/system losses

Full winter heating is not assumed.

---

# Irrigation system

Core detail:
- `48_IRRIGATION_ZONE_SIZING.md`
- `data/irrigation_zone_template.csv`

Default hydrozones:
1. Z1 kitchen Solanaceae
2. Z2 cucumber/cabbage/moist herbs
3. Z3 rotation blocks
4. Z4 permanent moist edibles
5. Z5 dry herbs
6. Z6 roses/flowers
7. Z7 greenhouse
8. Z8 sprawling/flex

Final sizing waits for measured source GPM/pressure.

A timer never counts as proof that watering is biologically needed.

---

# 2027 operating system

## Propagation
`42_2027_SEED_START_AND_SUCCESSION.md`

## Bed/rotation plan
`43_2027_BED_ASSIGNMENT_AND_ROTATION.md`

## Crop data
`data/2027_crop_plan.csv`

## Master build/season checklist
`50_2026_2027_MASTER_CHECKLIST.md`

First-year scale remains intentionally normal rather than maximum-output.

---

# Procurement / infrastructure

Build order:

`SITE → WATER/DRAINAGE → GREENHOUSE → PRIMARY PATHS → PERMANENT BEDS → IRRIGATION → ANNUAL BEDS → TRELLISES → FLOWERS/ROSES → POLISH`

Files:
- `44_INFRASTRUCTURE_AND_BUILD_SEQUENCE.md`
- `49_MATERIALS_AND_PROCUREMENT_REGISTER.md`

Do not buy high-rework materials before their dependency gate closes.

---

# Research model

Primary locality authority:
- Madison County Extension
- University of Kentucky Extension

Research ledger:
- `28_RESEARCH_LEDGER.md`

Evidence states:
- `PROVISIONAL`
- `RESEARCHED`
- `SITE CONFIRMED`
- `OBSERVED IN THIS GARDEN`
- `SUPERSEDED`

Older rose/cultivar trials may create candidates but not guarantees.

---

# Current unresolved decisions

The architecture does not block on these, but they affect final cultivar orders:
- squash = summer / winter / both
- daisy type
- geranium = Pelargonium / hardy Geranium
- eggplant form
- pumpkin purpose
- cherry tomato color preference
- final rose cultivar mix

See `31_CULTIVAR_MATRIX_PROVISIONAL.md`.

---

# Start here

1. `00_START_HERE.md`
2. `51_AI_CONTINUATION_PROTOCOL.md`
3. `50_2026_2027_MASTER_CHECKLIST.md`
4. `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
5. `docs/default_quarter_acre_masterplan.svg`
6. `40_DEFAULT_QUARTER_ACRE_LAYOUT.md`
7. `47_GREENHOUSE_EQUIPMENT_SPEC.md`
8. `48_IRRIGATION_ZONE_SIZING.md`
9. `49_MATERIALS_AND_PROCUREMENT_REGISTER.md`
10. `42_2027_SEED_START_AND_SUCCESSION.md`
11. `43_2027_BED_ASSIGNMENT_AND_ROTATION.md`
12. `46_ROSE_AND_FLOWER_DESIGN.md`
13. `04_PLANT_MASTER_LEDGER.csv`
14. `31_CULTIVAR_MATRIX_PROVISIONAL.md`
15. `28_RESEARCH_LEDGER.md`
16. `29_DECISION_LOG.md`
17. `garden_baseline.json`

Then use task-specific plant/IPM/disease/soil/calendar files as needed.

---

# Human operating principle

Deep detail belongs in the repository. Daily operation collapses to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Hard boundary

Do not let future work quietly turn the remaining 1.75 acres into more garden. Expansion requires an explicit user decision.

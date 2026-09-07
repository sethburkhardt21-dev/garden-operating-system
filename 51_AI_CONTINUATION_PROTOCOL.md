# AI Continuation Protocol — v0.7

**Purpose:** allow another AI to continue the Garden Operating System without losing constraints, duplicating work, or reintroducing stale assumptions.

This repository is not a pile of notes. It is a **living operational model of one specific quarter-acre garden in Richmond, Kentucky**.

Any AI continuing the work must preserve the current truth hierarchy and must update existing canonical files when conclusions change.

---

# 1. Read order before making changes

Minimum required read:
1. `README.md`
2. `00_START_HERE.md`
3. `garden_baseline.json`
4. `29_DECISION_LOG.md`
5. `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
6. `50_2026_2027_MASTER_CHECKLIST.md`
7. task-specific canonical files

Then run:

```bash
python scripts/validate_garden_data.py
```

Do not begin by guessing the current architecture from filenames alone.

---

# 2. Hard invariants

Do not change these without explicit user instruction:

## Site / scale
- location = Richmond, Kentucky / Madison County
- property context ≈ 2 acres
- Garden OS cultivated footprint = approximately **1/4 acre / 10,890 sq ft**
- remaining ~1.75 acres are not garden by default

## Default design canvas
- normalized rectangle = **90 × 121 ft**
- southwest origin = `(0,0)`
- east = +x
- north = +y
- design may be rotated/mirrored/translated onto real parcel later

## Greenhouse
- enclosed greenhouse required inside quarter-acre footprint
- default = **16 × 24 ft / 384 sq ft**
- propagation priority outranks permanent greenhouse crop occupation
- full winter heating is not assumed

## Plant list
The exact 38 canonical entries remain preserved in:
- `04_PLANT_MASTER_LEDGER.csv`
- `garden_baseline.json`
- `data/2027_crop_plan.csv`

A bad cultivar does not silently delete the requested crop category.

## Rose rule
- red roses dominate
- default 3–5 red roses
- optional white rose = 0–1, backyard/interior only

## Wildflower rule
- wildflower feature remains a separate tub/container project

## Water rule
- dry herbs are not watered on the same logic as thirsty vegetables
- greenhouse is an independent hydrozone
- timer schedules never count as biological proof that watering is needed

---

# 3. Current geometry authority

Bed-level geometry authority:
- `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
- `data/bed_inventory_v0_6.csv`
- `docs/default_quarter_acre_masterplan.svg`

Macro geometry:
- `40_DEFAULT_QUARTER_ACRE_LAYOUT.md`
- `data/default_layout_zones.csv`

Current rotation geometry:
- four blocks
- R1–R4
- each **16 × 16 ft**
- total active rotation soil = 1,024 sq ft

Do not reintroduce superseded four-12×24-ft geometry.

---

# 4. Evidence model

Use only these state labels:
- `PROVISIONAL`
- `RESEARCHED`
- `SITE CONFIRMED`
- `OBSERVED IN THIS GARDEN`
- `SUPERSEDED`

Evidence priority:
1. observed measurements from this actual garden
2. Madison County / University of Kentucky Extension
3. USDA / government / peer-reviewed sources
4. respected regional horticultural organizations
5. generic national references
6. seed companies/nurseries for availability and cultivar descriptions
7. forums/social/community sources for hypotheses only

Commercial claims do not automatically become horticultural truth.

---

# 5. Research rules

For meaningful horticultural claims:
- prefer Kentucky/local sources
- record source URL and finding in `28_RESEARCH_LEDGER.md`
- record age caveats for older cultivar trials
- distinguish hardiness zone from frost/planting dates
- distinguish cultivar claims from species-level guidance
- triangulate high-impact decisions

If sources conflict:
1. record the conflict
2. identify why they may differ
3. prefer the source closest to Richmond/current cultivar/current practice
4. keep the unresolved point provisional

---

# 6. Living-document rule

When a conclusion changes:

**DO:**
- update the current canonical file
- add/supersede the decision in `29_DECISION_LOG.md`
- update `garden_baseline.json` if machine-readable truth changes
- update CSV/SVG geometry if spatial truth changes
- run the validator

**DO NOT:**
- append a contradictory new file and leave stale instructions active
- preserve a known-wrong recommendation because it appeared earlier
- create `FINAL_FINAL_v2_revised.md` style document sprawl

History belongs in the decision log; current truth belongs in the canonical document.

---

# 7. Data integrity rule

Before committing changes to canonical data run:

```bash
python scripts/validate_garden_data.py
```

The GitHub Action `.github/workflows/validate-garden-data.yml` also runs this validator on pushes and pull requests.

At minimum it checks:
- quarter-acre area math
- greenhouse geometry
- plant count/IDs
- crop-plan coverage
- bed/zone coordinate bounds
- 16 × 16 rotation-block geometry
- required canonical files

If validation fails, fix the data before treating the repo as current.

---

# 8. Geometry change protocol

Before moving a bed/feature:
1. identify biological reason
2. identify path/irrigation/shade consequences
3. update `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`
4. update `data/bed_inventory_v0_6.csv` or successor
5. update `docs/default_quarter_acre_masterplan.svg`
6. update `data/default_layout_zones.csv` if macro zones change
7. update `garden_baseline.json` if a design invariant changes
8. run validator

Do not update only the picture.

---

# 9. Greenhouse change protocol

Canonical files:
- `38_GREENHOUSE_PLAN.md`
- `41_GREENHOUSE_OPERATING_SYSTEM.md`
- `47_GREENHOUSE_EQUIPMENT_SPEC.md`

Current design assumptions:
- 16 × 24 ft
- approximately 3,100–3,900 CFM effective summer exhaust planning target before final manufacturer/system verification
- excellent intake/ventilation is a first-order requirement
- heat level selected by actual crop mission
- propagation bench capacity protected February–May

Any exact heater/fan/electrical specification requires the selected greenhouse model and real site.

---

# 10. Irrigation change protocol

Canonical detail:
- `48_IRRIGATION_ZONE_SIZING.md`
- `data/irrigation_zone_template.csv`

Never final-size irrigation until source GPM/pressure are measured.

Default zones:
- Z1 kitchen Solanaceae
- Z2 cucumber/cabbage/moist herbs
- Z3 rotation
- Z4 permanent moist edibles
- Z5 dry herbs
- Z6 roses/flowers
- Z7 greenhouse
- Z8 sprawling/flex

Runtime is commissioned from wetting depth/width and observed conditions.

---

# 11. Cultivar protocol

A cultivar becomes `LOCKED` only after:
1. original requested category preserved
2. Richmond/site fit checked
3. disease-resistance evidence checked
4. mature size fits exact bed
5. user use/taste/color preference checked
6. current source/availability is realistic
7. `31_CULTIVAR_MATRIX_PROVISIONAL.md` updated
8. `04_PLANT_MASTER_LEDGER.csv` updated
9. `29_DECISION_LOG.md` updated

Do not silently reinterpret ambiguous categories.

Current important unresolved items include:
- squash type
- daisy type
- geranium type
- eggplant form
- pumpkin purpose
- final rose cultivar mix

---

# 12. Human-readability rule

Deep detail belongs in the repo.

Human daily output should remain:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

Every action should expose its reason.

Good:
`WATER K01–K03: root zone dry at 3–4 in, no meaningful rain, hot forecast.`

Bad:
`Water tomatoes because scheduled.`

---

# 13. Build dependency rule

Canonical build sequence:

`SITE → WATER/DRAINAGE → GREENHOUSE → PRIMARY PATHS → PERMANENT BEDS → IRRIGATION → ANNUAL BEDS → TRELLISES → FLOWERS/ROSES → POLISH`

Do not add finish work in a way that blocks buried infrastructure or greenhouse service.

---

# 14. Software reuse rule

Third-party garden software remains optional/detachable.

Current direction:
- precision geometry: Open Garden Planner candidate
- operations/journal: Jninty candidate
- generic plant data: OpenPlantDB with provenance/local validation
- collaborative/API mode: HortusFox if needed

Canonical Garden OS truth must remain usable if all third-party apps disappear.

---

# 15. Definition of a good continuation turn

A useful continuation should do one or more of:
- close a real open question with research
- increase physical buildability
- improve machine-readable consistency
- create/validate a seasonal operating procedure
- reduce maintenance friction
- improve disease/pest resilience
- improve greenhouse reliability
- improve irrigation efficiency
- improve visual coherence
- detect and remove stale contradictions
- add validation/testing that prevents future drift

It should **not** merely restate existing documents.

---

# 16. Handoff summary for another AI

You are continuing a quarter-acre residential garden project in Richmond, Kentucky. It contains 38 requested plant entries, a 16 × 24 ft greenhouse, normalized bed-level geometry, a 2027 crop/propagation plan, disease/IPM systems, irrigation zones, flower/rose composition, procurement sequencing, and automated repository validation.

Start with the validator and current canonical files. Improve the system without expanding beyond the quarter acre or silently changing the plant list.
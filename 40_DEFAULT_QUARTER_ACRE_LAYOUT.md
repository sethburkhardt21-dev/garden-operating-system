# Default Quarter-Acre Layout Blueprint — v0.6

**Status:** DEFAULT DESIGN LOCK / ROTATE OR MIRROR TO FIT THE REAL PARCEL  
**Location:** Richmond, Kentucky  
**Garden footprint:** 90 ft east–west × 121 ft south–north = **10,890 sq ft (1/4 acre)**

This file is the macro-layout. Bed-level geometry now lives in `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`, with machine-readable modules in `data/bed_inventory_v0_6.csv` and a visual schematic in `docs/default_quarter_acre_masterplan.svg`.

The plan is a normalized average design, not a survey of the real yard. It may be rotated, mirrored, or translated onto the best real quarter-acre location while preserving the internal relationships.

## Coordinate system

- southwest corner = `(0,0)`
- east = increasing `x`
- north = increasing `y`
- east boundary = `x=90`
- north boundary = `y=121`
- default entrance centered on the south side near `x=45`

## Why this shape

A 90 × 121 ft rectangle is:
- exactly one quarter acre
- large enough for the entire requested plant palette
- compact enough for a normal household garden
- wide enough for a greenhouse, production beds, flowers, permanent crops, and rotation
- easy to reproduce in Open Garden Planner/CAD

---

# Primary circulation

## Perimeter service strip
Reserve roughly 4 ft inside the outer edge where practical for:
- mower/fence access
- drainage observation
- hose/utility access
- visual breathing room

## Main north–south spine
Approximately:
- `x=43–47`
- `y=4–117`
- ~4 ft wide

Primary wheelbarrow/cart route.

## Main east–west cross path
Approximately:
- `y=57–61`
- `x=4–86`
- ~4 ft wide

No productive bed should require routine walking on productive soil.

---

# North-up room plan

```text
NORTH / y=121
┌──────────────────────────────────────────────────────────────────────────┐
│ GREENHOUSE + WORK HUB          │ KITCHEN GARDEN                         │
│ 16×24 greenhouse               │ K01–K08                                │
│ propagation / hardening        │ tomatoes / peppers / cucumber / herbs │
├────────────────────────────────┼─────────────────────────────────────────┤
│ DRY HERBS / PERMANENT SUPPORT  │ R1 + R2 ROTATION BLOCKS               │
│ lavender / thyme / rosemary    │ 16×16 each                             │
├────────────────────────────────┼─────────────────────────────────────────┤
│ ASPARAGUS + RHUBARB            │ R3 + R4 ROTATION BLOCKS               │
│ permanent edible infrastructure│ 16×16 each                             │
├────────────────────────────────┼─────────────────────────────────────────┤
│ FLOWERS + ROSE STRUCTURE       │ PUMPKIN / SQUASH FLEX                 │
│ dahlias / zinnia / cosmos      │ deliberate vine run                    │
│ perennial drift                │                                         │
├──────────────────────────────────────────────────────────────────────────┤
│ RED-ROSE ENTRANCE / WILDFLOWER TUB / BENCH / VISUAL FOREGROUND          │
└──────────────────────────────────────────────────────────────────────────┘
SOUTH / y=0
```

---

# Greenhouse / work hub

## GH-01 — greenhouse
`x=6–22`, `y=93–117`  
16 × 24 ft = 384 sq ft.

Default north-side placement reduces avoidable shade over outdoor production and keeps the operational hub close to the main spine.

## GH-WORK — hardening / potting apron
`x=4–28`, `y=81–93`.

Functions:
- hardening racks
- potting overflow
- media staging
- hose header
- cart parking
- temporary harvest crates

See:
- `38_GREENHOUSE_PLAN.md`
- `41_GREENHOUSE_OPERATING_SYSTEM.md`
- `47_GREENHOUSE_EQUIPMENT_SPEC.md`

---

# Kitchen garden

The high-frequency kitchen garden occupies the north-east room, generally `x=47–86`, `y=81–117`.

Bed-level defaults K01–K08 are now fixed in `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`:
- K01 heirloom tomatoes
- K02 beefsteak tomatoes
- K03 cherry tomatoes
- K04 bell peppers
- K05 jalapeño + eggplant
- K06 English cucumber trellis
- K07 cabbage succession
- K08 basil / parsley / cilantro

Tall tomato structures remain along the north side of the kitchen room where practical.

Reserve ground between/around modules is intentional for paths, airflow, staging, successions, and future adjustment.

---

# Rotation / flex field — v0.6 correction

v0.5 referenced four ~12 × 24 ft rotation blocks but the earlier `ROTATION-NE` envelope could not contain all four. That mismatch is superseded.

The canonical annual rotation field is now the **combined east-middle area**:
- approximately `x=47–86`
- approximately `y=37–77`

Inside it:
- R1 = `x=48–64`, `y=59–75`
- R2 = `x=68–84`, `y=59–75`
- R3 = `x=48–64`, `y=39–55`
- R4 = `x=68–84`, `y=39–55`

Each block is **16 × 16 ft = 256 sq ft**. Total active rotation soil = **1,024 sq ft**.

Default 2027 family use:
- R1 — Solanaceae / potatoes
- R2 — Cucurbitaceae / squash
- R3 — Brassica + garlic shoulder-season flex
- R4 — reset / annual flowers / trial / reserve

The service gaps between blocks remain useful for irrigation headers, carts, crop inspection, and rotation changes.

---

# Permanent edible + dry-herb structure

## P01 — asparagus
Default envelope in west-middle room; see exact coordinates in `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`.

Needs:
- full sun where practical
- strong drainage
- permanent access
- room for fern growth
- no annual tillage

## P02 — rhubarb
Separate crown grouping, not crowded into asparagus rows.

## P03 — dry herbs
Lavender / thyme / rosemary occupy a distinct freer-draining irrigation zone.

Do not put P03 on the same watering runtime as rhubarb or kitchen vegetables.

---

# Pumpkin / squash flex

## F01
Approximate default planting/run zone:
- `x=47–68`
- `y=13–31`

2027 default:
- 2 pumpkin plants/hills
- squash allocation depending whether summer/winter/both is resolved

Rooted planting points stay irrigated; vine travel is routed deliberately away from the central spine and main flower beds.

---

# Flower + rose room

The principal flower garden remains west of the main spine in the south-west room.

Bed-level defaults:
- FL01 — dahlias
- FL02 — zinnia/cosmos cutting block
- FL03 — perennial pollinator drift
- FL04 — cool-season flower/support strip
- FL05 — separate morning-glory vertical structure

The south entrance receives a matched red-rose pair plus a third red focal plant farther into the garden by default.

See `46_ROSE_AND_FLOWER_DESIGN.md` for the composition, candidate rose strategy, group sizes, and bloom sequence.

---

# South-east foreground

Use for a lower-maintenance visual transition:
- wildflower tub
- bench/pause point
- ornamental vertical feature
- part-shade impatiens only if real shade exists
- path-edge seasonal color

The south-east is not a hidden overflow dumping ground.

---

# Height / shade rules

- greenhouse stays toward north by default
- tallest tomato supports stay north of shorter kitchen crops where practical
- cucumber trellis should not shade peppers unnecessarily
- pumpkin vines run outward, not across primary paths
- dahlias/cosmos occupy back/north side within their flower block where practical
- roses retain open air around foliage

Map all tall structures:
- greenhouse ridge
- tomato supports
- cucumber trellis
- sweet-pea trellis
- morning-glory structure
- dahlia supports

---

# Default entrance sequence

From south to north:

**red rose pair → flower foreground → cutting/perennial garden → rotation/flex field → kitchen garden → greenhouse/work hub**

The strongest default remains **formal bones + cottage abundance**.

---

# What stays intentionally unfilled

Do not fill every square foot.

The quarter acre must retain:
- airflow
- cart access
- staging
- compost/material handling
- succession space
- recovery/unused soil
- comfortable visual rhythm

Unused capacity is valid when it prevents the garden from becoming a maintenance trap.

---

# Site-fit priority order

When the real yard placement is finalized, preserve these priorities:
1. strong sun for primary vegetables
2. drainage
3. easy water
4. greenhouse access
5. utility/septic safety
6. path efficiency
7. tall-structure shade control
8. disease airflow
9. aesthetics

Transform the normalized plan rather than redesigning from zero unless the real site makes a relationship biologically impossible.

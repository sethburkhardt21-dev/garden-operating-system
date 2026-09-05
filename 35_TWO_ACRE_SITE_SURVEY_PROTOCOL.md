# Two-Acre Site Survey Protocol

**Purpose:** turn the Richmond yard from “about two acres” into a map accurate enough to place beds, paths, trellises, irrigation, roses, perennial crops, and vine runs without false precision.

This protocol is designed to be doable by one person with a phone, tape measure/laser measure, stakes, and a notebook.

## Phase 1 — crude map in 15 minutes

Draw the property as a simple shape and add:
- house
- driveway
- street/front boundary
- sheds/outbuildings
- fences/gates
- major mature trees
- patio/deck
- current garden beds
- hose bibs
- visible slopes/ditches
- north arrow

Do not worry about scale yet.

## Phase 2 — establish fixed reference points

Choose 4–8 permanent points that are unlikely to move:
- house corners
- fence corners
- shed corners
- mature-tree trunks
- driveway corners

Give them IDs: `REF-01`, `REF-02`, etc.

Every future bed/feature should eventually be measurable from at least two known references. This makes the map recoverable even if stakes disappear.

## Phase 3 — property / garden-core dimensions

Priority is not measuring every inch of two acres first.

Measure in this order:
1. house footprint / major walls
2. candidate garden-core rectangle/polygon
3. distance from garden core to nearest water source
4. mature trees near the core
5. fences/gates controlling access
6. slopes/low spots
7. secondary expansion areas
8. remaining property boundary only as needed

Record units consistently in feet/inches or meters.

## Phase 4 — sunlight survey

For each candidate garden room create a row:

| Area ID | 9 AM | Noon | 3 PM | 6 PM | Approx direct sun | Shade source |
|---|---|---|---|---|---|---|
| CORE-A | | | | | | |
| PEREN-A | | | | | | |
| ROSE-A | | | | | | |
| DRY-A | | | | | | |

Repeat on at least two clear days if possible.

### Priority requirements
- tomatoes/peppers/eggplant/cucurbits: strongest sun candidates
- roses: strong sun + airflow
- lavender/rosemary/thyme: strong sun + drainage
- impatiens: part-shade candidate

## Phase 5 — drainage survey

After a meaningful rain event, inspect at:
- 1 hour
- 6 hours
- next morning
- ~24 hours if saturated

Mark:
- standing water
- saturated/spongy soil
- fast-draining high spots
- erosion channels
- downspout discharge
- roof runoff patterns

Photo-name examples:
`DRAIN_CORE-A_2026-09-20_1h.jpg`
`DRAIN_CORE-A_2026-09-20_24h.jpg`

## Phase 6 — topography / cold-air map

You do not need survey-grade elevation at first.

Label:
- HIGH
- MID
- LOW
- SLOPE-DOWN direction

Cold air tends to settle into low areas. Flag low sunny pockets as possible frost-risk zones rather than automatically calling them the best vegetable site.

## Phase 7 — water-friction test

From each hose bib:
- measure distance to candidate vegetable core
- test hose reach
- note elevation change
- note whether hose crosses driveway/path
- time how long it takes to fill a known container if irrigation sizing becomes necessary

Score candidate areas:
- `A` = easy water
- `B` = manageable
- `C` = annoying daily
- `D` = requires infrastructure

A perfect sunny bed that is miserable to water is not automatically the best garden location.

## Phase 8 — wildlife pressure survey

Record direct evidence, not assumptions:
- deer tracks/browse height
- rabbit pellets/bite pattern
- groundhog holes
- squirrel/chipmunk digging
- vole tunnels
- slug/snail evidence

Map entry points and shelter corridors.

## Phase 9 — soil sampling

Use the separate sample IDs in `34_RICHMOND_KY_SITE_BASELINE.md`.

Do not mix:
- vegetable core soil
- wet low spot
- rose/perennial soil
- dry-herb area

into one sample.

## Phase 10 — photograph protocol

Take fixed-view photographs at minimum:
- north-looking
- south-looking
- east-looking
- west-looking
- candidate kitchen garden
- candidate permanent bed
- candidate rose/flower area
- candidate pumpkin/outflow area

Stand in the same spot each season when possible.

Naming convention:
`SITE_REF01_NORTH_2026-09-05.jpg`

## Deliverable schema

The completed survey should eventually create:

```text
SITE/
  property_sketch.jpg
  measurements.csv
  reference_points.csv
  sun_map.csv
  drainage_log.csv
  soil_tests/
  photos/
  water_map.md
  wildlife_log.md
```

## Coordinate-lock gate

Do not call the map “exact” until it contains:
- north
- at least two reliable references
- major structures
- measured garden-core footprint
- water location
- major shade objects
- major slopes/low spots

Once this gate passes, reproduce the property in Open Garden Planner or equivalent precision-map tooling and export JSON + SVG/PDF + CSV plant list for portability.

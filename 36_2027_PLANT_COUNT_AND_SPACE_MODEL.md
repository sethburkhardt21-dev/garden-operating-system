# 2027 Plant Count + Space Model — Quarter-Acre Richmond Garden v0.7

**Status:** BALANCED FIRST-YEAR MODEL / exact shopping quantities still cultivar/site dependent  
**Updated:** 2026-09-07

The property is approximately two acres, but the Garden OS uses only about **1/4 acre (10,890 sq ft)** including greenhouse, paths, flowers, work areas, and all crops.

This file intentionally avoids scaling plant counts merely because a quarter acre can physically hold more. The goal is a normal, abundant household garden that remains pleasant to maintain.

## Core rule

**Quarter acre is the maximum designed footprint, not a command to fill every square foot.**

Use 2027 to learn actual household consumption, disease pressure, labor, irrigation behavior, and yield. Increase later only from evidence.

---

# Balanced 2027 edible counts

## Tomatoes — 6 outdoor plants
- heirloom: 2 in K01
- beefsteak: 2 in K02
- cherry: 2 in K03

Enough to compare types and create a strong household harvest without a tomato farm.

### Greenhouse tomato option
At most 1–2 protected indeterminate tomatoes as an experiment after propagation demand falls. Do not automatically add them on top of outdoor production.

## Peppers
- bell: 6 in K04
- jalapeño: 3 in K05

## Eggplant
- 3 in K05

## English cucumber
- 2–3 outdoor plants in K06 on dedicated trellis

Optional greenhouse cucumber: 1 trial vine only if it does not compromise propagation/workspace.

## Squash
Until type is resolved:
- summer: 2 plants/hills
- winter: 1–2 hills
- if both are selected, keep total modest

Geometry is reserved in R2/F01.

## Pumpkin
- 2 plants/hills in F01/R2 route

## Cabbage
- spring: 6–8 in K07
- fall: 6–8 in K07
- R3 can handle overflow/succession

## Garlic
- 40–80 cloves in R3

## Potatoes
R1:
- golden/yellow type: ~20–30 row-ft equivalent
- second cultivar for baby/new potatoes: ~20–30 row-ft equivalent

This fits comfortably in the 16 × 16 R1 block when laid out appropriately; final row geometry follows selected planting method and access.

## Asparagus
- 15–24 crowns in P01
- no first-year harvest

## Rhubarb
- 2–3 crowns in P02

---

# Herbs

## Basil
- 4–8 plants at a time in K08
- succession rather than one oversized planting

## Rosemary
- 1–2 in P03
- one may remain containerized for winter flexibility

## Thyme
- 2–4 in P03

## Parsley
- 3–6 in K08

## Cilantro
- repeated small K08 sowings

## Lavender
- 3–7 in P03 depending mature width

---

# Roses + flowers

## Red roses
- **3–5 total**

Default:
- matched entrance pair
- one transition/path focal
- optional two additional repetitions only if composition benefits

## Optional white rose
- 0–1, backyard/interior only

## Dahlias — FL01
- **8–12**

This supersedes older 8–16 wording and matches the current normal first-year design.

## Zinnias — FL02
- roughly **24–36** plants across one or two successions, adjusted for cultivar spacing

## Cosmos — FL02
- roughly **10–16**

## Marigolds
- roughly **18–30** repeated edge plants/groups across the design

## Snapdragons
- roughly **18–24** grouped cool-season plants

## Coneflower — FL03
- 5–7

## Black-eyed Susan — FL03
- 7–9

## Daylilies — FL03
- 5–7

## Daisies — FL03
- 3–5 after species resolves

## Geraniums
If hardy Geranium:
- 3–5 in FL03

If Pelargonium:
- roughly 6–9 seasonal/container plants in a suitable area

## Impatiens
- 12–18 only if a real part-shade pocket exists

## Morning glory
- 2–4 vines on one dedicated `VG-MORNING-GLORY` structure

## Sweet peas
- one 8–12 ft `VG-SWEET-PEA` support

## Lupines
- 3–5 plant trial only if selected

---

# Greenhouse occupancy — 16 × 24 ft

The greenhouse first supports the outdoor garden.

## Late winter / early spring
Use propagation capacity for:
- tomatoes
- peppers
- eggplant
- cabbage
- herbs
- snapdragons/flowers
- optional dahlia wake-up/propagation

Target working capacity: approximately 8–12 standard 1020-style trays without blocking aisle/workspace.

## Spring transition
- harden/stage transplants
- clear benches as crops move out
- retain active work/propagation space

## Summer optional
- 1 tomato and/or
- 1 cucumber and/or
- several peppers/herbs

Kentucky heat means summer greenhouse production may be harder, not easier. Ventilation/shade come first.

## Fall
- fall transplants
- herbs/cool-season trials
- frost extension

## Winter
Use depends on the selected heating mode; full commercial winter production is not default.

---

# Current exact bed-space program

Canonical modules now exist rather than approximate examples.

## Kitchen
- K01 4 × 16 — heirloom tomatoes
- K02 4 × 16 — beefsteak tomatoes
- K03 4 × 16 — cherry tomatoes
- K04 12 × 4 — bell peppers
- K05 4 × 16 — jalapeño + eggplant
- K06 4 × 12 — cucumber
- K07 4 × 12 — cabbage
- K08 4 × 12 — moist culinary herbs

## Rotation
- R1–R4 each 16 × 16
- 1,024 sq ft active rotation soil total

## Permanent
- P01 asparagus envelope: 18 × 14
- P02 rhubarb envelope: 15 × 12
- P03 dry herb room: 24 × 16

## Flowers
- FL01 dahlias: 8 × 22
- FL02 zinnia/cosmos: 10 × 22
- FL03 perennial drift: 11 × 22

## Flex
- F01 pumpkin/sprawling crop envelope: 21 × 18

Exact normalized coordinates are in `data/bed_inventory_v0_6.csv`.

---

# Active soil vs total quarter-acre footprint

Not all 10,890 sq ft is production soil.

The footprint includes:
- 384 sq ft greenhouse
- main/secondary paths
- work/hardening area
- trellis/rose feature clearances
- wildflower/bench detail
- airflow
- reserve/succession ground
- irrigation/compost/service space

This is intentional.

---

# Expansion trigger

Increase a crop only when 2027 shows:
- harvest is consistently used/gifted/preserved
- household wants more
- maintenance is comfortable
- disease burden acceptable
- irrigation/support capacity adequate

Reduce when:
- food is wasted
- flavor is disappointing
- labor is disproportionate
- disease pressure remains high
- greenhouse/outdoor duplication produces excess

## Default philosophy

A successful quarter-acre garden has **room to breathe**. Empty/reserve soil is resilience, not failure.

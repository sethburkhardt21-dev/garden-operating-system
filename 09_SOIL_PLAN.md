# Soil Plan — Richmond Quarter-Acre Garden v0.6

**Status:** SAMPLING STRATEGY LOCKED / AMENDMENTS PROVISIONAL UNTIL TEST RESULTS  
**Updated:** 2026-09-07

## First principle

**Test before aggressively amending.**

The property is ~2 acres, but the Garden OS cultivates only one quarter acre. Soil sampling should therefore focus on the biologically distinct management zones **inside or directly affecting the quarter-acre garden**, not the entire yard.

Madison County currently advertises free soil testing for residents, up to 10 samples per home/farm per calendar year. Use that capacity strategically.

## Sample architecture

### SOIL-A — kitchen + primary annual production
Use for K01–K08 and representative annual vegetable soil where the same soil history/management applies.

### SOIL-B — rotation field
Use for R1–R4 if this field differs from the kitchen beds or will be managed in-ground rather than with imported raised-bed soil.

### SOIL-C — permanent asparagus/rhubarb room
Prepare this correctly before crowns go in; future correction is harder.

### SOIL-D — rose / cutting-flower garden
Use before investing in long-lived roses and perennial flowers.

### SOIL-E — dry-herb garden
P03: lavender, rosemary, thyme. Drainage may matter more than maximizing fertility.

### SOIL-F — greenhouse native soil / foundation edge
Only if greenhouse beds/native soil will actually be used. If the greenhouse is entirely benches/containers over a constructed floor, a native-soil fertility test may not be useful.

### SOIL-G — problem wet/poor area
Only sample separately when a visibly distinct problem area intersects the planned garden or drainage route.

### Remaining sample capacity
Use only for a genuinely different management zone, not to test the ordinary lawn just because free samples remain.

---

# Sampling rule

Within one management zone:
- collect multiple representative subsamples
- avoid compost piles, fertilizer spills, pet waste spots, ash piles, fence edges, and other abnormal points unless diagnosing that exact spot
- mix subsamples for that zone according to Extension instructions
- label the sample before leaving the site

Do **not** mix kitchen beds, dry herbs, roses, wet spots, and rotation soil into one composite sample.

## What to record with every result

- sample ID
- exact bed/zone IDs
- date
- current vegetation/use
- intended 2027 use
- pH
- phosphorus result/recommendation
- potassium result/recommendation
- lime recommendation
- fertilizer recommendation
- organic matter if provided
- Extension notes
- original report file/photo

Store the original report, not only a transcription.

---

# Biological soil zones

## Annual vegetable / cutting-flower production soil
Applies primarily to:
- K01–K08
- R1–R4 depending crop
- FL01/FL02 where soil is shared

Goal:
- good aggregation
- adequate organic matter
- water-holding without chronic saturation
- fertility based on test

## Dry-herb soil — P03
Lavender / rosemary / thyme.

Goal:
- drainage first
- avoid rich wet soil
- independent irrigation

## Permanent edible soil — P01/P02
Asparagus / rhubarb.

Goal:
- deep preparation before planting
- perennial weed suppression before crowns go in
- drainage correction before the bed becomes permanent
- fertility correction before planting where test supports it

## Rose / perennial flower soil
Goal:
- drainage
- suitable pH/fertility from actual test
- organic matter where appropriate
- mulch/irrigation system that reduces splash and does not bury rose crowns/canes

## Greenhouse media
Container/bench crops are not automatically governed by native-yard soil tests.

Track separately:
- purchased media lot/type
- pH/EC if measured
- crop response
- fertilizer history
- sanitation/reuse status

---

# Do not do these before results

- do not automatically lime
- do not add phosphorus “for roots” without evidence
- do not repeatedly add high-P manure/compost without tracking accumulation
- do not assume the entire quarter acre needs the same compost rate
- do not bury unfinished organic waste in planting holes
- do not fertilize lavender/rosemary heavily by default
- do not use one lawn test to represent raised beds or imported garden soil
- do not use a greenhouse potting-mix test to represent outdoor soil

---

# Drainage is separate from chemistry

A perfect pH result does not fix standing water.

For each garden zone record:
- standing-water duration after rain
- saturation/sponginess
- crusting
- compaction
- erosion
- slope
- downspout/runoff influence

If a candidate greenhouse, asparagus, lavender, rose, or vegetable area remains wet, solve placement/drainage before fertilizing the problem.

---

# Bed-area amendment rule

When a soil report recommends a rate per 1,000 sq ft or acre, calculate the amendment from the **actual managed bed area**, not the full quarter-acre boundary.

Examples of managed areas are stored in:
- `data/bed_inventory_v0_6.csv`
- `45_VISUAL_MASTERPLAN_AND_BED_GRID.md`

Paths, greenhouse floor, benches, and unused buffer ground should not automatically receive vegetable-bed amendments.

---

# Multi-year soil improvement

## Pre-plant / 2026–early 2027
- test
- correct documented chemistry issues
- remove perennial weeds
- improve structure with appropriate organic matter where needed
- solve drainage
- establish paths so bed soil is not repeatedly compacted

## 2027
- record growth/deficiency patterns
- avoid chasing every leaf color with fertilizer
- mulch appropriately
- keep amendment history by bed
- re-test only where needed or where major changes were made

## 2028+
Track trend by bed/zone:
- pH
- nutrient accumulation/depletion
- organic matter
- drainage/compaction
- crop performance
- disease relationship to drainage/crowding

The goal is a stable soil system, not maximum fertilizer input.

---

# Soil-result integration gate

When reports arrive:
1. save original reports
2. enter raw results into the repository
3. map each result to specific bed IDs
4. compare with crop needs and Extension recommendations
5. calculate amendments from actual managed area
6. separate required corrections from optional optimization
7. record product/rate/date/reason
8. update that zone from `PROVISIONAL` to `SITE CONFIRMED`

Do not purchase bulk amendments until both the relevant soil result and actual managed bed area are known.

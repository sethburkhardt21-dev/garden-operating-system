# Irrigation Zone Sizing + Hydraulic Design — v0.6

**Status:** DESIGN METHOD LOCKED / FINAL FLOW, PRESSURE, PIPE SIZES, AND RUN TIMES SITE-DEPENDENT  
**Garden:** quarter-acre Garden OS, Richmond, Kentucky

This file converts the irrigation concept into a measurable system. It intentionally separates **hydraulic sizing** from **watering duration**. A zone can be engineered correctly and still be watered too much; plant/soil/weather evidence controls runtime.

## Kentucky evidence anchors

University of Kentucky irrigation guidance identifies the normal building blocks of drip systems as:
- water source
- backflow/check protection as applicable
- filter
- pressure regulator/gauge
- delivery/main lines
- drip lines/emitters
- valves/zones

UK resources also emphasize system-specific design, soil moisture, and zoning rather than one universal setup.

References:
- https://ccd.uky.edu/resources/systems/irrigation
- https://publications.mgcafe.uky.edu/sites/publications.ca.uky.edu/files/ID-36.pdf
- https://uknowledge.uky.edu/bae_present/1/

---

# 1. Source-water gate

Before final pipe/tube sizing, measure:

1. **static pressure** at the garden source
2. **dynamic pressure** while flowing
3. **flow rate** using a timed-volume test
4. distance from source to greenhouse/header
5. elevation change

## Timed-volume test

Use a known container.

Example formula:
`GPM = container gallons ÷ fill minutes`

Repeat at least twice.

Record:
- faucet/source ID
- hose/no-hose condition
- container size
- fill time
- calculated GPM
- pressure if gauge available

## Design reserve

Do not design a normal zone to consume 100% of measured source flow.

**Default engineering reserve:** target routine simultaneous zone demand at roughly **60–70% or less of the reliably measured source flow**, unless the irrigation designer/manufacturer validates a different operating point.

Reason:
- protects against pressure drop
- accommodates filter fouling
- leaves margin for other household demand
- reduces poor emitter uniformity at the far end

This is a Garden OS design heuristic, not a plumbing-code rule.

---

# 2. Canonical hydrozones

## Z1 — kitchen Solanaceae
Beds:
- K01 heirloom tomatoes
- K02 beefsteak tomatoes
- K03 cherry tomatoes
- K04 bell peppers
- K05 jalapeño/eggplant

Reason to group:
- similar preference for consistent root-zone moisture
- high-frequency inspection
- easy independent shutoff if disease or crop removal changes demand

## Z2 — cucumber / cabbage / moist culinary herbs
Beds:
- K06 cucumber
- K07 cabbage
- K08 basil/parsley/cilantro

Keep this distinct from dry herbs.

## Z3 — rotation blocks
Beds:
- R1–R4

Use individual block valves or quick shutoffs even if a shared header supplies them. Rotation crops change yearly.

## Z4 — permanent moist edibles
- P01 asparagus
- P02 rhubarb

Keep permanent plumbing stable even when annual beds rotate.

## Z5 — dry herbs
- P03 lavender/thyme/rosemary

Must be independently controllable.

## Z6 — roses + flower garden
- red roses
- dahlias
- zinnias/cosmos
- perennial drift
- other ornamentals where moisture needs are compatible

Use subvalves if roses need a distinctly different frequency from annual cut flowers.

## Z7 — greenhouse
- propagation
- benches/containers
- protected tall crops

Greenhouse should have at least two internal subzones or manual branches:
- `GH-PROP`
- `GH-TALL/BENCH`

## Z8 — sprawling/flex
- F01 pumpkin
- squash route
- temporary flex crops

Use movable/repairable above-ground distribution because crop geometry may change.

---

# 3. Default dripline design language

A common baseline for vegetable beds is dripline with approximately 12 in emitter spacing. Exact manufacturer flow/pressure specifications control the real design.

For planning only, a convenient example is:
- **0.5 gal/hr per emitter**
- **12 in spacing**

This example lets us estimate hydraulic demand without pretending every crop requires the same runtime.

## Flow formula

For line emitters:

`zone GPH = total dripline feet ÷ emitter spacing feet × emitter GPH`

Then:

`zone GPM = zone GPH ÷ 60`

### Example 4 × 16 ft bed
If four 16 ft laterals are used:
- total dripline = 64 ft
- at 12 in spacing = ~64 emitters
- at 0.5 GPH = ~32 GPH
- ~0.53 GPM

### Example 4 × 12 ft bed
Four 12 ft laterals:
- 48 ft dripline
- ~24 GPH at the same example emitter spec
- ~0.40 GPM

These numbers are **hydraulic examples**, not watering-duration instructions.

---

# 4. Crop-specific delivery style

## Tomatoes
Prefer either:
- individual emitters near each plant with provision to expand wetted root area as plants mature
- or parallel dripline if the whole bed is cropped/rotated

Do not wet the stem/crown constantly.

## Peppers / eggplant / cabbage / herbs
Dripline is straightforward when spacing is reasonably regular.

## English cucumber
One or two lines along the trellis bed depending soil texture/wetted width.

## Potatoes
Use parallel dripline/row delivery that remains accessible during hilling.

## Asparagus
Permanent lines should not interfere with crown rows or later fern maintenance.

## Rhubarb
Deliver to the root zone without keeping crowns chronically saturated.

## Lavender / rosemary / thyme
Use wider-spaced individual emitters or a conservative dedicated dry-zone line. Do not copy vegetable runtimes.

## Roses
Use soil-level individual emitters or a ring/paired-emitter pattern appropriate to mature root spread. Avoid routine foliage wetting.

## Dahlias / cut flowers
Parallel dripline can simplify dense cutting rows.

## Pumpkin / squash
Use emitter(s) at the rooted planting station rather than trying to irrigate the entire vine path.

---

# 5. Mainline/header architecture

Default functional sequence:

`SOURCE → BACKFLOW/VACUUM PROTECTION AS REQUIRED → SHUTOFF → FILTER → PRESSURE REGULATOR → PRESSURE GAUGE → MAINLINE → ZONE MANIFOLD → LATERALS/EMITTERS → FLUSH ENDS`

## Why the gauge matters
A regulator can fail or a filter can clog. A gauge makes invisible pressure problems visible.

## Why flush ends matter
Sediment and biological material accumulate. Every zone should have a practical way to flush.

## Why zone valves matter
The quarter-acre garden contains biologically incompatible moisture groups. One giant timer circuit is not acceptable.

---

# 6. Recommended control topology

## Controller output / manifold concept

Minimum practical controllable groups:
1. kitchen vegetables
2. rotation/flex
3. permanent edibles
4. dry herbs
5. roses/flowers
6. greenhouse

Preferred:
7. separate cut-flower valve
8. separate sprawling-crop valve

Manual shutoff at each sub-area is still useful even when automated valves exist.

---

# 7. Pressure strategy

Drip tubing/tape has a manufacturer operating-pressure range.

Rules:
- regulate to the selected product requirement
- do not assume house pressure is safe for drip tubing
- do not assume a pressure regulator fixes undersized long delivery lines
- account for elevation and friction losses
- do not exceed maximum lateral length for the selected product

Kentucky ultra-low-pressure research shows that specialized small-plot systems can run at very low pressures, but that is a distinct design regime and should not be mixed casually with standard drip components.

Reference:
https://publications.ca.uky.edu/sites/publications.ca.uky.edu/files/HO120.pdf

---

# 8. Watering-duration logic

Runtime is **not** hard-coded by crop name.

Use:
- soil moisture at root depth
- recent rainfall
- crop stage
- soil texture
- air temperature/wind
- container vs in-ground behavior
- drainage
- observed plant response

Kentucky guidance favors deep root-zone wetting over repeated shallow sprinkling.

## Commissioning procedure

For each zone:
1. start with dry-ish but not wilted soil
2. run a measured interval
3. wait for redistribution
4. dig/check wetting depth and width
5. record result
6. adjust runtime

Create a zone-specific calibration, not a universal “20 minutes every day” schedule.

---

# 9. Rain override

After meaningful rain:
- pause automatic irrigation
- inspect soil moisture
- inspect low/drainage-prone areas
- resume only when root-zone evidence supports it

Use a rain sensor/forecast as an input, not as the sole proof that every zone is wet enough.

---

# 10. Flow anomaly detection

Optional but high value.

Red flags:
- zone flow suddenly much higher → broken line/emitter/valve
- much lower → clog, kink, closed valve, filter restriction
- flow when all zones are off → leak/stuck valve

If a flow meter is added, record normal baseline flow for each zone after commissioning.

---

# 11. Greenhouse-specific plumbing

Provide:
- greenhouse shutoff
- hose/wand tap
- regulated micro-irrigation branch
- propagation subzone
- tall-crop/container subzone
- drain-safe floor/work area

If year-round water is desired, freeze protection must be designed rather than improvised.

---

# 12. Winterization

Before hard freeze:
- shut down/drain vulnerable above-ground lines
- disconnect/store timer/regulator components as manufacturer requires
- open flush ends/low points if system design permits
- protect valves/manifold
- mark any buried line locations in the map

Permanent buried infrastructure must be recorded before mulch/landscape hides it.

---

# 13. Irrigation definition of done

The system is not complete until:
- source GPM measured
- operating pressure known
- all hydrozones independently controllable
- filter/regulator/gauge installed where needed
- every lateral can be flushed
- greenhouse branch exists
- dry-herb branch is independent
- roses are not routinely overhead-watered
- zone flows are recorded
- each zone runtime has been calibrated by soil wetting evidence
- winter shutdown procedure is documented

See `data/irrigation_zone_template.csv` for the commissioning worksheet.
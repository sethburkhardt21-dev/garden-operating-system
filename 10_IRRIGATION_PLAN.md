# Irrigation Plan — Richmond Quarter-Acre Garden

**Status:** BIOLOGICAL ZONES RESEARCHED / PHYSICAL PIPE ROUTES PROVISIONAL  
**Updated:** 2026-09-05

The yard is about two acres, but irrigation is designed for one **quarter-acre garden (~10,890 sq ft)** plus its 16 × 24 ft enclosed greenhouse. Do not build an irrigation network for the entire yard.

## Core invariant

A timer may request water. It does **not** prove water is needed.

Every irrigation decision should consider:
- recent rain
- soil moisture at useful root depth
- plant stage
- container vs in-ground conditions
- greenhouse vs outdoor conditions
- heat/wind
- drainage
- disease pressure

## Hydrozone H1 — consistent-moisture outdoor production

Plants:
- tomatoes
- peppers
- eggplant
- English cucumber
- squash
- pumpkin
- cabbage
- potatoes
- basil
- parsley
- cilantro

Preferred delivery:
- dripline/emitters at soil level
- mulch where appropriate
- separately controllable from dry herbs and greenhouse

## H2 — dry/drainage herbs

- lavender
- rosemary
- thyme

Use less frequent watering and excellent drainage. Do not copy H1 runtime.

## H3 — roses / selected perennials

Deep soil-level watering with foliage kept as dry as practical.

## H4 — containers / wildflower tub

Containers may need water when in-ground beds do not. Use separate micro-drip or manual inspection.

## H5 — permanent edible perennials

- asparagus
- rhubarb

Establishment-year attention is higher than mature-year care.

## H6 — greenhouse

The enclosed greenhouse is its own irrigation environment.

Possible delivery:
- hand hose/wand for seedlings
- bench-level micro-irrigation for pots
- drip for tall protected crops
- separate shutoff from outdoor beds

Greenhouse watering must respond to:
- pot/container size
- substrate
- crop stage
- inside temperature
- ventilation
- humidity

Do not assume outdoor rainfall reduces greenhouse water demand.

---

# Physical architecture

## Water entry / garden hub

The quarter-acre plan should have one deliberate water/irrigation hub near the greenhouse/work area where practical.

Suggested sequence:
1. backflow protection as locally appropriate
2. timer/controller
3. filter
4. pressure regulator
5. main header/manifold
6. independently controlled zone branches
7. flush ends / service points
8. manual override

## Recommended controllable branches
- `OUT-VEG` — annual vegetables
- `OUT-DRY` — lavender/rosemary/thyme
- `OUT-ROSE` — roses/perennials as needed
- `OUT-PERM` — asparagus/rhubarb
- `OUT-CONT` — containers/wildflower tub
- `GH` — greenhouse

The exact number of valves can be simplified if the actual bed layout is small enough, but greenhouse and dry-herb control should remain independent.

## Mainline scale rule

Do not extend buried or permanent irrigation across the remaining ~1.75 acres unless a future non-garden need is explicitly added.

---

# Greenhouse-specific water notes

- locate the greenhouse where a reliable water route is practical
- use a shutoff inside or immediately adjacent if feasible
- design floor/drainage so spills are harmless
- avoid standing water under benches
- keep seedling watering gentle enough not to displace media
- separate propagation water needs from large fruiting-crop drip needs

If gutters are installed, captured rainwater may supplement container/ornamental watering, but storage volume and water quality must be managed realistically.

---

# Richmond humidity / disease design

Prefer:
- soil/substrate-level watering
- morning irrigation where timing matters
- adequate spacing/airflow
- fast drying after accidental foliar wetting
- no sprinkler overspray across tomatoes/cucurbits/roses if avoidable

In the greenhouse, ventilation and watering interact: overwatering + poor air exchange is a disease amplifier.

## Heavy-rain outdoor override
Pause outdoor schedules after significant rain and inspect drainage. Greenhouse irrigation remains a separate decision because roofed crops received no rain.

## Heat-wave override
Prioritize:
1. greenhouse temperature/ventilation
2. greenhouse containers
3. outdoor containers
4. newly established plants
5. root-zone moisture in high-demand outdoor beds

---

# Best-value implementation target

For an average quarter-acre garden, the preferred endpoint is:
- compact buried/secured mainline only within the garden
- drip/micro-irrigation by hydrozone
- greenhouse branch
- simple controller with manual override
- rain gauge
- optional one or two representative soil-moisture sensors later
- optional flow/leak alert later

Do not over-automate before observing one full season.

---

# Data still needed for final bill of materials

- quarter-acre garden coordinates
- water source location
- pressure/flow rate
- greenhouse location
- bed lengths/widths
- greenhouse bench/ground-crop layout
- elevation changes
- container count
- exact number of hydrozones

Until these are known, reserve the system architecture but do not buy arbitrary tubing lengths.

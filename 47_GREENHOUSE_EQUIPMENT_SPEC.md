# Greenhouse Equipment + Controls Specification — v0.6

**Status:** FUNCTIONAL SPECIFICATION / FINAL PRODUCT SELECTION AND CODE COMPLIANCE SITE-DEPENDENT  
**Structure:** 16 × 24 ft enclosed greenhouse, Richmond, Kentucky

This file converts the greenhouse from a concept into a procurement/engineering specification without locking a brand before the real site, electrical service, foundation, glazing package, and local code requirements are known.

## Design priority

1. structural safety
2. ventilation/cooling
3. reliable water
4. propagation/work capacity
5. frost protection
6. monitoring/alerts
7. optional automation
8. decorative upgrades

Do not reverse this order by buying sensors and shelves before the greenhouse can safely vent summer heat.

---

# 1. Structure

## Required
- rigid residential greenhouse frame sized for 16 × 24 ft footprint
- manufacturer-rated anchoring/foundation system appropriate to the selected structure and site
- durable greenhouse glazing; twin-wall polycarbonate or equivalent is the default direction
- door wide enough for wheelbarrow/cart access
- operable ventilation openings
- gutters where compatible with the structure
- insect screening only where it does not excessively cripple airflow

## Target clearances
- useful sidewall height: approximately 6.5–7+ ft
- enough ridge/headroom for tall plants, hanging hardware, and air movement
- no low structural members across the main cart path

## Do not lock yet
- exact foundation type
- exact glazing thickness
- snow/wind load package
- door side
- automatic vent opener model

Those depend on the selected manufactured structure and real siting.

---

# 2. Summer ventilation capacity

Current University of Kentucky greenhouse guidance states that summer ventilation should generally exchange roughly the greenhouse air volume each minute to a height of about 8–10 ft; winter ventilation can use roughly one-quarter that volume.

For the 16 × 24 ft footprint:

- at 8 ft effective height: `16 × 24 × 8 = 3,072 ft³`
- at 10 ft effective height: `16 × 24 × 10 = 3,840 ft³`

### Default summer exhaust design target
**Approximately 3,100–3,900 CFM effective installed capacity.**

This is a design target, not a claim that a single fan labeled 3,500 CFM will actually deliver that after shutters, screens, intake restrictions, static pressure, and installation losses.

### Preferred architecture
- staged exhaust rather than one all-or-nothing fan where practical
- large low-resistance intake louvers/openings on the opposite end/side
- roof/upper vents for passive buoyancy relief
- large door/end opening for manual emergency venting
- circulation fans to prevent dead/stagnant pockets

### Circulation
UK guidance recommends greenhouse fans be positioned so stagnant areas are avoided and fans are not spaced excessively far apart. In a 24 ft greenhouse, two appropriately sized horizontal-airflow/circulation fans can usually create a useful circulation loop if positioned correctly.

**Default:** provision for 2 circulation fans, final size/placement by manufacturer airflow pattern.

Source anchor:
https://ccd.uky.edu/sites/default/files/2025-09/final-version.pdf

---

# 3. Intake sizing rule

Do not size intake by guesswork.

For the selected exhaust fan(s):
- follow manufacturer required free-air intake area
- use actual louver/screen free area, not nominal frame dimensions
- avoid tiny screened openings that starve the fan
- keep intake path clear of tall plants/storage

If exhaust fan noise increases and airflow drops when the door is closed, suspect inadequate intake or restriction.

---

# 4. Shade system

Provide attachment points for removable greenhouse shade cloth.

Default strategy:
- no permanent heavy shade that destroys spring propagation light
- deploy only when solar load/plant stress requires it
- favor exterior shade when practical because heat intercepted outside the glazing is easier to manage than heat trapped inside

Exact shade percentage depends on crop mix, glazing, season, and measured temperatures. Do not purchase the final cloth solely from a generic percentage recommendation.

---

# 5. Heating

The greenhouse is **not** assumed to be heated all winter.

## Heating mode hierarchy

### Mode 0 — no active heat
Season extension only.

### Mode 1 — emergency/frost protection
Protect seedlings/transplants during short cold events.

### Mode 2 — active propagation heat
Maintain plant-appropriate temperatures during early spring starts.

### Mode 3 — full winter production
Not a default Garden OS requirement.

## Heater sizing method

Do not size heat from floor area alone.

Final heat-loss calculation needs:
- glazing U-value
- greenhouse surface area
- desired indoor temperature
- outdoor design temperature
- infiltration/air leakage
- foundation/perimeter losses
- wind exposure

Conceptual heating load:
`Q ≈ U × A × ΔT + infiltration loss`

A greenhouse installer/HVAC professional should verify the actual heater size when fuel-burning or fixed electrical heat is used.

## Safety
- any combustion heater must be approved for greenhouse/indoor use as applicable and properly vented when required
- keep combustible materials away from heaters
- electrical heaters/outlets must be appropriately protected for a wet environment
- never rely on an extension cord as permanent infrastructure

---

# 6. Environmental controls

## Minimum useful controls
- min/max thermometer
- greenhouse thermostat/controller for exhaust fan
- independent high-temperature alarm if practical
- heater thermostat if heat is installed

## Recommended v0.6 sensor package
- air temperature sensor at plant-canopy height
- relative humidity sensor
- second temperature sensor near propagation bench or opposite greenhouse end
- soil/media probe only for experiments, not as the sole watering authority

## Optional
- outdoor temperature sensor
- leak/flow sensor
- door-open sensor
- internet alerting
- data logging

Every automated action should still be understandable manually.

---

# 7. Greenhouse irrigation

Greenhouse watering is its own hydrozone.

## Required
- shutoff valve at greenhouse
- filter if drip/micro-irrigation is used
- pressure regulation matched to emitters
- hose/wand connection for manual watering
- ability to isolate benches/containers from tall-crop bay

## Propagation bench
Preferred:
- hand watering or controlled fine watering during early seedling stages
- do not place tiny seedlings on the same coarse irrigation runtime as large tomato containers

## Tall protected crops
If used:
- individual emitters or dedicated dripline
- separate valve/subzone from propagation

## Drainage
Water spills must drain without creating chronic puddles/algae around the work area.

---

# 8. Electrical specification

Final electrical work must comply with applicable electrical/building requirements.

Provision conceptually for:
- exhaust fan circuit
- circulation fans
- heater circuit if needed
- lighting/work outlet circuit
- controller/sensor power
- GFCI protection appropriate to wet greenhouse conditions
- weather/wet-location rated fixtures and boxes as required

Do not undersize the service before heater/fan loads are known.

---

# 9. Benches and interior zoning

## Center aisle
Target approximately **3.5–4 ft clear**.

## Side benches
Default:
- 30–36 in deep
- at least one long propagation bench
- work height comfortable for repetitive seeding/potting

## GH-PROP
Primary propagation bench space.

## GH-BENCH
Pots/herbs/young plants.

## GH-TALL
Keep a section floor-level/open for:
- tall tomato trial
- English cucumber
- peppers
- large overwintered pots

## GH-WORK
Potting station near entrance.

## GH-QUAR
A small physically separable shelf/area for questionable incoming plants.

---

# 10. Propagation capacity target

The greenhouse only needs to support a normal quarter-acre household garden.

Default spring design capacity:
- 8–12 standard 1020-style trays simultaneously without blocking aisles or workbench
- room for pot-up containers afterward
- reserve floor/bench space for hardening transitions

Do not build a 100-tray nursery operation unless the garden later expands.

---

# 11. Greenhouse storage rule

Allowed:
- active trays/pots
- labels
- propagation media in sealed/organized containers
- small hand tools
- irrigation parts
- current-season fertilizers/inputs appropriately stored

Not allowed to consume propagation space:
- unrelated household storage
- broken pots “for someday”
- permanent piles of soil bags
- lawn equipment
- winter furniture

The greenhouse is a growing/work structure, not a shed.

---

# 12. Failure playbooks

## Exhaust fan failure during hot weather
**FIRST 5 MINUTES**
- open doors/vents fully
- deploy passive ventilation
- stop adding heat/light load

**NEXT HOUR**
- add temporary portable air movement if electrically safe
- deploy shade cloth if solar load is severe
- monitor canopy temperature

**NEXT 24 HOURS**
- repair/replace fan/controller
- inspect plants for heat injury

## Heater failure during freeze threat
- move highest-value seedlings to safer indoor space if feasible
- use crop-safe temporary frost protection/thermal buffering
- reduce exposed propagation inventory
- restore heat safely; do not improvise hazardous combustion systems

## Power failure
- manually vent if warm/sunny
- manually protect plants if cold
- irrigation may need manual hose backup

## Water failure
- prioritize seedlings and small containers first
- hand carry limited water if necessary
- repair supply before starting new propagation batches

---

# 13. Procurement gates

## May be selected before exact site placement
- bench style
- tray standard
- labels
- handheld thermometer
- propagation tools

## Must wait for selected greenhouse model/site
- foundation
- anchors
- exhaust fan exact model
- intake louvers
- heater capacity
- electrical service size
- fixed plumbing route
- shade cloth dimensions
- gutter/downspout system

## Definition of ready-to-order greenhouse package
All must be known:
1. exact site location
2. foundation/anchoring method
3. manufacturer wind/snow rating acceptable for site
4. door orientation/access
5. water route
6. electrical strategy
7. ventilation opening/fan package
8. summer shade attachment plan
9. drainage path
10. local permit/code requirements checked where applicable

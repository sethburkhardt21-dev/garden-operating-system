# Today Engine — Human Operating Layer v0.6

**Site:** Richmond, Kentucky / quarter-acre Garden OS inside an approximately 2-acre yard  
**Goal:** open the project and know what matters today without reading the entire repository.

The engine is rule-based first. Weather/sensor automation may enrich it later but never becomes the only way to operate the garden.

## Required daily output

Every brief contains exactly four sections:

### URGENT
Delay is likely to cause meaningful damage, loss, safety risk, or missed harvest.

### THIS WEEK
Normal work that should happen soon but does not require panic.

### OPTIONAL
Style upgrades, experiments, record-keeping, and nonessential improvements.

### DO NOT TOUCH YET
Actions that are premature, unsupported by evidence, or likely to create rework.

---

# Daily decision sequence

## 1. Weather gate
Check Richmond-area conditions, then compare them with the actual quarter-acre garden:
- overnight low
- daytime high
- rainfall in previous 24–72 hours
- forecast rain
- wind
- severe weather
- unusually humid/wet stretch

Create alerts for:
- frost/freeze
- heat wave
- drought
- heavy rain
- hail
- damaging wind

Weather alerts outrank routine tasks.

Also ask whether one Garden OS room is behaving differently:
- greenhouse overheated while outdoors is mild?
- low outdoor bed still saturated?
- south flower bed hotter/drier than kitchen beds?
- greenhouse frost-protected while outdoor crops are exposed?

## 2. Greenhouse gate
When greenhouse is active, check before ordinary garden chores if weather could create a rapid failure.

Look at:
- current inside temperature
- daily high/low
- exhaust/vent status
- humidity/condensation
- propagation-bench moisture
- heater state during cold events
- door/vent position

Urgent greenhouse triggers include:
- rising temperature with failed fan/closed vent
- heater failure during freeze threat
- wilted propagation trays
- standing water/electrical concern
- rapid pest outbreak in enclosed space

Use `41_GREENHOUSE_OPERATING_SYSTEM.md` and `47_GREENHOUSE_EQUIPMENT_SPEC.md`.

## 3. Water gate
Do not water because “today is watering day.”

For each hydrozone:
1. Check recent rainfall.
2. Inspect soil moisture at useful root depth.
3. Check containers/greenhouse media separately.
4. Look for stress symptoms but do not diagnose from wilting alone.
5. Water only when root-zone evidence supports it.

Default zones:
- Z1 kitchen Solanaceae
- Z2 cucumber/cabbage/moist herbs
- Z3 rotation blocks
- Z4 permanent moist edibles
- Z5 dry herbs
- Z6 roses/flowers
- Z7 greenhouse
- Z8 sprawling/flex

Kentucky Extension guidance favors deep root-zone wetting rather than frequent shallow sprinkling.

## 4. Harvest gate
High-frequency summer checks:
- cherry tomatoes
- slicing tomatoes
- cucumbers
- summer squash if selected
- peppers
- basil
- cut flowers

If a cucumber or summer squash is ready, harvest generally outranks cosmetic work.

## 5. Support gate
Check:
- indeterminate tomatoes
- English cucumber
- morning glory
- sweet peas
- dahlias
- tall zinnias/cosmos
- greenhouse tall-crop supports if used

Act when:
- stems escape support
- fruit weight pulls branches down
- ties constrict stems
- anchors loosen
- vines invade paths/other crops/greenhouse vents

## 6. Disease gate
Inspect lower/inner foliage first on:
- tomatoes
- peppers
- cucurbits
- roses
- greenhouse crops

Look for:
- spots
- yellowing patterns
- powdery growth
- black lesions
- leaf drop
- stem lesions
- unusual wilt
- fruit rot
- distorted rose growth that may need rose-rosette escalation

If symptoms appear:
1. photograph before removing evidence
2. record bed ID + date + weather pattern
3. compare multiple symptoms
4. distinguish likely infectious vs environmental stress
5. use `13_DISEASE_PLAYBOOK.md`
6. escalate uncertain/high-value cases to Extension rather than guessing

## 7. Pest gate
Priority:
- cabbage
- cucurbits
- roses
- tomatoes/peppers
- potatoes
- greenhouse undersides/new growth

Record:
- organism or damage seen
- rough count/density
- damage severity
- beneficial insects
- action taken

Do not spray merely because one insect exists.

## 8. Flower-performance gate
Check:
- spent flowers
- broken stems
- cutting-stage blooms
- support
- shading/crowding

High-return cutting/deadheading group:
- roses
- zinnias
- dahlias
- cosmos
- snapdragons
- sweet peas

## 9. Perennial protection gate

### Asparagus
Healthy fern growth after harvest season supports future crowns. Do not cut simply for tidiness.

### Rhubarb
Do not heavily harvest establishing crowns. Leaves are not edible.

### Roses / daylilies / coneflower / Rudbeckia
Avoid unnecessary root disturbance.

### Dry herbs
Do not respond to every wilt-looking moment with vegetable-style irrigation; confirm root-zone dryness.

## 10. Infrastructure gate
Quick scan:
- irrigation leak?
- greenhouse fan/controller fault?
- hose across path?
- trellis leaning?
- standing water?
- gate/fence problem?
- deer/rabbit/groundhog evidence?
- path hazard?

A system problem can affect many plants at once.

---

# Maintenance modes

## Five-minute check
1. Weather/freeze/heat warning?
2. Greenhouse failure warning?
3. Anything obviously wilted/broken?
4. Harvest urgent crops.
5. Check containers/propagation.
6. Look for catastrophic pest/disease change.

## Fifteen-minute check
Five-minute check plus:
- inspect tomato/cucumber supports
- quick cabbage/cucurbit pest check
- rose foliage glance
- deadhead obvious spent blooms
- one-line journal update

## Thirty-minute session
- full moisture check
- harvest
- train/tie plants
- disease/pest scouting
- deadhead/cut flowers
- pull young weeds before seed set
- update observations

## One-hour session
- all above
- mulch touch-up
- irrigation inspection
- greenhouse bench cleanup
- detailed pruning/training
- measurements/photos
- inventory updates

## Weekend project
Only schedule jobs such as:
- greenhouse construction/equipment
- irrigation commissioning
- trellis building
- bed edging
- compost work
- perennial planting
- soil amendments based on test
- lifting/storing dahlias
- wildflower-tub work
- fencing/barrier work
- path surfacing

---

# Example brief — September 2026

### URGENT
- Secure garlic planting stock before preferred varieties disappear.
- Photograph active disease/pest symptoms before cleanup destroys evidence.
- During heavy rain, mark actual standing-water zones while they are visible.

### THIS WEEK
- Walk/stake the 90 × 121 ft quarter-acre footprint or a transformed equivalent.
- Confirm greenhouse candidate location, drainage, sun, cart access, and water route.
- Measure water-source flow/pressure.
- Submit separate soil samples for relevant garden management zones.
- Tag dahlias intended for storage.

### OPTIONAL
- Test the red-rose entrance pair with temporary stakes.
- Mock up the bench/wildflower-tub position.
- Choose the trellis/material language.

### DO NOT TOUCH YET
- Do not cultivate the remaining ~1.75 acres.
- Do not bulk-buy soil amendments before tests.
- Do not buy final greenhouse exhaust hardware before structure/intake design is known.
- Do not install final path aggregate before buried water/electrical routes are settled.
- Do not buy a large rose collection; default is 3–5 red roses.

---

# Machine-readable future inputs

The Today Engine may eventually ingest:
- date
- Richmond forecast
- observed rainfall
- greenhouse temperature/RH
- hydrozone moisture
- plant stage
- last watering
- harvest history
- disease flags
- pest flags
- task due dates
- irrigation flow anomalies

But every generated task must expose its reason, for example:

`WATER: K01–K03 tomatoes — root zone dry at 3–4 in, no meaningful rain in 3 days, hot forecast.`

Not:

`Water tomatoes because the app says so.`

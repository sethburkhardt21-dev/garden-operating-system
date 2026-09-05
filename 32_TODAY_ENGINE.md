# Today Engine — Human Operating Layer

**Goal:** A person should be able to open the garden project and know what matters today without reading the entire repository.

The engine is rule-based first. Weather/sensor automation may enrich it later but must never become the only way to operate the garden.

## Output format

Every daily brief must contain exactly these four sections:

### URGENT
Only items where delay is likely to cause meaningful damage, loss, or missed harvest.

### THIS WEEK
Normal maintenance that should happen soon but does not require panic.

### OPTIONAL
Style upgrades, experiments, record-keeping, and nonessential improvements.

### DO NOT TOUCH YET
Plants/actions where intervention would be premature or harmful.

---

# Daily decision sequence

## 1. Weather gate
Check:
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

## 2. Water gate
Do not water because "today is watering day."

For each hydrozone:
1. Check recent rainfall.
2. Inspect soil moisture at useful root depth.
3. Check container weight/moisture where relevant.
4. Look for stress symptoms but do not diagnose from wilting alone.
5. Water deeply if the root zone actually needs water.

Kentucky Extension guidance for summer vegetables emphasizes moistening roughly the upper 6–8 inches rather than frequent shallow sprinkling.

### High-priority moisture group
- tomatoes
- peppers
- eggplant
- cucumbers
- squash
- pumpkin
- cabbage
- potatoes
- basil
- parsley
- cilantro

### Separate dry/drainage group
- rosemary
- thyme
- lavender

### Separate container logic
- wildflower tub
- any potted herbs
- grow-bag potatoes
- movable flowers

Containers can require attention when in-ground beds do not.

## 3. Harvest gate
Check crops where delayed harvest reduces quality or future production.

High-frequency summer checks:
- cherry tomatoes
- slicing tomatoes
- cucumbers
- summer squash if selected
- peppers
- basil
- cut flowers

If a cucumber or summer squash has reached usable size, harvest should generally outrank cosmetic tasks.

## 4. Support gate
Check fast-growing vertical/heavy plants:
- indeterminate tomatoes
- English cucumber
- morning glory
- sweet peas
- tall dahlias
- tall zinnias/cosmos if wind exposed

Action only when:
- stems are escaping support
- fruit weight is pulling branches down
- ties are cutting into stems
- trellis anchors are loosening

## 5. Disease gate
Walk the garden once, slowly.

Inspect lower/inner foliage first on:
- tomatoes
- peppers
- cucurbits
- roses

Look for:
- spots
- yellowing patterns
- powdery growth
- black lesions
- leaf drop
- stem lesions
- unusual wilt
- fruit rot

If symptoms appear:
1. photograph before removing evidence
2. record bed + date + weather pattern
3. compare multiple symptoms
4. isolate likely infectious vs environmental cause
5. use the disease playbook before treating

## 6. Pest gate
Look at both sides of leaves and plant bases.

Priority crops:
- cabbage
- cucurbits
- roses
- tomatoes/peppers
- potatoes

Record:
- pest seen
- number seen
- damage level
- beneficial insects present

Do not spray merely because one insect exists.

## 7. Flower-performance gate
Check:
- spent flowers
- broken stems
- cutting-stage blooms
- plants being shaded
- supports

High-return deadheading/cutting group:
- roses
- zinnias
- dahlias
- cosmos
- snapdragons
- sweet peas

## 8. Perennial protection gate
Permanent plants receive different treatment.

### Asparagus
After the harvest season, fern growth is future-energy infrastructure. Do not cut healthy ferns merely because they look untidy.

### Rhubarb
Do not harvest heavily from newly establishing crowns. Leaves are not edible.

### Roses/daylilies/coneflower/Rudbeckia
Avoid unnecessary digging around established root zones.

---

# Maintenance modes

## Five-minute check
1. Weather warning?
2. Anything obviously wilted/broken?
3. Harvest cucumbers/squash/ripe fruit.
4. Check containers.
5. Look for catastrophic pest/disease change.

## Fifteen-minute check
Five-minute check plus:
- inspect tomato/cucumber supports
- quick cabbage/cucurbit pest check
- deadhead obvious spent blooms
- update one-line journal entry

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
- detailed pruning/training
- soil/plant measurements
- inventory updates
- photos

## Weekend project
Only schedule jobs such as:
- building trellises
- installing drip irrigation
- bed edging
- compost work
- perennial planting
- soil amendments based on test
- lifting/storing dahlias
- constructing the wildflower tub

---

# Example September brief — provisional Northern Kentucky

### URGENT
- If current warm-season plants are still producing, harvest overripe cucumbers/squash/tomatoes before deterioration.
- Photograph any disease symptoms before fall cleanup removes evidence.

### THIS WEEK
- Order/select garlic planting stock.
- Decide which bed can remain occupied by garlic through early summer.
- Measure the garden and begin the sun map.
- Mark dahlias intended for winter storage.
- Submit soil test if not already available.

### OPTIONAL
- Photograph the garden from fixed reference points for year-over-year comparison.
- Pick trellis/label/edging aesthetic.

### DO NOT TOUCH YET
- Do not plant garlic just because it has arrived; use the appropriate fall window and soil conditions.
- Do not randomly fertilize before the soil test.
- Do not finalize asparagus/rhubarb coordinates without permanent-bed geometry.

---

# Future machine-readable inputs

The eventual Today Engine may ingest:
- date
- confirmed location
- local forecast
- observed rainfall
- frost dates
- plant stage
- last watering
- soil moisture
- last fertilizer
- harvest history
- disease flags
- pest flags
- task due dates

But every generated task must expose its reason, for example:

`WATER: Bed B tomatoes — soil dry at 3–4 in, no meaningful rain in 3 days, hot forecast.`

Not:

`Water tomatoes because the app says so.`

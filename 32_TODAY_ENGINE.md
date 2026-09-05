# Today Engine — Human Operating Layer v0.3

**Site:** Richmond, Kentucky / approximately 2-acre yard  
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
Check Richmond-area conditions and then compare them with the actual yard:
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

On the two-acre site, also ask: **is one garden room behaving differently from the rest of the yard?** A low pocket can frost or stay wet while the house-side core remains fine.

## 2. Water gate
Do not water because “today is watering day.”

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
- grow-bag potatoes if used
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

For this two-acre yard, also inspect whether storm exposure differs between open-yard structures and sheltered garden rooms.

## 5. Disease gate
Walk the garden slowly.

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
2. record bed/garden-room + date + weather pattern
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
After harvest season, fern growth is future-energy infrastructure. Do not cut healthy ferns merely because they look untidy.

### Rhubarb
Do not harvest heavily from newly establishing crowns. Leaves are not edible.

### Roses/daylilies/coneflower/Rudbeckia
Avoid unnecessary digging around established root zones.

## 9. Site-infrastructure gate
Because the property is two acres, add a quick infrastructure scan when working outside:
- hose left across mower/path?
- irrigation leak?
- trellis leaning?
- fence/gate breach?
- standing water after rain?
- deer/groundhog evidence?
- new shade or tree-limb issue?

A site problem can affect more plants than an individual plant problem.

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
- property/site surveying
- building trellises
- installing drip irrigation
- bed edging
- compost work
- perennial planting
- soil amendments based on test
- lifting/storing dahlias
- constructing the wildflower tub
- fence/barrier work

---

# Example brief — September 2026, Richmond site

### URGENT
- If current warm-season plants are still producing, harvest overripe cucumbers/squash/tomatoes before deterioration.
- Photograph any disease symptoms before fall cleanup removes evidence.
- If a heavy-rain event occurs, mark standing-water/slow-drainage zones while they are visible.

### THIS WEEK
- Order/select garlic planting stock if not already secured.
- Use `35_TWO_ACRE_SITE_SURVEY_PROTOCOL.md` to sketch house, driveway, trees, fences, north, water points, and candidate garden core.
- Start separate Madison County soil samples for candidate vegetable/perennial areas.
- Measure hose distance to the best sunny garden-core candidate.
- Mark dahlias intended for winter storage.

### OPTIONAL
- Photograph the two-acre yard from fixed reference points for year-over-year comparison.
- Choose a likely aesthetic direction from `25_STYLE_UPGRADES.md`.
- Mark possible red-rose sightline/focal locations on the rough sketch.

### DO NOT TOUCH YET
- Do not cultivate a huge portion of the two acres merely because it is available.
- Do not buy a property-scale irrigation system until water points and garden-room coordinates are known.
- Do not randomly fertilize before zone-specific soil tests.
- Do not finalize asparagus/rhubarb coordinates without drainage/sun evidence.
- Do not call the parcel USDA 7a or 6b with certainty until the exact location is pinned on the USDA map.

---

# Future machine-readable inputs

The eventual Today Engine may ingest:
- date
- confirmed Richmond location
- local forecast
- observed rainfall
- garden-room microclimate
- frost alerts
- plant stage
- last watering
- soil moisture
- last fertilizer
- harvest history
- disease flags
- pest flags
- task due dates

But every generated task must expose its reason, for example:

`WATER: Kitchen Garden tomatoes — soil dry at 3–4 in, no meaningful rain in 3 days, hot forecast.`

Not:

`Water tomatoes because the app says so.`

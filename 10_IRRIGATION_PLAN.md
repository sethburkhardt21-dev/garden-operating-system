# Irrigation Plan — Hydrozone Architecture

## H1 — Consistent-moisture production
Tomatoes, peppers, eggplant, cucumber, squash, pumpkin, cabbage, basil, parsley, cilantro, potatoes.

Goal: deep, consistent root-zone moisture without chronic saturation or frequent leaf wetting.

## H2 — Dry/drainage herb zone
Lavender, rosemary, thyme.

Goal: allow more drying between irrigation events; drainage is a design requirement.

## H3 — Roses
Deep watering at soil level. Avoid designing routine overhead irrigation that keeps foliage wet.

## H4 — Containers
Wildflower tub and any potato/herb containers. Containers may dry dramatically faster than ground beds.

## H5 — Permanent edible perennials
Asparagus/rhubarb; establishment-year monitoring is more intensive than mature-year care.

## Three implementation levels

### Manual
Hose + watering wand + rain gauge + finger/trowel soil checks.

### Best value
Pressure regulator + filter + mainline + drip zones + timer with manual override.

### Advanced
Weather-aware controller + selected soil-moisture sensors + flow anomaly detection.

## Automation invariant
A schedule may request water. It must not be treated as proof that water is needed.

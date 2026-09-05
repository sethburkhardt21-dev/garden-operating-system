# GitHub / Open-Source Reuse Audit — v0.1

This is an initial technical triage, not yet the final code/license audit.

## 1. cofade/open-garden-planner
**Observed 2026-09-05:** active public repository; Python; GPL-3.0; not archived; project description emphasizes CAD-like precision, rich plant metadata, and standard-format exports.

**Provisional classification:** BORROW IDEAS / EVALUATE FOR FORK  
**High-value concepts:** scaled property map, plant metadata, export, layer-based garden planning.  
**Caution:** GPL-3.0 has reciprocal-license implications if code is reused/distributed; architectural borrowing is simpler than direct code reuse unless we deliberately accept GPL terms.

## 2. HapiCreative/jninty
**Observed:** public TypeScript garden journal; MIT license; garden inventory, schedules, tasks, expenses, seed banks, maps; not archived.

**Provisional classification:** BORROW COMPONENTS / BORROW DATA MODEL IDEAS  
Especially relevant to the “garden memory” layer: season history, task queue, seed inventory, expenses, maps.

## 3. MDeLuise/plant-it
**Observed from repository search:** active/public repository exists.  
**Provisional classification:** EVALUATE  
Likely useful for plant-care history/reminder patterns. Must inspect current README, license, storage model, mobile UX, and export capability before reuse decision.

## 4. danielbrendel/hortusfox-web
**Observed from repository search:** public web project exists; companion Android repo is archived while web repo is not.  
**Provisional classification:** EVALUATE / BORROW IDEAS  
Potential value: collaborative plant management and self-hosted garden UI. Need detailed license/architecture inspection.

## 5. cwfrazier1/openplantdb
**Observed from repository search:** public active repository exists.  
**Provisional classification:** DATA/SCHEMA EVALUATION  
Potentially useful machine-readable plant knowledge source. Must verify provenance, license, schema quality, coverage of cultivars, and whether horticultural claims are cited.

## 6. FarmBot/Farmbot-Web-App
**Observed:** public large FarmBot web application repository, not archived.  
**Provisional classification:** ADVANCED/OPTIONAL — BORROW IDEAS  
Useful if future robotics or map/action sequencing is desired. Grossly oversized as the core system for a normal manual residential garden.

## 7. OpenSprinkler/OpenSprinkler-Weather
**Observed:** public weather service repository, not archived.  
**Provisional classification:** BORROW IRRIGATION CONCEPTS / OPTIONAL INTEGRATION  
Useful for weather-adjusted irrigation patterns. Do not make the biological garden dependent on cloud service availability.

## Architectural conclusion

Do **not** build the first garden system as a giant custom application.

Preferred sequence:
1. Keep canonical garden state in portable Markdown + CSV/JSON.
2. Use a mature mapping/planning concept for geometry.
3. Add task/journal capability only if it reduces friction.
4. Add weather/irrigation integration as a detachable layer.
5. Treat robotics as optional future infrastructure.
6. Preserve human-readable operation if every app disappears.

## Next audit pass
For each candidate:
- fetch README
- license
- recent commit history
- data schema
- export/import
- mobile/offline behavior
- self-host burden
- API availability
- maintenance activity
- privacy model
- component-level reuse value
- final ADOPT/FORK/BORROW/REJECT score

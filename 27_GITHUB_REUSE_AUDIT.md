# GitHub / Open-Source Reuse Audit — v0.3

**Status:** RESEARCHED technical triage. No third-party code has been copied into this repository.  
**Site context:** Richmond, Kentucky / ~2-acre yard.

Scoring: 0 = poor fit, 5 = excellent fit. Scores are for **this Garden Operating System**, not overall project quality.

| Project | Fit | Code/Architecture | Data Value | UX Value | Reuse Value | Deployment Ease | Current Classification |
|---|---:|---:|---:|---:|---:|---:|---|
| cofade/open-garden-planner | 5 | 4 | 4 | 4 | 4 | 4 | BORROW IDEAS / STRONG EXTERNAL TOOL CANDIDATE |
| HapiCreative/jninty | 5 | 4 | 4 | 5 | 5 | 5 | STRONG ADOPT/FORK CANDIDATE FOR OPERATIONS LAYER |
| cwfrazier1/openplantdb | 4 | 4 | 5 | 2 | 5 | 5 | DATA/SCHEMA SOURCE CANDIDATE |
| MDeLuise/plant-it | 3 | 4 | 2 | 4 | 3 | 4 | BORROW CARE-HISTORY UX |
| danielbrendel/hortusfox-web | 4 | 4 | 3 | 4 | 4 | 3 | BORROW/ADOPT IF MULTIUSER SELF-HOSTING DESIRED |
| FarmBot/Farmbot-Web-App | 2 | 4 | 2 | 4 | 2 | 1 | FUTURE ROBOTICS ONLY |
| OpenSprinkler/OpenSprinkler-Weather | 3 | 4 | 1 | 2 | 4 | 3 | OPTIONAL IRRIGATION LAYER |

---

## 1. cofade/open-garden-planner

### Verified capabilities
Current README describes:
- centimeter-level calibrated canvas
- satellite/image calibration
- plant metadata
- beds, containers, trellises, paths and fences
- layers
- JSON project format
- PNG/SVG/PDF/DXF export
- CSV plant lists
- harvest tracking
- tasks/reminders
- succession planting
- soil tracking
- embedded MCP/AI-agent integration

### Stack / license
- Python 3.11+
- PyQt6 desktop UI
- GPL-3.0
- current repository activity observed in 2026

### Garden OS value
This is currently the strongest candidate for the **precision geometry/layout layer**. The value increased after the two-acre site was confirmed because image calibration, layers, paths, fences, trellises, and standard exports are much more useful for a property-scale plan than for a tiny single bed.

### Decision
**BORROW IDEAS / EVALUATE AS EXTERNAL TOOL.**

Do not copy GPL-3.0 code into a differently licensed future app without deliberately accepting GPL obligations. Running it as an independent planning tool avoids unnecessary coupling.

### Next test
After the site survey exists:
1. import/calibrate an overhead image or measured sketch
2. map house, water, trees, fences, paths
3. build the maintenance-gradient garden rooms
4. export JSON + SVG/PDF + CSV plant list
5. verify that the exported plan is independently readable without the app

---

## 2. HapiCreative/jninty

### Verified capabilities
Current README describes a local-first PWA with:
- plant inventory
- garden journal + photos
- quick field logging
- plant knowledge base
- planting calendar
- task management
- rule-generated tasks
- garden map
- seed bank with germination rates/sow-by dates
- seasons/plantings and year-over-year comparison
- expense tracking
- full-text search
- ZIP export/import
- frost alerts
- optional multi-device sync

### Architecture
- React 18 + strict TypeScript
- Vite
- PouchDB/IndexedDB
- optional CouchDB replication
- Zod validation
- Konva garden map
- Vitest
- PWA/offline support

### License
MIT.

### Garden OS value
Very close to the desired **daily operations + memory layer**. Local-first, offline, exportable, and phone-friendly match the design principles unusually well.

### Two-acre relevance
A larger yard makes fast field logging more valuable. The user should not need to walk back to a desktop to record pest, harvest, irrigation, or disease observations.

### Risks
- built-in plant knowledge must not automatically become the scientific source of truth
- last-write-wins sync may not be ideal for complex collaboration
- hosted cloud is optional but creates a dependency if chosen

### Decision
**STRONGEST APP-LAYER CANDIDATE.**
Before custom development, test whether Garden OS can use Jninty for journal/task/inventory while retaining Markdown/CSV/JSON as canonical portable truth.

---

## 3. cwfrazier1/openplantdb

### Verified capabilities
README describes:
- machine-readable garden plant database
- 294 plants at time of inspection
- JSON + CSV flat-file data
- USDA-zone/frost-anchor planting model
- mature size and spacing
- germination and maturity ranges
- PostgreSQL schema
- build script with schema validation/deduplication

### License
CC0 1.0 / public domain.

### Important strength
The repository explicitly warns that values are typical ranges and vary by cultivar, region and microclimate. This aligns with the Garden OS evidence model.

### Decision
**BORROW DATA MODEL; selectively import CC0 fields with provenance labels after validation.**

Richmond/Madison Extension evidence and exact cultivar data override generic zone-based ranges.

---

## 4. MDeLuise/plant-it

### Verified capabilities
README describes:
- plant collection
- care-event logs
- photos
- elapsed-time reminders

It intentionally does **not** decide when a plant needs water/fertilizer; the user remains responsible for horticultural judgment.

### Maintenance / license
- repository describes itself as mature/stable and says active feature development has slowed
- repository metadata shows Dart/Flutter
- GPL-3.0
- public, not archived at time of inspection

### Garden OS value
Its philosophy strongly matches the automation invariant: logging/reminders should not pretend elapsed time proves biological need.

### Decision
**BORROW CARE-HISTORY / REMINDER UX IDEAS.**
Jninty remains broader for this project's operations layer.

---

## 5. danielbrendel/hortusfox-web

### Verified capabilities
README describes a maintained, self-hosted collaborative plant system with:
- plants assigned to locations
- photos, notes, logs
- tasks
- inventory
- calendar
- search/history
- weather
- reminders
- backups
- REST API
- QR codes
- plant identification
- multiuser/group features

### Stack / deployment
- PHP
- MariaDB
- Docker/Compose available
- MIT license per README

### Garden OS value
Best fit if this garden eventually needs a **multiuser household workspace**, API access, or QR labels on physical plants/beds.

### Tradeoff
More server/database administration than a local-first PWA.

### Decision
**BORROW / POSSIBLE ADOPT FOR COLLABORATIVE SELF-HOSTED MODE.**
Do not deploy unless collaboration/API/server features are actually needed.

---

## 6. FarmBot/Farmbot-Web-App

### Garden OS value
FarmBot remains the major reference for future robotic bed automation, map/action sequencing and device-driven gardening.

The two-acre yard does not make whole-yard robotics automatically sensible; FarmBot-like systems are best considered for a deliberately structured bed area.

### Decision
**FUTURE ROBOTICS RESEARCH ONLY.**

---

## 7. OpenSprinkler/OpenSprinkler-Weather

### Garden OS value
Useful reference for weather-adjusted irrigation infrastructure.

The two-acre property makes detachable irrigation control more relevant, especially if a remote manifold/mainline becomes justified.

### Decision
**OPTIONAL INTEGRATION / BORROW CONTROL CONCEPTS.**
Weather adjustment may suggest watering changes but soil/plant conditions retain override authority.

---

# Architecture decision after v0.3 pass

Do **not** build a monolithic custom garden app first.

```text
CANONICAL GARDEN TRUTH
Markdown + CSV + JSON + photos
        |
        +--> PRECISION PROPERTY MAP
        |    Open Garden Planner or equivalent
        |
        +--> DAILY OPERATIONS / JOURNAL
        |    Jninty is leading candidate
        |
        +--> OPTIONAL COLLABORATION/API
        |    HortusFox candidate
        |
        +--> GENERIC PLANT SEED DATA
        |    OpenPlantDB, provenance-tagged and validated
        |
        +--> CARE-HISTORY UX
        |    Plant-it concepts
        |
        +--> WEATHER / IRRIGATION
        |    detachable automation layer
        |
        +--> FUTURE ROBOTICS
             FarmBot-class integration
```

## Non-negotiable portability rule
If every third-party application vanished tomorrow, the user must still retain:
- plant inventory
- exact layout export
- cultivar decisions
- care history
- seed inventory
- harvest history
- research evidence
- photos
- current tasks/calendar

## Next engineering experiment

The location/yard-size gate is resolved. The remaining blocker is geometry.

After `35_TWO_ACRE_SITE_SURVEY_PROTOCOL.md` is completed:
1. create the measured Richmond property in Open Garden Planner
2. map the same plants/tasks/journal in Jninty
3. test export/backup recovery
4. record workflow friction on phone + desktop
5. decide whether integration is worth building
6. only then consider custom software

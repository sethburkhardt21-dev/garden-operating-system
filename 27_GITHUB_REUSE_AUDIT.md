# GitHub / Open-Source Reuse Audit — v0.7

**Status:** RESEARCHED technical triage. No third-party code has been copied into this repository.  
**Site context:** Richmond, Kentucky; ~2-acre residential property containing one ~1/4-acre Garden OS.

Scores are for **this Garden Operating System**, not overall project quality.

| Project | Fit | Code/Architecture | Data Value | UX Value | Reuse Value | Deployment Ease | Current Classification |
|---|---:|---:|---:|---:|---:|---:|---|
| cofade/open-garden-planner | 5 | 4 | 4 | 4 | 4 | 4 | STRONG EXTERNAL PRECISION-MAP CANDIDATE |
| HapiCreative/jninty | 5 | 4 | 4 | 5 | 5 | 5 | STRONG OPERATIONS-LAYER CANDIDATE |
| cwfrazier1/openplantdb | 4 | 4 | 5 | 2 | 5 | 5 | DATA/SCHEMA SOURCE CANDIDATE |
| MDeLuise/plant-it | 3 | 4 | 2 | 4 | 3 | 4 | BORROW CARE-HISTORY UX |
| danielbrendel/hortusfox-web | 4 | 4 | 3 | 4 | 4 | 3 | OPTIONAL MULTIUSER SELF-HOSTED MODE |
| FarmBot/Farmbot-Web-App | 2 | 4 | 2 | 4 | 2 | 1 | FUTURE ROBOTICS ONLY |
| OpenSprinkler/OpenSprinkler-Weather | 3 | 4 | 1 | 2 | 4 | 3 | OPTIONAL IRRIGATION CONCEPT LAYER |

---

## 1. cofade/open-garden-planner

### Verified capabilities
Current README/repository inspection found:
- calibrated CAD-like canvas
- satellite/image calibration
- plant metadata
- beds, containers, trellises, paths and fences
- layers
- JSON project format
- PNG/SVG/PDF/DXF export
- CSV plant lists
- harvest/tasks/succession/soil features
- MCP/AI-agent integration

### Stack / license
- Python 3.11+
- PyQt6 desktop UI
- GPL-3.0
- current repository activity observed in 2026

### Garden OS value now
The value is **higher after the normalized quarter-acre blueprint was created**, because the project already has:
- 90 × 121 ft design canvas
- bed coordinates
- greenhouse coordinates
- path geometry
- rose/vertical-feature positions
- machine-readable CSV geometry
- SVG schematic

Open Garden Planner can now be tested against a concrete design rather than a vague property concept.

### Decision
**STRONG EXTERNAL TOOL CANDIDATE / BORROW IDEAS.**

Do not copy GPL-3.0 code into a differently licensed custom app without deliberately accepting GPL obligations. Running it as a separate planning tool avoids unnecessary coupling.

### Next test
1. Recreate/import the normalized 90 × 121 ft design.
2. Compare geometry against `data/bed_inventory_v0_6.csv`.
3. Export JSON + SVG/PDF + CSV.
4. Verify lossless round-trip or record data loss.
5. Later transform the normalized plan onto the real parcel.

---

## 2. HapiCreative/jninty

### Verified capabilities
Current README describes a local-first PWA with:
- plant inventory
- journal/photos/quick log
- planting calendar
- tasks and rule-generated tasks
- garden map
- seed bank
- season/year comparison
- expenses
- search
- ZIP backup/restore
- frost alerts
- optional multi-device sync

### Architecture
- React 18 + strict TypeScript
- Vite
- PouchDB/IndexedDB
- optional CouchDB replication
- Zod
- Konva map
- Vitest
- PWA/offline

### License
MIT.

### Garden OS value now
Strong match for **daily operations + memory**, especially now that Garden OS has stable bed IDs such as K01, R1, P01, FL01 and greenhouse zones.

A good integration test should determine whether Jninty can preserve these IDs without forcing its own plant knowledge to become scientific truth.

### Decision
**STRONGEST APP-LAYER CANDIDATE.**

Keep Markdown/CSV/JSON as canonical truth even if Jninty is adopted.

---

## 3. cwfrazier1/openplantdb

### Verified capabilities
- machine-readable plant database
- JSON + CSV flat files
- frost-anchor planting model
- mature size/spacing
- germination/maturity
- PostgreSQL schema
- validation/dedupe build script
- CC0 license

### Garden OS value
Excellent generic **seed-data/schema source**, but generic values never override Richmond/Kentucky/cultivar evidence.

### Decision
**SELECTIVELY BORROW CC0 DATA/SCHEMA WITH PROVENANCE.**

---

## 4. MDeLuise/plant-it

### Verified capabilities
- plant collection
- care-event logs
- photos
- elapsed-time reminders

Its philosophy intentionally does not claim that time-since-last-water proves biological need.

### Maintenance / license
- Dart/Flutter
- GPL-3.0
- mature/stable; feature development described as slower

### Decision
**BORROW CARE-HISTORY / REMINDER UX IDEAS.**

This philosophy aligns with the Garden OS rule that timers/reminders expose reasons and never substitute for moisture/weather/plant evidence.

---

## 5. danielbrendel/hortusfox-web

### Verified capabilities
- location-based plants
- photos/notes/logs
- tasks/inventory/calendar
- search/history/weather/reminders
- backups
- REST API
- QR codes
- plant identification
- multiuser/group features

### Stack
- PHP
- MariaDB
- Docker option
- MIT per README

### Decision
**OPTIONAL MULTIUSER/API MODE.**

Do not deploy a server simply because it exists. Adopt only if household collaboration/API/QR workflows justify the extra administration.

---

## 6. FarmBot/Farmbot-Web-App

Useful as a future reference for robotic bed automation and action sequencing.

The quarter-acre Garden OS does **not** assume FarmBot-compatible geometry or robotics.

### Decision
**FUTURE RESEARCH ONLY.**

---

## 7. OpenSprinkler/OpenSprinkler-Weather

Useful reference for weather-adjusted irrigation logic.

Garden OS now has its own eight-zone hydraulic design and commissioning framework, so any OpenSprinkler-style integration must map onto:
- measured source hydraulics
- Z1–Z8
- manual overrides
- evidence-based runtime

### Decision
**OPTIONAL DETACHABLE CONTROL LAYER.**

---

# Current architecture

```text
CANONICAL GARDEN TRUTH
Markdown + CSV + JSON + SVG + photos
        |
        +--> SELF-VALIDATION
        |    scripts/validate_garden_data.py + GitHub Actions
        |
        +--> PRECISION MAP
        |    Open Garden Planner candidate
        |
        +--> DAILY OPERATIONS / JOURNAL
        |    Jninty candidate
        |
        +--> OPTIONAL COLLABORATION/API
        |    HortusFox candidate
        |
        +--> GENERIC PLANT SEED DATA
        |    OpenPlantDB, provenance-tagged and locally validated
        |
        +--> CARE-HISTORY UX
        |    Plant-it concepts
        |
        +--> WEATHER / IRRIGATION
        |    detachable control layer over Garden OS Z1–Z8
        |
        +--> FUTURE ROBOTICS
             FarmBot-class research only
```

## Non-negotiable portability rule
If every third-party application disappeared tomorrow, the user must still retain:
- 38-entry plant inventory
- bed-level map/coordinates
- greenhouse specification
- cultivar decisions
- care/harvest history
- seed inventory
- research evidence
- photos
- tasks/calendar
- irrigation zones/calibration

---

# Next software experiment

The geometry blocker is no longer conceptual; v0.7 has a concrete normalized blueprint.

Next engineering experiment should:
1. reproduce `45_VISUAL_MASTERPLAN_AND_BED_GRID.md` in Open Garden Planner
2. compare exported geometry with `data/bed_inventory_v0_6.csv`
3. model the same bed IDs/plants/tasks in Jninty
4. test backup/export recovery
5. record data loss and phone/desktop friction
6. decide whether lightweight integration is useful
7. only then consider custom Garden OS software

No software layer may become the only copy of the biological garden truth.

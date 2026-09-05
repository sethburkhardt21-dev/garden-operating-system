# Garden Operating System — v0.3

**Status:** RICHMOND SITE CONFIRMED / TWO-ACRE ARCHITECTURE / COORDINATES PROVISIONAL  
**Updated:** 2026-09-05  
**Purpose:** Turn the exact requested plant list into a living, research-backed system for planning, growing, maintaining, diagnosing, harvesting, beautifying, and improving this specific Richmond, Kentucky garden year after year.

## Site truth now locked

- **Location:** Richmond, Kentucky / Madison County
- **Property scale:** approximately 2-acre yard
- The requested garden inventory remains preserved; plants are not silently removed.
- Red roses remain the dominant rose theme; one optional white backyard rose is the only exception.
- The wildflower tub remains physically separate.
- Asparagus and rhubarb are permanent edible infrastructure.
- Herbs remain split into biologically different moisture/drainage groups.
- Canonical garden truth stays portable in Markdown + CSV + JSON.
- Third-party apps remain detachable helpers, not the only copy of the garden.

## Major v0.3 architecture change

The yard is large enough to stop treating the project like a cramped suburban bed.

The design now uses a **maintenance gradient**:
- **Ring 0:** near-house herbs/containers and frequent-use plants
- **Ring 1:** compact high-maintenance kitchen garden
- **Ring 2:** permanent edible + ornamental garden rooms
- **Ring 3:** pumpkins/squash, potatoes, garlic, rotation and expansion
- **Ring 4:** lower-frequency ecological/visual edge

The goal is **large capability without large daily walking distance**.

Two acres does **not** mean two acres should be cultivated.

## Richmond-specific research now integrated

- Madison County Extension is the primary local Extension reference.
- Madison County currently advertises free soil testing for residents, up to 10 samples per home/farm per calendar year.
- Richmond/Madison County sits across the USDA 2023 **6b–7a transition** at coarse city/ZIP scale; exact parcel half-zone remains to be pinned.
- Kentucky Central/Eastern planting windows replace the old northern-Kentucky assumption.
- The 2027 planning calendar is localized to Richmond.
- The first evidence-based plant-count/space envelope is now built from current Kentucky home-garden guidance.
- An active September–December 2026 implementation sprint is now in the repo.

## What is still provisional

The site is known, but the exact physical map still needs:
- house/property geometry
- north orientation
- mature trees/shade
- slopes and wet areas
- water/hose locations
- current beds/structures
- soil-test results
- wildlife pressure
- final cultivated footprint
- household production/preservation goals
- several cultivar/use choices

## Start here

1. `00_START_HERE.md` — current state and next gate.
2. `37_FALL_2026_RICHMOND_ACTION_PLAN.md` — what to execute now through winter.
3. `02_SITE_PROFILE.md` — confirmed Richmond/two-acre site facts + remaining inputs.
4. `03_MASTER_LAYOUT_PROVISIONAL.md` — two-acre maintenance-gradient architecture.
5. `34_RICHMOND_KY_SITE_BASELINE.md` — local climate/Extension/soil-testing research.
6. `35_TWO_ACRE_SITE_SURVEY_PROTOCOL.md` — how to convert the yard into an exact map.
7. `36_2027_PLANT_COUNT_AND_SPACE_MODEL.md` — first-year count/bed sizing framework.
8. `04_PLANT_MASTER_LEDGER.csv` — canonical requested inventory.
9. `05_PLANT_PROFILES/` — human care cards.
10. `06_ANNUAL_CALENDAR_PROVISIONAL.md` — Richmond seasonal calendar.
11. `31_CULTIVAR_MATRIX_PROVISIONAL.md` — Richmond/Kentucky-aware cultivar shortlist.
12. `32_TODAY_ENGINE.md` — simple daily operating logic.
13. `09_SOIL_PLAN.md` — site-specific soil sampling/improvement plan.
14. `10_IRRIGATION_PLAN.md` — two-acre irrigation/hydrozone architecture.
15. `12_PEST_IPM.md` — integrated pest management.
16. `13_DISEASE_PLAYBOOK.md` — symptom-first diagnosis/prevention.
17. `25_STYLE_UPGRADES.md` — two-acre style/garden-room system.
18. `27_GITHUB_REUSE_AUDIT.md` — open-source reuse analysis.
19. `28_RESEARCH_LEDGER.md` — evidence/provenance ledger.
20. `29_DECISION_LOG.md` — accepted decisions and superseded assumptions.
21. `30_OPEN_QUESTIONS.md` — remaining site/use/aesthetic questions.

## Human operating principle

Deep detail belongs in the repository. Daily operation should collapse to:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Evidence states

Every important conclusion is one of:
- `PROVISIONAL`
- `RESEARCHED`
- `SITE CONFIRMED`
- `OBSERVED IN THIS GARDEN`
- `SUPERSEDED`

When evidence changes, update current truth and preserve old reasoning in the decision/history log instead of accumulating contradictory instructions.

## Current software direction

The project is intentionally **not** becoming a monolithic custom app yet.

Current best-of-breed direction:
- precision geometry: Open Garden Planner or equivalent
- daily journal/tasks/seed bank: Jninty is the leading candidate
- machine-readable generic plant seed data: OpenPlantDB, provenance-tagged and locally validated
- collaborative/API-heavy mode: HortusFox if needed
- care-history/reminder UX: Plant-it concepts
- irrigation/weather: detachable layer
- robotics: future-only FarmBot-class research

The biological garden must remain fully usable if all software integrations disappear.

## Current highest-value next step

The location question is resolved. The physical-design bottleneck is now **site geometry**.

Use `35_TWO_ACRE_SITE_SURVEY_PROTOCOL.md` to produce a crude overhead yard sketch with:
- house
- driveway
- trees
- fences
- sheds
- north
- water points
- slopes/low spots
- candidate sunny garden core

That is enough to start converting the architecture into a scaled property plan.

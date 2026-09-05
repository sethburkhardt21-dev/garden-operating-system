# Garden Operating System — v0.2

**Status:** PROVISIONAL SITE / RESEARCHED OPERATING CORE  
**Updated:** 2026-09-05  
**Purpose:** Turn the exact requested plant list into a living, research-backed system for planning, growing, maintaining, diagnosing, harvesting, beautifying, and improving the garden year after year.

## What is locked

- The requested garden inventory is preserved; plants are not silently removed.
- Red roses remain the dominant rose theme; one optional white backyard rose is the only exception.
- The wildflower tub remains a physically separate feature.
- Asparagus and rhubarb are permanent edible infrastructure.
- Herbs are split into biologically different moisture/drainage groups.
- Canonical garden truth stays portable in Markdown + CSV + JSON.
- Third-party apps remain detachable helpers, not the only copy of the garden.

## What is still provisional

Exact property geometry, ZIP, sun map, soil test, water access, wildlife pressure, bed dimensions, and several cultivar choices are not yet site-confirmed.

A coarse working assumption suggests northern Kentucky. Any climate-specific statement remains **PROVISIONAL** until location is confirmed.

## Start here

1. `00_START_HERE.md` — project rules/current state.
2. `02_SITE_PROFILE.md` — unknowns required to lock the physical site.
3. `03_MASTER_LAYOUT_PROVISIONAL.md` — spatial architecture before exact coordinates.
4. `04_PLANT_MASTER_LEDGER.csv` — canonical requested inventory.
5. `05_PLANT_PROFILES/` — human care cards for core edibles, flowers, and herbs.
6. `06_ANNUAL_CALENDAR_PROVISIONAL.md` — seasonal operating calendar.
7. `12_PEST_IPM.md` — integrated pest management.
8. `13_DISEASE_PLAYBOOK.md` — symptom-first diagnosis/prevention.
9. `27_GITHUB_REUSE_AUDIT.md` — deep open-source reuse analysis.
10. `28_RESEARCH_LEDGER.md` — evidence/provenance ledger.
11. `30_OPEN_QUESTIONS.md` — minimal remaining site questions.
12. `31_CULTIVAR_MATRIX_PROVISIONAL.md` — Kentucky-aware cultivar shortlist.
13. `32_TODAY_ENGINE.md` — simple daily operating logic.

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

When evidence changes, update current truth and preserve the old reasoning in the decision/history log instead of accumulating contradictory instructions.

## Current software direction

The project is intentionally **not** becoming a monolithic custom app yet.

Current best-of-breed direction:
- precision geometry: Open Garden Planner or equivalent
- daily journal/tasks/seed bank: Jninty is the leading candidate
- machine-readable generic plant seed data: OpenPlantDB, provenance-tagged and locally validated
- collaborative/API-heavy mode: HortusFox if needed
- irrigation/weather: detachable layer
- robotics: future-only FarmBot-class research

The biological garden must remain fully usable if all software integrations disappear.

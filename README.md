# Garden Operating System — v0.1

**Status:** PROVISIONAL BASELINE / RESEARCH IN PROGRESS  
**Built:** 2026-09-05  
**Purpose:** Convert the exact requested plant list into a living, research-backed garden operating system that a normal human can actually run.

## Current truth

The requested plant list has been authenticated from the supplied screenshots and converted into a structured plant ledger. Nothing has been silently removed.

This version does **not** pretend to know the exact property geometry, sunlight map, soil, water pressure, deer/rabbit pressure, or exact ZIP. Those are the remaining inputs needed before the physical layout can be locked.

A coarse location estimate available to the assistant suggests **northern Kentucky**. All climate-specific material in this version is therefore marked **PROVISIONAL** until the user confirms the location. For northern Kentucky, USDA 2023 mapping commonly places the area around zones 6b/7a, but exact zone must be resolved from the actual ZIP/address.

## Open first

1. `00_START_HERE.md` — operating rules and project state.
2. `02_SITE_PROFILE.md` — what is known vs unknown.
3. `03_MASTER_LAYOUT_PROVISIONAL.md` — bed architecture before dimensions.
4. `04_PLANT_MASTER_LEDGER.csv` — canonical requested plant inventory.
5. `06_ANNUAL_CALENDAR_PROVISIONAL.md` — first seasonal operating calendar.
6. `27_GITHUB_REUSE_AUDIT.md` — software/open-source reuse findings.
7. `30_OPEN_QUESTIONS.md` — smallest set of questions needed to lock the exact design.

## Operating principle

Deep detail lives in the repo. Daily operation should be simple:

**URGENT → THIS WEEK → OPTIONAL → DO NOT TOUCH YET**

## Version rules

Every important conclusion is one of:
- PROVISIONAL
- RESEARCHED
- SITE CONFIRMED
- OBSERVED IN THIS GARDEN
- SUPERSEDED

Never append contradictions forever. Update current truth and preserve old decisions in the decision log.

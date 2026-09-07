#!/usr/bin/env python3
"""Validate Garden Operating System canonical data using only Python stdlib.

Run from repository root:
    python scripts/validate_garden_data.py

The validator checks invariants that must not silently drift:
- quarter-acre area math
- greenhouse geometry
- canonical plant IDs/count
- 2027 crop-plan coverage and key location references
- bed/zone coordinate bounds
- rotation block geometry
- required canonical files
- superseded location IDs do not reappear
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"Missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        error(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")
    return None


def load_csv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except FileNotFoundError:
        error(f"Missing CSV file: {path.relative_to(ROOT)}")
    return []


def as_float(row: dict[str, str], key: str, context: str) -> float | None:
    try:
        return float(row[key])
    except (KeyError, TypeError, ValueError):
        error(f"{context}: invalid/missing numeric field {key!r}: {row.get(key)!r}")
        return None


def check_required_files() -> None:
    required = [
        "README.md",
        "00_START_HERE.md",
        "04_PLANT_MASTER_LEDGER.csv",
        "28_RESEARCH_LEDGER.md",
        "29_DECISION_LOG.md",
        "40_DEFAULT_QUARTER_ACRE_LAYOUT.md",
        "43_2027_BED_ASSIGNMENT_AND_ROTATION.md",
        "45_VISUAL_MASTERPLAN_AND_BED_GRID.md",
        "46_ROSE_AND_FLOWER_DESIGN.md",
        "47_GREENHOUSE_EQUIPMENT_SPEC.md",
        "48_IRRIGATION_ZONE_SIZING.md",
        "49_MATERIALS_AND_PROCUREMENT_REGISTER.md",
        "50_2026_2027_MASTER_CHECKLIST.md",
        "51_AI_CONTINUATION_PROTOCOL.md",
        "data/default_layout_zones.csv",
        "data/bed_inventory_v0_6.csv",
        "data/2027_crop_plan.csv",
        "data/irrigation_zone_template.csv",
        "docs/default_quarter_acre_masterplan.svg",
        "scripts/validate_garden_data.py",
        ".github/workflows/validate-garden-data.yml",
        "garden_baseline.json",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            error(f"Required canonical file missing: {relative}")


def check_baseline() -> dict | None:
    baseline = load_json(ROOT / "garden_baseline.json")
    if not baseline:
        return None

    site = baseline.get("site", {})
    canvas = baseline.get("default_design_canvas", {})
    greenhouse = baseline.get("greenhouse", {})
    area_budget = baseline.get("area_budget_sqft", {})
    rotation = baseline.get("annual_rotation", {})

    target = site.get("garden_square_feet_target")
    width = canvas.get("width_east_west_ft")
    length = canvas.get("length_south_north_ft")

    if target != 10890:
        error(f"Garden target must remain 10,890 sq ft, got {target!r}")
    if width != 90 or length != 121:
        error(f"Default canvas must remain 90x121 ft, got {width!r}x{length!r}")
    if isinstance(width, (int, float)) and isinstance(length, (int, float)):
        if width * length != 10890:
            error(f"Default canvas area mismatch: {width} * {length} = {width * length}")

    numeric_budget = [v for v in area_budget.values() if isinstance(v, (int, float))]
    total = area_budget.get("total")
    component_sum = sum(v for k, v in area_budget.items() if k != "total" and isinstance(v, (int, float)))
    if total != 10890:
        error(f"Area budget total must be 10,890, got {total!r}")
    if component_sum != total:
        error(f"Area budget components sum to {component_sum}, but total is {total}")
    if not numeric_budget:
        error("Area budget has no numeric values")

    gh_w = greenhouse.get("default_width_ft")
    gh_l = greenhouse.get("default_length_ft")
    gh_area = greenhouse.get("default_area_sqft")
    if gh_w != 16 or gh_l != 24 or gh_area != 384:
        error(f"Greenhouse default must remain 16x24=384 sq ft, got {gh_w}x{gh_l}={gh_area}")

    coords = greenhouse.get("default_design_coordinates", {})
    try:
        coord_w = coords["x_max_ft"] - coords["x_min_ft"]
        coord_l = coords["y_max_ft"] - coords["y_min_ft"]
        if (coord_w, coord_l) != (16, 24):
            error(f"Greenhouse coordinate geometry is {coord_w}x{coord_l}, expected 16x24")
    except (KeyError, TypeError):
        error("Greenhouse default_design_coordinates missing or invalid")

    if rotation.get("block_count") != 4:
        error(f"Annual rotation must contain 4 blocks, got {rotation.get('block_count')!r}")
    if rotation.get("default_block_size_ft") != "16x16":
        error(
            "Annual rotation default_block_size_ft must be '16x16'; "
            f"got {rotation.get('default_block_size_ft')!r}"
        )
    if rotation.get("total_active_rotation_soil_sqft") != 1024:
        error(
            "Annual rotation active soil must be 1,024 sq ft; "
            f"got {rotation.get('total_active_rotation_soil_sqft')!r}"
        )

    plants = baseline.get("plants", [])
    plant_count = baseline.get("plant_count")
    ids = [p.get("id") for p in plants]
    if plant_count != 38:
        error(f"Canonical plant_count must be 38, got {plant_count!r}")
    if len(plants) != plant_count:
        error(f"Baseline contains {len(plants)} plants but plant_count says {plant_count}")
    if len(ids) != len(set(ids)):
        error("Duplicate plant IDs in garden_baseline.json")

    return baseline


def check_crop_plan(baseline: dict | None) -> None:
    rows = load_csv(ROOT / "data/2027_crop_plan.csv")
    if not rows:
        return

    ids = [row.get("plant_id") for row in rows]
    if len(ids) != len(set(ids)):
        error("Duplicate plant IDs in data/2027_crop_plan.csv")

    if baseline:
        baseline_ids = {p.get("id") for p in baseline.get("plants", [])}
        plan_ids = set(ids)
        missing = sorted(baseline_ids - plan_ids)
        extra = sorted(plan_ids - baseline_ids)
        if missing:
            error(f"2027 crop plan missing canonical plant IDs: {missing}")
        if extra:
            error(f"2027 crop plan contains unknown plant IDs: {extra}")
        if len(rows) != baseline.get("plant_count"):
            error(f"2027 crop plan has {len(rows)} rows; expected {baseline.get('plant_count')}")

    by_id = {row.get("plant_id"): row for row in rows}

    # Superseded v0.5 conceptual location IDs must never reappear in active crop locations.
    legacy_tokens = {"F02", "F03", "F04", "FL04", "FL05", "FL06", "FL07"}
    for row in rows:
        location = row.get("primary_location", "")
        for token in legacy_tokens:
            # Match whole slash/space-delimited legacy token rather than substrings of unrelated IDs.
            normalized = location.replace("/", " ").replace(",", " ").replace(";", " ")
            if token in normalized.split():
                error(
                    f"2027 crop plan {row.get('plant_id')}: primary_location uses superseded token {token}: {location!r}"
                )

    expected_location_contains = {
        "VEG-007": {"R2", "F01"},
        "VEG-010": {"R3"},
        "VEG-011": {"R1"},
        "VEG-012": {"R1"},
        "VEG-013": {"F01"},
        "FLW-001": {"RS-ENT-L", "RS-ENT-R", "RS-FOCAL"},
        "SPEC-001": {"WF-01"},
    }
    for plant_id, required_tokens in expected_location_contains.items():
        row = by_id.get(plant_id)
        if not row:
            continue
        location = row.get("primary_location", "")
        for token in required_tokens:
            if token not in location:
                error(f"{plant_id}: primary_location must include {token!r}; got {location!r}")


def check_rect_csv(path: Path, id_field: str, site_width: float = 90, site_length: float = 121) -> None:
    rows = load_csv(path)
    if not rows:
        return

    ids = [row.get(id_field) for row in rows]
    if len(ids) != len(set(ids)):
        error(f"Duplicate {id_field} values in {path.relative_to(ROOT)}")

    for row in rows:
        item_id = row.get(id_field, "<unknown>")
        context = f"{path.relative_to(ROOT)}:{item_id}"
        xmin = as_float(row, "x_min_ft", context)
        xmax = as_float(row, "x_max_ft", context)
        ymin = as_float(row, "y_min_ft", context)
        ymax = as_float(row, "y_max_ft", context)
        if None in (xmin, xmax, ymin, ymax):
            continue
        assert xmin is not None and xmax is not None and ymin is not None and ymax is not None
        if not (0 <= xmin < xmax <= site_width):
            error(f"{context}: x bounds {xmin}-{xmax} outside 0-{site_width}")
        if not (0 <= ymin < ymax <= site_length):
            error(f"{context}: y bounds {ymin}-{ymax} outside 0-{site_length}")

        if "width_ft" in row and row.get("width_ft"):
            declared = as_float(row, "width_ft", context)
            if declared is not None and abs((xmax - xmin) - declared) > 0.01:
                error(f"{context}: width {declared} != coordinate width {xmax - xmin}")
        if "length_ft" in row and row.get("length_ft"):
            declared = as_float(row, "length_ft", context)
            if declared is not None and abs((ymax - ymin) - declared) > 0.01:
                error(f"{context}: length {declared} != coordinate length {ymax - ymin}")


def check_bed_inventory() -> None:
    rows = load_csv(ROOT / "data/bed_inventory_v0_6.csv")
    by_id = {row.get("bed_id"): row for row in rows}

    required_beds = {
        "GH-01",
        "K01", "K02", "K03", "K04", "K05", "K06", "K07", "K08",
        "R1", "R2", "R3", "R4",
        "P01", "P02", "P03",
        "F01",
        "FL01", "FL02", "FL03",
        "VG-MORNING-GLORY", "VG-SWEET-PEA",
        "RS-ENT-L", "RS-ENT-R", "RS-FOCAL",
        "WF-01",
        "MAIN-SPINE", "MAIN-CROSS",
    }
    missing = sorted(required_beds - set(by_id))
    if missing:
        error(f"Bed inventory missing required canonical IDs: {missing}")

    for rid in ("R1", "R2", "R3", "R4"):
        row = by_id.get(rid)
        if not row:
            continue
        width = as_float(row, "width_ft", rid)
        length = as_float(row, "length_ft", rid)
        if (width, length) != (16.0, 16.0):
            error(f"{rid} must be 16x16 ft in v0.6+, got {width}x{length}")


def check_zone_site_row() -> None:
    rows = load_csv(ROOT / "data/default_layout_zones.csv")
    site = next((row for row in rows if row.get("zone_id") == "SITE"), None)
    if not site:
        error("data/default_layout_zones.csv missing SITE row")
        return
    area = as_float(site, "approx_area_sqft", "SITE")
    if area != 10890:
        error(f"SITE zone area must be 10,890 sq ft, got {area}")

    rotation_field = next((row for row in rows if row.get("zone_id") == "ROTATION-FIELD"), None)
    if not rotation_field:
        error("data/default_layout_zones.csv missing ROTATION-FIELD row")


def main() -> int:
    check_required_files()
    baseline = check_baseline()
    check_crop_plan(baseline)
    check_rect_csv(ROOT / "data/default_layout_zones.csv", "zone_id")
    check_rect_csv(ROOT / "data/bed_inventory_v0_6.csv", "bed_id")
    check_bed_inventory()
    check_zone_site_row()

    print("Garden OS validation")
    print("====================")
    if WARNINGS:
        print(f"Warnings: {len(WARNINGS)}")
        for message in WARNINGS:
            print(f"  WARN: {message}")
    if ERRORS:
        print(f"Errors: {len(ERRORS)}")
        for message in ERRORS:
            print(f"  ERROR: {message}")
        return 1

    print("PASS: canonical data and geometry invariants are internally consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

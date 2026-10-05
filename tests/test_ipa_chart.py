"""Tests for the curated IPA chart pass-list.

Contract: dc_ipa_reference.rst Implementation Bindings,
"Chart membership filter" — membership is INTERSECTION with the
vendored PHOIBLE shared-symbol set, never heuristic approximation.

The chart file (data/ipa_chart.json) is CURATED: hand-transcribed
from the IPA chart (1999 Handbook; 2015 rendering). Curation is
checked, not trusted: every symbol must exist as a features row
in the vendored PHOIBLE data. A typo'd or hallucinated spelling
fails here, by name, before it can pollute ipa_reference.json.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CHART_FILE = ROOT / "data" / "ipa_chart.json"
VENDOR_FEATURES = (
    ROOT / "vendor" / "phoible-2.0" / "phoible-dev-862bec9"
    / "raw-data" / "FEATURES" / "phoible-segments-features.tsv"
)

# Groups mirror the chart's own sections. Fixed-cell symbols only:
# affricates/ejectives are separate decisions (see chart file notes).
EXPECTED_GROUPS = (
    "pulmonic_consonants",
    "affricates",
    "non_pulmonic_consonants",
    "vowels",
    "other_symbols",
)

VENDORED = VENDOR_FEATURES.is_file()

requires_vendor = pytest.mark.skipif(
    not VENDORED, reason="vendored PHOIBLE data absent")


def load_chart() -> dict:
    with open(CHART_FILE, encoding="utf-8") as f:
        return json.load(f)


def vendor_feature_symbols() -> set[str]:
    """All symbols with a features row. The symbol column is read
    BY POSITION (first column) — no remembered column names."""
    with open(VENDOR_FEATURES, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        symbol_col = reader.fieldnames[0]
        return {row[symbol_col] for row in reader}


def chart_symbols(chart: dict) -> list[str]:
    return [s for g in EXPECTED_GROUPS for s in chart.get(g, [])]


# --- Schema -------------------------------------------------------

def test_chart_file_exists():
    """The pass-list is a committed repo artifact (bundling decision)."""
    assert CHART_FILE.is_file(), "data/ipa_chart.json missing"


def test_chart_schema():
    """Provenance block + the four chart groups, all string lists."""
    chart = load_chart()
    assert chart["schema_version"] == "1.0"
    assert chart["pinned_sources"]["ipa_chart_year"] == "2015"
    assert chart["pinned_sources"]["ipa_handbook"] == "1999"
    assert "attribution" in chart
    for group in EXPECTED_GROUPS:
        assert group in chart, f"group {group!r} missing"
        assert all(isinstance(s, str) and s
                   for s in chart[group]), f"{group}: non-string/empty entry"


def test_no_duplicate_symbols():
    """Curation is a set: duplicates are transcription slips."""
    symbols = chart_symbols(load_chart())
    dupes = {s for s in symbols if symbols.count(s) > 1}
    assert not dupes, f"duplicated chart symbols: {sorted(dupes)}"


# --- Intersection with PHOIBLE (the curation check) ---------------

@requires_vendor
def test_every_chart_symbol_has_phoible_features():
    """The intersection guarantee. Failure output IS the curation
    typo report — the offending spellings are listed by name."""
    vendor = vendor_feature_symbols()
    missing = [s for s in chart_symbols(load_chart())
               if s not in vendor]
    assert not missing, (
        "chart symbols with no PHOIBLE features row "
        "(spelling error — verify against the chart and the "
        "vendor TSV): " + ", ".join(missing)
    )

def test_deferred_documented():
    """Chart-canonical symbols awaiting PHOIBLE features (F-3).
    Each carries a reason string — pending is stated, never silent."""
    chart = load_chart()
    deferred = chart.get("deferred", {})
    for symbol, reason in deferred.items():
        assert isinstance(reason, str) and reason, (
            f"deferred symbol {symbol!r} lacks a reason"
        )

@requires_vendor
def test_deferred_symbols_are_genuinely_featureless():
    """Anti-abuse guard: a deferred symbol that HAS vendor features
    is misfiled — it belongs in an emission group, not parking."""
    vendor = vendor_feature_symbols()
    chart = load_chart()
    misplaced = [s for s in chart.get("deferred", {}) if s in vendor]
    assert not misplaced, (
        "deferred but features exist (move to emission group): "
        + ", ".join(misplaced)
    )

"""Tests for the mini-fixture regeneration script (test-first).

Regeneration contract (dc_ipa_reference.rst, Implementation
Bindings, Specimen roster): the mini fixtures are GENERATED,
not authored — rows sliced verbatim from the vendored PHOIBLE
files, real counts, true headers, zero invented values.

Two-file shape: the real pipeline reads two sources (features
TSV + phonemes listing) and joins them, so a pre-joined single
fixture would hide the join, the pair-dedup, and the
denominator count from testing.

Vendor note: vendor/phoible-2.0/ is local-only (PROVENANCE.txt
is the tracked file), so vendor-dependent tests SKIP when the
data is absent — CI machines see only the vendor-independent
half validating the committed artifacts.

Sources of truth:
- Roster: dc_ipa_reference.rst, Specimen roster binding
- Dedup rule: AGENTS.md, Trumped-Denominator Recipe
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from scripts.regenerate_mini_fixture import (
    MINI_UNIVERSE_SIZE,
    EXPECTED_FEATURE_HEADER,
    EXPECTED_LISTING_HEADER,
)

FIXTURES = Path(__file__).parent / "fixtures"
FEATURES_FIXTURE = FIXTURES / "phoible_mini_features.tsv"
ATTESTATION_FIXTURE = FIXTURES / "phoible_mini_attestation.tsv"

# Repo root: tests/ -> LatticeLang/
VENDOR = (Path(__file__).resolve().parents[1] / "vendor"
          / "phoible-2.0" / "phoible-dev-862bec9")
FEATURES_SRC = (VENDOR / "raw-data" / "FEATURES"
                / "phoible-segments-features.tsv")
LISTING_SRC = (VENDOR / "gold-standard"
               / "phoible-phonemes.tsv")

# Roster per dc_ipa_reference Implementation Bindings: p b t i a,
# the t+esh affricate (proves plain-sequence rows flow), long a,
# syllabic m, plus the five tone letters (prove toneme routing).
# \u escapes: clipboard round-trips cannot mangle the codepoints.
ROSTER = [
    "p", "b", "t", "i", "a",
    "t\u0320\u0283",                    # t + dental/minuscule-below + esh
    "a\u02d0",                          # a + length mark
    "m\u0329",                          # m + syllabic mark
    "\u02e5", "\u02e6", "\u02e7", "\u02e8", "\u02e9",  # tone letters
]

VENDORED = FEATURES_SRC.is_file() and LISTING_SRC.is_file()
requires_vendor = pytest.mark.skipif(
    not VENDORED, reason="vendored PHOIBLE data absent (local-only)")


def read_tsv(path: Path) -> tuple[list[str], list[dict]]:
    """Return (header, rows) of a TSV, DictReader-parsed."""
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        header = list(reader.fieldnames or [])
        return header, list(reader)


# --- Vendor-independent: validate the committed artifacts -------

def test_features_header_is_the_real_38():
    """Header equals the script's pinned header AND is 38 cols."""
    header, _ = read_tsv(FEATURES_FIXTURE)
    assert header == EXPECTED_FEATURE_HEADER
    assert len(header) == 38
    assert header[0] == "segment"


def test_no_invented_columns_survive():
    """The old fabricated schema's ghost columns are all absent."""
    header, _ = read_tsv(FEATURES_FIXTURE)
    ghosts = {"place", "manner", "voice", "inventory_count",
              "sonority_rank", "height", "backness", "roundedness"}
    assert ghosts.isdisjoint(header), sorted(ghosts & set(header))


def test_roster_exact():
    """Segments are exactly the 13 roster symbols, no strays."""
    _, rows = read_tsv(FEATURES_FIXTURE)
    segments = [r["segment"] for r in rows]
    assert set(segments) == set(ROSTER)
    assert len(segments) == len(set(ROSTER)) == 13


def test_feature_values_are_controlled_vocab():
    """Every feature cell is '+', '-', or '0' (ADR-033)."""
    _, rows = read_tsv(FEATURES_FIXTURE)
    for row in rows:
        for feat in EXPECTED_FEATURE_HEADER[1:]:
            assert row[feat] in ("+", "-", "0"), (
                f"{row['segment']}.{feat} = {row[feat]!r}")


def test_attestation_header_is_the_listing_header():
    """Attestation slice carries the listing's real 11 columns."""
    header, _ = read_tsv(ATTESTATION_FIXTURE)
    assert header == EXPECTED_LISTING_HEADER


def test_attestation_pairs_are_unique():
    """(InventoryID, Phoneme) dedup: no inflated counts (AGENTS
    Trumped-Denominator Recipe)."""
    _, rows = read_tsv(ATTESTATION_FIXTURE)
    pairs = [(r["InventoryID"], r["Phoneme"]) for r in rows]
    assert len(pairs) == len(set(pairs))


def test_attestation_covers_only_roster():
    """No non-roster symbol leaked into the slice."""
    _, rows = read_tsv(ATTESTATION_FIXTURE)
    assert {r["Phoneme"] for r in rows} <= set(ROSTER)


def test_mini_denominator_within_universe_bound():
    """Distinct InventoryIDs in the slice: sane, within universe."""
    _, rows = read_tsv(ATTESTATION_FIXTURE)
    ids = {r["InventoryID"] for r in rows}
    assert 1 <= len(ids) <= MINI_UNIVERSE_SIZE


# --- Vendor-gated: re-verify against source when data exists ----

@requires_vendor
def test_pinned_headers_match_vendor_files():
    """The constants the fixtures are checked against are REAL —
    the layered truth: constant <- vendor, fixture <- constant."""
    feat_header, _ = read_tsv(FEATURES_SRC)
    list_header, _ = read_tsv(LISTING_SRC)
    assert EXPECTED_FEATURE_HEADER == feat_header
    assert EXPECTED_LISTING_HEADER == list_header


@requires_vendor
def test_feature_rows_sliced_verbatim():
    """Each fixture row equals its source row, cell for cell."""
    _, src_rows = read_tsv(FEATURES_SRC)
    src = {r["segment"]: r for r in src_rows}
    _, fx_rows = read_tsv(FEATURES_FIXTURE)
    for row in fx_rows:
        assert row == src[row["segment"]], row["segment"]


@requires_vendor
def test_full_trumped_denominator_is_2155():
    """Regression pin, verified 2026-10-01 (AGENTS.md recipe).
    If this trips, the vendored data CHANGED — re-run the
    PROVENANCE chain-of-custody checks; do not 'fix' the number."""
    _, rows = read_tsv(LISTING_SRC)
    assert len({r["InventoryID"] for r in rows}) == 2155


@requires_vendor
def test_mini_counts_match_independent_recount():
    """Independent recount: per-symbol distinct-InventoryID counts
    over the first MINI_UNIVERSE_SIZE distinct inventories in
    listing order must equal counts computed from the fixture.
    Different code path than the script's — output beats output."""
    _, rows = read_tsv(LISTING_SRC)
    universe: list[str] = []
    seen: set[str] = set()
    for r in rows:
        inv = r["InventoryID"]
        if inv not in seen:
            seen.add(inv)
            if len(universe) < MINI_UNIVERSE_SIZE:
                universe.append(inv)
    uni = set(universe)
    expected = {
        s: len({r["InventoryID"] for r in rows
                if r["Phoneme"] == s and r["InventoryID"] in uni})
        for s in ROSTER}
    _, fx = read_tsv(ATTESTATION_FIXTURE)
    actual = {
        s: len({r["InventoryID"] for r in fx if r["Phoneme"] == s})
        for s in ROSTER}
    assert actual == expected
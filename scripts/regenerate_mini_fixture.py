"""Regenerate the mini PHOIBLE fixtures from vendored real data.

Contract (dc_ipa_reference.rst, Implementation Bindings, Specimen
roster; AGENTS.md, Fixture Doctrine): the mini fixtures are
GENERATED, never authored. Rows are sliced verbatim from the
vendored PHOIBLE 2.0 files; every count is computed from real
rows; the headers are the true headers. Zero invented values.

Two-file shape (Option A): the real derive pipeline reads two
sources — the segments-features TSV and the gold-standard
phonemes listing — and joins them with (InventoryID, Phoneme)
pair dedup. A pre-joined single fixture would hide that join
from testing, so the fixture mirrors the two-source shape:

  tests/fixtures/phoible_mini_features.tsv
      verbatim 38-column rows for the roster symbols
  tests/fixtures/phoible_mini_attestation.tsv
      verbatim 11-column listing rows for the roster symbols,
      restricted to the first MINI_UNIVERSE_SIZE distinct
      InventoryIDs in listing order (a deterministic real
      universe, not a random sample)

Headers are validated loudly against the vendored files before
anything is written: if the vendor data changed shape, this
script raises, it never adapts silently.

Usage:
    poetry run python -m scripts.regenerate_mini_fixture --write

Without --write, prints the summary and writes nothing (dry run).
The committed fixtures change only via an explicit --write run.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

# The true 38-column header, transcribed from
# `head -1 .../phoible-segments-features.tsv` (verified by
# count 2026-10-01; vendor-gated tests pin it to the live file).
# 'segment' is the symbol key; the other 37 are feature columns
# with controlled values '+'/'-'/'0' (ADR-033).
from latticelang.core.feature_vocabulary import FEATURE_HEADER_ORDER

# Repo root: scripts/ -> LatticeLang/
REPO_ROOT = Path(__file__).resolve().parents[1]

VENDOR = (REPO_ROOT / "vendor" / "phoible-2.0"
          / "phoible-dev-862bec9")
FEATURES_SRC = (VENDOR / "raw-data" / "FEATURES"
                / "phoible-segments-features.tsv")
LISTING_SRC = (VENDOR / "gold-standard" / "phoible-phonemes.tsv")

FIXTURES_DIR = REPO_ROOT / "tests" / "fixtures"
FEATURES_FIXTURE = FIXTURES_DIR / "phoible_mini_features.tsv"
ATTESTATION_FIXTURE = FIXTURES_DIR / "phoible_mini_attestation.tsv"

# The true 38-column header — single source of truth is
# feature_vocabulary.FEATURE_HEADER_ORDER (shared with
# Phoneme validation). This list adapter exists for
# list-vs-list equality with read_tsv output (a tuple never
# equals a list in Python) and for csv.DictWriter, which wants
# a mutable sequence.
EXPECTED_FEATURE_HEADER = list(FEATURE_HEADER_ORDER)

# The true 11-column listing header, likewise transcribed from
# `head -1 .../phoible-phonemes.tsv`. Field 1 is InventoryID
# (the denominator column); field 8 is Phoneme (NOT GlyphID,
# field 7 — the 0-overlap crisis lineage; see AGENTS.md).
EXPECTED_LISTING_HEADER = [
    "InventoryID", "Source", "LanguageCode", "LanguageName",
    "Trump", "PhonemeID", "GlyphID", "Phoneme", "Class",
    "CombinedClass", "NumOfCombinedGlyphs",
]

# Specimen roster per dc_ipa_reference Implementation Bindings:
# p b t i a (core), t+esh affricate (plain sequences flow as
# ordinary rows), long a and syllabic m (real derive cases),
# and the five tone letters (toneme routing). \u escapes so no
# clipboard round-trip can mangle the codepoints.
ROSTER = [
    "p", "b", "t", "i", "a",
    "t\u0320\u0283",
    "a\u02d0",
    "m\u0329",
    "\u02e5", "\u02e6", "\u02e7", "\u02e8", "\u02e9",
]

# The attestation slice draws from the first MINI_UNIVERSE_SIZE
# distinct InventoryIDs in listing order: a deterministic, real
# sub-universe. The mini denominator is COUNTED from the slice,
# never asserted. 100 keeps the committed file small while
# giving every roster symbol a fighting chance of attestation.
MINI_UNIVERSE_SIZE = 100


def read_tsv(path: Path) -> tuple[list[str], list[dict]]:
    """Return (header, rows) of a TSV, DictReader-parsed."""
    if not path.is_file():
        raise FileNotFoundError(
            f"vendored PHOIBLE data not found: {path}\n"
            f"(vendor/ ships with the repo per the bundling "
            f"decision — see MANIFEST.in; custody record in "
            f"vendor/phoible-2.0/PROVENANCE.txt)")
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        header = list(reader.fieldnames or [])
        return header, list(reader)


def require_header(actual: list[str], expected: list[str],
                   path: Path) -> None:
    """Fail loud if the vendored file's header changed shape."""
    if actual != expected:
        raise ValueError(
            f"Header mismatch for {path.name}.\n"
            f"The vendored data does not match the pinned schema.\n"
            f"Re-run the PROVENANCE chain-of-custody checks; "
            f"do not edit the expected header to fit.\n"
            f"  actual:   {actual}\n"
            f"  expected: {expected}")


def slice_features() -> list[dict]:
    """Verbatim feature rows for the roster, source order kept.

    Raises KeyError-equivalent (loud) if any roster symbol is
    absent from the features file — a missing specimen is a
    contract change, not a skip.
    """
    header, rows = read_tsv(FEATURES_SRC)
    require_header(header, EXPECTED_FEATURE_HEADER, FEATURES_SRC)

    by_segment: dict[str, dict] = {}
    for row in rows:
        seg = row["segment"]
        if seg in by_segment:
            raise ValueError(
                f"Duplicate segment row in features file: {seg!r}. "
                f"The vendored data changed shape; investigate.")
        by_segment[seg] = row

    missing = [s for s in ROSTER if s not in by_segment]
    if missing:
        raise ValueError(
            f"Roster symbols absent from features file: {missing!r}. "
            f"Update the roster in BOTH this script and "
            f"dc_ipa_reference.rst, or the vendor data changed.")
    return [by_segment[s] for s in ROSTER]


def build_mini_universe(rows: list[dict]) -> list[str]:
    """First MINI_UNIVERSE_SIZE distinct InventoryIDs, listing order."""
    universe: list[str] = []
    seen: set[str] = set()
    for row in rows:
        inv = row["InventoryID"]
        if inv not in seen:
            seen.add(inv)
            if len(universe) < MINI_UNIVERSE_SIZE:
                universe.append(inv)
    return universe


def slice_attestation() -> tuple[list[dict], list[str]]:
    """Verbatim listing rows for roster symbols inside the mini
    universe, with (InventoryID, Phoneme) pairs deduplicated —
    repeated rows within one inventory must not survive into
    the slice (AGENTS.md, Trumped-Denominator Recipe).

    Returns (rows, universe).
    """
    header, rows = read_tsv(LISTING_SRC)
    require_header(header, EXPECTED_LISTING_HEADER, LISTING_SRC)

    universe = build_mini_universe(rows)
    uni = set(universe)
    roster = set(ROSTER)

    out: list[dict] = []
    seen_pairs: set[tuple[str, str]] = set()
    for row in rows:
        inv, ph = row["InventoryID"], row["Phoneme"]
        if inv in uni and ph in roster and (inv, ph) not in seen_pairs:
            seen_pairs.add((inv, ph))
            out.append(row)
    return out, universe


def write_tsv(path: Path, header: list[str],
              rows: list[dict]) -> None:
    """Write rows under header, tab-delimited, UTF-8, LF endings."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header,
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def summarize(feature_rows: list[dict], attestation_rows: list[dict],
              universe: list[str]) -> str:
    """Human-readable summary — printed on every run."""
    lines = [
        f"mini universe: first {len(universe)} distinct InventoryIDs "
        f"in listing order (target {MINI_UNIVERSE_SIZE})",
        f"features rows: {len(feature_rows)} (roster size "
        f"{len(ROSTER)})",
        f"attestation rows: {len(attestation_rows)} "
        f"(post pair-dedup)",
    ]
    counts = {s: 0 for s in ROSTER}
    for row in attestation_rows:
        counts[row["Phoneme"]] += 1
    for sym in ROSTER:
        lines.append(f"  {sym!r}: attested in {counts[sym]} "
                     f"of {len(universe)} mini universes")
    lines.append(
        "NOTE: 0-attestation symbols are legitimately absent from "
        "the mini universe — counts are computed facts, not presence "
        "requirements.")
    return "\n".join(lines)


def main(write: bool) -> int:
    feature_rows = slice_features()
    attestation_rows, universe = slice_attestation()

    print(summarize(feature_rows, attestation_rows, universe))

    if not write:
        print("\n(dry run — no files written; pass --write to emit)")
        return 0

    write_tsv(FEATURES_FIXTURE, EXPECTED_FEATURE_HEADER, feature_rows)
    write_tsv(ATTESTATION_FIXTURE, EXPECTED_LISTING_HEADER,
              attestation_rows)
    print(f"\nwrote {FEATURES_FIXTURE.relative_to(REPO_ROOT)}")
    print(f"wrote {ATTESTATION_FIXTURE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Regenerate mini PHOIBLE fixtures from "
                    "vendored real data.")
    parser.add_argument(
        "--write", action="store_true",
        help="Write the fixture files (default: dry run)")
    args = parser.parse_args()
    raise SystemExit(main(args.write))

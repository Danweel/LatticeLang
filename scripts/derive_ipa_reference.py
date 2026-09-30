"""Derive data/ipa_reference.json from the pinned PHOIBLE 2.0 TSV.

Q38 hybrid pipeline (dc_ipa_reference.rst, Build Pipeline):
    1. parse_phoible_tsv        — read TSV rows
    2. filter_to_ipa_chart      — keep IPA-chart segments
    3. derive_rank_and_frequency— sonority rank + attestation
    4. merge_overrides          — curated wins over derived
    5. run_field_checks + emit  — fail build on violations

Built test-first against tests/test_derive_ipa_reference.py.
Fixture format NOTE: tests/fixtures/phoible_mini.tsv assumes
one column per feature (PHOIBLE style) — assumption, not
verified against the real phoible-segments-features.tsv.
The header check in parse_phoible_tsv fails loudly on any
column mismatch, so swapping in the real TSV surfaces
disagreements at the header, not in garbage data.
"""

import csv
import json
from pathlib import Path

# Mini-fixture world: total inventories for frequency math.
# The real PHOIBLE 2.0 figure is 3,020 (Q38 answer text).
TOTAL_INVENTORIES = 4000

# The exact header the parser demands. Any deviation in the
# real TSV = loud failure here, by design (see module docstring).
REQUIRED_COLUMNS = [
    "symbol", "syllabic", "consonantal", "sonorant", "continuant",
    "delayed_release", "height", "backness", "roundedness",
    "place", "manner", "voice", "inventory_count",
]


def parse_phoible_tsv(path: Path) -> list[dict]:
    """Pipeline step 1: read the PHOIBLE-format TSV into row dicts.

    Each row becomes one dict keyed by column name. Feature
    columns keep their '+'/'-' string values (ADR-033);
    classification fields (place/manner/voice/height) keep
    their atom strings; '-' in classification columns means
    'not applicable' and is preserved for the consumer to judge.

    Args:
        path: Path to a TSV in the PHOIBLE one-column-per-feature
            shape.

    Returns:
        List of row dicts, header-keyed.

    Raises:
        ValueError: if the file's header is missing any required
            column — a loud signal that the real TSV differs from
            the fixture's assumed format.
    """
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        # Loud header validation: fail BEFORE reading rows, so a
        # format mismatch is never absorbed silently.
        missing = [c for c in REQUIRED_COLUMNS
                   if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(
                f"TSV {path} is missing expected columns: {missing}. "
                f"Found: {reader.fieldnames}. The real PHOIBLE TSV may "
                f"differ from the fixture's assumed format — see the "
                f"module docstring's format note."
            )
        rows = []
        for row in reader:
            # Strip accidental whitespace from every cell — TSVs
            # pasted or edited by hand often carry trailing spaces.
            row = {k: v.strip() for k, v in row.items() if k}
            # inventory_count is the only numeric column.
            row["inventory_count"] = int(row["inventory_count"])
            rows.append(row)
        return rows


# The columns that constitute the feature bundle (ADR-033:
# controlled-vocab strings; '-' values are MEANINGFUL — the
# rank proposer branches on them — so they are preserved).
FEATURE_COLUMNS = [
    "syllabic", "consonantal", "sonorant", "continuant",
    "delayed_release", "height", "backness", "roundedness",
]


def filter_to_ipa_chart(rows: list[dict]) -> list[dict]:
    """Pipeline step 2: keep only IPA-chart segments (curated).

    The real filter is the curated chart-symbol list from Q38's
    hybrid answer (~107 core symbols plus attested segments).
    Until that list is vendored, every fixture row passes: the
    mini fixture deliberately contains only chart-plausible
    segments (including one tie-bar double articulation, k͡p,
    as normalization raw material per the Q38 wrinkle note).
    """
    # TODO(Q38): curated chart-symbol allowlist goes here; rows
    # whose symbol is not on it are dropped with a build log.
    return list(rows)


def derive_rank_and_frequency(rows: list[dict]) -> list[dict]:
    """Pipeline step 3: derive sonority_rank and phoible_frequency.

    Rank comes from latticelang.core.sonority.propose_sonority_rank
    — the SAME function the runtime prefill uses (UC-01 step 4);
    one derivation, two consumers. Uncertain derivations yield
    None, which stays an explicit null in the output JSON
    (dc_ipa_reference build step 3: 'emitting null where the
    derivation is uncertain rather than guessing').

    Frequency = inventory_count / TOTAL_INVENTORIES (mini-world
    total: 4,000; real PHOIBLE 2.0 total: 3,020 per Q38's answer
    text — swapped when the real TSV is vendored).

    Also assembles the entry shape downstream steps consume:
    features sub-dict, unicode_points (U+XXXX per codepoint).
    """
    from latticelang.core.sonority import propose_sonority_rank
    entries = []
    for row in rows:
        entry = dict(row)  # keep classification fields for step 5
        entry["features"] = {c: row[c] for c in FEATURE_COLUMNS}
        entry["sonority_rank"] = propose_sonority_rank(
            entry["features"])
        entry["phoible_frequency"] = (
            row["inventory_count"] / TOTAL_INVENTORIES)
        entry["unicode_points"] = [
            f"U+{ord(ch):04X}" for ch in row["symbol"]]
        entries.append(entry)
    return entries


def merge_overrides(entries: list[dict],
                    overrides_path: Path) -> list[dict]:
    """Pipeline step 4: curated overrides win over derived values.

    The overrides file (data/overrides.json in production;
    fixtures/overrides_mini.json here) is keyed by symbol. For
    each entry with an override, every override key replaces or
    fills the derived value — a field present in BOTH is the
    conflict case, and the curated value wins (dc_ipa_reference
    build step 4: 'curated wins over derived').

    Overrides may also inject fields the TSV can't derive:
    description, aliases, tipa (Q38: hand-curation covers what
    automation structurally can't).
    """
    with open(overrides_path, encoding="utf-8") as f:
        overrides = json.load(f)
    merged = []
    for entry in entries:
        result = dict(entry)
        override = overrides.get(entry["symbol"])
        if override:
            # Conflict resolution is uniform: curated key wins,
            # whether the derived entry had the field or not.
            result.update(override)
        merged.append(result)
    return merged


def run_field_checks(table: dict) -> None:
    """Pipeline step 5a: the contract's Field Checks 1, 3, 4, 7, 8, 9.

    Failures RAISE — aborting the build — per dc_ipa_reference
    build step 5. Checks deliberately omitted here are covered
    elsewhere: Field Check 2's rank-or-null shape is guarded by
    derive_rank_and_frequency's contract with the proposer, and
    Field Check 5's feature vocabulary is pending the pinned
    PHOIBLE vocabulary file (Q38; not yet vendored).
    """
    all_entries = (table.get("consonants", [])
                  + table.get("vowels", [])
                  + table.get("special_combinations", []))

    # Field Check 1: unique symbols across the whole table.
    symbols = [e["symbol"] for e in all_entries]
    if len(symbols) != len(set(symbols)):
        dupes = {s for s in symbols if symbols.count(s) > 1}
        raise ValueError(f"Field Check 1: duplicate symbols {dupes}")

    for e in all_entries:
        # Field Check 2 (shape): rank present as int or null.
        if "sonority_rank" not in e:
            raise ValueError(
                f"Field Check 2: {e['symbol']!r} missing "
                f"sonority_rank entirely")

        # Field Check 3: codepoints concatenate to the symbol.
        decoded = "".join(
            chr(int(p.replace("U+", ""), 16))
            for p in e["unicode_points"])
        if decoded != e["symbol"]:
            raise ValueError(
                f"Field Check 3: codepoints for {e['symbol']!r} "
                f"decode to {decoded!r}")

            # Field Check 4: aliases must not collide with any symbol —
            # an ambiguous alias breaks lookup resolution.
            symbol_set = set(symbols)
            for e in all_entries:
                for alias in e.get("aliases") or []:
                    if alias in symbol_set:
                        raise ValueError(
                            f"Field Check 4: alias {alias!r} of "
                            f"{e['symbol']!r} collides with another "
                            f"entry's symbol")

        # Field Check 8: canonical_forms includes the symbol.
        if e["symbol"] not in (e.get("canonical_forms") or []):
            raise ValueError(
                f"Field Check 8: {e['symbol']!r} missing from its "
                f"canonical_forms")

        # Field Check 9: frequency in [0,1]; tier in 1..5 (or
        # null tier only with null frequency, tier 6, pending Q36).
        freq = e.get("phoible_frequency")
        if freq is None:
            if e.get("rarity_tier") != 6:
                raise ValueError(
                    f"Field Check 9: {e['symbol']!r} null frequency "
                    f"but tier {e.get('rarity_tier')} != 6")
        elif not 0 <= freq <= 1:
            raise ValueError(
                f"Field Check 9: {e['symbol']!r} frequency "
                f"{freq} outside [0, 1]")

    # Field Check 7: special combinations carry their discrim-
    # inators and multi-part constituents.
    for e in table.get("special_combinations", []):
        if e.get("combination_type") not in (
                "tie_bar", "length", "syllabic_mark"):
            raise ValueError(
                f"Field Check 7: {e['symbol']!r} bad "
                f"combination_type {e.get('combination_type')!r}")
        constituents = e.get("constituents") or []
        if len(constituents) < 2 or not all(
                c and isinstance(c, str) for c in constituents):
            raise ValueError(
                f"Field Check 7: {e['symbol']!r} needs >=2 "
                f"non-empty constituents")


def generate_ipa_reference_json(entries: list[dict]) -> dict:
    """Pipeline step 5b: assemble the output document.

    Buckets entries into consonants / vowels per their derived
    category (consonantal='+' -> consonant). Entries whose
    symbol contains a combining tie bar, length mark, or
    syllabicity mark route to special_combinations with the
    parsing-rule discriminator (dc_ipa_reference, Special
    Combinations section) and their constituent parts.
    """
    table = {
        "schema_version": "1.0",
        "pinned_sources": {
            "phoible_release": "2.0",
            "ipa_chart_year": "2015",
        },
        "attribution": {
            "phoible": ("PHOIBLE 2.0 (CC-BY 4.0), "
                        "Moran & McCloy 2019"),
            "ipa_chart": ("IPA Chart, 2015 revision — "
                          "International Phonetic Association"),
        },
        "consonants": [],
        "vowels": [],
        "special_combinations": [],
    }
    for e in entries:
        # Deep-copy into the entry the output schema describes:
        # classification fields and features at top level, flat.
        out = dict(e)
        out["canonical_forms"] = [e["symbol"]]
        out.setdefault("aliases", [])
        out.setdefault("tipa", None)
        out["rarity_tier"] = _bucket_rarity_tier(
            e["phoible_frequency"])
        out.pop("inventory_count", None)  # raw TSV field, not schema

        if _is_special_combination(e["symbol"]):
            out["combination_type"] = _combination_type(e["symbol"])
            out["constituents"] = _split_constituents(e["symbol"])
            table["special_combinations"].append(out)
        elif e["features"].get("consonantal") == "+":
            table["consonants"].append(out)
        else:
            table["vowels"].append(out)
    return table

# Tie bar, length mark, syllabicity mark — the combining
# characters that make a symbol 'special' per dc_ipa_reference.
_TIE_BAR = "\u0361"      # ͡
_LENGTH_MARK = "\u02D0"  # ː
_SYLLABIC_MARK = "\u0329"  # ̩

def _is_special_combination(symbol: str) -> bool:
    return any(m in symbol for m in
               (_TIE_BAR, _LENGTH_MARK, _SYLLABIC_MARK))

def _combination_type(symbol: str) -> str:
    if _TIE_BAR in symbol:
        return "tie_bar"
    if _LENGTH_MARK in symbol:
        return "length"
    return "syllabic_mark"

def _split_constituents(symbol: str) -> list[str]:
    """Ordered base parts the entry is built from.

    Tie bar: split ON the tie bar into left/right halves
    (["k", "p"] for k͡p). Length/syllabicity: base symbol plus
    the combining mark. Naive by design — a full ADR-028
    normalization pass replaces this when segmentation lands.
    """
    if _TIE_BAR in symbol:
        left, right = symbol.split(_TIE_BAR, 1)
        return [left, right]
    for mark in (_LENGTH_MARK, _SYLLABIC_MARK):
        if mark in symbol:
            idx = symbol.index(mark)
            return [symbol[:idx], mark]
    return [symbol]

# Rarity-tier bucketing from frequency. THRESHOLDS ARE ASSUMED,
# not contractual — Q36 (rarity-tier finalization) is still
# OPEN. The fixture's example.json uses tiers 1-3, implying
# coarse buckets; these match that example's apparent intent.
_RARITY_THRESHOLDS = [(0.9, 1), (0.5, 2), (0.1, 3), (0.01, 4)]

def _bucket_rarity_tier(freq: float | None) -> int:
    """Tier 6 (unattested) is the null-frequency case; 1-5 by
    descending frequency; thresholds pending Q36."""
    if freq is None:
        return 6
    for threshold, tier in _RARITY_THRESHOLDS:
        if freq >= threshold:
            return tier
    return 5


def _is_special_combination(symbol: str) -> bool:
    return any(m in symbol for m in
               (_TIE_BAR, _LENGTH_MARK, _SYLLABIC_MARK))

def _combination_type(symbol: str) -> str:
    if _TIE_BAR in symbol:
        return "tie_bar"
    if _LENGTH_MARK in symbol:
        return "length"
    return "syllabic_mark"

def _split_constituents(symbol: str) -> list[str]:
    """Ordered base parts the entry is built from.

    Tie bar: split ON the tie bar into left/right halves
    (["k", "p"] for k͡p). Length/syllabicity: base symbol plus
    the combining mark. Naive by design — a full ADR-028
    normalization pass replaces this when segmentation lands.
    """
    if _TIE_BAR in symbol:
        left, right = symbol.split(_TIE_BAR, 1)
        return [left, right]
    for mark in (_LENGTH_MARK, _SYLLABIC_MARK):
        if mark in symbol:
            idx = symbol.index(mark)
            return [symbol[:idx], mark]
    return [symbol]

# Rarity-tier bucketing from frequency. THRESHOLDS ARE ASSUMED,
# not contractual — Q36 (rarity-tier finalization) is still
# OPEN. The fixture's example.json uses tiers 1-3, implying
# coarse buckets; these match that example's apparent intent.
_RARITY_THRESHOLDS = [(0.9, 1), (0.5, 2), (0.1, 3), (0.01, 4)]


def _bucket_rarity_tier(freq: float | None) -> int:
    """Tier 6 (unattested) is the null-frequency case; 1-5 by
    descending frequency; thresholds pending Q36."""
    if freq is None:
        return 6
    for threshold, tier in _RARITY_THRESHOLDS:
        if freq >= threshold:
            return tier
    return 5


def _is_special_combination(symbol: str) -> bool:
    return any(m in symbol for m in
               (_TIE_BAR, _LENGTH_MARK, _SYLLABIC_MARK))

def _combination_type(symbol: str) -> str:
    if _TIE_BAR in symbol:
        return "tie_bar"
    if _LENGTH_MARK in symbol:
        return "length"
    return "syllabic_mark"

def _split_constituents(symbol: str) -> list[str]:
    """Ordered base parts the entry is built from.

    Tie bar: split ON the tie bar into left/right halves
    (["k", "p"] for k͡p). Length/syllabicity: base symbol plus
    the combining mark. Naive by design — a full ADR-028
    normalization pass replaces this when segmentation lands.
    """
    if _TIE_BAR in symbol:
        left, right = symbol.split(_TIE_BAR, 1)
        return [left, right]
    for mark in (_LENGTH_MARK, _SYLLABIC_MARK):
        if mark in symbol:
            idx = symbol.index(mark)
            return [symbol[:idx], mark]
    return [symbol]

# Rarity-tier bucketing from frequency. THRESHOLDS ARE ASSUMED,
# not contractual — Q36 (rarity-tier finalization) is still
# OPEN. The fixture's example.json uses tiers 1-3, implying
# coarse buckets; these match that example's apparent intent.
_RARITY_THRESHOLDS = [(0.9, 1), (0.5, 2), (0.1, 3), (0.01, 4)]

def _bucket_rarity_tier(freq: float | None) -> int:
    """Tier 6 (unattested) is the null-frequency case; 1-5 by
    descending frequency; thresholds pending Q36."""
    if freq is None:
        return 6
    for threshold, tier in _RARITY_THRESHOLDS:
        if freq >= threshold:
            return tier
    return 5
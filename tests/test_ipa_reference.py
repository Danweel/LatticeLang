"""Tests for the ipa_reference.json data contract.

The fixture (tests/fixtures/ipa_reference.example.json) is also
embedded in dc_ipa_reference.rst via literalinclude — if the
contract changes, both change together.

Each test maps to a numbered Field Check in the contract, which
lists these as the derive script's acceptance tests.
"""

import json
from pathlib import Path

import pytest

FIXTURE = Path(__file__).parent / "fixtures" / "ipa_reference.example.json"
COMBINATION_TYPES = {"tie_bar", "length", "syllabic_mark"}

# Placeholder for Field Check 5: the allowed feature-key set is
# exercised with only the keys the fixture uses. Replace with the
# pinned PHOIBLE 2.0 vocabulary once Q38 / ADR-033 defines it.
KNOWN_FEATURE_KEYS = {
    "syllabic", "consonantal", "sonorant", "continuant",
    "delayed_release", "long", # 'long' provisional pending pinned vocabulary
}

@pytest.fixture()
def ref():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))

def all_entries(ref):
    return ref["consonants"] + ref["vowels"] + ref["special_combinations"]


# --- Field Check 1 --------------------------------------------------

def test_symbols_unique(ref):
    """No duplicate symbols across all arrays."""
    symbols = [e["symbol"] for e in all_entries(ref)]
    assert len(symbols) == len(set(symbols))


# --- Field Check 2 --------------------------------------------------

def test_every_entry_has_required_keys(ref):
    """sonority_rank and tipa present; null allowed, absence is not."""
    for entry in all_entries(ref):
        assert entry["symbol"]
        assert entry["features"]
        assert "sonority_rank" in entry
        assert "tipa" in entry


# --- Field Check 3 --------------------------------------------------

def _decode_codepoint(cp: str) -> str:
    """Decode a 'U+XXXX' formatted codepoint string."""
    assert cp.startswith("U+") and len(cp) > 2, f"malformed codepoint {cp!r}"
    return chr(int(cp[2:], 16))

def test_unicode_points_concatenate_to_symbol(ref):
    """Codepoints concatenate to the symbol. Implies the array is
    non-empty whenever the symbol itself is non-empty."""
    for entry in all_entries(ref):
        assert entry["unicode_points"]  # explicit non-emptiness
        decoded = "".join(_decode_codepoint(cp) for cp in entry["unicode_points"])
        assert decoded == entry["symbol"]


# --- Field Check 4 --------------------------------------------------

def test_all_lookup_keys_resolve_unambiguously(ref):
    """Symbols, canonical forms, and aliases are all lookup keys
    for UC-012 — each key must resolve to exactly one symbol.
    Duplication within one entry (symbol also in its own
    canonical_forms) is required, not forbidden; collision
    across entries is the ambiguity that breaks lookups."""
    resolution: dict[str, str] = {}
    for entry in all_entries(ref):
        for key in [entry["symbol"], *entry["canonical_forms"], *entry["aliases"]]:
            prior = resolution.setdefault(key, entry["symbol"])
            assert prior == entry["symbol"], (
                f"lookup key {key!r} resolves to both "
                f"{prior!r} and {entry['symbol']!r}"
            )

# --- Reinstated canonical_forms check -------------------------------

def test_canonical_forms_include_symbol(ref):
    """canonical_forms must contain the symbol itself."""
    for entry in all_entries(ref):
        assert entry["symbol"] in entry["canonical_forms"]


# --- New combination checks -----------------------------------------

def test_special_combinations_well_formed(ref):
    """combination_type from the allowed set; constituents is an
    ordered array of at least two non-empty strings."""
    for entry in ref["special_combinations"]:
        assert entry["combination_type"] in COMBINATION_TYPES
        constituents = entry["constituents"]
        assert len(constituents) >= 2
        assert all(isinstance(c, str) and c for c in constituents)


# --- Field Check 5 (fixture-scoped) ---------------------------------

def test_feature_keys_known(ref):
    """Every features key is in the recognized vocabulary.
    Placeholder scope: currently validates only the keys the
    fixture uses; replace KNOWN_FEATURE_KEYS with the pinned
    PHOIBLE 2.0 vocabulary when Q38 defines it."""
    for entry in all_entries(ref):
        for key in entry["features"]:
            assert key in KNOWN_FEATURE_KEYS


# --- Fixture sanity --------------------------------------------------

def test_top_level_shape(ref):
    """schema_version, pinned_sources, three non-empty arrays."""
    assert ref["schema_version"] == "1.0"
    assert ref["pinned_sources"]["phoible_release"] == "2.0"
    assert ref["attribution"]["phoible"]
    for key in ("consonants", "vowels", "special_combinations"):
        assert isinstance(ref[key], list) and ref[key]

# --- Rarity tier --------------------------------------------------


def test_rarity_tier_in_range(ref):
    """New field check: tier in 1–5. Extend to 1–6 when Q36
    confirms the unattested tier."""
    for entry in all_entries(ref):
        assert entry["rarity_tier"] in range(1, 6)

# --- Frequency --------------------------------------------------

def test_phoible_frequency_unit_interval(ref):
    """New field check: frequency in [0, 1] or explicit null."""
    for entry in all_entries(ref):
        freq = entry["phoible_frequency"]
        assert freq is None or 0.0 <= freq <= 1.0


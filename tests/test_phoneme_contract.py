"""Tests for the Phoneme class against dc_phoneme.rst.

Written RED: the current Phoneme in core/phonology.py is Phase
Alpha scaffold (enum category, boolean features) and will be
replaced. These tests define the replacement's contract.

Sources of truth:
- Field list + validation rules: dc_phoneme.rst
- Merge semantics: ADR-051 (field-class rules, superseding
  ADR-040's undifferentiated merge)
- Feature representation: ADR-033 (controlled-vocab strings,
  never booleans, never enums; PHOIBLE 2.0 vocabulary)
- Frequency semantics: Q7 (positive relative weight, ratios only)
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from latticelang.core.phonology import (
    Phoneme,
    merge_phonemes,          # ADR-051 deterministic fallback
    CategoryDivergenceWarning,
)

FIXTURE = Path(__file__).parent / "fixtures" / "ipa_reference.example.json"

# Real PHOIBLE 2.0 feature atoms (ADR-033; binary '+'/'-'/'0',
# camelCase where PHOIBLE spells them). No ghost atoms: no
# 'place', no 'manner', no 'voice', no 'height'.
P = {  # 'p': known symbol, voiceless bilabial stop
    "symbol": "p",
    "features": {"syllabic": "-", "consonantal": "+", "sonorant": "-",
                 "continuant": "-", "labial": "+"},  # place = labial via 'labial'+'-'/'round'
}
# Open vowel uses real high/low binary pair instead of 'height'
A = {"symbol": "a", "features": {"syllabic": "+", "consonantal": "-",
                                  "high": "-", "low": "+"}}


# --- Construction (field list) -------------------------------------

def test_features_are_strings_not_booleans():
    """ADR-033: '+'/'-'/'0' strings; boolean feature values rejected."""
    with pytest.raises((TypeError, ValueError)):
        Phoneme(symbol="p", features={"labial": False, "strident": "-"})

def test_empty_symbol_rejected():
    """Validation rule: symbol non-empty."""
    with pytest.raises(ValueError):
        Phoneme(symbol="", features=P["features"])

def test_known_symbol_is_not_custom():
    """Membership in ipa_reference determines the custom flag."""
    p = Phoneme.from_reference(P["symbol"], FIXTURE)
    assert p.custom is False

def test_unknown_symbol_is_custom_with_no_prefill():
    """Custom phonemes get no automatic features, rank, or
    frequency until reviewed (UC-01 ext 1a3). The custom flag
    is a membership fact, determined against the reference
    table via from_reference."""
    q = Phoneme.from_reference("ʠ", FIXTURE)
    assert q.custom is True
    assert q.features == {}
    assert q.sonority_rank is None
    assert q.frequency == 1.0  # Q7 default for unattested


# --- Rank and frequency (validation rules) --------------------------

def test_rank_out_of_expected_range_warns():
    """UC-01 ext 4a: stop with rank 5 -> warning, stored anyway."""
    with pytest.warns(UserWarning, match="unusual"):
        p = Phoneme(symbol="p", features=P["features"], sonority_rank=5)
    assert p.sonority_rank == 5  # warning is advisory; stored wins

def test_frequency_must_be_positive():
    """Q7 item 3: zero/negative invalid; exclusion has another path."""
    with pytest.raises((ValueError, TypeError)):
        Phoneme(symbol="p", features=P["features"], frequency=-0.5)


# --- Diphthong (fields + notes) --------------------------------------

def test_diphthong_requires_two_components():
    """components required iff category = diphthong."""
    d = Phoneme(symbol="aɪ", features={}, components=["a", "ɪ"])
    assert d.category == "diphthong"


# --- Category divergence (validation rules) --------------------------

def test_divergent_stored_category_warns_and_retains():
    """Q5 (resolved 2026-09-16): recompute is advisory; stored
    category is the author's ruling. The warning fires on LOAD
    (from_json), not construction — construction with an
    explicit category is the UC-01 extension 2a override path,
    which records silently."""
    stored = Phoneme(symbol="p", features=P["features"], category="vowel")
    with pytest.warns(CategoryDivergenceWarning):
        loaded = Phoneme.from_json(stored.to_json())
    assert loaded.category == "vowel"  # stored value retained


# --- ADR-051 merge semantics (pure functions) ------------------------

def test_merge_features_union_existing_wins_conflicts():
    new = Phoneme(symbol="p", features={"labial": "-", "strident": "-"})
    old = Phoneme(symbol="p", features={"labial": "+"})
    merged = merge_phonemes(old, new)
    assert merged.features["labial"] == "+"  # existing wins
    assert merged.features["strident"] == "-"   # union: new key added

def test_merge_sonority_rank_existing_wins_always():
    old = Phoneme(symbol="p", features=P["features"], sonority_rank=0)
    new = Phoneme(symbol="p", features=P["features"], sonority_rank=1)  # was 3
    assert merge_phonemes(old, new).sonority_rank == 0

def test_merge_frequency_summed_not_averaged():
    """Q7: duplicates are double-counted attestation."""
    old = Phoneme(symbol="p", features=P["features"], frequency=1.9)
    new = Phoneme(symbol="p", features=P["features"], frequency=0.4)
    assert merge_phonemes(old, new).frequency == pytest.approx(2.3)

def test_merge_category_recomputed_from_merged_features():
    """ADR-032: category is derived, never merged."""
    old = Phoneme(symbol="p", features={"syllabic": "-", "consonantal": "+"})
    new = Phoneme(symbol="p", features={})
    assert merge_phonemes(old, new).category == "consonant"

def test_merge_metadata_new_only_fill():
    old = Phoneme(symbol="p", features=P["features"], metadata={"x": 1})
    new = Phoneme(symbol="p", features={},
                  metadata={"y": 2})
    merged = merge_phonemes(old, new)
    assert merged.metadata == {"x": 1}  # populated retains


# --- Round-trip ------------------------------------------------------

def test_json_round_trip_preserves_fields():
    p = Phoneme(symbol="p", features=P["features"],
                sonority_rank=0, frequency=1.93)
    restored = Phoneme.from_json(p.to_json())
    assert restored == p  # needs __eq__ on Phoneme

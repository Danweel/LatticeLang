"""Phoneme validation against dc_phoneme.rst (ADR-033 vocabulary).

Tests the fail-loud rule (AGENTS.md): unknown feature keys raise,
never pass silently.
"""

from __future__ import annotations

import pytest

from latticelang.core.phonology import Phoneme, CategoryDivergenceWarning

# --- Feature key validation (fail-loud rule) --------------------

def test_unknown_feature_key_rejected():
    """Ghost 'voice' atom (not in pinned vocabulary) must raise,
    never pass silently. This catches Defect A from the audit."""
    with pytest.raises(ValueError, match="unknown feature key"):
        Phoneme(symbol="p", features={"voice": "-"})

def test_custom_feature_key_accepted_when_declared():
    """Declare custom keys via custom_features; they're then valid."""
    p = Phoneme(
        symbol="x",
        features={"my_custom_feature": "+"},
        custom_features=["my_custom_feature"],
    )
    assert "my_custom_feature" in p.features

def test_builtin_features_pass_without_declaration():
    """PHOIBLE 2.0 keys don't need custom_features declaration."""
    p = Phoneme(
        symbol="p",
        features={"syllabic": "-", "consonantal": "+"}
    )
    assert p.custom_features == []

# --- Round-trip integrity (Defect B fix) -------------------------

def test_round_trip_preserves_overridden_rank():
    """Store rank 5 on a stop (UC-01 ext 4a); round-trip must
    preserve it. Previously lost (re-proposed to 0) — Defect B."""
    p = Phoneme(
        symbol="p",
        features={"syllabic": "-", "consonantal": "+"},
        sonority_rank=5,  # deliberate override
    )
    loaded = Phoneme.from_json(p.to_json())
    assert loaded.sonority_rank == 5, "Overridden rank was silently lost"

def test_round_trip_emits_schema_version():
    """to_json includes schema_version per the contract example."""
    import json
    p = Phoneme(symbol="p", features={"syllabic": "-"})
    obj = json.loads(p.to_json())
    assert obj.get("schema_version") == "0.1.0"

def test_round_trip_preserves_custom_features():
    """custom_features survives the round-trip."""
    p = Phoneme(
        symbol="x",
        features={"custom": "+"},
        custom_features=["custom"],
    )
    loaded = Phoneme.from_json(p.to_json())
    assert loaded.custom_features == ["custom"]

# --- Boolean feature rejection (existing behavior, verified) ----

def test_boolean_features_rejected():
    """Booleans are invalid feature values (ADR-033)."""
    with pytest.raises(TypeError, match="must be a string"):
        Phoneme(symbol="p", features={"syllabic": False})

# --- Positive frequency (existing behavior, verified) -----------

def test_negative_frequency_rejected():
    """Q7: frequency must be positive."""
    with pytest.raises(ValueError, match="positive"):
        Phoneme(symbol="p", features={}, frequency=-1.0)

def test_zero_frequency_rejected():
    """Q7: zero frequency is invalid."""
    with pytest.raises(ValueError, match="positive"):
        Phoneme(symbol="p", features={}, frequency=0.0)
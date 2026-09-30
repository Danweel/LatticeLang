"""Phonology module for LatticeLang.

Phoneme representation, category derivation (ADR-032/033), and
the merge surface (ADR-051). The Phoneme class is being rewritten
against dc_phoneme.rst, replacing the Phase Alpha scaffold.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import warnings


# Names kept for ADR-051's interactive-path future; merge_phonemes
# arrives in the next chunk (tests already drafted, currently RED).
# from latticelang.core.sonority import propose_sonority_rank  # see note below


def derive_category(features: dict[str, str]) -> str | None:
    """Derive a phoneme's category from its major-class features.

    Implements the ADR-032 derivation table in dc_phoneme.rst.
    Categories are controlled-vocabulary strings (ADR-033),
    never enums. 'syllabic' takes precedence over
    'consonantal' when both are '+' (ADR-033 edge case:
    syllabic consonants get vowel-like slot treatment but
    remain consonants).

    Args:
        features: Flat feature dict with '+', '-', or atom
            string values (e.g., 'coronal'). Booleans are
            invalid per ADR-033.

    Returns:
        One of 'consonant', 'vowel', 'glide'; or None when
        the major-class features are missing (uncertain
        derivations are surfaced, never guessed).

    Raises:
        Nothing — missing features are a None, not an error,
        because UC-01 treats unknowns as prompts.
    """
    syllabic = features.get("syllabic")
    consonantal = features.get("consonantal")

    # 'syllabic' branches first: it takes precedence (row 4).
    if syllabic == "+":
        if consonantal == "+":
            return "consonant"  # syllabic consonant (n̩)
        return "vowel"
    if syllabic == "-":
        if consonantal == "+":
            return "consonant"  # stops, fricatives, nasals...
        if consonantal == "-":
            return "glide"      # /j/, /w/
    return None  # uncertain — never guess


class CategoryDivergenceWarning(UserWarning):
    """Stored category disagrees with recomputation on load (Q5)."""


@dataclass
class Phoneme:
    """A phoneme: symbol, features, and derived metadata.

    Constructor surface (assumption ledger, dc_phoneme.rst):
    - direct construction (symbol + features required)
    - from_reference() — UC-01 prefill from ipa_reference.json
    - to_json()/from_json() — persistence round-trip

    Category and sonority_rank are proposed from features when
    not supplied; the stored values are authoritative once
    confirmed (UC-01 step 4, dc_phoneme validation rules).
    """

    symbol: str
    features: dict[str, str]
    category: str | None = None
    sonority_rank: int | None = None
    frequency: float = 1.0
    components: list[str] = field(default_factory=list)
    custom: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate basics; propose category and rank when unset."""
        if not self.symbol:
            raise ValueError("Phoneme symbol cannot be empty")
        for key, value in self.features.items():
            if isinstance(value, bool):
                raise TypeError(
                    f"feature {key!r} must be a string ('+'/'-'), "
                    f"got boolean {value!r} (ADR-033)"
                )

        # Q7 item 3: zero/negative weights are invalid
        if self.frequency is not None and self.frequency <= 0:
            raise ValueError(
                f"frequency must be positive, got {self.frequency!r} (Q7)"
            )

        # UC-01 ext 4a: warn if stored rank outside band for features
        if self.sonority_rank is not None:
            from latticelang.core.sonority import expected_rank_range
            band = expected_rank_range(self.features)
            if band and not (band[0] <= self.sonority_rank <= band[1]):
                warnings.warn(
                    f"Rank {self.sonority_rank} is unusual for "
                    f"{self.category} with these features. "
                    f"Expected range: {band[0]}-{band[1]}",
                    UserWarning,
                )

        # Diphthong determination: components present (dc_phoneme
        # notes; diphthong row keys on components, not features).
        if not self.category:
            if self.components:
                self.category = "diphthong"
            else:
                self.category = derive_category(self.features)
        if self.sonority_rank is None:
            from latticelang.core.sonority import propose_sonority_rank
            self.sonority_rank = propose_sonority_rank(self.features)

    @classmethod
    def from_reference(cls, symbol: str, fixture: Path) -> "Phoneme":
        """Build a Phoneme from ipa_reference.json (UC-01 prefill).

        Unknown symbols return a custom Phoneme: no automatic
        features, rank, or frequency (UC-01 extension 1a3).
        """
        with open(fixture, encoding="utf-8") as f:
            ref = json.load(f)
        for entry in (
            ref.get("consonants", []) + ref.get("vowels", [])
            + ref.get("special_combinations", [])
        ):
            if entry.get("symbol") == symbol:
                return cls(
                    symbol=symbol,
                    features=entry.get("features", {}),
                    sonority_rank=entry.get("sonority_rank"),
                    frequency=entry.get("phoible_frequency") or 1.0,
                    custom=False,
                    metadata={"description": entry.get("description")},
                )
        return cls(symbol=symbol, features={}, custom=True)

    def to_json(self) -> str:
        """Serialize to a JSON string."""
        return json.dumps({
            "symbol": self.symbol,
            "category": self.category,
            "features": self.features,
            "sonority_rank": self.sonority_rank,
            "frequency": self.frequency,
            "components": self.components,
            "custom": self.custom,
            "metadata": self.metadata,
        }, indent=2, ensure_ascii=False)

    @classmethod
    def from_json(cls, data: str | dict[str, Any]) -> "Phoneme":
        """Deserialize from a JSON string or dict."""
        if isinstance(data, str):
            data = json.loads(data)
        phoneme = cls(
            symbol=data["symbol"],
            features=data.get("features", {}),
            category=data.get("category"),
            frequency=data.get("frequency", 1.0),
            components=data.get("components", []),
            custom=data.get("custom", False),
            metadata=data.get("metadata", {}),
        )

        # Q5 ruling: divergence warns on LOAD (not construction)
        from latticelang.core.sonority import propose_sonority_rank
        recomputed = derive_category(phoneme.features)
        if (phoneme.category is not None and recomputed is not None
                and phoneme.category != recomputed):
            warnings.warn(
                f"Stored category {phoneme.category!r} for "
                f"{phoneme.symbol!r} diverges from recomputation "
                f"{recomputed!r}; stored value retained.",
                CategoryDivergenceWarning,
            )
        return phoneme

def merge_phonemes(existing: Phoneme, incoming: Phoneme) -> Phoneme:
    """Merge a duplicate-symbol pair per ADR-051 field classes.

    Deterministic fallback path (batch import, headless runs,
    test fixtures). The interactive path (UC-01 extension 6a)
    prefills its dialog from these same outcomes. Category
    recompute is silent by design (ruled 2026-09-29, recorded in
    dc_phoneme.rst); divergence warnings fire on load only.

    Args:
        existing: The stored phoneme (authoritative ranks,
            confirmed values).
        incoming: The newly encountered duplicate (import,
            re-entry, shared-definition arrival).

    Returns:
        A new merged Phoneme; inputs are not mutated.
    """
    # features: union, existing wins conflicts (never-downgrade,
    # ADR-040 via ADR-051).
    merged_features = dict(incoming.features)
    merged_features.update(existing.features)

    # frequency: sum (double-counted attestation, Q7).
    # sonority_rank: existing wins, always.
    # components/custom/metadata: new-only fill (populated
    # fields retain).
    return Phoneme(
        symbol=existing.symbol,
        features=merged_features,
        sonority_rank=existing.sonority_rank,
        frequency=existing.frequency + incoming.frequency,
        components=(existing.components or list(incoming.components)),
        custom=existing.custom or incoming.custom,
        metadata=dict(existing.metadata) if existing.metadata
            else dict(incoming.metadata),
    )
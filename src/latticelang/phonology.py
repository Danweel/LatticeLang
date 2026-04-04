"""Phonology module for LatticeLang.

This module provides classes for representing and manipulating phoneme
inventories in constructed languages.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class PhonemeCategory(Enum):
    """Categories of phonemes."""

    CONSONANT = "consonant"
    VOWEL = "vowel"
    DIPHTHONG = "diphthong"
    TONE = "tone"


@dataclass
class Phoneme:
    """Represents a single phoneme with its linguistic features.

    A phoneme is the smallest unit of sound that distinguishes meaning
    in a language. Each phoneme has an IPA symbol and a set of features
    that describe its articulatory properties.

    Example:
        >>> p = Phoneme(symbol="p", category=PhonemeCategory.CONSONANT,
        ...             features={
                            "voiced": False,
                            "place": "bilabial",
                            "manner": "plosive"
                        })
        >>> p.symbol
        'p'
        >>> p.features["voiced"]
        False
    """

    symbol: str
    category: PhonemeCategory
    features: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the phoneme after initialization."""
        if not self.symbol:
            raise ValueError("Phoneme symbol cannot be empty")

    def has_feature(self, feature: str, value: Any = True) -> bool:
        """Check if this phoneme has a specific feature value.

        Args:
            feature: The feature name to check.
            value: The expected value (defaults to True for boolean features).

        Returns:
            True if the phoneme has the feature with the specified value.

        Example:
            >>> p = Phoneme("b", PhonemeCategory.CONSONANT, {"voiced": True})
            >>> p.has_feature("voiced")
            True
            >>> p.has_feature("nasal")
            False
        """
        return self.features.get(feature) == value

    def __str__(self) -> str:
        """Return the IPA symbol as the string representation."""
        return self.symbol

    def __repr__(self) -> str:
        """Return a detailed representation for debugging."""
        return f"Phoneme('{self.symbol}', {self.category.value}, {self.features})"

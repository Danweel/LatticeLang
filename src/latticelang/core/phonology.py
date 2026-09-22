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
import json
from typing import List

class PhonemeInventory:
    """Represents a collection of phonemes in a language.

    This class allows for adding, removing, and retrieving phonemes
    from the inventory. It also supports serialization and deserialization
    of the inventory to JSON format.
    """

    def __init__(self):
        self.phonemes: List[Phoneme] = []

    def add_phoneme(self, phoneme: Phoneme) -> None:
        """Add a phoneme to the inventory."""
        self.phonemes.append(phoneme)

    def remove_phoneme(self, symbol: str) -> None:
        """Remove a phoneme from the inventory by its symbol."""
        self.phonemes = [p for p in self.phonemes if p.symbol != symbol]

    def get_phoneme(self, symbol: str) -> Phoneme | None:
        """Retrieve a phoneme from the inventory by its symbol."""
        for phoneme in self.phonemes:
            if phoneme.symbol == symbol:
                return phoneme
        return None

    def to_json(self) -> str:
        """Serialize the phoneme inventory to a JSON string."""
        phoneme_dict_list = [
            {
                "symbol": phoneme.symbol,
                "category": phoneme.category.value,
                "features": phoneme.features
            }
            for phoneme in self.phonemes
        ]
        return json.dumps(phoneme_dict_list, indent=4)

    @classmethod
    def from_json(cls, json_str: str) -> 'PhonemeInventory':
        """Deserialize the phoneme inventory from a JSON string."""
        phoneme_dict_list = json.loads(json_str)
        inventory = cls()
        for phoneme_dict in phoneme_dict_list:
            phoneme = Phoneme(
                symbol=phoneme_dict["symbol"],
                category=PhonemeCategory[phoneme_dict["category"]],
                features=phoneme_dict["features"]
            )
            inventory.add_phoneme(phoneme)
        return inventory


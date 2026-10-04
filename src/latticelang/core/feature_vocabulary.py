"""Pinned PHOIBLE 2.0 feature vocabulary (ADR-033).

Single source of truth for feature key validation:
- ``latticelang.core.phonology.Phoneme.__post_init__`` rejects keys
  outside the pinned vocabulary unless declared via ``custom_features``
- ``scripts.regenerate_mini_fixture`` and ``scripts.derive_ipa_reference``
  use the same constants for header validation (dev-time only)
- Tests compare against this constant (not duplicated strings)

Source: ``head -1 phoible-segments-features.tsv`` on the pinned
vendor release (verified 2026-10-01). All 38 column names,
camelCase as PHOIBLE spells them.

Note: the module ships with the runtime package, but the TSV
files it describes live only in the development repository
(vendor/phoible-2.0/), which is excluded from distributions.
Users receive pre-generated reference data (``ipa_reference.json``).
"""

from __future__ import annotations

# Ordered header — TSV column order, source of truth for writers.
FEATURE_HEADER_ORDER: tuple[str, ...] = (
    "segment", "tone", "stress", "syllabic", "short", "long",
    "consonantal", "sonorant", "continuant", "delayedRelease",
    "approximant", "tap", "trill", "nasal", "lateral",
    "labial", "round", "labiodental", "coronal", "anterior",
    "distributed", "strident", "dorsal", "high", "low",
    "front", "back", "tense", "retractedTongueRoot",
    "advancedTongueRoot", "periodicGlottalSource",
    "epilaryngealSource", "spreadGlottis", "constrictedGlottis",
    "fortis", "raisedLarynxEjective", "loweredLarynxImplosive",
    "click",
)

# Membership view — validation's source of truth.
FEATURE_COLUMNS = frozenset(FEATURE_HEADER_ORDER) - {"segment"}
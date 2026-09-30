"""Tests for runtime phoneme derivation functions (dc_phoneme.rst).

Tests are written RED against the contract tables, not against
existing code — src/latticelang/core/sonority.py is empty, and
core/phonology.py is Phase Alpha scaffold slated for replacement.

Sources of truth:
- Category derivation: the ADR-032 table in dc_phoneme.rst
- Rank proposal:       the sonority table in dc_phoneme.rst
- Rank semantics:      advisory proposal (UC-01 step 4); bands,
                       not pinned integers; uncertain -> None
                       (dc_ipa_reference.rst build step 3)

1. Diphthong derivation is deliberately absent. The ADR-032 table's
diphthong row keys on components being present, not on features — so
derive_category's signature question (does it take components? a
keyword arg?) is a genuine spec gap I won't guess at. Cheapest
resolution: a diphthong determination happens where components
already live, arguably in the Phoneme constructor, not in
`derive_category`. Want a ruling from you, or defer to implementation time?

2. The manner detection from features is my inference, not a pinned
decision — e.g., I inferred affricate = −continuant, +delayed_release
from the PHOIBLE vocabulary (delayed_release appears in your fixture
test's KNOWN_FEATURE_KEYS). If the pinned PHOIBLE 2.0 vocabulary
(Q38/ADR-033) names manners differently, the input bundles adjust — the
bands under test don't.

3. OPEN_VOWEL at 8–9 flattens the close→open gradient the table mentions;
testing the gradient properly needs the height-by-height mapping, which
is exactly the kind of refinement the range approach is meant to survive.
"""

import pytest

# These imports fail on first run — that IS the red state.
# Category derivation lives with the Phoneme class (phonology.py,
# per ADR-014); rank proposal lives in sonority.py.
from latticelang.core.phonology import derive_category
from latticelang.core.sonority import propose_sonority_rank


# --- Feature bundles used as test inputs ----------------------------
# Values follow ADR-033: +/- strings and atom strings, never booleans.

STOP = {"syllabic": "-", "consonantal": "+", "sonorant": "-",
        "continuant": "-", "delayed_release": "-"}
AFFRICATE = {"syllabic": "-", "consonantal": "+", "sonorant": "-",
             "continuant": "-", "delayed_release": "+"}
FRICATIVE = {"syllabic": "-", "consonantal": "+", "sonorant": "-",
             "continuant": "+"}
NASAL = {"syllabic": "-", "consonantal": "+", "sonorant": "+",
         "continuant": "-"}
LIQUID = {"syllabic": "-", "consonantal": "+", "sonorant": "+",
          "continuant": "+"}
GLIDE = {"syllabic": "-", "consonantal": "-", "sonorant": "+"}
CLOSE_VOWEL = {"syllabic": "+", "consonantal": "-", "height": "close"}
OPEN_VOWEL = {"syllabic": "+", "consonantal": "-", "height": "open"}
SYLLABIC_NASAL = {"syllabic": "+", "consonantal": "+", "sonorant": "+"}


# --- Category derivation (dc_phoneme.rst, ADR-032 table) -------------

@pytest.mark.parametrize("features,expected", [
    (STOP, "consonant"),
    (FRICATIVE, "consonant"),
    (NASAL, "consonant"),
    (CLOSE_VOWEL, "vowel"),
    (OPEN_VOWEL, "vowel"),
    (GLIDE, "glide"),
])
def test_category_from_major_class_features(features, expected):
    """Rows 1-3 of the ADR-032 table: [±syllabic]/[±consonantal]."""
    assert derive_category(features) == expected


def test_syllabic_takes_precedence_over_consonantal():
    """Row 4: [+syllabic, +consonantal] -> consonant (vowel-like
    slot treatment) — 'syllabic' wins per ADR-033."""
    assert derive_category(SYLLABIC_NASAL) == "consonant"


# --- Rank proposal (dc_phoneme.rst sonority table) -------------------

@pytest.mark.parametrize("features,low,high", [
    (STOP, 0, 1),
    (AFFRICATE, 1, 3),
    (FRICATIVE, 2, 3),
    (NASAL, 4, 5),      # dual nasal hypothesis: band, not a point
    (LIQUID, 6, 7),
    (CLOSE_VOWEL, 8, 9),
    (OPEN_VOWEL, 8, 9),
])
def test_rank_lands_in_contracted_band(features, low, high):
    """Each manner class proposes a rank inside its dc_phoneme
    band. Bands, not pinned integers: the proposal is advisory
    (UC-01 step 4) and the user's confirmed value is stored."""
    rank = propose_sonority_rank(features)
    assert rank is not None
    assert low <= rank <= high


def test_glide_rank_is_exact_eight():
    """The glide row is the one exact value in the table (8)."""
    assert propose_sonority_rank(GLIDE) == 8


def test_boundary_tie_at_eight_permitted():
    """dc_ipa_reference Field Check 6: glide 8 and close vowel 8
    are an expected tie, not an anomaly."""
    assert propose_sonority_rank(GLIDE) == 8
    close = propose_sonority_rank(CLOSE_VOWEL)
    assert close in (8, 9)  # and if close is 8, that's fine


def test_uncertain_features_return_none():
    """Insufficient features for any table row -> None, never a
    guess (dc_ipa_reference.rst build step 3; UC-01 treats null
    as a prompt)."""
    assert propose_sonority_rank({}) is None


def test_more_sonorant_than_obstruent():
    """The invariant the ranks exist for: sonorants outrank
    obstruents (dc_phoneme relations section)."""
    assert propose_sonority_rank(NASAL) > propose_sonority_rank(STOP)
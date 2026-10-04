"""Sonority rank proposal (dc_phoneme.rst rank table).

Pure functions only: feature dict in, rank (or None) out.
No inventory, no I/O — the same function is callable both at
runtime (UC-01 step 4) and by the Q38 derive script
(dc_ipa_reference.rst build step 3).
"""

def expected_rank_range(features: dict[str, str]) -> tuple[int, int] | None:
    """The contracted band for these features, or None.

    Single source of truth for the dc_phoneme.rst rank table:
    propose_sonority_rank returns this band's floor (with vowel
    height promotion), and Phoneme's rank validation warns when
    a stored rank falls outside it (UC-01 extension 4a).

    Feature names are the pinned PHOIBLE 2.0 columns (ADR-033;
    camelCase where PHOIBLE spells them so, e.g. delayedRelease).
    """
    # Tonemes: tone + carries null rank by contract (dc_ipa_
    # reference Implementation Bindings, Tonemes; ADR-048).
    # Explicit guard so future table rows cannot accidentally
    # admit tone letters — their all-'0'/'-' profile matches
    # no row only by luck without this.
    if features.get("tone") == "+":
        return None

    syllabic = features.get("syllabic")
    consonantal = features.get("consonantal")
    sonorant = features.get("sonorant")
    continuant = features.get("continuant")

    if syllabic == "+" and consonantal == "-":
        return (8, 9)   # vowel
    if sonorant == "-":
        if continuant == "-":
            return (1, 3) if features.get("delayedRelease") == "+" else (0, 1)
        if continuant == "+":
            return (2, 3)  # fricative
    elif sonorant == "+" and consonantal == "+":
        if continuant == "-":
            return (4, 5)  # nasal (dual nasal hypothesis)
        if continuant == "+":
            return (6, 7)  # liquid
    elif sonorant == "+" and consonantal == "-":
        return (8, 8)      # glide — the one exact row
    return None             # no table row applies

def propose_sonority_rank(features: dict[str, str]) -> int | None:
    """Propose a sonority rank (0–9) from phonemic features.

    Implements the sonority-rank proposal table in
    dc_phoneme.rst. Band floors are returned where the table
    specifies a range (stop->0, affricate->1, fricative->2,
    nasal->4, liquid->6, glide->8); within-band refinement is
    deferred until the pinned PHOIBLE 2.0 vocabulary is fixed
    (Q38; dc_phoneme.rst's rank-table todo).

    The rank is advisory: UC-01 step 4 has the user confirm
    or adjust, and the stored value is authoritative.

    Args:
        features: Flat feature dict with '+'/'-' string values.

    Returns:
        Rank 0–9, or None when the features are insufficient
        to place the phoneme on any table row (UC-01 treats
        a null rank as a prompt, not an error).
    """
    rng = expected_rank_range(features)
    if rng is None:
        return None

    # Vowel band: open-ness promotes to 9 (2026-09-29 ruling).
    # Open-ness is signaled by the real binary features:
    # low + (high -) per the pinned vocabulary — there is no
    # scalar 'height' atom in PHOIBLE 2.0.
    syllabic = features.get("syllabic")
    consonantal = features.get("consonantal")
    if syllabic == "+" and consonantal == "-":
        if features.get("low") == "+" and features.get("high") == "-":
            return 9
        return 8

    # All other classes: return band floor
    return rng[0]
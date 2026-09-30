"""Sonority rank proposal (dc_phoneme.rst rank table).

Pure functions only: feature dict in, rank (or None) out.
No inventory, no I/O — the same function is callable both at
runtime (UC-01 step 4) and by the Q38 derive script
(dc_ipa_reference.rst build step 3).
"""


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
    syllabic = features.get("syllabic")
    consonantal = features.get("consonantal")
    sonorant = features.get("sonorant")
    continuant = features.get("continuant")

    # Vowels first (checked via syllabic, not sonorant, so a
    # [+syllabic] segment never falls into a consonant row).
    if syllabic == "+" and consonantal == "-":
        # Vowel band 8-9: the close->open gradient is flattened
        # to two values for now — open-ness promotes to 9.
        height = features.get("height")
        if height in ("open", "near-open", "open-mid"):
            return 9
        return 8

    # Obstruents: [-sonorant] splits by continuancy, and the
    # delayed-release feature separates affricates from stops.
    if sonorant == "-":
        if continuant == "-":
            # Delayed release marks affricates (band 1-3);
            # plain stops sit at the bottom (band 0-1).
            if features.get("delayed_release") == "+":
                return 1
            return 0
        if continuant == "+":
            return 2  # Fricative band 2-3
        return None   # sonorant known, continuancy unknown

    # Sonorant consonants: nasality vs. liquidity split by
    # continuancy (nasal band 4-5, liquid band 6-7).
    if sonorant == "+" and consonantal == "+":
        if continuant == "-":
            return 4  # Nasal
        if continuant == "+":
            return 6  # Liquid
        return None

    # Glides: [-syllabic, -consonantal, +sonorant] — the one
    # exact value in the table (a permitted tie with close
    # vowels; dc_ipa_reference Field Check 6).
    if sonorant == "+" and consonantal == "-":
        return 8

    return None  # Uncertain: no table row applies
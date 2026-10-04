"""Sonority-proposal tests against REAL vendored feature rows.

Audit lineage (2026-10-02 probe against the mini fixture):
the proposer was built on the invented schema. Two defects
confirmed against real rows:
  1. vowel open-promotion keyed on a ghost 'height' atom —
     every vowel returned 8, promotion never fired
  2. affricate detection keyed on snake_case 'delayed_release'
     — real column is camelCase 'delayedRelease', so affricates
     fell into the stop band

Expectations below are written against the CONTRACT rulings
(dc_phoneme.rst, rank table + 2026-09-29 implementation ruling),
not against current code behavior. Tone-letter nulls are pinned
deliberately: per dc_ipa_reference Implementation Bindings
(Tonemes), tonemes carry sonority_rank null — and the test
comment exists so a future refactor cannot break them silently.

Clicks ruling (2026-10-02, resolves dc_phoneme assumption
ledger item c): clicks propose stop-band rank 0 via
[-sonorant, -continuant] — obstruent treatment per standard
sonority scales; no null exception.
"""

from __future__ import annotations

import csv
from pathlib import Path

from latticelang.core.sonority import (
    propose_sonority_rank,
    expected_rank_range,
)

FIXTURE = (Path(__file__).parent / "fixtures"
           / "phoible_mini_features.tsv")

def load_rows() -> dict[str, dict[str, str]]:
    """segment -> feature dict (segment key stripped)."""
    with open(FIXTURE, encoding="utf-8", newline="") as f:
        rows = {
            r["segment"]: {k: v for k, v in r.items()
                           if k != "segment"}
            for r in csv.DictReader(f, delimiter="\t")}
    assert len(rows) == 13
    return rows

ROWS = load_rows()

# --- Stops: band floor 0 (probe-confirmed correct) --------------

def test_stops_propose_zero():
    for sym in ("p", "b", "t"):
        assert propose_sonority_rank(ROWS[sym]) == 0, sym

# --- Affricate: band floor 1 via delayedRelease -------------------
# Currently RED: ghost-key defect routes t+esh to the stop band.

def test_affricate_proposes_one_not_stop_band():
    """delayedRelease + with continuant - is the affricate
    signature; the 2026-09-29 ruling sets its band floor to 1.
    Confirms the camelCase key is honored (probe: returned 0)."""
    feats = ROWS["t\u0320\u0283"]
    assert feats["delayedRelease"] == "+"
    assert feats["continuant"] == "-"
    assert propose_sonority_rank(feats) == 1

def test_affricate_band_upper_bound_open():
    """Non-floor affricate behavior stays within the ruled band."""
    assert expected_rank_range(ROWS["t\u0320\u0283"]) == (1, 3)

# --- Nasal: band floor 4 (probe-confirmed correct) ---------------

def test_syllabic_nasal_proposes_four():
    assert propose_sonority_rank(ROWS["m\u0329"]) == 4

# --- Vowels: open-promotion must fire on real features -----------
# Currently RED: promotion keyed on ghost 'height' never fires.

def test_close_vowel_proposes_eight():
    """i is [+high, -low]: close vowel, no promotion."""
    feats = ROWS["i"]
    assert feats["high"] == "+"
    assert feats["low"] == "-"
    assert propose_sonority_rank(feats) == 8

def test_open_vowel_promotes_to_nine():
    """a is [-high, +low]: open vowel promotes to 9 per the
    2026-09-29 ruling ('open-ness promoting to 9'). The promotion
    must key on the real binary features, not a 'height' atom
    (probe: returned 8 for every vowel)."""
    feats = ROWS["a"]
    assert feats["high"] == "-"
    assert feats["low"] == "+"
    assert propose_sonority_rank(feats) == 9

def test_long_open_vowel_also_promotes():
    """Vowel length must not interact with rank proposal."""
    assert propose_sonority_rank(ROWS["a\u02d0"]) == 9

# --- Tonemes: null BY CONTRACT, not by accident ------------------

def test_tone_letters_propose_null():
    """Tonemes carry sonority_rank: null (dc_ipa_reference
    Implementation Bindings, Tonemes; ADR-048). Pinned so a
    refactor adding a catch-all table row cannot silently
    assign ranks to tone letters."""
    for sym in ("\u02e5", "\u02e6", "\u02e7",
                "\u02e8", "\u02e9"):
        feats = ROWS[sym]
        assert feats["tone"] == "+"
        assert propose_sonority_rank(feats) is None, repr(sym)
        assert expected_rank_range(feats) is None, repr(sym)
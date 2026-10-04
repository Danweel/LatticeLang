"""Tests for the Inventory validation layer against dc_inventory.rst.

Written RED: core/phonology.py has no Inventory class (the
Alpha-era core/inventory.py was empty and is deleted). These
tests define the validation-view contract per dc_inventory.rst.

Sources of truth:
- Severity policy + validation rules: dc_inventory.rst
  (six-rule table, committed 2026-09-30)
- Nucleus eligibility: ADR-034 rule 1, mirrored by INV-1
- Entry-level validation: dc_phoneme.rst (NOT repeated here)
- Merge participation: ADR-040/ADR-051 (checks re-run on
  mutation)

Assumptions under test (pending Implementation Bindings in
dc_inventory.rst):
- Inventory.add() exists; adding a duplicate symbol routes
  through merge_phonemes (deterministic fallback path)
- Inventory.check(templates=None) returns a report with
  .errors/.warnings/.notes (list[str]); only errors block
- INV-3 is template-aware when templates are passed;
  without templates the simplified zero-vowel warning fires
"""

import pytest

from latticelang.core.phonology import (
    Phoneme,
    Inventory,
    merge_phonemes,
)


# --- Helpers ---------------------------------------------------------

def stop(symbol="p", **kw):
    kw.setdefault("features", {
        "syllabic": "-", "consonantal": "+",
        "sonorant": "-", "continuant": "-",
    })
    return Phoneme(symbol=symbol, **kw)


def vowel(symbol="a", height="open", **kw):
    """Helper for tests — translates 'open'/'close' to real
    PHOIBLE binary features (low+/high- or high+/low-)."""
    features = {"syllabic": "+", "consonantal": "-"}
    if height == "open":
        features["low"] = "+"
        features["high"] = "-"
    elif height == "close":
        features["high"] = "+"
        features["low"] = "-"
    else:
        features["high"] = "-"
        features["low"] = "-"
    kw.setdefault("features", features)
    return Phoneme(symbol=symbol, **kw)


def syllabic_consonant(symbol="n̩"):
    return Phoneme(symbol=symbol, features={
        "syllabic": "+", "consonantal": "+",
        "sonorant": "+", "continuant": "-",
    })


def vowel_template():
    """Stand-in template: nucleus admits ['vowel'] only.
    Shape mirrors dc_syllable_template's allowed_categories."""
    return {"nucleus_categories": ["vowel"]}


# --- INV-1: Nucleus capacity (Error, blocks) --------------------------

def test_empty_inventory_reports_nucleus_error():
    report = Inventory().check()
    assert any("nucleus" in e.lower() for e in report.errors)

def test_consonants_only_reports_nucleus_error():
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(stop("t"))
    assert any("nucleus" in e.lower() for e in inv.check().errors)

def test_vowel_satisfies_nucleus_capacity():
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(vowel("a"))
    report = inv.check()
    assert not any("nucleus" in e.lower() for e in report.errors)

def test_diphthong_satisfies_nucleus_capacity():
    """ADR-034 rule 1: vowel or diphthong category is
    nucleus-capable."""
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(Phoneme(symbol="aɪ", features={},
                    components=["a", "ɪ"]))
    assert not any("nucleus" in e.lower()
                   for e in inv.check().errors)

def test_syllabic_consonant_satisfies_nucleus_capacity():
    """Nuxalk-style: syllabic consonant carries the nucleus
    (ADR-034 rule 1; the INV-1 predicate mirrors it)."""
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(syllabic_consonant())
    assert not any("nucleus" in e.lower()
                   for e in inv.check().errors)


# --- INV-2: Consonant absence (Warning) ------------------------------

def test_zero_consonants_warns():
    inv = Inventory()
    inv.add(vowel("a"))
    inv.add(vowel("i"))
    assert any("consonant" in w.lower() for w in inv.check().warnings)

def test_zero_consonants_never_blocks():
    inv = Inventory()
    inv.add(vowel("a"))
    assert not inv.check().errors


# --- INV-3: Vowel absence (Warning, template-aware) -----------------

def test_zero_vowels_with_vowel_template_warns():
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(syllabic_consonant())  # nucleus-capable, so no error
    report = inv.check(templates=[vowel_template()])
    assert any("vowel" in w.lower() for w in report.warnings)

def test_syllabic_consonant_nucleus_template_is_silent():
    """Contract: 'an inventory of syllabic-consonant nuclei
    with matching templates is silent.'"""
    inv = Inventory()
    inv.add(stop("p"))
    inv.add(syllabic_consonant())
    template = {"nucleus_categories": ["consonant"]}
    report = inv.check(templates=[template])
    assert not any("vowel" in w.lower() for w in report.warnings)


# --- INV-4: Identical feature sets (Warning) -------------------------

def test_identical_feature_sets_warn():
    inv = Inventory()
    # Note: "place" is a ghost key — remove it to use real vocab
    inv.add(stop("p", features={
        "syllabic": "-", "consonantal": "+", "labial": "+"}))
    inv.add(stop("b", features={
        "syllabic": "-", "consonantal": "+", "labial": "+"}))
    assert any("identical" in w.lower()
               for w in inv.check().warnings)


# --- INV-5: Minimal feature sets (Note, pairing-gated) ---------------

def test_minimal_pair_alone_is_silent():
    """/t/ vs /d/ differ in one feature: legitimate, unremarkable.
    Per the contract, INV-5 'never blocks, never warns on its
    own' — it pairs only with ADR-041 symbol similarity, which
    is not yet implemented. Positive pairing case awaits
    test_near_miss.py; this pins the negative."""
    inv = Inventory()
    inv.add(stop("t"))
    inv.add(stop("d", features={
        "syllabic": "-", "consonantal": "+", "sonorant": "-",
        "continuant": "-", "strident": "+"}))  # voice is ghost — use strident
    report = inv.check()
    assert not report.warnings
    assert not report.notes  # until ADR-041 pairing exists


# --- Rule 6: Missing diphthong component (Warning) -------------------

def test_missing_diphthong_component_warns():
    """dc_phoneme ledger item (e): evaluated at the Inventory
    boundary (ADR-036), not inside Phoneme."""
    inv = Inventory()
    inv.add(vowel("a"))
    inv.add(stop("p"))
    inv.add(Phoneme(symbol="aɪ", features={},
                    components=["a", "ɪ"]))  # 'ɪ' absent
    report = inv.check()
    assert any("component" in w.lower() or "ɪ" in w
               for w in report.warnings)

def test_complete_diphthong_components_do_not_warn():
    inv = Inventory()
    inv.add(vowel("a"))
    inv.add(vowel("ɪ", height="close"))
    inv.add(Phoneme(symbol="aɪ", features={},
                    components=["a", "ɪ"]))
    report = inv.check()
    assert not any("component" in w.lower()
                   for w in report.warnings)


# --- Load-time enforcement: checks re-run on mutation ----------------

def test_checks_rerun_after_add():
    """The contract: checks run at load and on every mutation
    that changes the outcome set. Adding a vowel clears the
    nucleus error between checks — no stale caching."""
    inv = Inventory()
    assert inv.check().errors            # nucleus error
    inv.add(vowel("a"))
    assert not inv.check().errors        # error cleared

def test_duplicate_add_routes_through_merge():
    """UC-01 step 6 / UC-009: duplicate symbol resolved by the
    ADR-051 deterministic fallback (merge_phonemes) rather than
    a second entry; check() reflects the merged state."""
    inv = Inventory()
    inv.add(stop("p", frequency=1.0))
    inv.add(stop("p", frequency=1.5))   # duplicate
    assert len(inv) == 1                 # one entry, not two
    assert inv.check().errors            # still no nucleus
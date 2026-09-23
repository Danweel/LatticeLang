.. _dc_phoneme:

Phoneme Data Contract
=====================

:Data Structure:
:Doc Status: Draft — open design flags resolved 2026-09-22
:Phase: Beta
:Schema Version: 0.1.0

.. note::

   This contract was reviewed during the 2026-09-16 use-case
   and spec-completeness audit. Key design decisions:
   :ref:`adr-047` (logical schema vs. adapters),
   :ref:`adr-048` (tone as separate stage),
   :ref:`adr-049` (coordinate-addressed random streams),
   :ref:`adr-050` (qualitative ambiguity tiers).

Overview
--------

A ``Phoneme`` is the atomic unit of the phoneme inventory (UC-01).
Each phoneme has a canonical IPA symbol, a feature set drawn from
a controlled vocabulary, a derived category, a sonority rank, and
a generation frequency weight. Tone-related feature values are
carried by the feature vector as data (ADR-048); nothing consumes
them until the tone stage exists.

This contract implements ADR-032 (category derived from features)
and ADR-033 (PHOIBLE 2.0-aligned feature system, pinned release,
controlled-vocabulary strings).

Fields
-------

.. csv-table::
   :header-rows: 1
   :widths: 20 15 15 50

   "Field","Type","Required","Description"
   "symbol","string","yes","Canonical IPA symbol in normalized tie-bar form (ADR-028). Input accepts tie-bar and non-tie-bar forms; stored normalized. Unique within an inventory."
   "features","object (string → string)","yes","Flat feature dictionary. Keys are feature names from the pinned vocabulary. Values are feature-appropriate strings (``+``, ``-``, or descriptive atoms like ``coronal``)."
   "custom_features","object (string → string)","no","User-defined feature names, validated for identifier syntax only. Kept separate from the built-in vocabulary."
   "category","string (derived)","yes","One of ``consonant | vowel | glide | diphthong | custom``. Derived from features per the derivation table; storable but recomputed on load with a divergence warning (see Validation Rules)."
   "sonority_rank","integer 0–9","yes","Proposed from features (see rank table below); stored value is authoritative once confirmed. Validated against the expected range with override warning (UC-01 extension 4a)."
   "frequency","float","yes","Relative weight for generation. Pre-filled from PHOIBLE attestation; default 1.0 for unattested/custom. Semantics: relative weight, normalized at generation time (not persisted normalized)."
   "components","array of strings","only if category = diphthong","The two component vowel symbols, e.g. ``[a, ɪ]``. Components should exist in the inventory; absence is a warning, not an error."
   "custom","boolean","yes","True if the symbol is not in the IPA reference table. Custom phonemes receive no automatic features, rank, or frequency until reviewed."
   "metadata","object","no","Optional pedagogy/display data: description, aliases, rarity_tier, phoible_frequency. Populated from ``ipa_reference.json`` for known symbols."

Serialization Example
----------------------

.. code-block:: json

   {
     "schema_version": "0.1.0",
     "symbol": "t͡ʃ",
     "category": "consonant",
     "features": {
       "syllabic": "-",
       "consonantal": "+",
       "sonorant": "-",
       "place": "coronal",
       "manner": "affricate",
       "voice": "-",
       "continuant": "-",
       "strident": "+"
     },
     "sonority_rank": 2,
     "frequency": 1.93,
     "custom": false
   }

Diphthong example:

.. code-block:: json

   {
     "symbol": "aɪ",
     "category": "diphthong",
     "features": {},
     "components": ["a", "ɪ"],
     "sonority_rank": 9,
     "frequency": 0.41,
     "custom": false
   }

Category Derivation
--------------------

Derived from the major-class features, per ADR-032 and ADR-033:

.. csv-table::
   :header-rows: 1
   :widths: 25 35 40

   "Feature signature","Category","Notes"
   "−syllabic, +consonantal","consonant","stops, fricatives, affricates, nasals, liquids"
   "+syllabic, −consonantal","vowel","Monophthongs"
   "−syllabic, −consonantal","glide","/j/, /w/"
   "+syllabic, +consonantal","consonant (vowel-like slot treatment)","Syllabic consonants (/n̩/) — ``syllabic`` takes precedence per ADR-033"
   "(category field = diphthong, components present)","diphthong","Sequence stored as one phoneme; documented deviation"

Overrides: a user-supplied category always wins, but is recorded
as an override and warned about when slot implications follow
(UC-01, extension 2a). Custom symbols (not in the IPA reference)
require manual feature entry and manual category.

Sonority Rank Proposal
----------------------

The system proposes a rank from features; the user confirms. The
expected-range table below is the initial proposal logic and must
be finalized against the pinned feature vocabulary:

.. csv-table::
   :header-rows: 1
   :widths: 35 20 45

   "Manner / class","Expected rank","Notes"
   "stop (−continuant, −sonorant)","0–1","Least sonorous"
   "affricate","1–3","Boundary class between stops and fricatives"
   "fricative (+continuant, −sonorant)","2–3",""
   "nasal","4–5", ""
   "liquid","6–7", ""
   "glide","8", ""
   "vowel (close → open)","8–9","Open vowels most sonorous"
   "diphthong","8–9","Same as high vowel per UC-01"

Ties with glides at 8 are expected, not anomalies. Consider 9 or
a clearer mechanism for glide vs. close vowel.
:cite:p:`clements1990`, :cite:p:`hayes2009` as basis,
:cite:p:`kramer2020` as known simplification.

.. todo::
   :class: warning

   **Validate expected-rank ranges**
   The ranges above are sketches from the standard sonority
   hierarchy (cite: :cite:p:`hayes2009`). Before implementation,
   verify each range against the full pinned vocabulary and
   decide behaviour for mixed-feature segments (e.g., prenasalized
   stops, which are phonetically complex). Feeds UC-01 extension 4a.

Validation Rules
-----------------

- ``symbol``: non-empty; unique in inventory; normalized to
  tie-bar form where applicable (ADR-028); membership in
  ``ipa_reference.json`` determines known vs custom
- ``features``: every key must be in the pinned vocabulary or the
  project's ``custom_features``; values validated per the
  vocabulary's value domains
- ``category``: stored (denormalized cache for fast lookups) and
  recomputed on load per the ADR-032 derivation table. On
  divergence: warning naming both values, **stored value
  retained** — the stored category is the author's ruling, the
  recompute is advisory (Q5, resolved 2026-09-16). Divergence
  indicates either a feature edit was made without refreshing
  category, or the derivation table changed between versions;
  the warning suggests reviewing the feature set rather than
  auto-correcting.
- ``sonority_rank``: integer 0–9; warn if outside expected range
  for features (overridable)
- ``frequency``: positive float; no upper bound (relative weight)
- Diphthong: both components should resolve to phonemes in the
  inventory; missing component → warning (severity: non-blocking)

Merge Semantics (Duplicate Symbols)
-----------------------------------

Resolved per :ref:`adr-051` (accepted 2026-09-23). When a
phoneme is added whose ``symbol`` already exists in the
inventory:

- **Interactive path** (UC-01 manual add): a dialog shows both
  records side-by-side with per-field selection, prefilled with
  the deterministic outcomes below (confirm-don't-block, per
  ADR-035's pattern).
- **Deterministic fallback** (UC-009 batch import, headless,
  test fixtures): field-class rules apply:

.. csv-table::
   :header-rows: 1
   :widths: 25 35 40

   "Field","Rule on conflict","Rationale"
   "features","Union: new keys added; conflicting values retain existing","Corrections are deliberate acts; never-downgrade (ADR-040)"
   "sonority_rank","Existing wins, always","Stored value is authoritative once confirmed (UC-01 ext 4a)"
   "frequency","Sum values; renormalize at selection time","Duplicates represent double-counted attestation (Q7)"
   "category","Recomputed from merged features","Derived, never merged (ADR-032)"
   "components, custom, metadata","New-only fill (empty adopts incoming; populated retains)","Least surprise"

Every fallback decision is written to the collision log, making
an interactive replay possible later and giving the rules a pure,
pytest-able surface.

Near-Miss Detection
-------------------

Decided per :ref:`ADR-041` (NFD base-stripping); tie-bar
compositions are excluded from diacritic-similarity comparison
by that ruling.

.. todo::
   :class: warning

   **Verify near-miss rule against tie-bar normalizer**
   Remaining: the implementation test that proves the normalizer
   and the similarity check compose correctly (``t͡s`` vs ``ts``
   must *not* be reported as a diacritic near-miss of each other).

Relations
---------

- Resolved by: ADR-032 (derived category), ADR-033 (feature
  system + representation), ADR-040 (merge safety — field-class
  rules above), ADR-041 (near-miss), ADR-051 (field-class rules above)
- Feeds: UC-01 (implementable — flags cleared), UC-005
  (serialization), UC-009 (import merge path), UC-012
  (segmentation/normalization), Q38 (``ipa_reference.json``
  supplies feature vocabulary, frequency, rarity data)
- Inventory-level structural checks (nucleus-capable minimum,
  complement warnings, identical-feature-set warning) are owned
  by :ref:`dc_inventory` invariants — not repeated here
- See also: :ref:`dc_language_definition`, :ref:`dc_ipa_reference`

Implementation Bindings
-----------------------

Planned homes (no code exists yet; subject to change without
contract amendment — the semantic rules above are the stable
part):

- ``latticelang.core.phonemes`` — ``Phoneme`` class, merge logic
- Warnings: ``CategoryDivergenceWarning``, near-miss report types
- Tests: ``tests/test_phoneme_merge.py`` (field-class rules are
  pure functions), ``tests/test_near_miss.py``
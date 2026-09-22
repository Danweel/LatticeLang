.. _dc_inventory:

Data Contract: dc_inventory
===========================

Purpose
-------
Defines the phoneme inventory: the complete set of segments a
language draws from, with their features, categories, sonority
ranks, and frequency weights. Created and maintained by UC-01;
consumed by UC-02 (template categories reference it), UC-03
(constraints validate against it), UC-04/UC-014 (eligibility and
selection), and UC-07 (export charts).

.. note::
   This contract was reviewed during the 2026-09-16 use-case
   and spec-completeness audit. See :ref:`audit-september-2026`
   for the full findings table. Key design decisions:
   :ref:`adr-047` (logical schema vs. adapters),
   :ref:`adr-048` (tone as separate stage),
   :ref:`adr-049` (coordinate-addressed random streams),
   :ref:`adr-050` (qualitative ambiguity tiers).

Shape
-----

.. code-block:: json

   {
     "schema_version": "1.0",
     "phonemes": [
       {
         "ipa": "ʃ",
         "features": { "place": "post_alveolar", "manner": "fricative", "voice": "+" },
         "category": "consonant",
         "syllabic": "-",
         "sonority": 4,
         "frequency": 0.052
       }
     ]
   }

Fields
------

``schema_version``
   Integer. Front-loaded per engineering phases — every breaking
   change bumps this.

``phonemes[].ipa``
   Unicode IPA string; unique within the inventory.

``phonemes[].features``
   Required, non-empty. Keys/values from the pinned controlled
   vocabulary (ADR-033, PHOIBLE 2.0 feature system). No
   user-defined feature names — custom segments use the same
   vocabulary (UC-07 extension 2b exists for chart placement, not
   for feature invention).

``phonemes[].category``
   One of the ADR-032 categories (``consonant``, ``vowel``,
   ``glide``, ``diphthong``, ``custom``). Derived from features,
   not stored as independent truth — if a loader computes a
   different category than stored, that's a validation error
   (ADR-032: category derives from features; this field is a
   denormalized cache for O(1) lookups).

``phonemes[].syllabic``
   ``"+" | "-"``. ``"+"`` phonemes are automatically eligible for
   nucleus slots (ADR-034 rule 2). Glides are opt-in for nuclei;
   a diphthong fills exactly one nucleus slot.

``phonemes[].sonority``
   Integer rank. Used by SSP evaluation and ordered filtering;
   no cross-phoneme rank uniqueness requirement (ties allowed —
   equal sonority is attested and meaningful).

``phonemes[].frequency``
   Positive number (Q7: positive relative weight — zero and
   negatives are invalid; zero-frequency is expressed by removing
   the phoneme). Never persisted-normalized; normalization is
   per-slot at selection time (Q7, UC-014 step 4).

#. Inventory-level structural checks (at least one nucleus-capable
   phoneme, complement warnings, identical-feature-set warning)
   are owned by :ref:`dc_inventory` invariants 1–4; this envelope
   validates them transitively whenever ``phonemes`` is non-empty.
   Rationale: duplicating the rules in two contracts recreates
   exactly the drift problem we spent this audit eliminating
   (the frequency_weights lesson). One owner, one cross-ref.

Invariants (validated at save, per UC-01)
-----------------------------------------

1. At least one phoneme with ``syllabic: "+"`` must exist (a
   language without a nucleus-capable segment cannot form
   syllables — UC-04 precondition, ADR-036 check)
2. Every ``category`` referenced by any template must be
   populated (UC-04 precondition; a template with a nucleus and
   no vowels is a generation-time deadlock caught at save)
3. IPA uniqueness within the inventory
4. Category derivation consistency (per ADR-032)

Consumers
---------
UC-02, UC-03, UC-04, UC-014 (via eligibility per ADR-034),
UC-07, and ``dc_ipa_reference`` (joined by IPA symbol; the
reference table is build-time, per ADR-033 — this contract is the
runtime source of truth).

Notes
-----

 ADR-036 ruled dc_inventory exists — the three rules
 belong there, with only "minimum viable inventory"
 also referenceable from UC-04's precondition.

   - Minimum viable inventory: at least one nucleus-capable
     phoneme before generation (UC-04 precondition)
   - Complement checks: warn if zero consonants or zero vowels
   - Identical-feature-set warning: two phonemes with
     non-identical symbols but identical full feature sets
     (likely allophones or an entry mistake)

The slot-fillability question for the fifth category. The answer
follows the model's own logic rather than needing a new rule: custom
is a valid entry in any slot's allowed_categories, and eligibility
is governed by the syllabic flag, not by the category label. A
custom phoneme with syllabic: "-" fills margins normally; a nucleus
slot listing custom admits any custom phoneme with syllabic: "+". The
category just means "no feature-pattern match" — it doesn't disable
participation. Two guard clauses make it safe: a custom phoneme appearing
in a slot must still satisfy the syllabic-mismatch warning rule
(below), and UC-01's custom-segment path already forces real feature
values (ADR-033: no feature invention), so sonority and constraint
evaluation still work on it. The chart-placement note from
dc_inventory (UC-07 ext 2b) is where custom interacts with export,
not eligibility. In short: custom is fully slot-eligible, checked
by the same two rules as everything else — which is the mark of a
well-behaved category.

- ``category``: stored (denormalized cache for O(1) lookups) and
  recomputed on load per the ADR-032 derivation table. On
  divergence: warning naming both values, **stored value
  retained** — the stored category is the author's ruling, the
  recompute is advisory (Q5 resolved 2026-09-16). Divergence
  indicates either a feature edit was made without refreshing
  category, or the derivation table changed between versions;
  the warning text should suggest reviewing the feature set
  rather than auto-correcting.
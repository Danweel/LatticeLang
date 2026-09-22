.. _dc_syllable_template:

Syllable Template Data Contract
===============================

:data structure: SyllableTemplate
:owner: Phonology Tool
:created by: UC-02; consumed by UC-04, UC-014, UC-013, UC-07
:status: Draft, revised 2026-09-16: mismatch rule softened per ADR-035 consistency

.. note::
   This contract was reviewed during the 2026-09-16 use-case
   and spec-completeness audit. See :ref:`audit-september-2026`
   for the full findings table. Key design decisions:
   :ref:`adr-047` (logical schema vs. adapters),
   :ref:`adr-048` (tone as separate stage),
   :ref:`adr-049` (coordinate-addressed random streams),
   :ref:`adr-050` (qualitative ambiguity tiers).

Overview
--------

A syllable template is a linear pattern of slot roles defining
one syllable type: a sequence of margin and nucleus slots, each
admitting phoneme categories per the eligibility rules below.
Templates are data — the generation pipeline composes words by
selecting templates (:ref:`ADR-049`, domain ``template``) and
filling their slots (:ref:`uc004`).

Logical schema per :ref:`ADR-047`; the JSON form is the Phase
Beta binding.

Fields (semantic)
-----------------

Templates
'''''''''

``templates[].id``
   String; required; unique within the definition; stable across
   saves (referenced by diagnostics and generation records).

``templates[].slots``
   Array of slot objects; required; non-empty. **Array order is
   semantic** — slot sequence defines syllable shape and must
   survive serialization round-trips (:ref:`uc005`).

Slots
''''

``slots[].slot_index``
   Integer; zero-based position within the template's slot
   sequence. Implied by array order; explicit in serialization.

``slots[].position``
   ``onset | nucleus | coda``. The slot's structural role.

``slots[].allowed_categories``
   Array; required; non-empty. Subset of ``consonant | vowel |
   glide | diphthong | custom`` (categories per ADR-032).
   **Tone is not a slot category** — tonal behavior is enforced
   by ``tone_assignment`` and configured by a future stage
   (:ref:`ADR-048`).

``slots[].allowed_phonemes``
   Optional array of IPA symbols restricting the slot beyond
   category eligibility; must intersect the category-eligible
   set (:ref:`uc004` receives template constraints as part of
   its inputs).

Reserved (post-MVP, not in Phase Beta schema): ``weight``
(template selection weight — MVP selection is uniform).

Eligibility Rules (normative)
-----------------------------

1. **Nucleus slots admit ``syllabic: "+"`` segments**
   (:ref:`ADR-034`): vowel and diphthong categories by default;
   glides are opt-in with a warning (attested but marginal).
2. **Margin slots admit ``syllabic: "-"`` segments.** A
   ``syllabic: "+"`` category listed in a margin slot triggers
   ``TypologicalMismatchWarning`` — shown and dismissible, never
   rejected (ADR-035 override philosophy; covers vowel/diphthong
   in onset and coda, including the typologically unprecedented
   diphthong-onset design).
3. **A diphthong occupies exactly one slot** (:ref:`ADR-028`);
   contrast with hiatus — two nuclei in adjacent syllables —
   and with nucleus + offglide (glide in margin), which are
   distinct, expressible structures.
4. **Explicit ``allowed_phonemes`` is an intersection filter**:
   the effective set is category-eligible ∩ explicit list. Empty
   effective set is a validation error, not a generation-time
   surprise.

Validation (at save, per UC-02)
-------------------------------

#. Exactly one nucleus slot per template (MVP; per-mora
   structures are post-MVP).
#. Slot-sequence extent: onset or coda slot count exceeding 3 →
   ``TypologicalRangeWarning``, confirmation required
   (:ref:`ADR-035`; UC-02's former hard cap is superseded).
#. Every ``allowed_categories`` entry populated in the
   inventory (cross-contract: dc_inventory invariant 2 —
   generation-time deadlock caught at save).
#. Every ``allowed_phonemes`` symbol exists in the inventory;
   effective set non-empty (rule 4).
#. Mismatch rules 1–2 above.

Relations
---------

Extends: :ref:`ADR-034` (eligibility), :ref:`ADR-047` (logical
schema). Enforced by: :ref:`uc013` (validation), :ref:`uc004` /
:ref:`uc014` (selection). Contrasts: hiatus (adjacent nuclei),
glide margins (:ref:`ADR-034`).

Test Cases
----------

Test-first sketch; each case names the clause it enforces:

.. code-block:: python

   import pytest

   def test_valid_cvc_constructs():
       """Minimal conforming template."""
       t = SyllableTemplate(slots=[C, V, C])
       assert t.slot_count == 3

   def test_requires_exactly_one_nucleus():
       """Validation 1: CC-only → ValidationError."""
       with pytest.raises(ValidationError):
           SyllableTemplate(slots=[C, C])

   def test_diphthong_in_margin_warns():
       """Eligibility 2: syllabic+ category in onset slot →
       TypologicalMismatchWarning, not rejection (revised
       ruling, 2026-09-16)."""
       with pytest.warns(TypologicalMismatchWarning):
           Slot(position="onset", allowed_categories=["diphthong"])

   def test_max_onset_extent_warns():
       """Validation 2: four onset slots → warn, confirm."""
       with pytest.warns(TypologicalRangeWarning):
           SyllableTemplate(slots=[C, C, C, C, V])

   def test_unpopulated_category_rejected():
       """Validation 3: category with no inventory members →
       error at save."""
       with pytest.raises(UnpopulatedCategoryError):
           validate(t, inventory_empty_for="glide")

   def test_explicit_list_intersection_empty():
       """Eligibility 4: allowed_phonemes disjoint from
       category set → ValidationError."""
       with pytest.raises(ValidationError):
           Slot(position="onset", allowed_categories=["consonant"],
                allowed_phonemes=["a"])

   def test_round_trip_preserves_slot_order():
       """UC-005: dump → load preserves slot sequence —
       order is semantic."""
       assert load(dump(t)) == t

Implementation Bindings
-----------------------

Current API homes (subject to change without contract amendment;
the semantic rules above are the stable part):

- ``latticelang.core.templates`` — ``SyllableTemplate``,
  ``Slot`` (``SlotPosition`` enum), ``TemplateValidator``
- Exceptions: ``ValidationError``, ``UnpopulatedCategoryError``
- Warnings: ``TypologicalMismatchWarning``,
  ``TypologicalRangeWarning``
- Preset example: ``english_ga.json``

(verify):
Adjust constructor/class names to the real API when it exists;
what's normative is the case list: each row of that table maps
a decision (ADR-028/034/035, dc_inventory invariant 2, UC-005
round-trip) to an assertion. If a test can't be written because
the contract is ambiguous, that's the contract telling you where
it's under-specified — the max_count warning case, for instance,
forced us to decide "warns, needs confirmation" rather than
leaving ADR-035's spirit implicit.
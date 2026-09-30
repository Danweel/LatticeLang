.. _dc_inventory:

Inventory Data Contract
=======================

:data structure: Inventory (validation view over the
   phoneme collection in :ref:`dc_language_definition`)
:source: user-defined entries (:ref:`dc_phoneme`), plus
   reference-sourced pre-fill (:ref:`dc_ipa_reference`)
:consumed by: UC-01 (inventory review), UC-04 (generation
   preconditions), UC-009 (import review), UC-08 (preview
   diagnostics)
:status: Draft
:note: Reviewed against ADR-036 (dedicated inventory contract).

Overview
--------

The phoneme inventory is a *set*, and sets have properties no
individual phoneme can violate: you can hold one perfectly valid
phoneme and still have an inventory that cannot generate a
single word. This contract specifies the checks that validate
the inventory as a whole.

It owns no serialization. :ref:`dc_language_definition` remains
the envelope that persists phonemes; entries themselves conform
to :ref:`dc_phoneme`. This contract is the validation layer
that runs over the loaded collection — at inventory review
(UC-01), before generation (UC-04), after corpus import
(UC-009), and for preview diagnostics (UC-08).

Severity Policy
---------------

All checks follow :ref:`ADR-035`:

- **Errors** fire only on structural impossibility — states
  where generation provably cannot succeed. An error blocks.
- **Warnings** fire on states that are probably mistakes but
  could be intended. A warning never blocks.
- **Notes** fire on states worth surfacing for pedagogy or
  data-quality review, including information that pairs two
  observations together.

Validation Rules
----------------

.. list-table::
   :header-rows: 1
   :widths: 22 12 66

   * - Rule
     - Severity
     - Condition
   * - Nucleus capacity
     - Error
     - No phoneme in the inventory is nucleus-capable
       (:ref:`ADR-034` rule 1: ``syllabic=+``, or category
       ``vowel`` or ``diphthong``)
   * - Consonant absence
     - Warning
     - Inventory contains zero consonants
   * - Vowel absence
     - Warning
     - Inventory contains zero vowels while a template's
       nucleus slot cannot be filled by a syllabic consonant
   * - Identical feature sets
     - Warning
     - Two phonemes carry fully identical ``features``
   * - Minimal feature sets
     - Note
     - Two phonemes' feature sets differ in exactly one feature
   * - Missing diphthong component
     - Warning
     - A diphthong's component symbol is not in the inventory
       (:ref:`dc_phoneme` validation rule, evaluated here per
       ADR-036; non-blocking)

Nucleus Capacity (INV-1)
~~~~~~~~~~~~~~~~~~~~~~~~

At least one phoneme must be eligible for a nucleus slot. This
mirrors :ref:`ADR-034`'s eligibility predicate exactly — one
definition, two consumers (the template engine reads the same
predicate when filling slots). An inventory failing this check
cannot generate any word with any template; the error blocks
UC-04 before generation starts, with a remediation hint ("add a
vowel or a syllabic consonant").

Consonant and Vowel Absence (INV-2, INV-3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A vowelless language is typologically real (e.g., Nuxalk), and
syllabic consonants can carry nuclei (:ref:`ADR-034` rule 1), so
absence is never a hard error. Both checks are warnings and
include their reasoning in the message: for INV-3, the warning
fires only when templates genuinely require filling — an
inventory of syllabic-consonant nuclei with matching templates
is silent.

Identical Feature Sets (INV-4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two phonemes with identical features but different symbols are
either allophones recorded as separate phonemes or an entry
mistake. The warning is paired with :ref:`ADR-041`'s NFD
detector: when the symbols are also near-misses ("n" and
"n̥"), the message upgrades to name the diacritic — this is the
paired observation the near-miss design predicts.

Minimal Feature Sets (INV-5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature sets differing in exactly one feature are legitimate
minimal pairs (/t/ vs /d/) — normal and unremarkable. The note
exists only for the entry-mistake case and surfaces only when
paired with symbol similarity (:ref:`ADR-041`), per :ref:`ADR-041`
's rejection of feature-distance as a similarity trigger on
its own. Never blocks, never warns on its own.

Load-Time Enforcement
---------------------

All checks run at inventory load and on every mutation that
changes the outcome set (add, remove, merge per :ref:`ADR-040`,
feature edit). Results are advisory surfaces to the callers
above; only INV-1 propagates as a blocking error into UC-04's
precondition check.

Post-MVP: the reverse pipeline's plausibility audit
(:ref:`q41-corpus-inference` layer 4) reports against these
same checks, extending the rule table rather than replacing it.

Implementation Bindings
-----------------------

Assumed surface (2026-09-30 implementation pass; subject to
change without contract amendment):

- ``latticelang.core.phonology.Inventory`` — class home per
  UC-01; ``add()`` routes duplicate symbols through the
  :ref:`ADR-051` deterministic fallback; ``check(templates)``
  returns an ``InventoryReport`` (errors/warnings/notes lists)
  and never raises
- Nucleus-capable predicate: ``syllabic='+'`` or category in
  {vowel, diphthong} — one definition mirroring :ref:`ADR-034`
  rule 1, shared with the future template engine
- INV-3 without templates is silent (ruled 2026-09-30): the
  warning fires only when a template's nucleus requires vowel
  category; with no template context the requirement cannot
  be judged, so no warning is emitted
- Templates arrive as stand-ins exposing
  ``nucleus_categories``; binding tightens to the real
  dc_syllable_template objects when the template engine lands
- INV-5 emits nothing until ADR-041 near-miss detection
  exists (pairing-gated per Relations); positive cases live
  in the future ``tests/test_near_miss.py``
- Tests: ``tests/test_inventory.py`` (one test per rule,
  red-first 2026-09-30)

Relations
---------

- Validates: collections of :ref:`dc_phoneme` entries
- Governs: UC-01 (review surface), UC-04 (preconditions),
  UC-009 (import review), UC-08 (diagnostics)
- Governs, severity policy from: :ref:`ADR-035`
- Shares predicates with: :ref:`ADR-034` (nucleus eligibility)
- Paired with: :ref:`ADR-041` (near-miss detection),
  :ref:`ADR-040` (merge participates in check triggers)
- Is NOT: a serialization format (LanguageDefinition owns
  persistence), nor entry-level validation (:ref:`dc_phoneme`)
.. _dc_language_definition:

LanguageDefinition Data Contract
================================

:data structure: LanguageDefinition
:serialization: JSON (Phase Beta); logical schema per :ref:`ADR-047`
:used by: UC-005 (Serialize/Deserialize), UC-01 (Define Phoneme
   Inventory), UC-02 (Define Syllable Templates), UC-03 (Define
   Constraints), UC-04 (Generate Words), UC-08 (Preview hydration),
   UC-09 (Import writes it), UC-11 (Orthography), UC-07 (Export)
:status: Draft — see Open Work below

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

The ``LanguageDefinition`` is the shared data contract for both the
forward (generation) and reverse (analysis) pipelines. It represents
a complete or partial phonological specification that can be
serialized, shared between users, and loaded by any pipeline
component.

This contract defines the **logical schema only**. Per
:ref:`ADR-047`, physical persistence is an adapter at the boundary:
Phase Beta ships a single-file ``*.json`` adapter; the multi-module
``.llp`` directory container arrives with the suite's second module
as an additional adapter. No code in the core depends on the
physical layout — everything below is container-independent.

Add one UX sentence to the orthography module docs: "Rules are
stored as roman→IPA to support batch import; the export view shows
the inverse mapping. You may edit rules in either direction; the
system maintains consistency." That transparency kills the "why
is this backwards?" question.

.. note::
   The ``import_dialect_profile`` field stores which orthography
   profile was used for the initial romanization→IPA translation
   of an imported corpus. This is metadata (provenance), not active
   logic — once words are converted to IPA, the dialect setting
   doesn't influence subsequent generation or validation. Users
   select this once during import (UC-009); changing it later
   doesn't retroactively re-translate existing words.

   - Minimum viable inventory: at least one nucleus-capable
     phoneme before generation (UC-04 precondition)
   - Complement checks: warn if zero consonants or zero vowels
   - Identical-feature-set warning: two phonemes with
     non-identical symbols but identical full feature sets
     (likely allophones or an entry mistake)

Information Nicknames
---------------------

Shorthand names used throughout the use cases and documentation:

- **phoneme inventory** — the set of phonemes defined for this
  language (``phonemes``; per-phoneme frequency weights are part
  of each phoneme record, see :ref:`dc_phoneme` — there is no
  separate top-level weight map)
- **syllable templates** — the set of syllable structure patterns
  (``syllable_templates``)
- **constraints** — the phonotactic constraints applied during
  generation and validation (``constraints``)
- **orthography rules** — the romanization mapping
  (``orthography_rules``)

Field List
----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 10 55

   * - Field
     - Type
     - Required
     - Description
   * - ``schema_version``
     - string
     - Yes
     - Schema version identifier (``major.minor``, see
       `Schema Versioning`_ below).
   * - ``language_name``
     - string
     - Yes
     - Human-readable name for the language.
   * - ``phonemes``
     - array
     - Yes
     - Array of phoneme objects. See :ref:`dc_phoneme` (for the
       collection-level invariants, see :ref:`dc_inventory`).
   * - ``syllable_templates``
     - array
     - No*
     - Array of syllable template objects. See
       :ref:`dc_syllable_template`.
   * - ``constraints``
     - array
     - No*
     - Array of constraint objects. See :ref:`dc_constraints`.
   * - ``orthography_rules``
     - array
     - No*
     - Array of orthography rule objects. See
       :ref:`dc_orthography_rules`.
   * - ``import_dialect_profile``
     - string
     - No
     - Identifier of the orthography profile used for initial
       corpus import (e.g., ``"american_english"``). Stored as
       provenance metadata; not actively consulted after the
       initial IPA translation completes. See :ref:`dc_orthography_rules`.

.. *Optional for partial definitions (e.g., presets containing only
   a phoneme inventory). Required for a "complete" definition usable
   by the generation pipeline; orthography rules are additionally
   required for round-tripping UC-011/UC-015 work.

Field Details
-------------

Each child collection's field schemas are owned by their own
contracts (:ref:`dc_phoneme`, :ref:`dc_syllable_template`,
:ref:`dc_constraints`, :ref:`dc_orthography_rules`); this contract
defines the envelope, cross-collection invariants (Field Checks),
and versioning. Not defined here: generation *records* (seed,
generator version, output) are runtime artifacts of :ref:`adr-049`,
not part of the persisted definition.

Field Checks
------------

Cross-collection invariants, validated at save (UC-01 through UC-03)
and at load (UC-005):

#. Every phoneme symbol referenced in ``syllable_templates``
   (allowed-phoneme lists) exists in ``phonemes``.
#. Every category referenced in ``syllable_templates`` exists in
   ``phonemes`` (populated categories — see dc_inventory
   invariant 2).
#. Every phoneme symbol and feature referenced in ``constraints``
   exists in ``phonemes`` or the pinned feature vocabulary
   (:ref:`ADR-033`).
#. Every IPA symbol referenced in ``orthography_rules`` exists in
   ``phonemes`` (warn per UC-11 extension 2a; partial coverage is a
   supported steady state) and is valid per :ref:`dc_ipa_reference`.
#. ``schema_version`` matches a known version identifier.
#. Duplicate phoneme symbols within ``phonemes`` are not permitted
   (collision handling itself is ADR-040 merge semantics).

.. _dc_schema_versioning:

Schema Versioning
-----------------

The ``schema_version`` field enables forward and backward
compatibility. This is deliberately front-loaded — retrofitting
versioning into an existing data format is significantly more
painful than including it from the start. The same field carries
:ref:`adr-049`'s generator-version key for determinism guarantees.

Version identifiers follow a ``major.minor`` string scheme
(e.g., ``"1.0"``):

- **Major** bump: breaking change to the data structure (fields
  removed or renamed, structure reorganized)
- **Minor** bump: additive change (new optional fields, new
  constraint types)

The deserialization logic (UC-005):

#. Reads ``schema_version`` first.
#. Loads the data with the appropriate schema handler if the
   version is known.
#. Raises ``DeserializationError`` recommending a LatticeLang
   update if the version is *newer* than the loader supports.
#. Attempts migration if the version is older (future work; for
   MVP, raise a descriptive error naming the detected version).

.. note::
   Migration logic for older schema versions is **post-MVP**. For
   MVP we include the version field and validate against it, but
   do not implement automated migration. The hook without the
   cost.

Implementation Bindings
-----------------------

Current homes (subject to change without contract amendment; the
semantic rules above are the stable part):

- ``latticelang.io`` — save/load adapters (:ref:`ADR-047`);
  Phase Beta ships ``save_project`` / ``load_project`` (single
  JSON)
- ``latticelang.io.import`` — UC-009's import wizard;
  dialect selection is presented here before corpus processing
- Preset example: ``english_ga.json``
- ``latticelang.core`` — the classes hydrated *by* the adapters

At import time (UC-009 step 2):

1. User selects a dialect profile (MVP default: ``"american_english"``).
2. The selected profile is stored in ``import_dialect_profile``.
3. The import wizard translates the corpus using that profile's rules.
4. After completion, the stored IPA words no longer depend on the
   profile — it becomes read-only history.

Future work: additional profiles inherit from or override the GA
baseline per :ref:`q2-dialect-rules` (dialect inheritance architecture).

Open Work
---------

- ``dc_constraints`` is still stub-grade; its finalization may add
  envelope-visible validation rules (ADR-046's report schema rides
  with it).
- ``dc_orthography_rules`` has a pending rule-orientation decision
  (see that contract's audit notes).

.. note::
   Migration logic for older schema versions is **post-MVP**. For
   MVP, the loader rejects unknown/newer versions with a descriptive
   error naming the detected version. Older versions may load with
   missing fields or degraded features. This gives you a hook
   without the upfront cost of writing migration transformers.
.. _architecture:

Architecture
============

:date: 2026-09-30 (rewritten; supersedes 2026-08-24 draft)
:type: Semi-static
:audience: Developers and contributors
:purpose: How is the code organized?

This document describes the module layout, interfaces, and design
patterns of LatticeLang. It was rewritten to realign with the
September 2026 decision records (ADR-032 through ADR-051) and the
current implementation state; items are labeled **implemented** or
**planned** so the document stays honest about which is which.

Module Layout
-------------

.. code-block:: text

   latticelang/
   ├── __init__.py
   ├── core/                # zero-dependency engine (ADR-010)
   │   ├── phonology.py     # IMPLEMENTED: Phoneme, merge_phonemes,
   │   │                    #   derive_category (ADR-032/033);
   │   │                    # PLANNED: Inventory, segment_ipa (ADR-014)
   │   ├── sonority.py      # IMPLEMENTED: propose_sonority_rank,
   │   │                    #   expected_rank_range (dc_phoneme)
   │   ├── syllable.py      # planned: Syllable (dc_syllable_template)
   │   ├── templates.py     # planned: SyllableTemplate, validation
   │   ├── constraints/     # planned: catalog validators (ADR-037)
   │   ├── generator.py     # planned: word composition (ADR-049)
   │   └── analysis.py      # planned: definition validation (UC-013)
   ├── io/                  # planned: persistence adapters (ADR-047);
   │                        #   Phase Beta ships single-file JSON
   ├── orthography/         # transitional: transliteration rules;
   │                        #   json_io migrates to latticelang.io
   ├── utils/
   └── ui/                  # Phase Gamma: PySide6 interface

Reference data lives outside the package, in the repository root:
``data/ipa_reference.json`` (built by the Q38 derive script,
read-only at runtime) and ``data/presets/`` (user starting points,
:ref:`dc_language_definition` instances).

.. note::

   Two Alpha-era files await reconciliation with this layout:
   ``core/inventory.py`` (the ``Inventory`` class belongs in
   ``core/phonology.py`` per UC-01's references) and
   ``orthography/json_io.py`` (superseded by ADR-047's
   ``latticelang.io``). Neither is referenced by current code.

Layering
--------

Dependency direction points inward (:cite:p:`martin2017`):

- ``core`` imports nothing outside the standard library
  (:ref:`ADR-010`).
- ``io`` adapts the logical schema (:ref:`dc_language_definition`)
  to physical containers; core never knows the container.
- ``ui`` and CLI shells wrap the same engine calls.
- Learning/statistical acquisition, when it exists, is an outer
  layer writing serialized definitions — never inside the
  evaluation loop (:ref:`ADR-045`).

Randomness is coordinate-addressed, not shared: every decision
draws from a pure stream keyed by (project_seed, word_position,
domain, index) (:ref:`ADR-049`), so downstream edits never
perturb upstream draws and any word regenerates in isolation.

Design Patterns
---------------

Universal→Override Model
~~~~~~~~~~~~~~~~~~~~~~~~

Inspired by Universal Dependencies' approach to language-specific
annotation :cite:p:`ud2024`, LatticeLang separates universal
defaults from language-specific overrides.

.. code-block:: json

   {
     "defaults": {
       "max_onset_length": 3,
       "max_coda_length": 3,
       "sonority_sequencing": true
     },
     "overrides": {
       "max_onset_length": 2,
       "prohibited_clusters": ["pk", "bg"]
     }
   }

This pattern supports clean base configurations that apply
broadly, language-specific overrides without duplicating the
full definition, and future dialect chains (:ref:`q2-dialect-rules`).

.. note::

   This pattern is **designed but not yet implemented**. See
   :ref:`q23-universal-override-model`. The visible-defaults
   principle it rests on *is* implemented in spirit: the default
   ``sonority_sequencing`` constraint ships visible and
   toggleable, not hidden (:ref:`ADR-038`).

Theory-Agnostic Constraint Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constraints carry a ``mode`` field indicating their theoretical
framework. Currently only ``"generative"`` is active; ``"OT"`` is
reserved (:ref:`ADR-037` reserves additional post-MVP types,
including probabilistic/gradient evaluation). See
:ref:`theoretical_framework` for details.

Extensibility
~~~~~~~~~~~~~

Following the CoNLL-U :cite:p:`conllu` design philosophy, data
contracts include a ``metadata`` or ``custom`` field as an escape
hatch for unforeseen user needs. This prevents format-breaking
migrations when new features are added. See :ref:`q21-conllu-interchange`.

Derivation as Data, Not Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Categories and sonority ranks are derived from feature data by
pure functions (:ref:`ADR-032`, :ref:`ADR-033`) — never enums,
never hard-coded dispatch. The same rank-proposal function serves
runtime confirmation (UC-01 step 4) and the Q38 build script
(dc_ipa_reference), giving the derivation one home.

Interfaces
----------

Constraint Validation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def validate_syllable(
       syllable: Syllable,
       constraints: list[Constraint],
       word_context: WordContext | None = None
   ) -> ValidationResult:
       """Validate a syllable against a set of constraints.

       Results are four-valued per constraint: PASSED / FAILED /
       SKIPPED / ERROR (Q37; :ref:`dc_constraints` validation
       result schema). Word-domain constraints report SKIPPED
       when word_context is absent — distinct from PASSED, so
       batch surfaces don't lie by omission (:ref:`ADR-046`).
       """

Generation
~~~~~~~~~~

.. code-block:: python

   def generate_syllables(
       inventory: Inventory,
       templates: list[SyllableTemplate],
       constraints: list[Constraint],
       count: int = 100
   ) -> list[Syllable]:
       """Generate valid syllables from an inventory and templates.

       Candidates are composed per template (UC-014, streams per
       :ref:`ADR-049`) and filtered through constraints. Only
       syllables passing all active constraints are returned.
       """

Testing Strategy
----------------

LatticeLang follows a **test-first** approach: tests are written
against data contracts before implementation code. Failures at
red are read as contract information, not nuisances — several
spec corrections in this project originated as test failures
that revealed the draft tests, not the code, had drifted from
the contract.

Principles:

- Use ``pytest`` (not ``unittest``) for all tests
- Core layer tests must pass with zero optional dependencies
  installed (:ref:`ADR-010`)
- Serialization tests verify round-trip integrity:
  serialize → deserialize → compare
- Constraint tests verify both acceptance and rejection for
  each type
- Generation tests use seeded, coordinate-addressed streams
  (:ref:`ADR-049`) for reproducibility
- Feature values are controlled-vocabulary strings; tests
  reject booleans and enums (:ref:`ADR-033`)

Current test layout (implemented):

.. code-block:: text

   tests/
   ├── test_ipa_reference.py        # dc_ipa_reference field
   │                                #   checks (fixture)
   ├── test_phoneme_derivation.py   # derive_category, rank
   │                                #   proposal (dc_phoneme)
   ├── test_phoneme_contract.py     # Phoneme class, ADR-051
   │                                #   merge semantics
   └── test_derive_ipa_reference.py # stub: Q38 derive script
                                    #   acceptance tests (planned)

Planned additions map to their contracts:
``test_inventory.py`` (dc_inventory invariants, including the
diphthong-component warning), ``test_syllable_templates.py``
(UC-02), ``test_constraints.py`` (UC-03), ``test_generator.py``
(UC-04), ``test_serializer.py`` (UC-005), ``test_near_miss.py``
(ADR-041), ``test_segmenter.py`` (UC-012).
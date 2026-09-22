.. _architecture:

Architecture
============

:date: 2026-08-24
:type: Semi-static
:audience: Developers and contributors
:purpose: How is the code organized?

This document describes the module layout, interfaces, and design patterns
of LatticeLang.

Module Layout
-------------

.. code-block:: text

   latticelang/
   ├── __init__.py
   ├── models/           # Data contracts (Phoneme, Syllable, LanguageDefinition)
   ├── ipadata/          # IPA reference tables (JSON)
   ├── constraints/      # Constraint validators
   ├── generator/        # Syllable/word generation engine
   ├── segmenter/        # Orthography → IPA segmentation
   ├── serializer/       # JSON load/save for LanguageDefinition
   └── gui/              # PySide6 interface (Phase Gamma)

Design Patterns
---------------

Universal→Override Model
~~~~~~~~~~~~~~~~~~~~~~~~

Inspired by Universal Dependencies' approach to language-specific
annotation :cite:p:`ud2024`, LatticeLang separates universal defaults from
language-specific overrides.

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

This pattern supports:

- Clean base configurations that apply broadly
- Language-specific or dialect-specific overrides without duplicating
  the full definition
- Future dialect chains (see :ref:`q2-dialect-rules`)

.. note::

   This pattern is **designed but not yet implemented**. See
   :ref:`q23-universal-override-model`.

Theory-Agnostic Constraint Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constraints carry a ``mode`` field indicating their theoretical framework.
Currently only ``"generative"`` is active; ``"OT"`` is reserved for future
implementation. See :ref:`theoretical_framework` for details.

Extensibility
~~~~~~~~~~~~~

Following the CoNLL-U :cite:p:`conllu` design philosophy, data contracts
should include a ``metadata`` or ``custom`` field as an escape hatch for
unforeseen user needs. This prevents format-breaking migrations when
new features are added.

See :ref:`q21-conllu-interchange` for details.

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

       Parameters
       ----------
       syllable
           The syllable to validate.
       constraints
           List of constraint definitions.
       word_context
           Optional surrounding word context for cross-syllable
           constraints. Currently unused (MVP constraints are
           within-syllable only), but the interface supports it
           for post-MVP harmony and stress constraints.
       """

Generation
~~~~~~~~~~

.. code-block:: python

   def generate_syllables(
       phoneme_inventory: PhonemeInventory,
       templates: list[SyllableTemplate],
       constraints: list[Constraint],
       count: int = 100
   ) -> list[Syllable]:
       """Generate valid syllables from an inventory and templates.

       Generates candidates from templates, then filters through
       constraints. Only syllables passing all constraints are returned.
       """

Testing Strategy
----------------

LatticeLang follows a **test-first** approach: tests are written against
data contracts before implementation code.

Principles:

- Use ``pytest`` (not ``unittest``) for all tests
- Core layer tests must pass with zero optional dependencies installed
- Serialization tests verify round-trip integrity: serialize → deserialize
  → compare
- Constraint tests verify both acceptance (valid candidates pass) and
  rejection (invalid candidates fail) for each constraint type
- Generation tests use seeded PRNG (ADR-024) for reproducibility

Tests are organized by module, mirroring the source structure:

.. code-block:: text

   tests/
   ├── test_phoneme_inventory.py    # UC-01
   ├── test_syllable_templates.py   # UC-02
   ├── test_constraints.py          # UC-03
   ├── test_generator.py            # UC-04
   ├── test_serializer.py           # UC-005
   └── test_segmenter.py            # UC-012
.. _decisions:

Decision Log
============

:date: 2026-08-24
:type: Append-only
:audience: Developers and contributors
:purpose: What did we decide and why?

This file is an **Architecture Decision Record (ADR) log**. Each entry
records a decision, its context, and its consequences. Entries are
append-only — past decisions are never edited, only superseded by new
ones.

---

.. contents::
   :local:
   :depth: 2

Tagging Convention
-------------------

Each ADR is tagged with its tool scope:

- ``[PHONO]``     — Phonology Tool
- ``[SUITE]``     — Cross-tool / Suite-level
- ``[ORTHO]``     — Orthography Tool
- ``[MORPH]``     — Morphology Tool
- ``[DOCS-WIDE]`` — Docs-specific decisions

---

ADR Index
=========

.. list-table::
   :header-rows: 1
   :widths: 10 15 50 10 15 15

   * - ID
     - Scope
     - Title
     - Status
     - Date
     - Deciders
   * - :ref:`ADR-001`
     - [SUITE]
     - GPL-3.0-or-later License
     - Accepted
     - 2026-04-03
     - Danweel
   * - :ref:`ADR-002`
     - [SUITE]
     - src/ Layout for Package
     - Accepted
     - 2026-04-03
     - Lumo
   * - :ref:`ADR-003`
     - [DOCS-WIDE]
     - PEP 621 Extras for Dependencies
     - Accepted
     - 2026-04-03
     - Lumo
   * - :ref:`ADR-004`
     - [DOCS-WIDE]
     - Sphinx Pinned Below 9.0
     - Accepted
     - 2026-04-03
     - Lumo
   * - :ref:`ADR-005`
     - [DOCS-WIDE]
     - Dev Tools Excluded from RTD Build
     - Accepted
     - 2026-04-03
     - Danweel
   * - :ref:`ADR-006`
     - [DOCS-WIDE]
     - Ruff E501 Suppression in conf.py
     - Accepted
     - 2026-04-03
     - Danweel
   * - :ref:`ADR-007`
     - [PHONO]
     - PySide6 Over PyQt6
     - Accepted
     - 2026-04-04
     - Danweel
   * - :ref:`ADR-008`
     - [PHONO]
     - TITLE
     - Accepted
     - 2026-04-04
     - Danweel
   * - :ref:`ADR-009`
     - [PHONO]
     - English as Validation Language
     - Accepted
     - 2026-04-04
     - Danweel
   * - :ref:`ADR-010`
     - [PHONO]
     - Core Layer is Zero-Dependency
     - Accepted
     - 2026-04-04
     - Danweel
   * - :ref:`ADR-011`
     - [PHONO]
     - Live Preview is a Core Differentiator
     - Accepted
     - 2026-04-04
     - Danweel
   * - :ref:`ADR-012`
     - [PHONO]
     - Bidirectional Pipeline Architecture
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-013`
     - [PHONO]
     - Orthography Decoupled from Core
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-014`
     - [PHONO]
     - IPA Segmenter Lives in Core
     - Accepted
     - 2026-08-23
     - Danweel, Lumo
   * - :ref:`ADR-015`
     - [SUITE]
     - Pedagogy is a UI-Layer Concern
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-016`
     - [DOCS-WIDE]
     - Use Cases Link to API via Sphinx Roles
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-017`
     - [DOCS-WIDE]
     - Combined Steps in Use Cases
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-018`
     - [DOCS-WIDE]
     - Hard-Coded Extension Labels
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-019`
     - [DOCS-WIDE]
     - Primary Actor Documented Once
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-020`
     - [SUITE]
     - Use Case Numbering Convention
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-021`
     - [SUITE]
     - Reference Notes vs. Research Notes
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-022`
     - [PHONO]
     - Extensible Constraint System
     - Accepted
     - 2026-08-23
     - Mostly Lumo
   * - :ref:`ADR-023`
     - [PHONO]
     - No Implementation Before Use Cases Complete
     - Accepted
     - 2026-08-23
     - Danweel
   * - :ref:`ADR-024`
     - [PHONO]
     - Seeded PRNG for Reproducibility
     - Accepted
     - 2026-08-23
     - Lumo
   * - :ref:`ADR-025`
     - [PHONO]
     - Three-Level Exception Hierarchy
     - Accepted
     - 2026-08-23
     - Lumo
   * - :ref:`ADR-026`
     - [SUITE]
     - Separating Use Cases from Interface Details
     - Accepted
     - 2026-08-24
     - Danweel
   * - :ref:`ADR-027`
     - [PHONO]
     - Rule-Based Constraints for MVP
     - Accepted
     - 2026-08-29
     - Mostly Lumo
   * - :ref:`ADR-028`
     - [PHONO]
     - Tie-Bar Policy for Affricates
     - Accepted
     - 2026-08-29
     - Danweel
   * - :ref:`ADR-029`
     - [PHONO]
     - PHOIBLE CC-BY 4.0 Compatible with MIT/GPL
     - Accepted
     - 2026-08-29
     - Danweel, Lumo
   * - :ref:`ADR-030`
     - [PHONO]
     - CSV Tables Over Grid Tables
     - Accepted
     - 2026-08-30
     - Danweel
   * - :ref:`ADR-031`
     - [DOCS-WIDE]
     - PEP 621-only dependency structure
     - Accepted
     - 2026-08-30
     - Danweel
   * - :ref:`ADR-032`
     - [PHONO]
     - Phoneme category derived from features
     - Accepted
     - 2026-08-31
     - Danweel
   * - :ref:`ADR-033`
     - [PHONO]
     - PHOIBLE-aligned feature system
     - Accepted
     - 2026-09-06
     - Lumo
   * - :ref:`ADR-034`
     - [PHONO]
     - Slot eligibility — category matching
     - Accepted
     - 2026-09-06
     - Lumo
   * - :ref:`ADR-035`
     - [SUITE]
     - Naturalistic defaults design principle
     - Accepted
     - 2026-09-06
     - Danweel
   * - :ref:`ADR-036`
     - [PHONO]
     - Dedicated inventory data contract
     - Accepted
     - 2026-09-06
     - Lumo
   * - :ref:`ADR-037`
     - [PHONO]
     - Constraint Catalog — Nine MVP Types
     - Accepted
     - 2026-09-09
     - Danweel
   * - :ref:`ADR-038`
     - [PHONO]
     - Default Constraint State
     - Accepted
     - 2026-09-09
     - Danweel, Lumo
   * - :ref:`ADR-039`
     - [PHONO]
     - Constraint Domains and Word Context
     - Accepted
     - 2026-09-06
     - Danweel, Lumo
   * - :ref:`ADR-040`
     - [PHONO]
     - Merge Semantics for Duplicate Symbols
     - Accepted
     - 2026-09-06
     - Danweel, Lumo
   * - :ref:`ADR-041`
     - [PHONO]
     - Near-Miss Symbol Similarity
     - Accepted
     - 2026-09-06
     - Lumo
   * - :ref:`ADR-042`
     - [PHONO]
     - Harmony Constraint Parameterization
     - Accepted
     - 2026-09-09
     - Danweel, Lumo
   * - :ref:`ADR-043`
     - [PHONO]
     - Segmenter Ambiguity
     - Accepted
     - 2026-08-23
     - Danweel, Lumo
   * - :ref:`ADR-044`
     - [PHONO]
     - Seed Stability
     - Accepted
     - 2026-09-12
     - Lumo
   * - :ref:`ADR-045`
     - [PHONO]
     - Evaluation vs. Acquisition Scope
     - Accepted
     - 2026-09-15
     - Danweel, Lumo
   * - :ref:`ADR-046`
     - [GEN]
     - Generation Diagnostics
     - Accepted, unscheduled
     - 2026-09-16
     - Lumo
   * - :ref:`ADR-047`
     - [CORE]
     - Project Persistence
     - Accepted
     - 2026-09-16
     - Lumo
   * - :ref:`ADR-048`
     - [PHONO]
     - Tone Not a Slot Category
     - Accepted
     - 2026-09-16
     - Danweel, Lumo
   * - :ref:`ADR-049`
     - [GEN]
     - Coordinate-Addressed Streams
     - Accepted
     - 2026-09-16
     - Lumo
   * - :ref:`ADR-050`
     - [PHONO]
     - Ambiguity Confidence
     - Accepted
     - 2026-09-16
     - Lumo

---

.. _adr-001:

ADR-001: [SUITE] GPL-3.0-or-later License
-----------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Suite-wide
:Deciders: Danweel

Context
~~~~~~~

The project needed a license. Initial consideration was CC-BY-SA-4.0,
which is designed for content, not software.

Decision
~~~~~~~~

Switch from CC-BY-SA-4.0 to GPL-3.0-or-later.

Rationale
~~~~~~~~~

LatticeLang is software, not content. GPL-3.0-or-later is appropriate
for copyleft software and aligns with FOSS principles.

Consequences
~~~~~~~~~~~~

All code is GPL-3.0-or-later. Documentation and data (IPA reference,
PHOIBLE-derived data) retain their respective licenses (see
:ref:`documentation_standards`).

---

.. _adr-002:

ADR-002: [SUITE] src/ Layout for Package
----------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Suite-wide
:Deciders: Lumo

Context
~~~~~~~

Package structure choice for the project.

Decision
~~~~~~~~

Adopt ``src/`` layout for the Python package.

Rationale
~~~~~~~~~

Standard practice. Prevents import shadowing during development and testing.

---

.. _adr-003:

ADR-003: [DOCS-WIDE] PEP 621 Extras for Dependencies
----------------------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Docs-wide
:Deciders: Lumo

Context
~~~~~~~

Poetry groups are invisible to pip. Read the Docs needs PEP 621 extras
to install documentation dependencies.

Decision
~~~~~~~~

Use PEP 621 ``[project.optional-dependencies]`` for optional dependency
groups (docs, dev, gui). Do NOT use Poetry groups alone.

Rationale
~~~~~~~~~

Groups are not portable across build backends; extras are the standard.
RTD uses pip, which reads PEP 621 extras.

Consequences
~~~~~~~~~~~~

Install with ``poetry install --extras docs``. Extras are visible to
any build backend.

Supersedes
~~~~~~~~~~

None.

---

.. _adr-004:

ADR-004: [DOCS-WIDE] Sphinx Pinned Below 9.0
--------------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Docs-wide
:Deciders: Lumo

Context
~~~~~~~

RTD builds broke when Sphinx 9.1.0 was released, breaking several
extensions.

Decision
~~~~~~~~

Pin Sphinx ``< 9.0`` in pyproject.toml docs extras.

Rationale
~~~~~~~~~

Stability over bleeding-edge. Sphinx 9.x caused extension breakage.

Consequences
~~~~~~~~~~~~

Stable RTD builds. May lag behind latest Sphinx features until manually
reviewed and bumped.

---

.. _adr-005:

ADR-005: [DOCS-WIDE] Dev Tools Excluded from RTD Build
------------------------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

RTD was installing pytest and ruff unnecessarily, slowing builds and
risking version conflicts.

Decision
~~~~~~~~

Removed pytest and ruff from ``.readthedocs.yaml``. RTD only needs docs
extras.

Rationale
~~~~~~~~~

RTD builds documentation, not tests. Dev tools are irrelevant to doc
builds.

---

.. _adr-006:

ADR-006: [DOCS-WIDE] Ruff E501 Suppression in conf.py
-----------------------------------------------------

:Date: 2026-04-03
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

Sphinx ``conf.py`` files routinely exceed 88 characters due to long
extension lists and URL strings.

Decision
~~~~~~~~

Suppress E501 (line too long) in ``conf.py`` via ruff configuration.

Rationale
~~~~~~~~~

Sphinx config files are not production code. Enforcing line length on
them adds friction without benefit.

---

.. _adr-007:

ADR-007: [PHONO] PySide6 Over PyQt6
-----------------------------------

:Date: 2026-04-04
:Status: Accepted
:Scope: Phonology Tool (GUI)
:Deciders: Danweel

Context
~~~~~~~

GUI framework choice. Both PySide6 and PyQt6 provide Qt bindings for
Python.

Decision
~~~~~~~~

Chose PySide6 over PyQt6.

Rationale
~~~~~~~~~

PySide6 is LGPL-licensed (compatible with GPL-3.0). PyQt6 is
GPL-licensed, which would also be compatible, but PySide6 is the
official Qt Group binding and is more widely used in the conlanging
community.

---

.. _adr-008:

ADR-008: [PHONO] LaTeX is Export-Only
-------------------------------------

:Date: 2026-04-04
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

Whether to use LaTeX as a data format or only as an export target.

Decision
~~~~~~~~

LaTeX is export-only, not a data format. JSON/YAML is canonical for
project files.

Rationale
~~~~~~~~~

Parsing LaTeX is complex and fragile. JSON/YAML is simpler, more
portable, and well-supported by Python's standard library and ecosystem.

---

.. _adr-009:

ADR-009: [PHONO] English as Validation Language
-----------------------------------------------

:Date: 2026-04-04
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

Need a test language to exercise the engine. Should be well-documented
and stress-test most engine features.

Decision
~~~~~~~~

English as the primary validation/test language.

Rationale
~~~~~~~~~

English has well-documented phonology. It exercises most engine
features: consonant clusters, /s/-appendix violations of SSP, complex
onsets and codas, position restrictions.

English phonotactics — including the /s/+C clusters and complex
codas this ADR exercises — receive a thorough introductory
treatment in :cite:p:`hayes2009`, making the validation target
easy to verify against published analyses.

---

.. _adr-010:

ADR-010: [PHONO] Core Layer is Zero-Dependency
----------------------------------------------

:Date: 2026-04-04
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

The core phonology engine should be usable headlessly and in any
environment.

Decision
~~~~~~~~

Core layer has zero external dependencies. Only Python standard library.

Rationale
~~~~~~~~~

Testability and headless operation. No risk of dependency conflicts.
Core can run on any Python installation.

---

.. _adr-011:

ADR-011: [PHONO] Live Preview is a Core Differentiator
------------------------------------------------------

:Date: 2026-04-04
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

No competing conlanging tool offers live preview of generated words
as constraints change.

Decision
~~~~~~~~

Live preview is a core feature, not an add-on. It is prioritized from
the beginning of GUI development.

Rationale
~~~~~~~~~

Competitive advantage. Unique selling point. The immediate feedback
loop (adjust constraint → see results) is fundamentally different from
the generate-then-review workflow of other tools.

---

.. _adr-012:

ADR-012: [PHONO] Bidirectional Pipeline Architecture
----------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

The tool needs both forward (generate words from rules) and reverse
(infer rules from corpus) directions.

Decision
~~~~~~~~

LanguageDefinition is the shared data contract for both the forward
(generation) and reverse (analysis) pipelines. Both pipelines
read/write the same structure.

Rationale
~~~~~~~~~

A single data contract avoids duplication and ensures consistency.
Future reverse-analysis features (:ref:`uc009`) slot in without refactoring
the data model.

Consequences
~~~~~~~~~~~~

The core layer serves both directions. Reverse analysis outputs the
same LanguageDefinition format that forward generation consumes.

---

.. _adr-013:

ADR-013: [PHONO] Orthography Decoupled from Core
------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

IPA-to-glyph mapping and script conversion are presentation concerns,
not phonological logic.

Decision
~~~~~~~~

Orthography (mapper, transliteration, export) is a separate layer from
core logic. Core never imports orthography.

Rationale
~~~~~~~~~

Separation of concerns. Core modules are pure logic with no I/O or
presentation dependencies. Orthography can be swapped or extended
independently.

---

.. _adr-014:

ADR-014: [PHONO] IPA Segmenter Lives in Core
--------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

IPA segmentation (splitting multi-character phonemes like ``tʃ``,
``ŋ̊``) is needed by both inventory loading (core) and transliteration
(orthography).

Decision
~~~~~~~~

The IPA segmenter function lives in ``core/phonology.py``, not in the
orthography layer.

Rationale
~~~~~~~~~

Both layers share the same segmentation logic. Placing it in core
maintains the one-way dependency rule (orthography imports from core,
never vice versa).

---

.. _adr-015:

ADR-015: [SUITE] Pedagogy is a UI-Layer Concern
-----------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Suite-wide
:Deciders: Danweel

Context
~~~~~~~

Explanations of sonority, constraints, etc. should appear when users
encounter them, not as separate reference lookups only.

Decision
~~~~~~~~

Pedagogical content (definitions, tooltips, warnings, explanations) is
rendered by the UI layer, not embedded in core logic.

Rationale
~~~~~~~~~

Core returns machine-readable results (violations, scores). UI
translates those into human-readable explanations. This keeps core
lightweight and allows different UIs (CLI, GUI, API) to present
information appropriately for their context.

---

.. _adr-016:

ADR-016: [DOCS-WIDE] Use Cases Link to API via Sphinx Roles
-----------------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel, based on industry standards provided by Lumo

Context
~~~~~~~

Use cases reference classes and functions. Duplicating signatures risks
drift between docs and code.

Decision
~~~~~~~~

Use Sphinx cross-reference roles (``:class:``, ``:func:``, ``:meth:``)
in use cases. Never duplicate API signatures in prose.

Rationale
~~~~~~~~~

If the API changes, Sphinx emits build warnings for broken references —
the docs pipeline catches drift automatically. Zero duplication means
zero maintenance burden for keeping signatures in sync.

---

.. _adr-017:

ADR-017: [DOCS-WIDE] Combined Steps in Use Cases
------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

Cockburn allows both "user action only" and "user action + system
response" step styles :cite:p:`cockburn2001`.

Decision
~~~~~~~~

Use combined steps (User Action → System Response) for User Goal use
cases. Use user-action-only for Summary use cases.

Rationale
~~~~~~~~~

User Goals are precise about system behavior — readers need to know
exactly what the system does. Summaries stay high-level and defer
detail to the subfunctions they call.

---

.. _adr-018:

ADR-018: [DOCS-WIDE] Hard-Coded Extension Labels
------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

Extension labels (e.g., "3a:", "3b:") reference step numbers, but
Sphinx cannot auto-track step numbers.

Decision
~~~~~~~~

Extension labels are hard-coded (e.g., "**3a:** Invalid parameters").
If steps are renumbered, extensions must be manually updated.

Rationale
~~~~~~~~~

Full control over label format. No dependency on Sphinx numbering
automation, which doesn't exist for this use case.

Consequences
~~~~~~~~~~~~

Slight maintenance burden. If use case steps are renumbered, extension
labels must be checked manually. This is acceptable given the low
frequency of renumbering.

---

.. _adr-019:

ADR-019: [DOCS-WIDE] Primary Actor Documented Once
--------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

The primary actor (Conlang Author) appears in every use case. Repeating
the description wastes space.

Decision
~~~~~~~~

The actor is documented once in the use case index (``index.rst``).
Individual use cases reference it without repeating the full description.

---

.. _adr-020:

ADR-020: [SUITE] Use Case Numbering Convention
----------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Suite-wide (documentation)
:Deciders: Danweel

Context
~~~~~~~

Use cases span multiple goal levels (User Goals, Subfunctions, Summaries).

Decision
~~~~~~~~

Two-digit numbering for User Goals and Summaries (:ref:`uc01`, :ref:`uc08`).
Three-digit numbering for Subfunctions (:ref:`uc005`, :ref:`uc013`).

Rationale
~~~~~~~~~

Numbering visually distinguishes goal levels. Stable references across
documentation. Two digits for top-level, three for sub-level mirrors
the hierarchy.

---

.. _adr-021:

ADR-021: [SUITE] Reference Notes vs. Research Notes
---------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Suite-wide (documentation)
:Deciders: Danweel, Danweel

Context
~~~~~~~

User-facing concept explanations and developer-facing open questions
serve different audiences.

Decision
~~~~~~~~

Separate documentation sections: user-facing reference (SSP, syllable
structure, constraints, error types) is distinct from developer-facing
research questions, bibliography, and design methodology notes.

Consequences
~~~~~~~~~~~~

Users find concepts in one place. Contributors find open questions in
another. No audience confusion.

.. note::

   This decision has been **superseded in part** by the documentation
   reorganization. User-facing concept explanations now live in the
   :ref:`glossary` and referenced by individual use case pages.
   Developer-facing questions live in :ref:`questions`. The principle
   (separation by audience) still holds; the locations have been refined.

---

.. _adr-022:

ADR-022: [PHONO] Extensible Constraint System
---------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Mostly Lumo

Context
~~~~~~~

Nine constraint types are defined for MVP, but more will be needed
post-MVP (vowel harmony, tone, stress, etc.).

Decision
~~~~~~~~

Constraints use a common interface. New constraint types slot into the
validation pipeline without refactoring existing constraints or the
generator.

Rationale
~~~~~~~~~

Future-proofs the pipeline. Post-MVP constraint types (allophonic rules,
cross-syllable harmony, stress) can be added incrementally.

The common-interface design implements Protected Variations
through polymorphism :cite:p:`larman2004` — new constraint types
plug in without modifying existing types or their callers.

See :ref:`constraints` for the full catalog and :ref:`architecture` for the interface design.

---

.. _adr-023:

ADR-023: [PHONO] No Implementation Before Use Cases Complete
------------------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

Premature coding risks building against assumed interfaces that change
when the full design is finalized.

Decision
~~~~~~~~

No code implementation until ALL use cases for the milestone are
drafted. The use cases ARE the specification.

Rationale
~~~~~~~~~

Design completeness before implementation. Reduces rework. Forces
explicit API decisions before coding.
Use cases ARE the contract; Cockburn treats them as the behavior
specification the design traces back to :cite:p:`cockburn2001`.

Consequences
~~~~~~~~~~~~

Slower start, but each implementation phase benefits from a complete
specification. Debugging is easier because the expected behavior is
fully documented.

---

.. _adr-024:

ADR-024: [PHONO] Seeded PRNG for Reproducibility
------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo

Context
~~~~~~~

Generated words should be reproducible for testing, sharing, and
debugging.

Decision
~~~~~~~~

WordGenerator uses Python's ``random.Random`` with an optional integer
seed. Same definition + same seed + same parameters = same output,
always.

Rationale
~~~~~~~~~

Essential for testing (assert exact output). Enables "language
snapshots" — users share a seed and definition file to reproduce
identical generated words.
Python's ``random.Random`` implements the Mersenne Twister
generator :cite:p:`matsumotonishimura1998`, whose determinism
guarantees reproducible snapshots.

---

.. _adr-025:

ADR-025: [PHONO] Three-Level Exception Hierarchy
------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo

Context
~~~~~~~

Generation can fail for different reasons with different remediation
paths.

Decision
~~~~~~~~

Three custom exceptions inheriting from a common base
``LatticeLangError``:

- ``ParameterError`` — bad input (e.g., invalid phoneme reference)
- ``GenerationError`` — structural impossibility (e.g., no valid
  syllables can be generated from the given inventory + constraints)
- ``NoValidTemplateError`` — all templates rejected by constraints

Rationale
~~~~~~~~~

Callers can catch at the granularity they need. Error messages guide
users to the right fix (adjust parameters, add phonemes, relax
constraints).

---

.. _adr-026:

ADR-026: [SUITE] Separating Use Cases from Interface Details
------------------------------------------------------------

:Date: 2026-08-24
:Status: Accepted
:Scope: Suite-wide (documentation)
:Deciders: Danweel

Context
~~~~~~~

Cockburn warns that use cases become brittle when they contain
low-level interface details — field names, widget specifications,
layout descriptions :cite:p:`cockburn2001`. These details change
frequently during development, and embedding them in use cases means
the use cases must be re-edited every time a field name changes.

However, requirements that *do* decide interface details still need to
be recorded somewhere. Cockburn recommends separating them into
companion documents:

- **Information nicknames** — short names for data elements used across
  use cases
- **Field lists** — names, types, and brief descriptions of fields
- **Field details** — validation rules, allowed values, format
  constraints
- **Field checks** — assertions that must hold true for the data to be
  valid

Constantine & Lockwood's *Software for Use* provides a deeper treatment
of these separations :cite:p:`constantine1999`.

Decision
~~~~~~~~

LatticeLang adopts the following document hierarchy:

1. **Use cases** (``docs/source/use_cases/*.rst``)
   - Describe *behavior and goals*, not interface details
   - Reference data contracts by information nickname
   - May note that a field-level decision is pending, with
   a cross-reference to the relevant data contract document

2. **Data contract documents** (``docs/source/data_contracts/*.rst``)
   - Define the field lists, field details, and field checks for eachmajor data structure
   - Are the authoritative source for serialization formats, validation rules, and data schema
   - Link back to use cases that depend on them - Include schema versioning where applicable

3. **Research questions** (``docs/source/research/questions.rst``)
   - Capture open questions, decisions under consideration
   - Record *why* a decision is being considered, not just *what*

4. **Decision log** (this file)
   - Records settled decisions with full rationale

Consequences
~~~~~~~~~~~~

- Use cases remain stable even when field names or JSON structure
  changes — only the data contract document needs updating.
- Developers have a single authoritative source for data structures,
  reducing ambiguity during implementation.
- The separation creates additional documents to maintain, but this
  is outweighed by reduced churn in the use cases.
- New data structures require a new data contract document before
  implementation begins — this is intentional and acts as a
  lightweight design gate.

---

.. _adr-027:

ADR-027: [PHONO] Rule-Based Constraints for MVP
-----------------------------------------------

:Date: 2026-08-29
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Mostly Lumo

Context
~~~~~~~

We need a constraint evaluation system for the MVP. Options include
rule-based (Generative Phonology), ranked violable (Optimality Theory),
or probabilistic (Usage-Based).

Generative Phonology's ordered-rule tradition descends from
Chomsky & Halle :cite:p:`chomskyhalle1968`; the ranked-violable
alternative is Optimality Theory :cite:p:`prince2004`, with the
standard pedagogical treatment in :cite:p:`kager1999`.

Decision
~~~~~~~~

Adopt rule-based, declarative constraints (Generative Phonology style).
Constraints are hard filters — a candidate either passes or fails.

Rationale
~~~~~~~~~

- Simpler to implement and debug
- More intuitive for non-linguists
- Faster generation loops (no candidate comparison needed)
- Clearer pedagogical value

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

- OT mode — deferred to Phase Delta (see :ref:`theoretical_framework`)
- Probabilistic constraints — deferred to Phase Delta

Consequences
~~~~~~~~~~~~

All nine MVP constraint types operate as boolean filters. The
architecture supports upgrading to OT mode in the future via the
``mode`` field on the ``Constraint`` data contract.

See :ref:`theoretical_framework` for the full theoretical comparison.

---

.. _adr-028:

ADR-028: [PHONO] Tie-Bar Policy for Affricates
----------------------------------------------

:Date: 2026-08-29
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

Affricates can be represented with or without a tie bar (e.g., /t͡s/
vs /ts/). Need a consistent policy.

Decision
~~~~~~~~

- **Display:** Always use tie bar for affricates (t͡s, t͡ʃ, etc.)
- **Input:** Accept both with and without tie bar
- **Internal:** Normalize to tie-bar form
- **Pedagogy:** Tooltip explaining the difference

Rationale
~~~~~~~~~

The tie bar is the IPA-standard notation indicating that two symbols
represent a single phoneme. Accepting non-tie-bar input accommodates
users who can't easily type the tie bar character. Normalizing
internally ensures consistency in data and output.

Tie bars indicate unit phonemes in the IPA's official
conventions :cite:p:`ipa1999`.

---

.. _adr-029:

ADR-029: [PHONO] PHOIBLE CC-BY 4.0 Compatible with MIT/GPL
----------------------------------------------------------

:Date: 2026-08-24
:Status: Accepted
:Scope: Suite-wide
:Deciders: Danweel, Lumo

Context
~~~~~~~

The project uses GPL-3.0-or-later for code and OFL for fonts. If we
incorporate IPA data from PHOIBLE, we need to verify license
compatibility.

Decision
~~~~~~~~

PHOIBLE 2.0 data (licensed CC-BY 4.0) is compatible with our project
license. Attribution is required and included in the IPA reference JSON
metadata and the bibliography.

Rationale
~~~~~~~~~

CC-BY 4.0 permits reuse with attribution. The IPA symbol set itself is
factual (not copyrightable), but the PHOIBLE compilation retains
CC-BY 4.0. Attribution is provided in:

- ``ipa_reference.json`` metadata fields.
- :ref:`bibliography`

See :ref:`q20-license-compatibility` for the full research record.
:ref:`bibliography`, citing PHOIBLE 2.0 :cite:p:`moran2019`

---

.. _adr-030:

ADR-030: [DOCS-WIDE] CSV Tables Over Grid Tables
------------------------------------------------

:Date: 2026-08-30
:Status: Accepted
:Scope: Docs-wide
:Deciders: Danweel

Context
~~~~~~~

RST grid tables (``+---+`` style) require exact character counting for
column alignment. This is tedious for humans and unreliable for AI
assistants.

Decision
~~~~~~~~

Use ``.. csv-table::`` or ``.. list-table::`` directives exclusively.
Never use RST grid tables.

Rationale
~~~~~~~~~

CSV and list tables require no alignment — just quoted,
comma-separated values. Sphinx handles all rendering. Same output,
much easier to write and maintain.

Consequences
~~~~~~~~~~~~

All existing grid tables in the documentation should be converted
to ``csv-table`` or ``list-table`` format.
See :ref:`documentation_standards` for the formatting rules.

.. _adr-031:

ADR-031: [SUITE] PEP 621 Extras Only — No Poetry Groups
-------------------------------------------------------

:Date: 2026-08-31
:Status: Accepted
:Scope: Suite-wide (build configuration)
:Deciders: Lumo

Context
~~~~~~~

The project originally declared dependencies in three places:

1. ``[project.optional-dependencies]`` (PEP 621 extras) — for RTD
2. ``[tool.poetry.group.docs.dependencies]`` (Poetry groups) — for
   local development
3. ``[tool.poetry.group.dev.dependencies]`` (Poetry groups) — for
   local development

This triple declaration caused recurring bugs:

- Version specifiers in PEP 621 arrays must use PEP 440 syntax
  (``">=2.5,<3.0"``), but entries were sometimes written with
  Poetry's caret syntax (``=^0.3.2``), which is invalid in array
  format and causes ``poetry lock`` to fail with cryptic errors like
  "Unexpected character at column N"
- Maintaining the same dependency list in two formats led to drift
  (packages present in one section but missing from another)
- Duplicate entries appeared when copying between sections

Decision
~~~~~~~~

Use **PEP 621 ``[project.optional-dependencies]`` exclusively**.
Remove all ``[tool.poetry.group.*]`` sections.

Poetry reads PEP 621 extras natively via ``poetry install --extras
dev``. RTD reads them via ``pip install .[docs]``. One source of
truth serves both consumers.

The ``dev`` extra self-references ``docs`` via
``"latticelang[docs]"``, so installing dev dependencies automatically
includes all documentation dependencies.

Rationale
~~~~~~~~~

PEP 621 is the Python packaging standard for optional dependencies.
It is understood by pip, Poetry, Hatch, Flit, and all PEP 517 build
backends. Poetry groups, by contrast, are a Poetry-specific feature
that is invisible to pip and other tools.

When Poetry groups ARE appropriate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Poetry groups are useful when you need dependency groups that are
**not installable extras** — for example, CI-only tools that
shouldn't be exposed as public install options. But ``docs`` and
``dev`` are exactly the kind of extras that downstream consumers
(RTD, contributors, CI) need to install, so they belong in PEP 621.

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

1. **Keep both formats** (original approach) — rejected due to
   maintenance burden and recurring syntax errors from format
   confusion.
2. **Poetry groups only** — rejected because RTD uses pip, which
   cannot read Poetry groups (confirmed in :ref:`ADR-003`).
3. **Single flat dependency list** — rejected because docs
   dependencies shouldn't be required for runtime installation.

Consequences
~~~~~~~~~~~~

- One source of truth for all optional dependencies
- No risk of format confusion (caret vs PEP 440 syntax)
- RTD configuration uses ``pip install .[docs]`` in
   ``.readthedocs.yaml``
- Local development uses ``poetry install --extras dev``
- Adding a new dependency requires editing only one location

Supersedes
~~~~~~~~~~

Refines :ref:`ADR-003` (Danweel) by clarifying that PEP 621 extras replace Poetry
groups entirely, not just supplement them.

Additional note: `esbonio` retired 2026-09-10 (Lumo) — sandboxed interpreter
made its diagnostics unreliable; live preview replaced by
make docs-live (sphinx-autobuild).

.. _adr-032:

ADR-032: [PHONO] Derive Phoneme Category from Features
------------------------------------------------------

:Date: 2026-08-31
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

:ref:`uc01` originally followed the Language Construction Kit workflow:
the user first picks consonants, then vowels, then arranges them.
This made **phoneme category** (consonant/vowel/diphthong) a
manual user decision preceding feature assignment.

Problems with the manual approach:

- Ambiguous residues have no clean home (glides /j/, /w/;
  syllabic consonants /n̩/)
- One more required step for the user
- Category declared first can conflict with features entered
  later (a "vowel" assigned manner=stop)

The phonological literature classifies sounds by **major class
features** — [±syllabic], [±consonantal], [±sonorant]
:cite:p:`chomskyhalle1968` — which partition all speech sounds.
Under this system, category is *derivable*, not declared.

Decision
~~~~~~~~

1. Phoneme category is a **derived field**, computed from the
   phoneme's features, per the major-class mapping.

2. Manual override exists as an escape hatch for:
   - Custom symbols absent from the IPA reference table
   - Edge residues (syllabic consonants, contour tones post-MVP)
   - Deliberate analyses that diverge from the default

3. The category set gains a **glide** value rather than
   shoehorning /j/, /w/ into consonant or vowel.

4. Diphthongs remain stored as single phonemes with a
   ``components`` field — a documented deviation from standard
   sequence analyses, kept for one-slot-per-segment syllable
   template mechanics (see :ref:`adr-028` for the related
   tie-bar policy).

5. The LCK-derived presentation order is retained in the UI
   wizard (inventory before templates) as *pedagogy*, not as
   data-flow dependency.

Rationale
~~~~~~~~~

Fewer steps, less ambiguity, literature-grounded. Deriving
category from features matches how linguists classify sounds
and removes a decision the user is often poorly placed to make.

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

1. **LCK-style manual category first** (original) — rejected:
   creates ambiguity for glides and syllabic consonants, adds
   a step, invites feature/category conflicts.
2. **Fully implicit category (no override)** — rejected:
   custom symbols and non-standard analyses need an escape
   hatch; conlangers sometimes deliberately violate the default
   mappings.
3. **Rosenfelder's framework retained as data model** — rejected:
   valuable as teaching sequence, misleading as data structure.

:cite:p:`rosenfelder2010`

Consequences
~~~~~~~~~~~~

- :ref:`uc01` step 2 reworded: "system derives category → user
  confirms or overrides"
- ``Phoneme`` data contract: category becomes computed field
  (or stored-but-validated) — decision recorded in the contract
- Category enum: ``consonant | vowel | glide | diphthong`` +
  post-MVP ``tone``
- Constraints that switch on category (slot restrictions) are
  unaffected — they read the derived value the same way
- :ref:`q6-feature-system-adoption` resolution feeds directly
  into this ADR; revisit if :ref:`q6-feature-system-adoption`
  lands on a different feature system
- Documented in :ref:`theoretical_framework`
  under "Novel Components"

Supersedes
~~~~~~~~~~

Partially supersedes the :ref:`uc01` step-2 workflow as originally
drafted (manual category selection), which followed the LCK.

.. _adr-033:

ADR-033: [PHONO] Adopt PHOIBLE-Aligned Feature System with Controlled Vocabulary
--------------------------------------------------------------------------------

:Date: 2026-08-31
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo proposed, Danweel accepted

Context
~~~~~~~

:ref:`q6-feature-system-adoption` asked which feature system the
``Phoneme`` data contract should adopt; :ref:`q24-feature-representation`
asked whether features should be enums, strings, or a hybrid. The two
questions are coupled: the representation choice follows from the vocabulary choice.

Research (:ref:`q38-ipa-reference-sourcing`) established that PHOIBLE 2.0 distributes a
distinctive feature file for all 3,183 of its segment types
(``phoible-segments-features.tsv``), built on a system loosely
based on :cite:p:`hayes2009` Hayes (2009) with laryngeal additions from
:cite:p:`moisikesling2011`, designed so that any two distinct symbols necessarily
have distinct feature sets. It is CC-BY 4.0 (cleared in :ref:`ADR-029`).

Adopting this system unifies the feature ontology and the IPA
reference dataset into one artifact (:ref:`q38-ipa-reference-sourcing` 's
hybrid sourcing) and makes :ref:`ADR-032`'s category derivation, sonority
rank proposal, and OCP/harmony feature matching all read from a Single
source of truth.

Built on a system loosely based on Hayes (2009) :cite:p:`hayes2009`

Decision
~~~~~~~~

1. Adopt PHOIBLE 2.0's feature system, **pinned to the 2.0
   release**, as the built-in feature vocabulary. PHOIBLE notes
   the system may evolve in future releases; we freeze at 2.0
   and upgrade deliberately, not automatically.

2. Features are stored as **controlled-vocabulary strings** in a
   flat dictionary (e.g., ``{"place": "coronal", "manner":
   "stop", "voice": "-"}``). The vocabulary is defined by a
   pinned feature-list file derived alongside the IPA reference;
   user-defined features may be added per project and are
   validated only for identifier syntax, not semantics.

3. A **flat feature set** is adopted for MVP rather than a full
   Clements feature-geometry tree. Rationale: PHOIBLE represents
   clicks with combined place features that a flat dict stores
   trivially, while a strict place-node tree does not. The
   geometry tree remains a post-MVP refinement of
   :ref:`theoretical_framework`; the OCP constraint works on
   shared features under either model.

4. Edge-case rules for category derivation (completing ADR-032):

   - **Syllabic consonants** (/n̩/): the [+syllabic] feature
     takes precedence over [+consonantal]; the phoneme is
     treated vowel-like for slot placement.
   - **Clicks**: stored with PHOIBLE's dual-place feature
     combination; category derives as consonant.
   - **Contour tones**: post-MVP category, deferred.
   - **Custom symbols**: manual feature entry using the same
     string-based vocabulary plus user additions.

Rationale
~~~~~~~~~

- **Artifact unification:** feature vocabulary = IPA reference
  data = one curated file, not two drifting sources.
- **Pedagogy:** Hayes's system is a textbook framework, teachable
  in tooltips, unlike raw SPE notation.
- **Effort:** deriving 3,183 feature-populated segments from an
  existing TSV replaces weeks of hand data entry.
- **Compatibility:** CC-BY 4.0, already cleared (:ref:`ADR-029`).

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

1. **SPE features** (classic): well-documented but notation
   predates feature-geometry refinements; no ready-made
   per-segment mapping file; would still require manual
   population. Rejected on effort and pedagogy.
2. **Full Feature Geometry tree**: theoretically richest, best
   fit for autosegmental spreading; rejected for MVP due to data
   model complexity and the clicks edge case. Remains post-MVP.
3. **panphon**: practical and complete, but adds a runtime
   dependency (violates :ref:`ADR-010` for the core) and its vocabulary
   would duplicate PHOIBLE's role. OptionalDependency status
   remains open under :ref:`q26-panphon-integration` but is no longer needed for the MVP.
4. **Free-form dicts** (original sketch): maximum flexibility,
   but no validation and fragile constraint rules. Rejected.

Consequences
~~~~~~~~~~~~

- ``dc_phoneme`` finalizes as: symbol (normalized string),
  features (flat string dict, controlled vocabulary), category
  (derived per :ref:`ADR-032` + :ref:`ADR-033` edge rules), sonority_rank
  (proposed from features), frequency (PHOIBLE-derived).
- The pinned feature list becomes a second derived artifact of
  the :ref:`q38-ipa-reference-sourcing` build script, versioned alongside
  ``ipa_reference.json``.
- :ref:`q26-panphon-integration` downgraded from MVP-blocking to post-MVP convenience
  (panphon could still power optional *phonetic* validation
  later, but is not needed for feature vocabulary).
- Schema versioning must record the PHOIBLE 2.0 pin (feeds :ref:`q5-project-file-versioning`'s
  persistence sub-question).
- Updating PHOIBLE requires a deliberate ADR superseding this
  one, plus a re-run of the derivation pipeline and a diff review.

Relations
~~~~~~~~~

Resolves: :ref:`q6-feature-system-adoption`, :ref:`q24-feature-representation` (see resolved entries in ``questions.rst``).
Feeds: :ref:`q38-ipa-reference-sourcing` (hybrid sourcing), :ref:`q36-rarity-tier-finalization` (tier thresholds computed from
the same aggregation), :ref:`UC01` (implementation-ready).

.. _adr-034:

ADR-034: [PHONO] Slot Eligibility — Category Matching with Syllabic Admission
-----------------------------------------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo proposed, Danweel accepted

Context
~~~~~~~

:ref:`UC-02_define_syllable_templates`. :ref:`ADR-032` introduced
``glide`` as a phoneme category, creating three ambiguities in
the original :ref:`uc02` draft: (1) glides were absent from allowed
categories, making /j/-in-onset templates impossible; (2)
extension 3b (nucleus allowing only consonants) contradicted
:ref:`ADR-033`'s vowel-like slot treatment of syllabic consonants;
(3) diphthong nucleus eligibility was implicit. Three candidate
models were considered: pure category matching, category
matching plus a syllabic-admission rule, and feature-based
slots.

Decision
~~~~~~~~

1. **Eligibility rule.** A phoneme is eligible for a slot when
   its category is in the slot's ``allowed_categories``, with
   one automatic rule: any phoneme with ``syllabic=+`` is
   eligible for *nucleus* slots regardless of category.

2. **Glide semantics.** ``glide`` joins the allowed-category
   vocabulary (``consonant | vowel | glide | diphthong``; tone
   post-MVP). Glides receive no automatic admission — they are
   explicit opt-in per slot, reflecting how natural languages
   restrict glides to onset/margin positions.

3. **Diphthongs** occupy exactly one nucleus slot when admitted
   (diphthong-as-unit-phoneme, per :ref:`adr-028`, :ref:`adr-032`'s documented
   deviation). Listing them in ``allowed_categories`` is
   explicit, never assumed.

4. **TBU reuse (post-MVP provision).** When tone is implemented,
   tone-bearing units are defined as exactly the
   nucleus-eligibility predicate from rule 1 — one definition,
   two consumers.

Rationale
~~~~~~~~~

Design principle (see :ref:`ADR-035`): the tool defaults to natural
language behavior so users discover constraints through
plausible output rather than upfront configuration. The
``syllabic=+`` rule is not a hidden convenience — it *is* the
linguistic definition of a nucleus; omitting it would make the
tool less faithful, not simpler. Forbidding is cheaper than
remembering for non-linguist users. Implementation delta versus
pure category matching is one conditional (near-zero cost).

Glides as explicit opt-in likewise tracks the science: glides
pattern with consonants distributionally but contrast with them
featurally; per-slot permission mirrors the cross-linguistic
fact that languages treat glide occurrence as an active
restriction.

The ``syllabic=+`` rule operationalizes the literature's
minimal-sonority findings for nucleus position
:cite:p:`zec1995`; glide margin-restriction parallels the
distributional facts summarized in :cite:p:`hayes2009`.

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

1. **Pure category matching** — maximally explicit and
   predictable, but hides the nucleus definition, forces users to
   remember the syllabic-consonant trick, and fails silently
   (zero-word generation) when forgotten. Rejected on the
   naturalistic-defaults principle.
2. **Feature-based slots** — most expressive, but heavyweight
   for MVP and hostile to beginners. Revisit post-MVP if
   category abstraction proves limiting.
3. **Auto-admit glides to onsets** (symmetric courtesy rule) —
   rejected: unlike syllabicity, glide-in-onset is *not* a
   definitional necessity, and unrequested glides would generate
   foreign-feeling words for users who never considered them.

Consequences
~~~~~~~~~~~~

- :ref:`uc02` extension 3b reframed: nucleus-with-consonants is valid
  only via the ``syllabic=+`` route; the warning educates.
- New extension 2b (glide presence note) added to :ref:`uc02`.
- ``dc_syllable_template`` must codify the eligibility rule as
  a normative clause when audited.
- Future pitch/stress work inherits the TBU predicate
  (rule 4); stress additionally requires metrical structure
  (out of scope, see theoretical framework).

Relations
~~~~~~~~~

Extends: :ref:`ADR-032` (categories), ADR-033 :ref:`ADR-033` (edge rules).
Resolves: :ref:`uc02` audit issues 1–3. Governs: :ref:`uc02`, :ref:`uc04`, :ref:`uc013`.

.. _adr-035:

ADR-035: [SUITE] Naturalistic Defaults — Design Principle
---------------------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Suite-wide
:Deciders: Danweel

Context
~~~~~~~

LatticeLang serves conlangers who often lack formal linguistic
training. They know the interesting properties they want a
language to have but cannot enumerate the full possibility
space those properties imply.

Decision
~~~~~~~~

When a design choice pits explicit user configuration against
natural language behavior, **default to what natural languages
do** (as established by the linguistic literature), and make
non-natural behavior an explicit, discoverable override.

Specifically:

1. Unrequested-but-naturalistic behavior is acceptable and
   desirable; it surfaces as explorable output, not silent
   failure.
2. Forbidding an undesired behavior must always be simpler than
   preemptively enabling a desired one.
3. Experiments that violate typology (the documented range of
   natural language variation) are the user's prerogative — but
   the tool neither assists them nor penalizes them; it simply
   does not default to them. Typological ranges are established empirically in
   :cite:p:`maddieson1984`; sonority-related defaults trace to
   :cite:p:`clements1990`.
4. When corpus data exists (reverse pipeline), it seeds the
   defaults; the user fills gaps the corpus leaves (:ref:`q41-corpus-inference`).

Rationale
~~~~~~~~~

Non-linguists learn the possibility space through surprising-
but-plausible output — each surprise is a teachable moment.
Silent failures from forgotten configuration teach nothing.
Staying within naturalistic bounds also keeps pedagogical
content (glossary, tooltips) truthful: every default can be
annotated with "languages tend to do X because..."

Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~

1. **Configurability-first** (every behavior an explicit
   option): maximum predictability, worst beginner experience;
   rejected as hostile to the target audience.
2. **Free generation, no typology awareness**: maximally
   creative, but the output teaches nothing and the tool
   cannot explain itself; rejected — naturalism is the
   product's spine (per theoretical framework).

Consequences
~~~~~~~~~~~~

- Adjudicates future ties the way :ref:`ADR-034` did (its first application).
- Every naturalistic default requires a documented override
  path; UX debt tracks "hard to forbid" cases as bugs.
- Documentation tone shifts from "configure correctly" toward
  "experiment, then refine."

Relations
~~~~~~~~~

First applied by: :ref:`ADR-034`. Grounds: :ref:`q4-ambiguity-confidence` (best-guess defaults),
:ref:`q41-corpus-inference` (corpus seeding). Constrains: all future module design.

.. _adr-036:

ADR-036: [PHONO] Dedicated Inventory Data Contract
--------------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo

Context
~~~~~~~

The ``dc_phoneme`` audit flagged that nothing governs the
inventory as a whole (versus individual phonemes): minimum
nucleus capacity, composition sanity, suspicious near-identical
entries. The home for those rules was open: a section of
``dc_language_definition`` or a dedicated contract.

Decision
~~~~~~~~

Create ``dc_inventory.rst`` as a dedicated data contract for
inventory-level validation. ``LanguageDefinition`` remains the
serialization envelope (ADR on schema versioning) and does not
absorb linguistic validity rules.

Initial rule catalog (MVP):

- At least one nucleus-capable phoneme (``syllabic=+`` or
  category ``vowel``/``diphthong``) — hard error; blocks
  generation (:ref:`uc04` precondition)
- Zero consonants, or zero vowels while templates require
  them — warning
- Two phonemes with fully identical feature sets — warning
  ("likely allophones or an entry mistake"; ties to :ref:`q40-near-miss-similarity`'s
  NFD detector for the near-miss variant)
- Feature sets differing in exactly one feature — informational
  note only (legitimate minimal pairs are normal; the note
  exists for the *entry mistake* case, paired with symbol
  similarity)
- All checks advisory except the nucleus-capacity hard error,
  per :ref:`ADR-035` (never block on heuristics, always block on
  structural impossibility)

Rationale
~~~~~~~~~

The rules are about *sets* of phonemes and are consumed by
three different callers (:ref:`uc04` generation preconditions,
:ref:`uc01`/:ref:`uc009` import review, :ref:`uc08` preview diagnostics). Embedding
them in the serialization envelope couples file format to
linguistic policy; a sibling contract keeps the same
separation :ref:`uc005`/:ref:`uc013` already established.

Consequences
~~~~~~~~~~~~

- New contract ``dc_inventory.rst`` (add to data_contracts
  toctree); ``dc_phoneme``'s inventory-validation TODO is
  replaced by a cross-reference to it.
- Reverse-pipeline import (:ref:`uc009`) gets a natural landing zone
  for its plausibility report (:ref:`q41-corpus-inference` layer 4, post-MVP).

Relations
~~~~~~~~~

Implements: the inventory-validation flags from the
``dc_phoneme`` audit. Governs: :ref:`uc01`, :ref:`uc04`, :ref:`uc009`.

.. _adr-037:

ADR-037: [PHONO] Constraint Catalog — Nine MVP Types, Ten Reserved
------------------------------------------------------------------

:Date: 2026-09-09
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel

Context
~~~~~~~

The constraint catalog previously lived only in the living design
document (``dev/design/constraints.rst``), where it drifted: the
intro claimed all nine MVP types operated within a syllable,
contradicting the :ref:`q35-prohibited-clusters-domain` ruling
(``no_geminate_obstruents`` is word-domain; geminates arise
across the coda-onset junction). The catalog needed a frozen,
append-only record of its membership so future edits to the
living document cannot silently add, remove, or re-scope a type.

Decision
~~~~~~~~

The MVP constraint catalog is fixed at nine types:

1. ``sonority_sequencing`` — SSP within onset and coda :cite:p:`clements1990`
2. ``allow_s_appendix`` — /s/+C onset clusters exempt from SSP :cite:p:`hayes2009`
3. ``no_geminate_obstruents`` — domain: **word** (fixed, :ref:`q35-prohibited-clusters-domain`)
4. ``max_onset_length`` — structural cap
5. ``max_coda_length`` — structural cap
6. ``position_restrictions`` — forbidden phonemes per position,
   including word-edge keys (``word_initial``/``word_final``,
   enabled by :ref:`q37-word-context-parameter`'s empty-coda semantics)
7. ``ocp`` — no adjacent segments sharing a designated feature;
   parameterized by feature (e.g., ``place``, ``voice``) :cite:p:`goldsmith1976`
8. ``harmony`` — feature agreement within the syllable (scope:
   Q34); parameterization per :ref:`q42-harmony-parameterization`, :cite:p:`goldsmith1990`
9. ``prohibited_clusters`` — explicit banned sequences; domain
   **defaults to syllable**, configurable per :ref:`q35-prohibited-clusters-domain`

Ten post-MVP types are RESERVED (names must not be displaced):
``cross_syllable_harmony``, ``stress_assignment``,
``tone_assignment``, ``alignment``, ``faithfulness (MAX-IO,
DEP-IO)``, ``morpheme_structure``, ``gradient_probabilistic``,
``dialectal_constraints``, ``allophonic_rules``, ``foot_structure``.

Adding or removing any MVP type requires superseding this ADR.

Cross-references for reserved types: ``tone_assignment`` uses TBUs
defined by :ref:`ADR-034` rule 4 (nucleus eligibility predicate) :cite:p:`yip2002`;
``stress_assignment``/``foot_structure`` depend on metrical
structure (see theoretical framework note distinguishing stress
from tone); ``dialectal_constraints``/``allophonic_rules`` map to
Research :ref:`q2-dialect-rules`; ``faithfulness`` presumes
morphological inputs :cite:p:`prince2004`; ``gradient_probabilistic``
defers with OT-style ranking; ``cross_syllable_harmony`` is
harmony's successor scope.

Authoritative living catalog: ``dev/design/constraints.rst``
(maintains status, phase, dependencies). This ADR freezes
membership and domain corrections only.

Relations
~~~~~~~~~

Corrects: domain column of ``dev/design/constraints.rst``
(no_geminate_obstruents within-syllable → word).
References: :ref:`q34-harmony-mvp-scope`, :ref:`q35-prohibited-clusters-domain`, :ref:`q37-word-context-parameter`, :ref:`q42-harmony-parameterization`, :ref:`ADR-034`, :ref:`ADR-035`.
Governs: :ref:`uc03` step 2, ``dc_constraints``.

.. _adr-038:

ADR-038: [PHONO] Default Constraint State — Visible SSP On
----------------------------------------------------------

:Date: 2026-09-09
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel with technicallities proposed by Lumo

Context
~~~~~~~

Applying :ref:`ADR-035` (naturalistic defaults) to :ref:`uc03` required a
ruling on what a brand-new project's constraint list contains
before the user configures anything. Three options were
considered.

Decision
~~~~~~~~

New projects ship with exactly one constraint, **enabled and visible**:

.. code-block:: json

   "constraints": [
     { "type": "sonority_sequencing", "enabled": true }
   ]

Visibility requirements (no silent machinery):

- The default is serialized in the project file (greppable, diffable)
- The Constraint Editor shows it as a normal, toggleable entry —
  indistinguishable from user-added constraints
- On first generation, the system notes SSP rejections as such
  ("rejected by sonority_sequencing (default)") rather than
  letting them appear as inexplicable behavior

Additionally, the Constraint Editor carries an informational
nudge — NOT an active constraint — pointing at the cluster-length
options most natural languages use: "Most languages also limit
cluster lengths — configure in Constraints."

he default encodes the Sonority Sequencing Principle
:cite:p:`clements1990`; speakers demonstrably internalize
sonority-based well-formedness even where surface evidence is
sparse :cite:p:`hayes2011`, making the visible default
pedagogically honest as well as typologically motivated.

Rejected Options
~~~~~~~~~~~~~~~~

1. **Empty default (``[]``)** — correct templates would generate
   typologically bizarre syllables (/tka/ onsets) until the user
   discovers the Constraints feature. This is :ref:`ADR-035`'s
   "remembering" failure mode: the user must preemptively know.
   Generating garbage before guardrails exist teaches the wrong
   lesson and undermines trust in the tool's naturalism claims.
2. **Full naturalistic preset** (SSP + cluster caps +
   no_geminate_obstruents) — more protective but buries decisions
   the user never made under invisible machinery; a user wanting
   /nk/ codas would face mysterious rejections. Surprises must be
   plausible AND attributable; four unseen constraints violate
   attribution.

Future Upgrade Paths
~~~~~~~~~~~~~~~~~~~~

- **Starter presets (post-MVP/Gamma):** a menu offering curated
  naturalistic bundles ("strict CV language", "English-like
  clusters") — opt-in, never default. Restores option 2's
  protection with option 1's consent.
- **Template-aware nudges:** if a template permits 3-consonant
  onsets and no cluster-length constraint exists, surface a
  suggestion in the editor (informational, per the nudge above).
- **Per-language typological profiles:** once romanization
  profiles (:ref:`q33-profile-based-inference`/:ref:`q41-corpus-inference`)
  mature, defaults could seed from profile data rather than
  universals — corpus-derived instead of universal. Deliberately
  out of MVP scope.

Relations
~~~~~~~~~

Applies: :ref:`ADR-035` (first application to constraint defaults).
Implemented by: :ref:`uc03` "Default State" section. Governs: :ref:`uc04`
(preconditions — a new project is generatable immediately).

.. _adr-039:

ADR-039: [PHONO] Constraint Domains and Word Context
----------------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

Three rulings were first recorded in the research questions and are
promoted here verbatim so the append-only decision log carries them:
the harmony constraint's MVP scope (:ref:`q34-harmony-mvp-scope`),
the evaluation domain of cluster and geminate constraints
(:ref:`q35-prohibited-clusters-domain`), and the optional
``word_context`` validation parameter
(:ref:`q37-word-context-parameter`). This ADR is a backfill of
existing rulings, not a new decision.

Decision
~~~~~~~~

1. **Constraints carry an explicit ``domain`` field** (enum:
   ``syllable | word``, default ``syllable``), with per-type
   restrictions on which values are permitted.

2. **Type-specific domain rules:**

   - ``prohibited_clusters`` — default ``domain: "syllable"``.
     Cluster well-formedness is overwhelmingly a syllable-internal
     affair; word-edge combinations are a different phenomenon.
     Users may set ``domain: "word"`` explicitly.
   - ``no_geminate_obstruents`` (and any identical-adjacent-segment
     constraint) — fixed ``domain: "word"``. Geminates arise across
     the coda-onset junction (/ab.ba/); a syllable-domain check
     would miss every actual gemination site.
   - ``harmony`` — within-syllable for MVP. Cross-syllable harmony
     requires the autosegmental tier model :cite:p:`goldsmith1990` and is deferred
     post-MVP as the reserved ``cross_syllable_harmony`` type.

3. **The validation interface accepts an optional
   ``word_context``** carrying only the minimum word-domain
   constraints need: ``preceding_coda`` and ``following_onset``.
   Syllable-domain constraints ignore it entirely.

4. **Four-state results.** When ``word_context`` is omitted (bare
   syllable validation, e.g. live preview), word-domain constraints
   report **SKIPPED, never PASSED** — a skipped check is honest;
   a false pass is silent corruption.

Rationale
~~~~~~~~~

The defaults are the naturalistic ones (:ref:`ADR-035`): languages that
ban clusters police syllables; the geminate constraint cannot do
its job in any smaller domain. The word context stays minimal so
syllable validation remains cheap and self-contained for preview,
while word validation composes from the same primitive.

Consequences
~~~~~~~~~~~~

- ``dc_constraints`` gains the ``domain`` field with per-type
  constraints.
- :ref:`uc013`'s validation result schema gains the four-state
  (passed/failed/skipped/error) outcome.
- Empty ``preceding_coda`` at word start enables word-edge
  ``position_restrictions`` without a separate parameter.
- :ref:`uc04`'s generation loop owns assembling ``word_context``; the
  generator always knows the preceding coda.

Relations
~~~~~~~~~

Resolves: :ref:`q34-harmony-mvp-scope`, :ref:`q35-prohibited-clusters-domain`,
:ref:`q37-word-context-parameter`. Referenced by: :ref:`ADR-037`.
Governs: :ref:`uc03`, :ref::`uc04`, :ref:`uc013`, ``dc_constraints``.

.. _adr-040:

ADR-040: [PHONO] Merge Semantics for Duplicate Symbols
-------------------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

:ref:`uc01` extension 6a offers replace/merge/cancel when a user adds a
phoneme whose normalized symbol already exists; bulk corpus import
(:ref:`uc009`) hits the same collision with no user present. Ruling
promoted from :ref:`q39-merge-semantics` (backfill of an existing
decision).

Superseded in part by :ref:`adr-051` (2026-09-23), which
defines the concrete field-class merge rules this decision
left open.

Decision
~~~~~~~~

**Interactive:** union merge with a single grouped conflict prompt —
agreeing fields merge silently; conflicting fields collect into one
prompt offering keep-all-existing / take-all-new / decide-individually.

**Bulk (UC009):** project-level policy, default
**first-wins + duplicate report**. Configurable:
``first-wins | last-wins | skip-duplicates | report-only``.

**Field participation rules (normative, both modes):**

- ``features``: union per-field; conflicts resolved by the chosen
  policy
- ``sonority_rank``: never merged — **recomputed** from the merged
  feature set (carrying a stale rank through a features-changing
  merge violates :ref:`ADR-032`'s invariant)
- ``frequency``: keep existing, unless existing is the untouched
  default (1.0) and incoming is reference-sourced
- ``components`` (diphthongs): conflicts always prompt
  interactively; in bulk, keep existing and report
- ``custom``: never downgraded — merged phoneme is custom if either
  source was

**Safety net:** pre-merge entry recoverable (undo stack);
merge-preview diff before committing. The dialog teaches:
"Your /t/ had manner=stop; the incoming entry says fricative — this
changes which constraints see it."

Rationale
~~~~~~~~~

First-wins is the best-guess default per :ref:`Q4`'s batch design and
:ref:`ADR-035` (never block, never destroy); the duplicate report doubles
as a data-quality signal for rule inference.

Relations
~~~~~~~~~

Resolves: :ref:`q39-merge-semantics`. Depends on: :ref:`ADR-032`,
:ref:`ADR-035`. Governs: UC01, UC009, ``dc_phoneme``,
``merge_phonemes()``.

.. _adr-041:

ADR-041: [PHONO] Near-Miss Symbol Similarity
--------------------------------------------

:Date: 2026-09-06
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

:ref:`uc01` extension 6b warns when a new symbol "differs only by
diacritic" from an existing one (adding "pʰ" when "p" exists):
"allophone or distinct phoneme?" Ruling promoted from
:ref:`q40-near-miss-similarity` (backfill).

Decision
~~~~~~~~

Layered detection with a strict order of operations:

1. Segment + normalize input (tie-bar, diphthong forms, ADR-028)
   — MUST precede comparison (the tie bar is itself a combining
   character; normalizing first prevents "tʃ" vs "t͡ʃ" surfacing
   as a diacritic variant)
2. Exact-match check → duplicate path (UC01 ext. 6a → ADR-040)
3. **NFD base-stripping detector** —
   ``unicodedata.normalize("NFD", ...)`` decomposition, strip
   combining marks, compare base characters. Runs for ALL symbols
   including custom ones — the general, zero-curation mechanism
4. Reference-table variant groups upgrade the *message* for known
   pairs ("pʰ is aspirated /p/ — in many languages an allophone
   of /p/")

Feature-distance comparison is **explicitly rejected** as a
similarity trigger: /t/ vs /d/ is a legitimate minimal pair, not a
probable mistake. One-off feature sets belong to inventory-level
validation warnings (dc_inventory).

NFD base-stripping follows the Unicode normalization model
(Unicode Standard Annex #15) :cite:p:`uax15`

Rationale
~~~~~~~~~

The prompt fires rarely and only ever *asks* — naturalistic
curiosity, no blocking, no silent reinterpretation (ADR-035).

Relations
~~~~~~~~~

Resolves: :ref:`q40-near-miss-similarity`. Depends on: ADR-028
(normalization precedes detection). Governs: UC01, ``dc_phoneme``.
Feeds: dc_inventory's near-identical-entry check.

.. _adr-042:

ADR-042: [PHONO] Harmony Constraint Parameterization
----------------------------------------------------

:Date: 2026-09-09
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

The MVP ``harmony`` constraint needs a precise parameterization:
what its ``feature`` parameter takes and how participating
phonemes are determined. Ruling promoted from
:ref:`q42-harmony-parameterization` (backfill).

Decision
~~~~~~~~

One harmony constraint instance per agreed feature:

- ``feature``: a single controlled-vocabulary feature name
  (``back``, ``round``, ``atr``, ``nasal`` — the attested harmony
  features; backness and rounding are the prototypes)
- ``targets``: participating categories. A phoneme absent from
  ``targets`` is **neutral** — transparent to the constraint,
  giving the typologically essential neutral-vowel concept via
  exclusion
- Languages with back + round harmony use two instances,
  mirroring AGREE([back]) + AGREE([round]) in the OT literature. :cite:p:`padgett2002`

Rejected: *total agreement* (typologically wrong — real harmony
is feature-class-selective) and *full OT ranking machinery*
(theoretically complete but requires a ranking engine — parked
with the reserved post-MVP types).

The safest immediate key is :cite:p:`prince2004` for the constraint-interaction framework

Rationale
~~~~~~~~~

With :ref:`Q34`'s within-syllable scope, MVP harmony's practical bite is
small (diphthong components, adjacent nucleus segments). The
parameterization is the durable design; the scope widens only with
the reserved ``cross_syllable_harmony`` type.

Consequences
~~~~~~~~~~~~

- ``dc_constraints`` documents the parameterization
- Neutral vowels fall out of ``targets`` exclusion — no separate
  mechanism

Relations
~~~~~~~~~

Resolves: :ref:`q42-harmony-parameterization`. Depends on:
:ref:`ADR-033` (controlled vocabulary), :ref:`ADR-039` (within-syllable scope).
Referenced by: :ref:`ADR-037`. Governs: ``dc_constraints``.

.. _adr-043:

ADR-043: [PHONO] Segmenter Ambiguity — Longest-Match with Override
------------------------------------------------------------------

:Date: 2026-08-23
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

Some segmented sequences are ambiguous: "ts" may represent the
affricate /t͡s/ or the sequence /t/ + /s/. The decision was first
tentatively recorded in :ref:`q1-segmenter-ambiguity`
("[x] Decide on default behavior" checked) and is promoted here so
the decision log carries it. The question is MVP-blocking (UC012
quality depends on it).

Longest-match disambiguation is standard lexer technology —
the "maximal munch" rule :cite:p:`aho2006` — adapted here to
an inventory-relative segment inventory.

Decision
~~~~~~~~

1. **Default: longest-match.** Prefer the affricate when a valid
   affricate phoneme exists in the inventory; fall back to the
   sequence otherwise. Eligibility is inventory-relative — a
   segmenter pass is only "greedy" toward phonemes that exist.
2. **Override: user-configurable preference** in the
   LanguageDefinition, per language.
3. **Ordering with normalization:** input is normalized to tie-bar
   form first (:ref:`ADR-028`), so "ts" typed without a tie bar resolves
   as /t͡s/ — longest-match is the internal-normalization policy
   continued, not a bold new choice.
4. **Batch behaviour:** the segmenter always commits (no blocking,
   no per-token prompts); uncertain resolutions surface through
   confidence reporting (:ref:`q4-ambiguity-confidence`).

Rejected
~~~~~~~~

1. **Context-sensitive rules** ("ts" before vowel = affricate):
   more linguistically precise in some cases, but requires
   conditioned context in the data contract, is harder to teach in
   tooltips, and batch mode still cannot resolve everything.
   Retained as a post-MVP refinement option.
2. **Require explicit tie bar in input:** breaks the reverse
   pipeline entirely — UC009 receives romanized text with no tie
   bars at all.
3. **Preference-configured only, no default:** shifts the decision
   to every user — the "remembering" failure mode ADR-035 prohibits.

Relations
~~~~~~~~~

Resolves: :ref:`q1-segmenter-ambiguity`. Reinforces: ADR-028
(normalization precedes matching). Governs: the segmenter,
UC012, ``dc_orthography_rules``. Batch confidence: :ref:`q4-ambiguity-confidence`.

.. _adr-044:

ADR-044: [PHONO] Seed Stability — Per-Slot Deterministic Streams
----------------------------------------------------------------

:Date: 2026-09-12
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Lumo via goals

Context
~~~~~~~

:ref:`uc04` specifies a seed for reproducibility (:ref:`adr-024`)
:cite:p:`matsumotonishimura1998`?. But a single shared
``random.Random(seed)`` stream consumes draws sequentially:
changing one phoneme's frequency weight shifts every subsequent
draw, so the entire word list re-rolls. That defeats the live
preview (:ref:`ADR-011`) for its central purpose — the user cannot tell
whether a change helped, because everything changed. The core
determinism question was first asked in
:ref:`q7-generation-determinism`; the frequency-weight half of that
question is settled separately as ``dc_phoneme`` weight semantics
and is out of scope here.

Decision
~~~~~~~~

1. **Per-slot deterministic streams.** Each slot derives its
   randomness from its identity rather than drawing from a shared
   sequence: the generator seeds per-slot streams from
   (definition seed, word position, slot position within the
   word). A weight change only changes the *selection* at slots
   where that phoneme was eligible; all other slots keep their
   draws and thus the same phonemes.
2. **Determinism preserved.** Output is still fully
   deterministic — same definition + seed + parameters = same
   output, always. Snapshot sharing is unaffected: it already
   requires sharing the definition file, so reproduction is exact.
3. **Seed edits re-roll everything, by design.** Editing the seed
   changes every stream's derivation, so the entire list changes.
   This is what a seed change *means*; documented explicitly so
   nobody mistakes it for a bug.
4. **Eligible-set changes shift affected slots.** Adding or
   removing a phoneme changes eligibility, so slots the change
   touches may select differently. Arguably correct behavior — the
   change is attributed, not invisible.
5. **Documented fallback position.** If per-slot streams prove
   fragile during implementation, shipping full reseed (:ref:`adr-024`
   as written) is an acceptable fallback: the program still
   accomplishes the author's goal, the reverse pipeline still
   works, and the loss is confined to feedback quality — trial
   and error instead of guided refinement. Learning value is a
   bonus to the baseline advantage, not the crucial aspect.

Rationale
~~~~~~~~~

Per-slot streams are the only option that makes the live preview
actually serve ADR-011's differentiation, and they preserve
:ref:`adr-024`'s determinism guarantee intact. The implementation delta
is one stream derivation per slot. Under the naturalistic-defaults
principle (:ref:`ADR-035`), "the user cannot evaluate their change" is a
silent failure mode of the shared-stream design.

Rejected
~~~~~~~~

1. **Full reseed on any change** (shipped as MVP-only): simplest
   and perfectly deterministic, but turns the live preview into
   trial and error — the fallback, not the default.
2. **Hybrid policy** (reseed for structural changes, stable
   streams for weight tweaks): adds a policy distinction users
   will find hard to predict — an attribution problem.
3. **Defer entirely:** ships the core differentiator in its least
   useful form.

Relations
~~~~~~~~~

Resolves: the determinism core of :ref:`q7-generation-determinism`
(weight semantics resolved via ``dc_phoneme``). Extends: :ref:`uc04`
(deterministic seeded PRNG), :ref:`adr-011` (live preview). Governs:
:ref:`uc04`'s generation loop, the live preview pathway.

.. _adr-045:

ADR-045: [PHONO] Deferral of Constraint-Weight Learning — Evaluation vs. Acquisition Scope
------------------------------------------------------------------------------------------

:Date: 2026-09-15
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

Recent research surfaced a natural question: could LatticeLang
*learn* constraint weights or rankings from user choices or
corpora? The motivating literature is Hayes (2011)
:cite:p:`hayes2011` (experimental SSP evidence largely explicable
by learned phonotactics), Hayes & Wilson (2008) :cite:p:`hayeswilson2008`
(maxent phonotactic learner, *Linguistic Inquiry* 39:379–440),
and Tesar & Smolensky (2000) :cite:p:`tesar2000` (constraint-ranking
induction in OT). A working open-source reimplementation exists
(``george-steel/maxent-learner``), making the temptation practical,
not hypothetical. The question is recorded as research questions
(:ref:`q44-maxent-phonotactic-learning`, :ref:`q45-ot-learnability-framework`).

The MVP, per :ref:`ADR-027`, uses designer-fixed boolean
constraints. This ADR records *why* statistical constraint
learning stays deferred and where its scope boundary lies, so
future contributors don't re-litigate or accidentally start it.

Decision
~~~~~~~~

1. **Deferred.** No constraint-weight or constraint-rank learning
   in the MVP or its currently drafted use cases. Statistical
   estimation is a post-MVP subsystem.

2. **Scope boundary: evaluation vs. acquisition.** The question
   "could LatticeLang learn constraint weights?" conflates two
   separable components:

   - **Evaluation (inside the phonology module — already ours).**
     Deciding whether a candidate satisfies a constraint, and by
     what margin. Extending constraints from boolean filters to
     weighted scores is an *evaluation-side* extension: it flows
     through the existing constraint interface (:ref:`ADR-022`),
     the reserved ``mode`` field (:ref:`ADR-027`), and the reserved
     ``gradient_probabilistic`` type (:ref:`ADR-037`). Nothing here
     escapes the module.
   - **Acquisition (outside the phonology module).** Estimating
     weights/rankings *from data* — user choices, corpora, or
     reverse-pipeline inputs. This requires data collection and
     persistence, a learning algorithm, model selection, and a
     consumer that writes the inferred configuration. Learning
     *sets* constraints; it must not live inside the component
     that *evaluates* them.

3. **Architectural corollaries:**

   - The deferral is forced by accepted architecture, not just
     roadmap sequencing. A maxent trainer implies numerical
     dependencies incompatible with :ref:`ADR-010`'s
     zero-dependency core — the learner would be an outer layer
     (a PEP 621 extra) even if scheduled for the MVP.
   - The learner, when built, writes serialized constraint
     configurations — the same ``LanguageDefinition`` the
     generator consumes (:ref:`ADR-012`'s shared data contract).
     One-way flow: learner → definition → core. Learning never
     runs inside the generation loop.
   - Post-MVP entry points are already reserved:
     ``gradient_probabilistic`` on the evaluation side
     (:ref:`ADR-037`); corpus inference :ref:`q41-corpus-inference`
     on the data side.

Rejected
~~~~~~~~

1. **Begin a learning prototype now** — no use case describes it
   (violates :ref:`ADR-023`), and it would pull numerical
   dependencies toward the core (:ref:`ADR-010`).
2. **Silently prepare the data model for learning** (e.g.,
   logging user constraint toggles "for later") — a speculative
   feature with privacy implications, undocumented and unwanted
   until a use case demands it.

Consequences
~~~~~~~~~~~~

- Research questions :ref:`q44-maxent-phonotactic-learning` and
  :ref:`q45-ot-learnability-framework` carry the literature trail;
  this ADR carries the architectural ruling.
- The nasal-sonority question (:ref:`q43-nasal-sonority-split`) is
  *not* covered by this deferral — it challenges data-model
  assumptions inside the module, not module scope, and remains
  a research question.
- :cite:p:`kramer2020`, :cite:p:`hayes2011`, :cite:p:`hayeswilson2008`, and
  :cite:p:`tesar2000` enter the bibliography because this ADR and the
  linked questions cite them.

Relations
~~~~~~~~~

Extends: :ref:`ADR-027` (rule-based MVP), :ref:`ADR-010`
(zero-dependency core), :ref:`ADR-012` (bidirectional pipeline).
Records the deferral requested by: :ref:`q44-maxent-phonotactic-learning`,
:ref:`q45-ot-learnability-framework`. Governs: nothing in the MVP
(by design).

.. _adr-046:

ADR-046: [GEN] Generation Diagnostics — Instrumented Funnel Reporting for Rejected-Word Diagnosis
-------------------------------------------------------------------------------------------------

:Date: 2026-09-16
:Status: Accepted (design); implementation unscheduled
:Scope: Generation Pipeline
:Deciders: Lumo

Context
~~~~~~~

Three use cases promise diagnosis when the constraint set
rejects everything: :ref:`UC-03_define_phonotactic_constraints`
extension 4a3, :ref:`UC-04_generate_words` extension 3a, and
:ref:`UC-08_work_in_a_gui_with_live_preview` extension 3b
(which additionally promises to *link to the offending
constraint or template*). The 2026-09-16 use-case audit found
the strongest form of this promise — causal attribution of
unsatisfiability — to be an unanalyzed commitment: determining
*which constraint* makes a conjunctive filter set unsatisfiable
approaches minimal-unsat-core computation, which the MVP's
rejection-sampling generator was never scoped to perform.

The question this ADR answers: what diagnosis can the pipeline
give *cheaply and honestly*, and what must wait?

Decision
~~~~~~~~

Diagnostics are provided by **instrumentation of the existing
screening pipeline**, not by constraint solving:

1. **Per-constraint tallies.** Every constraint evaluation
   already returns a four-value result (PASSED / FAILED /
   SKIPPED, ERROR) :ref:`q37`. The pipeline additionally counts evaluations
   per outcome per constraint during a generation run.

2. **Funnel report.** After a run that yields zero (or few)
   survivors, the system reports the survival funnel: candidates
   composed per template, then survivors after each active
   constraint in evaluation order. The funnel shows *where*
   candidates die, which is observable, without claiming
   *why* (causal minimality).

3. **Attribution heuristic.** The report ranks constraints by
   rejection share and highlights the top rejector with one
   concrete example: a rejected candidate and the specific
   constraint instance that rejected it. This is a heuristic,
   not proof — a low-share constraint may still be the sole
   cause of a hard zero. The report says "most-rejected," never
   "the culprit."

4. **Deferred to post-MVP:** (a) minimal-conflict computation
   (finding the smallest constraint subset whose removal
   restores satisfiability — requires search beyond counting);
   (b) bounded ablation probing (temporarily disabling
   constraints to isolate cause sets — multiplies generation
   cost); (c) GUI click-through from report line to the
   offending constraint's editor entry, refining :ref:`uc08`
   extension 3b's linking promise.

Rejected
~~~~~~~~

1. **Exact unsatisfiability attribution in the MVP** —
   unscoped algorithmic work, and no use case requires proof,
   only actionable guidance.
2. **Silence on zero-survival runs** ("you asked for impossible
   phonotactics") — the raw fact a user can act on is *which
   filter consumed the output*; withholding it serves nobody.

Consequences
~~~~~~~~~~~~

- The tallies are engine-level state owned by the generation
  run record (see :ref:`dc_constraints` for the reporting
  schema — added to its open questions).
- Word-domain constraints that report SKIPPED never appear as
  top rejectors from syllable-level runs — the funnel report
  must surface this distinction or the report lies by omission.
- :ref:`uc08` extension 3b is restated at its sustainable strength:
  "system displays the survival funnel and most-rejected
  constraint for the current configuration"; linking remains
  a documented post-MVP refinement.
- :ref:`uc04` extension 3a gains the funnel report as its mechanism;
  :ref:`uc03` extension 4a3's "reports which constraints are blocking"
  is similarly bounded to the heuristic semantics.

Relations
~~~~~~~~~

Extends: Four-value validation results (:ref:`q37`), constraint
pipeline design (:ref:`ADR-037`). Records the disposition requested by
the :ref:`uc08` audit (2026-09-16). Related: :ref:`q4-ambiguity-confidence`
(error reporting philosophy kinship).

.. _adr-047:

ADR-047: [CORE] Project Persistence — Logical Schema, Adapters, Phased Container Formats
----------------------------------------------------------------------------------------

:Date: 2026-09-16
:Status: Accepted
:Scope: Persistence / all modules
:Deciders: Lumo

Context
~~~~~~~

Three documents describe project persistence inconsistently:
the blueprint specifies an ``.llp`` directory of per-module
JSON files; the suite vision describes "a single JSON file
that grows"; the use cases and phases assume a single
``.json`` project file. Resolution must respect three
constraints: the core stays dependency-free (:ref:`ADR-010`),
linguistics-data interchange (CLDF-style ecosystems) favors
interchangeable, directory-structured datasets, and
:ref:`ADR-012`'s bidirectional pipeline must round-trip
losslessly (:ref:`uc005`).

Decision
~~~~~~~~

1. **The logical schema is the contract.** ``LanguageDefinition``
   (and its per-module successors) is defined logically in
   :ref:`dc_language_definition`. No code in the core depends
   on a physical file layout.

2. **Serialization is an adapter at the boundary.** Loaders and
   savers are interchangeable strategies (Protected Variations,
   :cite:p:`larman2004`). The project standardizes their home
   as a persistence layer — ``latticelang.io`` (sibling of
   ``core``, not inside it), resolving the current split between
   ``latticelang.orthography.json_io`` and ``latticelang.core.*``
   paths seen in the use cases. Dependency direction points
   inward, per :cite:p:`martin2017`.

3. **Container formats by phase.** Phase Beta ships exactly one
   adapter: single-file ``*.json`` (``save_project`` /
   ``load_project``). The multi-module ``.llp`` directory
   container (manifest + per-module files) is the full-suite
   form and arrives when Module 2 exists — a new adapter, not a
   schema change. The loader may detect file-vs-directory and
   dispatch, but only the directory form needs to exist before
   it is needed.

4. **Interchange with linguistics formats is by exporter, not
   by native format.** CLDF compatibility (and any future
   tooling) is an outward-facing converter adapter — the
   project file stays optimized for round-trip fidelity, not
   third-party consumption.

Rejected
~~~~~~~~

1. Native CLDF as the project format — couples persistence to
   an external specification before the suite's shape is known.
2. Directory container in Beta — speculative generality for a
   single module.

Consequences
~~~~~~~~~~~~

- Use cases referencing ``latticelang.orthography.json_io`` and
  ``latticelang.core.orthography`` paths update to the
  persistence layer's home in their Variations sections (the
  standard's rule 5 keeps steps immune to this).
- :ref:`q5`'s versioning answer scopes to the logical schema's
  ``schema_version``, which travels identically in either
  container.
- The blueprint's persistence paragraph is superseded by this
  ADR; the suite-vision sentence stands as a description of
  Phase Beta.

.. _adr-048:

ADR-048: [PHONO] Tone Handled as a Separate Design Stage, Not a Slot Category
------------------------------------------------------------------------------

:Date: 2026-09-16
:Status: Accepted
:Scope: Phonology Tool
:Deciders: Danweel, Lumo

Context
~~~~~~~

The 2026-09-16 use-case audit found a design tension: :ref:`uc02`
allowed ``tone`` as a slot-fillable category, while
:ref:`ADR-037` reserves ``tone_assignment`` as a constraint type
and the autosegmental literature treats tone as attaching to
tone-bearing units rather than occupying serial syllable
positions (:cite:p:`goldsmith1976`, :cite:p:`yip2002`). Three
options were compared: tone as slot category (current :ref:`uc02`
draft), tone as constraint-only, and tone as a separate
optional design stage.

Decision
~~~~~~~~

**Tone is a separate design stage, not a slot property.**

1. ``tone`` is removed from the syllable template's fillable
   slot categories (:ref:`UC-02_define_syllable_templates`).
   Slots carry segmental phonemes only; sonority and eligibility
   logic (:ref:`ADR-034`) applies to segments.
2. ``tone_assignment`` (:ref:`ADR-037`, reserved) remains the
   sole MVP enforcement point for tonal behavior, exercising
   minimal functionality.
3. A future "Design a Tone System" user-goal case (stubbed as
   :ref:`uc016` in ``possible_future_cases/``) owns tone configuration;
   ``tone_assignment`` executes what it configures. Normative
   division: tone behavior is *configured* in the tone stage and
   *enforced* by ``tone_assignment``.
4. Tone features present in the PHOIBLE-derived feature vectors
   (:ref:`ADR-033`) are carried by ``dc_phoneme`` as data, even
   though nothing consumes them until the tone stage exists.

Rejected
~~~~~~~~

1. **Tone as slot category** — serializes what the literature
   treats as autosegmental: contour tones on long nuclei,
   spreading, floating tones, and toneless syllables all break a
   one-slot-one-tone model; duplicates ``tone_assignment``;
   cannot be reached from corpus import (:ref:`uc012` segments
   segments, not tones).
2. **Constraint-only, permanently** — a constraint parameter
   block is the wrong interaction shape for designing a tone
   system, which is creative work deserving its own surface.

Timing
~~~~~~

Deferred by design. The MVP validates with segmental-only
phonologies; the tone stage is additive at every seam (extensible
constraint catalog, versioned schema, feature-vector data). No
structural work precedes it. See :ref:`UC-18_design_a_tone_system`

Relations
~~~~~~~~~

Amends: :ref:`UC-02_define_syllable_templates` (category list).
Extends: :ref:`ADR-037` (reserved types).
Cites: :cite:p:`goldsmith1976`, :cite:p:`goldsmith1990`, :cite:p:`yip2002`.
Creates: UC-16 stub (future case).

.. _adr-049:

ADR-049: [GEN] Stream Derivation Keys — Coordinate-Addressed Streams for All Random Decisions
---------------------------------------------------------------------------------------------

:Date: 2026-09-16
:Status: Accepted
:Scope: Generation Pipeline
:Deciders: Lumo, (with some constraints from Danweel)

Context
~~~~~~~

:ref:`ADR-044` established per-slot streams keyed by seed, word
position, and slot position — but two draws have no key: template
selection (:ref:`uc014` step 1) and syllable-count selection
(:ref:`uc04`). :ref:`q7` asks for the template key. The pattern must
also anticipate future decision kinds (notably tone, :ref:`ADR-046`)
without re-keying the scheme.

Decision
~~~~~~~~

1. Every random decision draws from a dedicated stream produced
   by one derivation function: **D(project_seed, word_position,
   domain, index)**. The function is pure: a stream depends only
   on its coordinates, never on another stream's consumption.

2. **Domain** is a closed vocabulary, extended only by ADR:
   ``template``, ``syllable_count``, ``slot`` (index = slot
   position within the template), and reserved ``tone``
   (:ref:`ADR-048`). Domains guarantee cross-decision
   uniqueness — word 3's template draw can never collide with
   word 3's slot-0 draw.

3. **Flat addressing, no sequential spawning.** Any word (or
   syllable, or slot) regenerates independently of all others —
   preserving :ref:`ADR-044`'s edit-locality, enabling parallel and
   isolated test regeneration, and excluding hidden global state.

4. **Versioned determinism.** The derivation function carries a
   generator version. Determinism is guaranteed *within* a
   version; changes to D are documented instability and bump the
   version. Generation records store seed + generator version
   (:ref:`Q5`'s ``schema_version`` is the carrier), so a saved project
   reproduces its words on the version that made them.

5. **Implementation-agnostic.** The contract is the key
   structure, not the algorithm; the reference technique is the
   standard library PRNG :cite:p:`matsumotonishimura1998` seeded
   per stream.

Rejected
~~~~~~~~

1. Sequential spawning (word streams derived from prior
   consumption) — breaks independent regeneration.
2. Extending :ref:`ADR-044` slot keys ad hoc per new decision — invites
   collisions and loses the single derivation point (Protected
   Variations, :cite:p:`larman2004`).

Consequences
~~~~~~~~~~~~

- :ref:`uc014` step 1 draws from domain ``template``; :ref:`uc04`'s count
  from ``syllable_count``; :ref:`uc017`'s weighted selection from
  ``slot`` — cite this ADR at those steps.
- :ref:`Q7` resolves: seeds recorded in generation records;
  stability is within-version; frequency normalization remains
  per-slot and never persisted (unchanged).
- Future tone draws have a reserved domain; no re-keying when
  the tone stage arrives.

  .. _adr-050:

ADR-050: [PHONO] Ambiguity Confidence — Qualitative Tiers, Non-Interruptive Batching
------------------------------------------------------------------------------------

:Date: 2026-09-16
:Status: Accepted
:Scope: Import Pipeline / Segmenter
:Deciders: Danweel, Lumo technicals

Context
~~~~~~~

:ref:`Q4` asked how the segmenter's ambiguity decisions (:ref:`q1-segmenter-ambiguity`)
should be surfaced to users, and how batch import (:ref:`uc009`)
avoids per-word interruption. Resolved during the :ref:`uc012` drafting
session (2026-09-16).

Decision
~~~~~~~~

1. **Confidence is surfaced, qualitatively.** Three tiers —
   high / medium / low — attached per ambiguity record
   (:ref:`uc012` step 5). No numeric probabilities; the tiers
   are heuristics, not statistics.

2. **The segmenter never interrupts.** In batch contexts,
   ambiguity flags accumulate and surface afterward through
   :ref:`uc009`'s review flow, including apply-to-all
   (extension 6a). Mid-batch prompting is rejected.

3. **Resolution order** (per ambiguity): user inventory
   (preferred — a reading whose segments all exist in the
   confirmed inventory wins) → longest-match (:ref:`adr-043`,
   :ref:`Q1`) → definition order (deterministic default for
   same-length alternates, flagged low).

4. **Frequency-statistics resolution is post-MVP.** Inferring
   readings from language-particular frequency is statistical
   learning — outside the boundary of :ref:`adr-045`.

Rejected
~~~~~~~~

1. Numeric confidence scores — spurious precision; the tiers
   carry the actionable information (needs review: yes/no).
2. Interruptive prompting in batch mode — tedium per Q4's own
   analysis; :ref:`uc009`'s review flow is the correction surface.
3. Frequency-based resolution in MVP — see Decision 4.

Relations
~~~~~~~~~

Resolves: :ref:`q4-ambiguity-confidence` (surfacing and batch
policy; mechanics remain :ref:`q1-segmenter-ambiguity`).
Implements: :ref:`uc012` steps 5–6, extensions 4a–5a.
Boundary: :ref:`adr-045`.


.. _adr-051:

ADR-051: Merge Field-Class Semantics for Duplicate Phonemes
============================================================

:Date: 2026-09-23
:Status: Accepted
:Scope: Generation Pipeline
:Deciders: Danweel, Lumo advisory

:Context: UC-01 extension 6a2 (duplicate symbol merge), UC-009
          (corpus import), ADR-040 (merge safety), Q7 (frequency semantics)
:Relates to: :ref:`adr-032` (derived category), :ref:`adr-035`
             (confirm-don't-block), :ref:`adr-040`, :ref:`adr-041` (near-miss detection)

Context
-------

When a phoneme is added whose ``symbol`` already exists in the
inventory — via manual UC-01 entry, UC-009 corpus import, or
importing a shared definition — the two records must become one.
The audit round of 2026-09-16 flagged this as undefined: which
phoneme's values win on conflict, and whether ``frequency`` and
``sonority_rank`` participate in the merge or only features.

Blanket rules fail differently on each side. "New wins"
overwrites user-confirmed values with data the user never
vetted; "existing wins" prevents corpus imports from ever
enriching a phoneme's frequency evidence, crippling the import
path. Per-field prompting is unusable in batch contexts
(UC-009 may process dozens of collisions headlessly) and is not
deterministically testable.

The underlying insight is that fields differ in *provenance*:
some incoming data is authority the user doesn't have
(attestation frequency from a corpus), and some existing data is
authority the incoming source can't supply (a confirmed
sonority rank).

Decision
--------

Merges resolve by **field-class rules**, applied through two
paths:

1. **Interactive path** (UC-01 manual add): a dialog presents
   both records side-by-side with per-field selection,
   prefilled with the deterministic outcomes below — the
   confirm-don't-block pattern of :ref:`adr-035`.
2. **Deterministic fallback** (UC-009 batch import, headless
   runs, test fixtures): the field-class rules apply as-is.

The field-class rules:

- ``features`` — union: new keys are added; conflicting values
  retain the existing value. Feature corrections are deliberate
  acts (ADR-040's never-downgrade).
- ``sonority_rank`` — existing wins, always. The stored value is
  authoritative once confirmed (UC-01 extension 4a).
- ``frequency`` — values are summed; normalization happens at
  selection time and is never persisted (Q7). Duplicates
  represent double-counted attestation.
- ``category`` — never merged; recomputed from the merged
  feature set per :ref:`adr-032`.
- ``components``, ``custom``, ``metadata`` — new-only fill:
  empty fields adopt the incoming value; populated fields
  retain theirs.

Every fallback decision is written to a collision log, enabling
interactive replay later and providing a pure-function test
surface. Near-miss candidates (symbols differing only by
diacritic) are handled *before* merge consideration, per
:ref:`adr-041` — they surface as suggestions, not collisions.

Consequences
------------

Positive: merge behavior is deterministic and testable without
a UI; the batch import path needs no interruption; different
data provenances are honored asymmetrically where they deserve
it; the collision log preserves user agency by allowing after-
the-fact review.

Negative: two code paths (interactive and fallback) must stay
consistent — mitigated by prefilling the dialog from the same
rules; the field-class table is one more normative artifact to
keep synchronized with ``dc_phoneme`` (which is now its
contract-level home).

The frequency-sum rule implies that importing the same corpus
twice doubles all frequencies — documented as expected
behavior; re-importing is an intentional act.

Follow-through: ``dc_phoneme`` carries these rules as its Merge
Semantics section; ``tests/test_phoneme_merge.py`` (future)
asserts each row of the table.
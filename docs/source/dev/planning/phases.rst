.. _phases:

Phonology Tool Development Phases
===================================

:date: 2026-08-24
:type: Living
:audience: Developers and contributors
:purpose: When do things happen?

These phases track the development of the **Phonology Tool** — the first
tool in the LatticeLang suite. For the broader suite-level roadmap, see
:doc:`suite_vision`.

Because this is a hobby and open-source project, LatticeLang is
developed in "coherent engineering phases", not "market-driven
milestones". Each phase delivers a **complete, testable system** — not
marketable features as-such.

Phases are the sole development-timeline vocabulary.
The informal term 'milestone' is deprecated in documentation.

.. contents::
   :local:
   :depth: 2

.. _phase_alpha:

Phase Alpha: Foundation
-----------------------

:Status: Complete
:Deliverable: Green CI, reproducible builds, zero lint errors
:Duration: Week 1

Infrastructure only. No user-facing features.

Completed:

- Project structure and Poetry setup
- YAML configuration support
- Sphinx documentation framework
- CI/CD pipeline setup

.. _phase_beta:

Phase Beta: Core Engine (Engineering MVP)
------------------------------------------

:Status: In Progress
:Deliverable: Runnable Python library supporting both forward and reverse pipelines
:Duration: Weeks 3–8

The **engineering minimum**. A developer can use the Python API
to define phonologies, generate words, and import romanized word
lists. No GUI; minimal CLI.

Features in this phase:

- :ref:`uc005` — Serialize/Deserialize LanguageDefinition
- :ref:`uc012` — Convert Orthography to IPA and Segment
- :ref:`uc01` — Define Phoneme Inventory (both manual and review modes)
- :ref:`uc02` — Define Syllable Templates
- :ref:`uc03` — Define Phonotactic Constraints
- :ref:`uc04` — Generate Words
- Python API only (no GUI)
- Basic CLI (``latticelang generate``, ``latticelang import``)
- Comprehensive test suite

In progress:

- [ ] Complete API documentation
- [ ] IPA reference table (complete symbol list)
- [ ] Dialect profiles (American English, Received Pronunciation)
- [ ] JSON persistence (.json project files)
- [ ] Unicode NFC normalization for IPA
- [ ] CLI interface refinement
- [ ] Example language configurations

.. _phase_gamma:

Phase Gamma: User Interfaces
-----------------------------

:Status: Planned
:Deliverable: Usable application with live preview
:Duration: Months 3–5

Human interaction layers built *on top of* the Phase Beta engine.

Features:

- Interactive GUI (PySide6)
- Word list management (add/edit/delete saved words)
- Custom orthography editor
- Audio playback (click-to-hear IPA)
- Improved CLI with tab completion, colored output
- Language preset system architecture

Technical requirements:

- PySide6 installation
- Font bundling (IPA-capable fonts)
- Event-driven architecture (live preview debouncing)

.. _phase_delta:

Phase Delta: Advanced Features
-------------------------------

:Status: Planned
:Deliverable: Extended linguistics toolkit and export capabilities
:Duration: Month 6+

Advanced linguistic features and professional-quality outputs.

Export and Analysis:

- :ref:`uc07` — Export to LaTeX
- CSV/HTML/plain-text word list export
- Language comparison tools
- Phoneme frequency statistics

Advanced Constraints:

- OT constraint mode (ranked, violable constraints)
- Dialect system (universal→override model)
- Cross-syllable harmony constraints
- Allophonic rules
- Gradient/probabilistic constraints
- Foot structure and prosodic hierarchy
- Giscus integration on research/questions.rst for community
  discussion
- Contribution guidelines published

Prosody:

- Tone assignment module
- Stress assignment module (requires moraic weight)
- Syllable weight (moraic counting)

.. _phase_epsilon:

Phase Epsilon: Future Research
--------------------------------

:Status: Future research
:Deliverable: Advanced linguistic toolkit
:Duration: 2027+

Advanced features for specialists. These features have no use cases
yet and are exploratory.

Proposed:

- Sound change simulation (historical linguistics)
- Corpus-based constraint inference (ML)
- Morphology module (evaluate :ref:`q22-unimorph-integration`)
- Syntax module (evaluate :ref:`q21-conllu-interchange`)
- Plugin API for custom generators
- Prosody module (sentence-level patterns)

.. _design-decisions:

Design Decisions
-----------------

1. **Engine-first approach** — Core logic is fully implemented
   before any UI work begins. This ensures the API is stable
   and the architecture is sound. See :ref:`decisions`.

2. **Both paths from Day 1** — Forward (define from scratch)
   and reverse (import words) workflows are both supported
   in Phase Beta. Neither is deferred.

3. **No "half-features"** — Each phase is complete enough to
   use independently. There are no "beta" or "experimental"
   flags on shipped features.

4. **Data contracts reflect full vision** — Even if some
   features aren't implemented in Phase Beta, the data
   structures are designed for the complete system. This
   prevents migrations later.

.. _out-of-scope:

Out of Scope (For Now)
-----------------------

LatticeLang intentionally excludes certain features to remain
focused and accessible. These may be revisited if community
interest and contributor capacity warrant:

- **Full linguistic database** — Unlike SIL FieldWorks, we don't
  aim to be a complete field linguistics suite. We focus on
  conlang creation, not documentation of existing languages.

- **Enterprise features** — No multi-tenant architecture,
  enterprise SSO, or commercial licensing.

- **Multi-user project sharing** — No real-time collaboration
  or cloud sync. Projects are local files.

- **Mobile companion app** — Desktop-first; mobile is not a
  priority.

- **Version control integration** — Language designs are
  versioned via standard file-based VCS (Git), not a custom
  system.

- **Community template library** — A hosted template repository
  is conceivable post-launch but requires infrastructure we
  don't have.

.. _positioning:

Positioning
------------

LatticeLang sits between hobbyist conlang tools and professional
linguistics suites:

.. csv-table::
   :header-rows: 1
   :widths: 20 20 20 20

   "Dimension","Hobbyist Tools","LatticeLang","Professional Suites"
   "Target audience","Casual conlangers","Serious conlangers","Professional linguists"
   "Learning curve","Low","Moderate","High"
   "Extensibility","Limited","High (plugins planned)","Very High"
   "Cost","Free/Paid","Free (FOSS, MIT)","Free (installed)"
   "Primary use case","Fun/Experiment","Naturalistic conlangs","Field documentation"

Examples: Hobbyist tools include simple web-based phoneme generators.
Professional suites include SIL FieldWorks and Praat.

References
----------

- :cite:p:`cockburn2001` — separates interface details from use case behavior.
- :cite:p:`constantine1999` — layered architecture (domain model → presentation).
- :cite:p:`martin2017` — stable interfaces, dependency inversion.
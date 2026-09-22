.. _suite_vision:

LatticeLang Suite Vision
==========================

:date: 2026-08-24
:type: Static
:audience: Developers and contributors
:purpose: Where does this fit in the bigger picture?

LatticeLang is a modular conlanging toolkit inspired (primarily) by the workflow
in :cite:p:`rosenfelder2010`. Each tool in the suite addresses one stage
of the language construction process. Tools are developed sequentially —
each builds on the outputs of previous tools.

.. contents::
   :local:
   :depth: 2

Design Principle: Composable Tools
-----------------------------------

Each tool is a self-contained module that:

- Has its **own** lifecycle (design → implement → ship)
- Shares the **same** project file format (LanguageDefinition JSON,
  extended per tool)
- Exposes a **stable API** that the next tool can consume
- Has its **own** use cases, data contracts, and test suite

Tools do not depend on each other at runtime — they communicate through
serialized data (project files, exports). This means you can use the
Phonology Tool without ever touching Morphology, or skip straight to
Lexicon if you have phonological data from another source.

Tool Sequence
--------------

.. csv-table::
   :header-rows: 1
   :widths: 15 10 15 40 20

   "Tool","LCK Stage","Status","Feeds Into","MVP Constraint"

   "Phonology","1–2","Active","Orthography, Morphology","Ship first"
   "Orthography","3","Planned","Lexicon","Needs phoneme inventory"
   "Morphology","4","Planned","Syntax","Needs phoneme sequences (roots)"
   "Syntax","5","Planned","Lexicon","Needs morphological words"
   "Lexicon","6","Planned","Worldbuilding","Needs words + meanings"
   "Worldbuilding","7","Speculative","—","Needs all of the above"

Shared Infrastructure
----------------------

Across all tools, LatticeLang provides:

- **Project file format** — A single JSON file that grows as more tools
  are used. The phonology section is populated first; morphology and
  syntax sections are added later.
- **Constraint system** — The same rule-based constraint architecture
  applies to phonotactics (Phonology), morpheme structure (Morphology),
  and word order (Syntax).
- **Generator engine** — The candidate-generation-plus-filtering pattern
  works for syllables (Phonology), word forms (Morphology), and
  sentences (Syntax).
- **Theoretical framework** — The Generative/OT/feature-based tagging
  system extends to all linguistic levels.

Current Focus: Phonology Tool
-------------------------------

The Phonology Tool is the first and only active tool. Its goal:

**Input:** A set of phonemes (defined manually or imported from
romanized examples).

**Output:** Generated words that obey the user's phonotactic rules,
adjustable in real time.

**Success criterion:** A conlanger can define a phonology, generate
sample words, adjust constraints, and see results immediately — entirely
through the GUI, without touching code.

See :doc:`phases` for the Phonology Tool's internal development phases.

Relationship to This Documentation
------------------------------------

Current documentation covers **Phase Beta of the Phonology Tool** only.
As other tools enter development, they will add:

- New use case sections (e.g., ``use_cases/morphology/``)
- New data contracts (e.g., ``data_contracts/morpheme.rst``)
- New research questions tagged with the tool name
- New phases for each tool

Research questions and ADRs are tagged with their tool scope:

- ``[PHONO]`` — Phonology Tool
- ``[ORTHO]`` — Orthography Tool
- ``[MORPH]`` — Morphology Tool
- ``[SYNTAX]`` — Syntax Tool
- ``[SUITE]`` — Cross-tool / suite-level

See :ref:`questions` for the current question registry.
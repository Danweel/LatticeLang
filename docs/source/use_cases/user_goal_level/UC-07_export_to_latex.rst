.. _UC-07_export_to_latex:
.. _uc07:

UC-07: Export to LaTeX
=======================

:Doc Status: Review
:Goal Level: User Goal
:Impl Status: Not Started
:Phase: Delta (export/polish)

Goal
----
Export a language definition and/or generated word list to a compilable
LaTeX document using the ``tipa`` package for IPA rendering. The output
is a minimal, dependency-light ``.tex`` file suitable for inclusion in a
larger document or standalone compilation.

Preconditions
-------------
- A LanguageDefinition is loaded in memory — see :ref:`uc005`
- Optionally: generated words exist — see :ref:`uc04`
- User has a LaTeX distribution with ``tipa`` installed (for local
  compilation; not required for the export itself)

Main Success Scenario
---------------------

1. User requests export with parameters:
   - Output file path
   - Content selection: definition only, words only, or both
   - Optionally: word count (if generating words as part of export): system validates the output path is writable

2. System generates the LaTeX document containing (based on content
   selection):
   - Phoneme inventory in three tables, by category (ADR-032): consonants (rows = manner, columns = place),
   vowels (trapezoid grid approximated by ``tabular``), and an "additional segments" table listing glides,
   diphthongs (component notation per ADR-028), and custom phonemes
   - Syllable template list - calls :func:`~latticelang.io.latex_export.render_templates`
   - Phonotactic constraint summary: calls :func:`~latticelang.io.latex_export.render_constraints`
   - Generated word list (if words exist or were requested): calls :func:`~latticelang.io.latex_export.render_word_list`

   IPA symbols render via ``tipa`` macros resolved from the
   ``tipa`` field of ``ipa_reference.json`` (populated by the Q38
   pipeline)

3. System writes the ``.tex`` file to the specified path: calls
   :func:`~latticelang.io.latex_export.export_latex`

4. User compiles locally:
   ``pdflatex report.tex``

Postconditions
--------------
- ``.tex`` file exists at the specified path
- File compiles with ``pdflatex + tipa`` without errors
- Symbols lacking a tipa macro appear as raw Unicode, flagged in
  the file's warning comments (see extension 3b)

Extensions
----------

* **1a:** Output path not writable
  - 1a1: System reports error with the attempted path
  - 1a2: User selects alternate location
  - TODO: troubleshooting page (file I/O)

* **2a:** No generated words exist at export time
  - 2a1: System offers to generate words as part of export
  - 2a2: If user accepts, system invokes :ref:`uc04` with default parameters (100 words, 1–4 syllables, frequency weighting on)
  - 2a3: If user declines, exports definition only (charts, templates, constraints)

* **2b:** Inventory contains custom or user-defined-feature phonemes
  with no place/manner axis position
  - 2b1: System places those phonemes in the "additional segments" table
  - 2b2: If a phoneme carries user-defined features, the exported constraint summary notes which features are non-standard

* **3b:** Symbol lacks a tipa macro
  - 3b1: System inserts the raw Unicode character
  - 3b2: A warning comment is written into the .tex file listing the affected symbols
  - 3b3: The export summary reports: "[N] symbols exported as Unicode — compilation requires a Unicode font (e.g., via
  fontspec/LuaLaTeX) for these to render"
  - Note: expected for rare PHOIBLE-derived segments (clicks, some modifier stacks); tipa predates full Unicode IPA.
  Known-symbol macro coverage comes from ``ipa_reference.json``'s ``tipa`` field

* **4a:** LaTeX compilation fails on user's machine
  - 4a1: Error is in user's local environment, not in the exported file (the file itself is pre-validated minimal)
  - 4a2: System provides a "minimal example" ``.tex`` snippet for testing
  - 4a3: Common causes: ``tipa`` not installed, encoding issues, missing ``utf8`` input encoding
  - TODO: troubleshooting page (LaTeX compilation)

Frequency
---------
Low — typically once per project when the language is finalized.

Related
-------

**Calls (delegates to):**
- :ref:`uc04` — Generate Words (optional, if words requested as part of export)
- :ref:`uc005` — Serialize/Deserialize (loads the definition being exported)

**Adjacent to:**
- :ref:`uc04` — Generate Words (source of the word list)
- ``dc_ipa_reference`` — supplies the ``tipa`` macro mapping

Variations
----------

* **Via CLI (Phase Delta):**

  .. code-block:: bash

     latticelang export --load my_language.json --format latex \
       --output report.tex --words 100

* **Via GUI (Phase Delta):**
  User selects File → Export → LaTeX. Dialog offers checkboxes for
  content selection (inventory, templates, constraints, words) and
  a word count field if words are requested.

* **Via Python API (Phase Delta):**

  .. code-block:: python

     from latticelang.io.latex_export import export_latex
     from latticelang.io.language_json import load_project

     definition = load_project("my_language.json")
     export_latex(
         definition=definition,
         output_path="report.tex",
         include_words=True,
         word_count=100,
     )

Notes
-----
The LaTeX export uses ``tipa`` for IPA symbols and standard
``tabular`` for phoneme charts. The template is intentionally
minimal — no custom styling, no dependencies beyond ``tipa`` —
so it compiles in any standard LaTeX distribution. Users can
customize the preamble after export.

The consonant table layout follows the standard IPA consonant
chart format: rows = manners of articulation, columns = places
of articulation, both axes drawn from the pinned feature
vocabulary (ADR-033). Vowels use the standard trapezoid layout
approximated with a ``tabular`` grid. Glides, diphthongs, and
custom phonemes are listed in a supplementary table rather than
forced onto a chart axis (ADR-032 categories have no canonical
grid position for these).

Symbols without tipa macros are an expected, handled case (see
extension 3b), not an error — the reference table's coverage and
tipa's coverage are documented independently in
``dc_ipa_reference``.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Request Export: path, content selection] --> B{Path Writable?}
       B -->|No| C[Report Error]
       C --> A
       B -->|Yes| D{Include Words?}
       D -->|Yes| E{Words Exist?}
       D -->|No| F[Render Definition Only]
       E -->|Yes| F
       E -->|No| G{Generate Words?}
       G -->|Yes| H[Invoke UC-04]
       H --> F
       G -->|No| F
       F --> I[Render Phoneme Tables: C + V + Additional]
       I --> J[Render Templates]
       J --> K[Render Constraints]
       K --> L{Include Words?}
       L -->|Yes| M[Render Word List]
   L -->|No| N[Resolve tipa Macros, Warn on Gaps]
       M --> N
       N --> O[Write .tex File]
       O --> P[Done]
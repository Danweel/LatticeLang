.. _uc07:

UC-07: Export to LaTeX
=======================

:Goal Level: User goal
:Priority: MVP — Milestone 4
:Status: Planned

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

#. User requests export with parameters:
   - Output file path
   - Content selection: definition only, words only, or both
   - Optionally: word count (if generating words as part of export)
   → system validates the output path is writable

#. System generates the LaTeX document containing (based on content
   selection):
   - Phoneme inventory table (consonants and vowels in separate tables,
     organized by place and manner) → calls
     :func:`~latticelang.orthography.latex_export.render_phoneme_table`
   - Syllable template list → calls
     :func:`~latticelang.orthography.latex_export.render_templates`
   - Phonotactic constraint summary → calls
     :func:`~latticelang.orthography.latex_export.render_constraints`
   - Generated word list (if words exist or were requested) → calls
     :func:`~latticelang.orthography.latex_export.render_word_list`

#. System writes the ``.tex`` file to the specified path → calls
   :func:`~latticelang.orthography.latex_export.export_latex`

#. User compiles locally:
   ``pdflatex report.tex``

Postconditions
--------------
- ``.tex`` file exists at the specified path
- File compiles with ``pdflatex + tipa`` without errors
- IPA symbols render correctly via ``tipa`` macros

Extensions
----------

* **1a:** Output path not writable
  - 1a1: System reports error with the attempted path
  - 1a2: User selects alternate location
  - → See :ref:`troubleshooting_file_io`

* **2a:** No generated words exist at export time
  - 2a1: System offers to generate words as part of export
  - 2a2: If user accepts, system invokes :ref:`uc04` with default
    parameters (100 words, 1–4 syllables)
  - 2a3: If user declines, exports definition only (charts, templates,
    constraints)

* **2b:** Phoneme inventory has phonemes with no ``place`` or ``manner``
  features
  - 2b1: System places those phonemes in an "Uncategorized" row
  - 2b2: Warning: "[N] phonemes lack place/manner features — table
    placement may be inaccurate"

* **4a:** LaTeX compilation fails on user's machine
  - 4a1: Error is in user's local environment, not in the exported file
  - 4a2: System provides a "minimal example" ``.tex`` snippet for
    testing
  - 4a3: Common causes: ``tipa`` not installed, encoding issues,
    missing ``utf8`` input encoding
  - → See :ref:`troubleshooting_latex_compile`

Frequency
---------
Low — typically done once per project when the language is finalized.

Related
-------

**Calls (delegates to):**
- :ref:`uc04` — Generate Words (optional, if words requested as part
  of export)
- :ref:`uc005` — Serialize/Deserialize (loads the definition being
  exported)

**Adjacent to:**
- :ref:`uc04` — Generate Words (source of the word list)

Variations
----------

* **Via CLI (Milestone 2+):**

  .. code-block:: bash

     latticelang export --load my_language.json --format latex \
       --output report.tex --words 100

* **Via GUI (Milestone 3+):**
  User selects File → Export → LaTeX. Dialog offers checkboxes for
  content selection (inventory, templates, constraints, words) and
  a word count field if words are requested.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.orthography.latex_export import export_latex
     from latticelang.orthography.json_io import load_project

     definition = load_project("my_language.json")
     export_latex(
         definition=definition,
         output_path="report.tex",
         include_words=True,
         word_count=100,
     )

Notes
-----
The LaTeX export uses ``tipa`` for IPA symbols and standard ``tabular``
for phoneme charts. The template is intentionally minimal — no custom
styling, no dependencies beyond ``tipa`` — so it compiles in any
standard LaTeX distribution. Users can customize the preamble after
export.

The phoneme table layout follows the standard IPA consonant chart
format: rows = manners of articulation, columns = places of
articulation. Vowels use the standard trapezoid layout approximated
with a ``tabular`` grid.

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
       F --> I[Render Phoneme Tables]
       I --> J[Render Templates]
       J --> K[Render Constraints]
       K --> L{Include Words?}
       L -->|Yes| M[Render Word List]
       L -->|No| N[Write .tex File]
       M --> N
       N --> O[Done]
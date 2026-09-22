.. _documentation_standards:

Documentation Standards
========================

:date: 2026-08-24
:type: Static
:audience: Developers and contributors
:purpose: Consistency

This file serves as a reference for consistent formatting and structure
across LatticeLang documentation. It is intentionally compact for easy
reference during development sessions.

File Organization
-----------------

.. code-block:: text

docs/source/
├── index.rst
├── use_cases/                    # Use case specifications
│   ├── index.rst                 # Use case index
│   ├── user_goals/               # Level 1 goals, also may include broader Summaries.
│   │   ├── uc01.rst
│   │   ├── uc02.rst
│   │   └── ...
│   └── subfunctions/             # Level 2 subfunctions
│       ├── uc005.rst
│       └── ...
├── data_contracts/               # Data structure specifications
│   ├── index.rst
│   ├── dc_phoneme.rst
│   ├── dc_syllable_template.rst
│   ├── dc_language_definition.rst
│   ├── dc_constraint.rst
│   ├── dc_orthography_rules.rst
│   └── dc_ipa_reference.rst
├── api/                          # Auto-generated API docs
│   ├── index.rst                 # autodoc output
│   ├── core.rst                  # blank, planned
│   ├── orthography.rst
│   └── ui.rst
├── dev/                          # Development documentation
│   ├── index.rst                 # Dev section index
│   ├── planning/                 # Milestones and vision
│   │   ├── blueprint.rst
│   │   ├── suite_vision.rst
│   │   └── phases.rst
│   ├── design/                   # Architecture and theory
│   │   ├── architecture.rst
│   │   ├── theoretical_framework.rst
│   │   ├── constraints.rst
│   │   └── testing.rst           # blank, planned
│   └── governance/               # Process and decisions
│       ├── decisions.rst
│       └── documentation_standards.rst
├── research/                     # Research tracking
│   ├── index.rst
│   ├── questions.rst
│   ├── refs.bib
│   └── bibliography.rst
├── community/                    # Community/contributing
│   └── index.rst
├── todo/                         # TODO tracking
│   └── index.rst
├── user/
│   ├── index.rst
│   ├── troubleshooting/
│   │   ├── index.rst
│   │   └── ...
│   ├── tutorials/
│   │   ├── index.rst
│   │   └── ...
│   ├── about.rst
│   ├── contributing.rst
│   ├── installation.rst
│   ├── quickstart.rst
│   └── reference.rst             # Specifically aimed at users
└── glossary.rst

Table Formatting Rules
----------------------

- **Never** use RST grid tables (``+---+`` style).
- Use ``.. csv-table::`` for data-heavy tables, ``.. list-table::``
  for moderate complexity, and MyST Markdown pipe tables in
  ``.md`` files for simple tables.

Construction pitfalls (all produce build ERRORS, not warnings):

- In ``csv-table`` cells, a literal double quote inside a quoted
  value breaks CSV parsing. Backslash escapes (``\"``) do NOT work
  — CSV has no backslash escapes. Double the embedded quotes
  (``""a""``) or, usually better, use single quotes in example
  text (``'a'``).
- ``list-table`` rows must all contain the same number of items.
  An unfilled skeleton row (``* - ...``) breaks the entire table;
  either fill every cell or omit the row.
- ``:widths:`` must declare exactly as many values as the table
  has columns, counting the header row.

Cross-Reference Conventions
---------------------------

Roles and syntax:

- Labels: ``.. _label-name:`` (lowercase, hyphenated); references
  use ``:ref:`label-name```.
- Questions: ``.. _qXX-topic:`` → ``:ref:`qXX-topic``
- Glossary terms: ``:term:`affricate``
- Parenthetical citations: ``:cite:p:`key``
- Textual citation: ``:cite:t:`key```, ``{see}:cite:t:`key`{p. 1166}``
- Footnotes: ``:footcite:t:``, ``:footcite:p:``

Label semantics (why refs fail silently):

- Labels are exact-match: ``adr_037`` and ``adr-037`` are different
  labels, and case matters (``ADR-032`` ≠ ``adr-032``).
- Labels bind to the NEXT document node. A label placed between a
  section heading and its first paragraph attaches to the
  paragraph, not the heading; bare ``:ref:`` calls to it then fail
  with "A title or caption not found." Place labels ABOVE headings.
- Toctree entries are FILE PATHS, not labels. The toctree and the
  label namespace are separate: defining ``.. _index_api:`` does not
  create a document named ``api/index_api``. Toctree lines point at
  the real file (``<directory>/index``); prose references use the
  ``index_<area>`` label.
- ADR labels are lowercase-hyphenated (``.. _adr-037:``), per the
  general label rule.

Same-commit hygiene:

- Every term must have a matching entry in
  ``glossary.rst`` committed in the same change. Write the term
  first, the referencing prose second.

- Backticks in titles are a Markdown-ism leaking into bibtex; the title should use straight quotes: The {'Whole Larynx'}

BibTeX Entry Hygiene
~~~~~~~~~~~~~~~~~~~~

Every field line inside an entry must end with a comma except the
final field before the closing brace (trailing commas after the
last field are tolerated by BibTeX's parser but are inconsistent
style — either style, but uniformly). Before saving ``refs.bib``:

1. Every opening ``{`` has a closing ``}`` — balance check:
   ``grep -c '{' refs.bib`` equals ``grep -c '}' refs.bib``
   (URLs in ``\url{}`` count; escaped braces are rare enough to
   ignore, but investigate any mismatch before trusting it)
2. Paste edits as **complete entries** (key line through closing
   brace), never partial fragments — mid-entry pastes truncate
   exactly like mid-script shell pastes
3. The census crashes at ``builder-inited`` with "syntax error in
   line N" are refs.bib errors, not document errors — go to line
   N of refs.bib first

Question-Resolution Hygiene (Questions ↔ Decisions)
---------------------------------------------------

Every new decision (ADR) and every answered research question must
keep both registries synchronized in the same commit:

1. **Check the question first.** Before writing an ADR, check
   whether a research question already covers the topic
   (``grep -n '^[A-Z].*[Tt]opic-word' research/questions.rst``
   or Ctrl-F by keyword). A decision on a topic that already has
   a question is a *resolution*, and the question page must
   record it — otherwise the question shows OPEN while a ruling
   exists, or worse, both drift apart.

2. **Update the question body.** Set its Status line to
   ``ANSWERED (date, :ref:`adr-0XX`)`` (or a split status if only
   part of the question is settled — say which part).

3. **Update the Status Overview table.** The table row for that
   question must reflect the new status, the ADR reference, and
   any re-scoped Blocks value. A question with an ANSWERED body
   but an OPEN table row is a documentation bug.

4. **Update the Decisions side.** New ADRs get an index row in
   the ADR Index table (scope tag, title, status, date, deciders)
   and a full entry with a Relations block naming the resolved
   question. Existing ADRs that cite a question ruling must
   cite it via the question's *label*, not prose.

5. **Promote backfilled rulings.** If a question's body already
   records a dated ruling with no ADR, promote the ruling to a
   new ADR (citing the question as origin) rather than leaving
   the decision log dependent on the questions file for its
   normative content.

6. **Sweep the question's action items.** Checked-off decisions
   strike through stale items; answered questions may acquire
   new documentation, test-suggestion, or implementation items
   (mark implementation items explicitly as later-phase).

Bonus: Ctrl-F workflow — noted; from now on, whenever I draft an
ADR or answer a question, I'll prompt you explicitly: "Remember
the question-side sync: status line + Status Overview row."
Same in reverse for new questions. This adds a user manual check as well.

Todo directives
---------------

   ``.. todo::`` supports only ``:class:`` (severity styling)
   and ``:name:``. There is NO ``:title:`` option — put the
   title in the BODY as a bold first line, followed by the
   substance:

   .. code-block:: rst

      .. todo::
         :class: warning

         **Title in bold, ending with a period.** The actual
         reminder text follows, including WHEN the deferred work
         becomes safe (dependencies), not just that it exists.

   ``:class: warning`` renders amber; plain (no class) renders
   neutral. ``todo_include_todos = True`` must stay set in
   conf.py or todos build invisibly.

   The dependency-encoding convention: todos for deferred
   features name the conditions under which they become safe
   ("revisit once X and Y are both working"), so upgrades can't
   be jumped prematurely without contradicting their own
   recorded rationale.

Question Lifecycle
------------------

1. **OPEN** — New question identified
2. **ANSWERED** — Decision made, documented in ``questions.rst``
3. **IMPLEMENTED** — Coded and tested; update status

Sphinx Extensions in Use
------------------------

.. csv-table::
   :header-rows: 1

   "Extension","Purpose"
   "sphinx.ext.autodoc","Auto-generate API docs from docstrings"
   "sphinx.ext.todo","Track TODO items across docs"
   "sphinxcontrib.bibtex","Bibliography management"
   "sphinxcontrib.mermaid","Mermaid diagrams"
   "sphinx_design","Cards, badges, dropdowns, tabs"
   "sphinx_togglebutton","Collapsible content"
   "sphinx_notfound_page","Custom 404 page"
   "sphinx_copybutton","Copy buttons on code blocks"
   "myst_parser","Markdown support"

IPA Reference Data Fields
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - symbol
     - Canonical form (tie bar for affricates: t͡s)
   * - description
     - Human-readable description
   * - place / manner / voicing
     - Consonant features
   * - height / backness / roundedness
     - Vowel features
   * - unicode_points
     - Array of Unicode code points
   * - aliases
     - Informal names
   * - alternate_forms
     - Valid IPA variations (e.g., "ts" for "t͡s")
   * - rarity_tier
     - 1–5: universal to rare; 6: unattested
   * - phoible_frequency
     - Decimal 0–1, from PHOIBLE data
   * - license
     - License metadata for data source

Toctree and filename coupling
-----------------------------

   The toctree chases the file, never the reverse: when a
   mismatch produces ``toc.not_readable``, edit the toctree line
   to match the actual filename — do not rename files to match a
   toctree typo. Coupling rule: a file move or rename is ONE
   operation of THREE — rename the file, update its toctree line,
   and grep for stale ``:ref:`` labels. Renames skip step 3 at
   their peril; unlabeled breakage surfaces only as unresolved
   references later. (Grep patterns: old filename stem, old
   title phrase, old label with surrounding context.)

   Label aliases: a section may carry both a long readable label
   (``.. _UC-014_compose_candidate_syllable:``) and a short link label
   (``.. _uc014:``) stacked directly above the heading. Use the long
   form where the ref text should be self-describing, the short form
   inside dense prose. Never invent a spelling that has no label.

Full-build audits
-----------------

   Incremental Sphinx builds re-read only changed files; a build
   with no changed targets reports zero warnings regardless of the
   actual state of the docs. When auditing for warnings, force a
   full re-read:

   .. code-block:: bash

      poetry run sphinx-build -E -b html docs/source docs/build/html \
        2>&1 | grep -iE 'warning|error' | head -40

   (``-E`` discards the cached environment. The "Line block ends
   without a blank line" class of docutils warnings is invisible to
   a no-op build.)

   Audit with grep -rn 'pattern' use_cases/ (directory, not glob)
   or the traversal silently skips the level subdirectories.

RST indentation in nested lists
-------------------------------

Bullet Continuation Indentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List item continuation lines must align with the bullet marker, not the text.

* Correct

   - Item text continued
     on the next line

If you cannot confidently count the spaces, prefer one long
unwrapped line — a long line is ugly but builds; a wrong indent
is a warning.

Docutils reports it as
"Unexpected indentation" followed by "Block quote ends without a blank line."
Inline roles (``:class:``, ``:ref:``, ``:meth:``) that force awkward wraps are safest unrolled onto
one line — prose RST has no line-length limit.

Stale editor diagnostics
------------------------

   The IDE Problem panel accumulates diagnostics from every
   past state of the workspace — mid-rename, mid-config-edit —
   and does not reliably flush them. After refactor-heavy
   sessions, the build output is the only authority: restart the
   editor (or reopen affected files), rebuild, and reconcile
   against THAT list. Panel counts that exceed build warnings
   by an order of magnitude are stale, not alarming.

Stub pages over absent toctree entries
--------------------------------------

   When a page is referenced (by toctree or by use-case links)
   but not yet written, create a stub rather than omitting the
   reference. A stub is visible to humans (site navigation
   shows what isn't done) and machines (no broken refs); an
   omitted entry is invisible silence that looks like
   completeness. Stub anatomy: real title, ``:Status: Stub``
   field naming the referencing use case, and a ``.. todo::``
   (class: warning) sketching the expected content.

Theoretical Framework
-----------------------

- **Primary:** Generative Phonology (rule-based constraints)
- **Future option:** OT mode (ranked, violable constraints)
- **Warning:** Don't mix theories without explicit user notification
- **Tagging:** Constraints carry ``theory_origin`` field

See :ref:`theoretical_framework` for full explanation.

Licensing
---------

- Code: GPL-3.0-or-later
- IPA symbols: Factual (no copyright)
- PHOIBLE data: CC-BY 4.0 (attribution required)
- Font (Junicode): SIL OFL

Phases
------

- **Alpha:** Project scaffold, CI/CD, basic tooling (complete)
- **Beta:** Core engine, all MVP use cases (current)
- **Gamma:** GUI, polish, community features
- **Delta:** Advanced features (OT mode, dialects, tone/stress, export)
- **Epsilon:** Future research (morphology, syntax, sound change, ML)

Use Case Status Fields
----------------------

Every use case must include three status fields:

- ``:Doc Status:`` — Draft, Review, or Final (state of the document)
- ``:Impl Status:`` — Not Started, In Progress, or Complete (state of the code)
- ``:Phase:`` — Alpha, Beta, Gamma, Delta, or Epsilon

Use Case Extensions
-------------------

   Extensions are keyed as ``[step][letter]`` (``3a``, ``3b``) and
   MUST match the main success scenario's step numbers exactly. When
   steps are added, removed, or reordered, rewrite ALL extension keys
   in the same edit — never leave stale keys. Present extensions in
   ascending step order for readability; numbering is semantic,
   presentation is secondary. Never renumber via find-and-replace;
   rewrite the extensions section whole.

Level Assignment (Cockburn)
---------------------------

   A use case belongs at the level where its steps describe the
   user's observable transaction. Signals that content sits at the
   wrong level:

   - Mechanical substeps inside a user-goal step (PRNG seeding,
     retry counters, per-slot logic) → candidate for extraction
     to a subfunction the goal delegates to
   - More than ~7 main steps at user-goal level → check whether
     multiple intents or leaked mechanics are hiding; extract
     before flattening
   - An extension that keys to a step belonging to a different
     actor's concern → the seam is wrong

   Extraction is validated when extensions re-home cleanly along
   the proposed boundary and the extracted case gains a second
   caller. Extracted content NEVER appears in full at the caller's
   level — the caller summarizes in one step; the callee specifies.

   This is guidance, not law: level assignment is the most
   interpretive part of Cockburn's method, and Daniil has final
   judgment. Flag the tension; don't apply rules mechanically.
   When in doubt, raise it rather than split.

Use-Case Documentation Standard
===============================

:Applies to: docs/source/use_cases/**

Metadata fields
---------------

Every use case opens with this field list, in this order:

:Doc Status: Stub, Draft, Review, Complete
:Goal Level: Summary, User Goal, Subfunction
:Impl Status: Not Started, In Progress, Blocked, Done
:Phase: Alpha, Beta, Gamma, Delta, Epsilon

Rules for values:

- **Phase is the sole development-timeline vocabulary.** The
  phases document (see :ref:`phases`) is authoritative; the
  word "Milestone" does not appear in use cases or other
  specifications. A use case's Phase is the phase in which its
  implementation is *usable*, not merely started.
- Doc Status tracks the document; Impl Status tracks the code.
  A use case may be Complete (the usecase) and Not Started (the code) simultaneously.
- A -? suffix on Phase (e.g., ``Beta?``) marks an unconfirmed
  assignment; it must be resolved before the use case reaches
  Doc Status: Review.
- :ref:`blueprint` sketches out the Modules that the whole
  suite will comprise of (eventually).

Structure
---------

Sections in order, omitting any that don't apply: Goal,
Preconditions, Inputs (subfunctions only), Main Success Scenario,
Postconditions, Extensions, Frequency, Related (Calls /
Called by / Consumes / Data contracts), Variations, Notes,
Open Questions, Flow Diagram (Goal and Subfunction levels only).

Rules
-----

1. **Steps cite their warrants.** Any step implementing an ADR
   consequence or an answered question carries the reference
   inline — ``(:ref:`ADR-034`)``, ``(Q7)`` — so research and
   reasoning are traceable from the step itself, not only
   backward from the ADR. If a step exists and no warrant can
   be named, that is a documentation defect.
2. **Extension numbers match the step they branch from** and
   nest as ``Na``, ``Na1``, ``Na2``. Renumber extensions when
   steps renumber.
3. **Summary-level cases have no step lists and no extensions**
   (Cockburn); failures are owned by the included cases.
4. **Directory placement matches Goal Level.**
5. **Repository code paths appear only in Variations and
   Notes**, never in numbered steps — steps describe behavior,
   variations describe bindings. This keeps steps stable while
   implementation homes move.
6. Cross-references must resolve; the build is zero-warning
   (see RTD covenant).


Glossary Formatting
-------------------

Glossary multi-term syntax: aliases are STACKED consecutive term
lines (RST definition-list native), not comma-separated. A term
line containing commas registers as a single term whose name
contains commas — it renders (anchor = comma-stripped slug) but
no :term: reference can ever match it. Diagnostic fingerprint: a
warning says a term is missing while an anchor with its name
exists in the rendered HTML. Case-variant stacked terms may
raise duplicate-term warnings (matching is case-insensitive,
Sphinx ≥ 3.0).
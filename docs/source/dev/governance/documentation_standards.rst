.. _documentation_standards:

Documentation Standards
=======================

:date: 2026-08-24 (updated 2026-09-30)
:type: Static (Append-only without an ADR)
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
│   ├── user_goal_level/           # User-goal level cases
│   ├── subfunction_level/         # Subfunction cases
│   ├── summary_level/             # Summary level cases
│   └── possible_future_cases/     # Parked ideas
├── data_contracts/               # Data structure specifications
│   ├── index.rst
│   ├── dc_phoneme.rst
│   ├── dc_syllable_template.rst
│   ├── dc_language_definition.rst
│   ├── dc_constraints.rst
│   ├── dc_orthography_rules.rst
│   ├── dc_inventory.rst
│   ├── dc_ipa_reference.rst
│   └── dc_phoible_source.rst
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

Nested directives in containers (dropdowns, admonitions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A directive placed at column 0 inside a container (``..
dropdown::``) TERMINATES the container body — but the
container's remaining indented content does not return to
prose. It is swallowed as the directive's own content, and
everything downstream parses as directive body (table rows,
admonition text, etc.).

- Symptoms point the wrong way: docutils reports at the
  directive's line and blames COLUMN COUNT, while the
  offending "row" may be prose tens of lines later (any
  comma-containing sentence becomes a multi-column cell).
- Rule: directives nested in containers inherit the
  container's indentation (directive at container indent,
  options/rows one level deeper — e.g., dropdown body at 3,
  directive at 3, rows at 6).
- Diagnostic order when a container-nested table fails:
  inspect the directive's indentation RELATIVE TO ITS
  CONTAINER first (``sed -n 'X,Yp' file | cat -A``), not the
  table's own rows. The reported row is rarely the culprit.

Cross-Reference Conventions
---------------------------

Roles and syntax:

- Labels: ``.. _label-name:`` (lowercase, hyphenated); references
  use ``:ref:`label-name```.
- Questions: .. _qXX-topic: or ref:`QXX`
- Glossary terms: ``:term:`affricate```
- Parenthetical citations: ``:cite:p:`key```
- Textual citation: ``:cite:t:`key```, ``{see}:cite:t:`hayes2008`{p. 1166}``
- Footnotes: ``:footcite:t:``, ``:footcite:p:``

Label semantics (why refs fail silently):

- Labels are exact-match: ``ADR_037`` and ``ADR-037`` are different
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
- ADR labels are uppercase-hyphenated (``.. _ADR-037:``).

Same-commit hygiene:

- Every term must have a matching entry in
  ``glossary.rst`` committed in the same change. Write the term
  first, the referencing prose second.
- Backticks in titles are a Markdown-ism leaking into bibtex; the title should use straight quotes: The {'Whole Larynx'}
- Heading underline length must be the same number of characters as the heading itself.
- There is only an underline to headings, no overline.

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
   ``ANSWERED (date, :ref:`ADR-0XX`)`` (or a split status if only
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

Bonus: Ctrl-F workflow — noted; from now on, whenever LLM drafta an
ADR or answer a question, it prompts USER explicitly: "Remember
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

Question Entry Format
---------------------

:Applies to: ``docs/source/research/questions.rst``

Every question has TWO homes that must stay synchronized:
(1) a Status Overview table row, and (2) a detailed entry body.
Both change in the same commit.

Structure
~~~~~~~~~

Each entry follows this exact order:

.. code-block:: rst

   .. _QNN:
   .. _qNN-label-text:

   QNN: [SCOPE] Question Title
   ===========================

   :Status: OPEN | ANSWERED (date, :ref:`ADR-XXX`) | IMPLEMENTED
   :Scope: [PHONO] | [SUITE] | [ORTHO] | [MORPH] | [DOCS-WIDE]

   **Question.** One paragraph stating the problem or decision
   needed. Use imperative phrasing ("Which...?", "How should
   the pipeline handle...?").

   **Answer.** For ANSWERED questions only. One paragraph
   stating the ruling, citing the binding location
   (e.g., ":ref:`dc_ipa_reference` Implementation Bindings").
   Include the date and any key rationale.

   **Evidence.** For ANSWERED questions where empirical
   verification occurred. Include probe commands with
   ``[verified: output]`` tags, counts, and provenance notes.
   Commands should be paste-safe (no clipboard Unicode,
   ``LC_ALL=C`` where applicable).

   **Dependencies.** Bulleted list of related questions,
   ADRs, use cases, or data contracts using ``:ref:`` roles.

   **Action items.** Bulleted checkboxes (``- [ ]``) for
   follow-up work. If deferred, mark as parked/post-MVP.

Label convention
~~~~~~~~~~~~~~~~

Stack two labels above the heading:
- Short form (``.. _QNN:``) for internal references
- Long form (``.. _qNN-label-text:``) for semantic links

The short label matches the Status Overview table's Related
column (e.g., ``:ref:`Q46```). The long label allows
descriptive prose references (e.g., ``:ref:`q46-ascii-spelling-variants```).

Status Overview row
~~~~~~~~~~~~~~~~~~~

The Status Overview list-table row mirrors the entry's
metadata:

.. code-block:: rst

   * - QNN
     - Short topic description
     - STATUS (date, :ref:`ADR-XXX`)
     - Blocks / Resolved / Non-blocking
     - :ref:`ADR-YYY`, :ref:`QMM`

Rules:
- **Same-commit sync:** Changing the entry's Status requires updating the table row in the same commit.
- **Blocks field:** State whether this blocks MVP or another question. Use "Non-blocking" if open but not urgent.
- **Related column:** List ADRs and questions that are dependencies or consequences.

Example — see Q41 (pastes you shared) for a full
illustration of the dropdown-admonition style used for
OPEN/PARKED questions. The Q46 draft I provided uses the
simple prose style (better for ANSWERED rulings; dropdowns
clutter answered entries).

When to create a question
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a Q entry when:
- A binding decision is needed (not covered by an existing ADR)
- An empirical finding needs documented evidence (probe output, counts, locale lessons)
- A follow-up follow-up (F-1, F-2...) is scoped as a separate investigation

Do NOT create a Q entry for:
- TODO items that lack a decision/question shape
- Glossary terms (use glossary.rst)
- Minor clarifications that fit in a docstring or comment

Contract-consumer sweep: when a data contract introduces an optional/null
field, a nullable enum, or relaxes an invariant, grep the repo for the
field name and confirm each consumer (contract, use case, design doc)
either handles the new possibility or records an open question about it.
Silent consumers are assumed total — that assumption is the drift.

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

      poetry run sphinx-build -E -b html docs/source docs/_build/html \
        2>&1 | grep -iE 'warning|error' | head -40

   (``-E`` discards the cached environment. The "Line block ends
   without a blank line" class of docutils warnings is invisible to
   a no-op build.)

   Audit with grep -rn 'pattern' use_cases/ (directory, not glob)
   or the traversal silently skips the level subdirectories.

   Build output lives in ``docs/_build/`` (Sphinx convention,
   gitignored). ``AGENTS.md`` is a tracked file — it is the
   session-start bootstrap index.

**Design-doc amendments** preserve the original supposition.
When implementation reality contradicts a design doc's claim,
the claim is not rewritten — it's amended with a dated note
stating what changed and why, with a warrant (ADR or Q-number).
A silent rewrite is drift; an overturn without rationale is
"whatever works." Living docs (like this one) accumulate history;
they don't erase it.

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
   inline — ``(:ref:`ADR-034`)``, ``(:ref:`Q7`)`` — so research and
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

Edit-Location Conventions
-------------------------

:Applies to: all documentation edits (humans and assistants)

When suggesting or making edits, state **where** they go using these anchors:

- **Replace [section name]** — the entire section (heading and
  body) is deleted and replaced with the provided block.
- **In [section name], after the [X] paragraph/block** — insert
  the new text at that specific point; existing text stays.
- **Delete [section name]** — remove entirely.
- **Renumber** — a numbered list's items shift when items are
  added; verify numbering references elsewhere (e.g., "Field
  Checks 1–4") still match.

Always include the filename including file suffix.
If switching folders or subjects, include the file path if known.

Standard section order for data contracts (Posture B):
Overview → Information Nicknames → Field List → Field Details →
Validation Rules/Field Checks → Relations/Test Cases →
Implementation Bindings → Open Work → References.

When receiving an edit without a location anchor, ask:
"Which section, and replace or insert?"

When making an edit yourself, note in the commit/changelog which
sections changed.

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

Sentinel greps for glossary edits: glossary term lines are
INDENTED (definition-list syntax nested in the glossary tree),
so a column-0 anchor like ``grep -n '^romanization'`` never
matches — an empty result can mean "not landed" OR "landed at
indent." Match at the actual indentation instead, allowing any
leading whitespace::

   grep -nE '^[[:space:]]*romanization$' glossary.rst

(Lineage 2026-10-06: a landed glossary entry read as "not
landed" because the sentinel assumed column 0.)

Glossary Entry Format
~~~~~~~~~~~~~~~~~~~~~

:Applies to: ``docs/source/glossary.rst``

Structure
~~~~~~~~~

Multi-term entries use **stacked definition-list lines** (RST
native). Each term line is a single synonym/alias — do NOT use
commas to separate terms, as this registers as a single term
with commas in its name (broken ``:term:`` references).

.. code-block:: rst

   term name
      Definition sentence ending with a period. Further
      explanation on continuation lines aligned with the first
      word of the definition. Synonyms or aliases that render
      identically go on stacked term lines.

   alternate spelling
      (same definition block, indented continuation of the
      parent term's definition)

Example
~~~~~~~

romanization
   Writing a language in the Latin alphabet (or another
   adopted script) rather than its native script, or
   transcribing speech in practical letter-spellings rather
   than IPA. Romanized spellings differ from IPA transcriptions
   and can resemble multi-glyph IPA sequences (e.g., ``ts`` vs
   t͡s); PHOIBLE carries some source data in romanized form.

   Also called: practical orthography, transcription (context-dependent).

Rules
~~~~~

- **Definition first:** Write the term entry before referencing it elsewhere. Same-commit requirement per documentation standards.
- **One-period sentences:** Definitions should read as clean prose, not run-on chains.
- **Aliases:** Stacked term lines for common synonyms. Case variants may raise duplicate warnings (Sphinx ≥ 3.0 matching is case-insensitive).
- **Cross-links:** Use ``:term:`` roles liberally in definitions for linked glossaries. Avoid circular chains.
- **Prose-friendly:** The definition should make sense out of context when read in isolation (user-facing docs may render the glossary as a standalone page).

Diagnostic
~~~~~~~~~~

A broken reference warning says a term is missing while an
anchor with its slug exists in the HTML. Cause: the term line
contained commas or unexpected whitespace. Fix: verify the
term line has no internal commas; if the term naturally has
one, use a parenthetical instead (e.g., ``romanization (practical orthography)``).

Changelog Standards
===================

:Applies to: ``CHANGELOG.md`` (repo root)

Audience and Purpose
--------------------

The ``CHANGELOG.md`` is written for **users of LatticeLang** —
writers and linguists who run the tool — plus future
contributors (including future you) reconstructing why outputs
changed. It answers the question git history can't: *"What
changed in the tool's behavior, and what should I do about
it?"*

It is NOT a commit log. Commit messages serve developers; the
changelog serves consumers. A commit describes *what was
touched*; a changelog entry describes *what it means for
someone using the output*.

When to Update (Trigger Conditions)
-----------------------------------

Update ``CHANGELOG.md`` in the **same commit** that makes the
change — never retroactively, never batched for later.
Specifically, add an entry when a change meets ONE OR MORE of
these criteria:

1. **User-visible output change:** alters emitted data
   (e.g., ``ipa_reference.json`` contents, rank assignments,
   chart pass-list membership), validation warnings, or
   rendered text. Example: adding implosives to the chart
   (this affects downstream inventory pre-fill and export).

2. **Binding decision recorded:** a ruling that changes
   downstream behavior, even if the code hasn't changed yet.
   Example: Q46 spelling-variant ruling recorded in
   ``dc_ipa_reference.rst``.

3. **Data contract evolution:** modifying schema, field
   semantics, or vendor-pinning rules (e.g., introducing the
   ``deferred`` map in the chart file).

4. **Test count milestone:** suite size crosses a round number
   or completes a major batch (e.g., 109 tests after implosives
   batch).

Do NOT add entries for:
- Pure refactors with no behavioral change
- Typo fixes in documentation (unless they affect user understanding)
- Internal-only test hardening (new tests that don't alter behavior)
- Editor configuration, CI tweaks, .gitignore polish

Granularity
~~~~~~~~~~~

Accumulate under ``[Unreleased]`` until release time:
- **Individual story commits** (e.g., "add implosives test", "add implosives data") — keep separate bullets
- **Milestone-scale completions** (e.g., "implosives batch complete, 4/5 symbols added") — group under a parent bullet
- **Release tags** — promote ``[Unreleased]`` to a dated version heading (e.g., ``## [0.2.0] — 2026-10-06``), link to GitHub tag

Rule of thumb: if the commit message contains a colon and
three short phrases (e.g., "Add implosives: test-first,
data-entry, deferred ʛ"), that's a grouping candidate.

What to Include
---------------

Follow Keep a Changelog (https://keepachangelog.com/en/1.0.0/)
section headings, in this order:

- **Added** — new features, files, data contract elements
- **Changed** — modified behavior; state old → new where
  applicable
- **Fixed** — corrected defects; describe the symptom a user
  saw
- **Removed** — deleted features, files, deprecated data
- **Deprecated** — soon-to-be-removed items
- **Dependencies** — external data or library pins (e.g.,
  PHOIBLE DOI, version hashes)
- **Tests** — suite size at this version (running total,
  brief — the reader's regression sanity check)

Style Rules
-----------

- **Imperative mood** ("Add implosives", not "Added
  implosives..." or "Adding implosives...")
- **One bullet per discrete change**; group related
  micro-changes under one parent bullet with sub-bullets
- **Numbers are exact** (109 tests, not "~100"; 88 ASCII
  rows, not "about 90")
- **Pin versions and DOIs** where applicable (PHOIBLE hash,
  schema version)
- **Every release section ends with the test count**
- **Link each release heading to its GitHub tag** (footnote-style
  link refs at file bottom)
- **Keep an ``[Unreleased]`` section at top** collecting
  pending work; promote it to a dated version at release time

Entry Template (Unreleased)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ## [Unreleased]

   ### Added
   - Add the four attested non-pulmonic implosives (U+0253, U+0257,
     U+0284, U+0260) to the curated chart pass-list
     (data/ipa_chart.json), with an exact-group membership test.

   ### Changed
   - Institute the `deferred` map in data/ipa_chart.json; park
     the voiced uvular implosive (U+029B) — unattested voiced
     in PHOIBLE 2.0, only the voiceless variant (U+029B U+0325)
     has a features row. Promotion occurs if PHOIBLE gains a
     row (vendor-gated test guards it).
   - Record the ASCII/homoglyph spelling-variant ruling (Q46)
     in the dc_ipa_reference Implementation Bindings.

   ### Tests
   - 109 passing

Example Entry (Full Release Tag)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ## [0.2.0] — 2026-10-06

   ### Added
   - Non-pulmonic consonant batch: implosives (ɓ ɗ ʄ ɠ) to
     chart pass-list and membership tests.

   ### Changed
   - Chart file schema extended with `deferred` map for
     chart-canonical but PHOIBLE-unattested symbols.
   - ASCII/homoglyph spelling-variant ruling documented in
     IPA Reference contract.

   ### Tests
   - 109 passing

   [Full diff](https://github.com/Danweel/LatticeLang/compare/v0.1.0...v0.2.0)

Backfill Policy
~~~~~~~~~~~~~~~

If a milestone completes without a CHANGELOG entry:
- Create the entry **now**, not at the next milestone
- Date the release heading to the actual completion date
- Use the commit history to reconstruct the summary (do not invent numbers; count tests, verify hashes)
- Add a note in the commit message: "CHANGELOG backfill for v0.2.0"

This keeps the record honest without allowing indefinite
drift. Last backfill threshold: **two weeks** from commit
date — if more than 14 days pass, add a preamble warning
("Backfilled entry, completed 2026-10-06").

What to Include
---------------

Follow Keep a Changelog (https://keepachangelog.com/en/1.0.0/)
section headings, in this order:

- **Added** — new features, files, data contracts
- **Changed** — modified behavior; state old → new where applicable
- **Fixed** — corrected defects; describe the symptom a user saw
- **Removed** — deleted features, files, deprecated data
- **Dependencies** — external data or library pins (e.g., PHOIBLE DOI)
- **Tests** — suite size at this version (running total, brief)

Style Rules
-----------

- Imperative mood ("Add", not "Added... by us" or "Adding")
- One bullet per discrete change; group related micro-changes under
  one parent bullet
- Numbers are exact (71 tests, not "~70"); pin versions and DOIs
- Every release section ends with the test count — the reader's
  regression sanity check
- Link each release heading to its GitHub tag (footnote-style link
  refs at file bottom)
- Keep an ``[Unreleased]`` section at top collecting pending work;
  promote it to a dated version at release time

When Not Yet Final
------------------

Known-but-open items (assumptions pending a question, naive
implementations pending an ADR) go under ``[Unreleased]`` as
"to be" bullets — e.g., rarity thresholds pending Q36. This keeps
honest visibility without claiming shipped behavior.

.. _fixture-doctrine:

Fixture Doctrine (adopted 2026-10-01)
-------------------------------------

Fixtures are EXPORTS of real data, never invented worlds:

- Never hand-author fixture values. A fixture is generated from
  the pinned real source by a regeneration script, and the
  regeneration is verified by vendor-gated tests (verbatim-row
  equality) whenever the source is present.
- Prefer real data in tests whenever it is fast and pinned. At
  our scale (tens of thousands of rows) full-data integration
  tests cost <1s — the speed justification for miniature
  fixtures does not exist here. Fixtures earn their keep ONLY
  for portability: the vendor data now ships in the repo
  (2026-10-04 bundling decision), so vendor-gated tests run
  everywhere; committed fixtures persist for portability and
  as the delegated, regenerable layer.
- Layered authority: vendor-gated tests against full real data
  are the authority; committed fixtures are the portable layer,
  and their truth is delegated, not asserted. When a count
  appears in a fixture, it was computed from real rows or it
  doesn't exist.
- Golden numbers pinned in tests (e.g., denominator 2155)
  carry a provenance comment and a "data changed" failure
  message — a tripped pin means re-run the PROVENANCE checks,
  never edit the number.
- Fresh-clone principle: `git clone && poetry install --extras
  dev && poetry run pytest` must be green on any machine; vendor-
  gated tests skip VISIBLY (named reasons), never fail silently,
  never vanish.

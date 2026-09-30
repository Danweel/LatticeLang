.. _UC-00_design_a_phonology:
.. _uc00:

UC-00: Design a Phonology
==========================

:Doc Status: Draft
:Goal Level: Summary
:Impl Status: Not Started
:Phase: Beta


Goal
----

The conlanger takes a language idea — perhaps nothing more
than a feeling for how the language should sound — and, by
iterating, arrives at a working phonology: a phoneme inventory,
syllable templates, phonotactic constraints, and a set of
generated words that match their intention, with an optional
orthography and a durable export.

The system's role is to make the iteration loop fast and
informed: every rule remains the user's decision, while the
program supplies sensible defaults, immediate feedback, and
typological context for those decisions.

A writer or linguist constructs a complete, machine-usable
description of a language's sound system — phoneme inventory,
syllable structures, phonotactic constraints, and orthography —
held as a single :ref:`dc_language_definition`, and uses it to
generate new words in that language's sound pattern, to analyze
existing words against it, or both.

Primary actor: the conlanger or worldbuilding author.

Scope and Level
---------------

Scope: the phonology module of the LatticeLang suite.
Morphology, syntax, and diachronic simulation are future
modules (:ref:`suite_vision`) and out of scope here.

This use case collects the user-goal and
subfunction use cases below; it describes the shape of the
overall endeavor, not the mechanics of any single interaction.
Per Cockburn, it carries no step list and no extensions —
failures and branches are owned by the included (user goal) cases.

Included Cases
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Stage
     - Included use case
   * - Establish the inventory
     - :ref:`UC-01_define_phoneme_inventory`
   * - Structure the syllable
     - :ref:`UC-02_define_syllable_templates`
   * - Constrain the combinations
     - :ref:`UC-03_define_phonotactic_constraints`
   * - Generate and evaluate
     - :ref:`UC-04_generate_words`
   * - Romanize
     - :ref:`UC-11_define_orthography_mapping`
   * - Persist across sessions
     - :ref:`uc005`

Adjacent (not included): :ref:`UC-07_export_to_latex`
(the deliverable, not the design activity), :ref:`uc009`
(an entry path, see Variations), :ref:`UC-08_work_in_a_gui_with_live_preview`
(the GUI embodiment of this entire journey).

Preconditions
-------------

- LatticeLang is installed and runnable.
- No project file is required — designing from a blank
  inventory is the common starting path; an existing
  :ref:`dc_language_definition` may also be loaded (:ref:`uc005`)
  and modified.

Scenario Sketch
---------------

The conlanger enters from one of two directions.

**Scratch-first:** starting from an idea of the sound system,
they define a phoneme inventory (:ref:`UC-01_define_phoneme_inventory`),
taking advantage of typological defaults and rarity warnings
while retaining full freedom to defy them. They sketch syllable
templates (:ref:`UC-02_define_syllable_templates`) and accept
or override the universal defaults — notably the Sonority
Sequencing Principle, visible and on by default (:ref:`ADR-038`) —
through the constraint editor (:ref:`UC-03_define_phonotactic_constraints`).
They generate words (:ref:`UC-04_generate_words`) and judge the
output against their intention, adjusting and regenerating until
the result sounds like the language in their head.

**Corpus-first:** starting from romanized sample words, they
import them (:ref:`uc009`), segment the input (:ref:`uc012`),
and allow the program to propose an inventory and constraints
from the sample, correcting its proposals by hand. (Corpus-first
constraint inference is post-MVP — see :ref:`q41-corpus-inference` —
but the entry path and data flow are designed for it.)

Either way, the loop is the same: **decide, generate, evaluate,
adjust.** The user may work the stages in any order, revisit
earlier ones at any time, and rely on the program to flag —
never silently rewrite — the consequences of changes
("changes propagate by notification, not auto-correction").
An orthography may be layered on (:ref:`UC-11_define_orthography_mapping`)
once the phonology stabilizes, and the whole phonology saves
and reloads intact (:ref:`uc005`).

Main Success Scenario
---------------------

*(Summary level — no step list; the workflow narrative.
Failures are owned by the included cases.)*

The author defines the language's phoneme inventory
(:ref:`uc01`), drawing proposed features, sonority ranks,
and attestation-based frequencies from the IPA reference
table (:ref:`dc_ipa_reference`) and confirming or overriding
each proposal. Shaping syllable structure follows
(:ref:`uc02`): onset/nucleus/coda slot patterns are defined
with category eligibility rules, and phonotactic constraints
(:ref:`uc03`) restrict the legal combinations — from
defaults like sonority sequencing to bespoke prohibitions.

From here the path forks, and the summary deliberately spans
both directions. **Forward** (generation): the author requests
words (:ref:`uc04`), which are composed per template
(:ref:`uc014`), slot by slot (:ref:`uc19`), checked against
every enabled constraint, and reported with a survival funnel
(:ref:`ADR-046`) when the constraints starve the pipeline.
Generated or hand-authored words can be romanized for display
(:ref:`uc015`) and the whole system exported as reference
charts and tables (:ref:`uc07`). **Reverse** (analysis): the
author imports romanized text (:ref:`uc009`), which is
segmented to IPA (:ref:`uc012`) — the confirmed inventory,
not segmenter guesswork, disambiguating diphthong, hiatus, and
glide readings — and merged into the inventory with explicit
collision semantics (:ref:`ADR-051`).

Throughout, the project serializes and reloads without loss
(:ref:`uc005`), and the author can validate the current
definition at any time (:ref:`uc013`). Orthography mapping
(:ref:`uc11`) may be defined at any point in the authoring
sequence; it is required for import and export work but not
for pure generation.

Success Guarantee (Postconditions)
----------------------------------

At any stopping point, the phonology is internally consistent
(validation passes, :ref:`uc013`), persisted to the project
file, and exportable (:ref:`UC-07_export_to_latex`). The design
judgment — "does this match my intention?" — belongs to the
user alone; the system guarantees only that what they built
is coherent and recoverable.

- The authored language is persisted as a complete or partial
  :ref:`dc_language_definition` that round-trips losslessly
  (:ref:`uc005`).
- Generation from the definition is reproducible: the same
  seed and generator version produce the same words
  (:ref:`ADR-049`).
- The definition is validatable against its own constraints
  (:ref:`uc013`) with full per-constraint diagnostics
  (:ref:`ADR-046`).

Variations
----------

* **GUI vs. scriptable session.** The journey above is
  tool-agnostic; (:ref:`UC-08_work_in_a_gui_with_live_preview`)
  is its GUI embodiment. A scripted/CLI path exercises the
  same engine without the live preview.

* **Novice vs. expert pacing.** Novices lean on defaults,
  rarity tiers, and pedagogical tooltips; experts start from
  blank slates. The pedagogy layer scales without forking
  the workflow.

- **Forward-only author:** pure conlanging with no corpus —
  import (UC-009) and segmentation (UC-012) are never invoked.

- **Reverse-only analyst:** a corpus is imported and validated
  against constraints; generation is never requested. The
  definition is an analytic record, not a generative engine
  configuration.

- **Bootstrapping:** a corpus import seeds an initial
  inventory, which the author then curates and extends before
  generating — the blended path the merge semantics
  (:ref:`ADR-051`) exist to serve.

Frequency
---------

Authoring spans sessions — days to months for a serious
project. Serialization and validation occur many times per
session; import and export are episodic; generation is
on-demand.

Related
-------

Included cases (user goals, the workflow's actual steps):

.. list-table::
   :header-rows: 1
   :widths: 20 40 20

   * - Case
     - Role in this summary
     - Level

   * - :ref:`uc01`
     - Define the phoneme inventory
     - User Goal
   * - :ref:`uc02`
     - Define syllable templates
     - User Goal
   * - :ref:`uc03`
     - Define phonotactic constraints
     - User Goal
   * - :ref:`uc04`
     - Generate words (forward pipeline)
     - User Goal
   * - :ref:`uc07`
     - Export reference charts
     - User Goal
   * - :ref:`uc08`
     - Preview/inspect results *(see Notes — second summary)*
     - Summary
   * - :ref:`uc009`
     - Import romanized corpus (reverse pipeline)
     - User Goal
   * - :ref:`uc11`
     - Define orthography mapping
     - User Goal
   * - :ref:`uc012`
     - Segment IPA input
     - Subfunction
   * - :ref:`uc013`
     - Validate definition against constraints
     - User Goal
   * - :ref:`uc015`
     - Apply orthography rules
     - User Goal

Consumes: :ref:`dc_language_definition` (the envelope and all
child contracts). Delegates failure handling entirely to the
included cases and their subfunctions (:ref:`uc04`,
:ref:`uc005`, :ref:`uc014`).


Notes
-----

The workflow shape — inventory, then syllable structure,
then phonotactics, then word generation — follows conlanging
practice as codified in the Language Construction Kit
:cite:p:`rosenfelder2010`. The *mechanics* behind each stage
are grounded in the theoretical literature; see
:ref:`theoretical_framework` and the module documentation.

This use case deliberately contains no extensions: at summary
level, Cockburn prescribes collecting goals rather than
enumerating failure modes, which are owned by the included
user-goal and subfunction cases.

Completion is judged by the user's satisfaction, not by a
system criterion — consistent with the project philosophy
that the creative decisions remain with the user.

- **UC-016 (tone system)** is intentionally outside this
  summary: per :ref:`ADR-048`, tone features ride in the data
  now but are consumed by no pipeline until the tone stage
  exists. This summary describes the Beta phonology module
  only.
- **Statistical inference stays out** (:ref:`ADR-045`): all
  corpus interpretation routes through user-confirmed review
  (:ref:`uc009`'s flow), never autonomous learning.
- The Included Cases table double-checks against
  ``use_cases/index.rst`` before this document reaches
  Doc Status: Review — levels and IDs here are drafted from
  conversation references and must be reconciled against the
  authoritative index.

Open Questions
--------------

None — summaries inherit open questions from their included
cases rather than owning any.
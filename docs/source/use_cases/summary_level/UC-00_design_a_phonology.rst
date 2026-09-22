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

Scope and Level
---------------

Summary level. This use case collects the user-goal and
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

Success Guarantee
-----------------

At any stopping point, the phonology is internally consistent
(validation passes, :ref:`uc013`), persisted to the project
file, and exportable (:ref:`UC-07_export_to_latex`). The design
judgment — "does this match my intention?" — belongs to the
user alone; the system guarantees only that what they built
is coherent and recoverable.

Variations
----------

* **GUI vs. scriptable session.** The journey above is
  tool-agnostic; UC-08 (:ref:`UC-08_work_in_a_gui_with_live_preview`)
  is its GUI embodiment. A scripted/CLI path exercises the
  same engine without the live preview.

* **Novice vs. expert pacing.** Novices lean on defaults,
  rarity tiers, and pedagogical tooltips; experts start from
  blank slates. The pedagogy layer scales without forking
  the workflow.

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
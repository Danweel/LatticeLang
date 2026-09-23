.. _index_use_cases:

Use Case Index
==============

Design Considerations for Contributors
--------------------------------------

Use cases describe **behavior** (functional decomposition): what happens,
in what order, from the actor's perspective. Object-oriented design
describes **structure**: what entities exist, what they know, what they
do. These are complementary, not competing.

The common mistake (especially for developers who learned only OO) is
to jump from "the system validates a syllable" directly to "I need a
Validator class" without considering whether validation is better
expressed as:

- A method on ``Syllable`` (``syllable.is_valid(constraints)``)
- A method on ``Constraint`` (``constraint.check(syllable)``)
- A standalone function (``validate_syllable(syllable, constraints)``)
- An internal method of ``WordGenerator`` (``self._validate(syllable)``)

Use cases are deliberately OO-agnostic. The decision of which object
owns which behavior is a design choice informed by cohesion, coupling,
and the single responsibility principle — not dictated by the use case.
See Wirfs-Brock (2003) and Larman (2004) for guidance on this
transition.

Within LatticeLang, we use a **mixed paradigm**: the layered architecture
(core → orthography → ui) is functionally decomposed (each layer
transforms data and passes it upward), while the data model within each
layer is object-oriented (Phoneme, Syllable, Constraint are entities
with state). The generator is an object that contains a stateful
functional pipeline. This is intentional, not accidental.

See :ref:`questions`

Actors
------

LatticeLang has one primary actor: the **Conlanger**. Sub-types
include:

- **Author:** Using the tool for fiction/worldbuilding. May prioritize
  aesthetics over linguistic accuracy.
- **Student:** Learning phonology through experimentation. Benefits
  from pedagogical guidance (post-MVP).
- **Script:** Automated generation via CLI for batch processing.

All sub-types share the same interactions; the distinction affects
interface design and documentation tone, not use case structure.

.. toctree::
   :maxdepth: 2
   :caption: Summary Level

   summary_level/UC-00_design_a_phonology
   summary_level/UC-08_work_in_a_gui_with_live_preview

.. toctree::
   :maxdepth: 2
   :caption: User Goal Level

   user_goal_level/UC-01_define_phoneme_inventory
   user_goal_level/UC-02_define_syllable_templates
   user_goal_level/UC-03_define_phonotactic_constraints
   user_goal_level/UC-04_generate_words
   user_goal_level/UC-07_export_to_latex
   user_goal_level/UC-11_define_orthography_mapping


.. toctree::
   :maxdepth: 2
   :caption: Subfunction Level


   subfunction_level/UC-005_serialize_deserialize_LanguageDefinition
   subfunction_level/UC-009_import_words
   subfunction_level/UC-012_segment_ipa_input
   subfunction_level/UC-013_validate_against_constraints
   subfunction_level/UC-014_compose_a_candidate_syllable
   subfunction_level/UC-015_apply_orthography_rules
   subfunction_level/UC-016_preview_regeneration
   subfunction_level/UC-017_select_a_phoneme_for_a_slot

.. toctree::
   :maxdepth: 2
   :caption: Possible Future Cases


   possible_future_cases/UC-06_snapshot_comparison_UX
   possible_future_cases/UC-10_compare_sample_vs_generated_output
   possible_future_cases/UC-18_design_a_tone_system
   possible_future_cases/UC-19_inspect_a_syllable
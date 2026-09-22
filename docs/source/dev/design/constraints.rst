.. _constraints:

Constraint Types Overview
=========================

:date: 2026-08-24
:type: Living (Incremental)
:audience: Developers and contributors
:purpose: What specific constraint types exist?

This table catalogues all phonotactic constraint types in LatticeLang, organized
by implementation phase and theoretical classification.

.. contents::
   :local:
   :depth: 2

MVP Constraints
---------------

Nine constraint types are planned for the MVP. All operate within a
single syllable boundary.

.. csv-table::
   :header-rows: 1
   :widths: 25 15 20 40

   "Constraint","Category","Domain","Description"
   "sonority_sequencing","Markedness","Within syllable","Enforces Sonority Sequencing Principle: sonority rises in onset, falls in coda"
   "allow_s_appendix","Exception","Within syllable","Permits /s/+C clusters that violate SSP (e.g., /sp/, /st/)"
   "no_geminate_obstruents","Markedness","Within syllable","Prohibits identical adjacent obstruents"
   "max_onset_length","Structural","Within syllable","Upper bound on consonant count in onset"
   "max_coda_length","Structural","Within syllable","Upper bound on consonant count in coda"
   "position_restrictions","Positional","Within syllable","Forbidden phonemes per position (onset/coda/nucleus)"
   "ocp","Markedness","Within syllable","Obligatory Contour Principle: no adjacent segments sharing specified feature (place, voicing, etc.)"
   "harmony","Harmonic","Within syllable (MVP only)","Features must agree across adjacent segments; cross-syllable deferred"
   "prohibited_clusters","Concrete","Any (configurable)","Explicit list of banned consonant sequences"

Post-MVP Constraints
--------------------

Ten additional constraint types are planned for post-MVP phases.
Dependencies and theoretical basis are noted for each.

.. csv-table::
   :header-rows: 1
   :widths: 25 25 15 35

   "Constraint","Dependency","Status","Notes"
   "cross_syllable_harmony","Word-level context","Post-MVP","Interface supports it; generator loop needs modification"
   "stress_assignment","Moras, foot structure","Post-MVP","Depends on moraic syllable weight calculation"
   "tone_assignment","Tone-bearing units","Post-MVP","Needs dedicated tone module"
   "alignment","Morpheme boundaries","Post-MVP","Align morpheme edges with syllable or prosodic edges"
   "faithfulness (MAX-IO, DEP-IO)","Input-output comparison","Post-MVP","OT-style; penalizes deletion or insertion relative to input"
   "morpheme_structure","Root/affix distinction","Post-MVP","Constraints specific to morpheme type"
   "gradient_probabilistic","Statistical modeling","Post-MVP","Non-binary violations; probabilistic likelihood of patterns"
   "dialectal_constraints","Multiple dialects","Research Q2","Different constraint sets per dialect variant"
   "allophonic_rules","Context-sensitive realization","Research Q2","Context-dependent phoneme realization (e.g., nasal assimilation)"
   "foot_structure","Prosodic hierarchy","Post-MVP","Hierarchical syllable grouping for stress assignment"

Theoretical Classification
--------------------------

.. csv-table::
   :header-rows: 1
   :widths: 30 50 20

   "Theory","Constraint Families","Our Use"
   "Generative Phonology","Ordered rules, transformations","**Primary (MVP)**"
   "Optimality Theory","Markedness + Faithfulness (ranked, violable)","Post-MVP option"
   "Autosegmental Phonology","Tiers, feature spreading","Partially (harmony)"
   "Feature Geometry","Hierarchical feature trees, natural classes","OCP uses features"
   "Natural Phonology","Articulatory/perceptual biases","Not implemented"

See :ref:`theoretical_framework` for detailed explanation of each framework.

See Also
--------

:ref:`uc03`
:ref:`dc_constraints`
:ref:`theoretical_framework`
:ref:`questions`
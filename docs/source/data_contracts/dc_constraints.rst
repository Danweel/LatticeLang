.. _dc_constraints:

Constraint Data Contract
========================

:data structure: Constraint
:owner: Phonology Tool
:created by: UC-03 (Define Constraints); consumed by
   UC-005 (Serialize/Deserialize), UC-013 (Validate Against
   Constraints), UC-04 (Generation Loop)
:status: Draft — nine types finalized, ADR-046 diagnostics pending

.. note::
   This contract was reviewed during the 2026-09-16 use-case
   and spec-completeness audit. Key design decisions:
   :ref:`adr-047` (logical schema vs. adapters),
   :ref:`adr-048` (tone as separate stage),
   :ref:`adr-049` (coordinate-addressed random streams),
   :ref:`adr-050` (qualitative ambiguity tiers).

   Correction 2026-10-31: that review also introduced defects,
   since found in systemized review rotation and corrected in
   place — the MVP catalog had been silently swapped (restored
   to :ref:`ADR-037`'s frozen nine below) and a ``params``
   field-name stray (normalized to ``parameters``). The original
   note above is kept unchanged for the record; see the realignment
   note in Constraint Types (MVP Catalog) for the full account.

Overview
--------

Constraints are phonotactic rules that restrict which combinations
of phonemes are permissible in a syllable. The constraint system
is extensible — nine catalog types are frozen for MVP (:ref:`ADR-037`),
and new types slot in without refactoring the pipeline (protected
by the ``type`` dispatch mechanism).

This contract defines the **logical schema only**. Physical
persistence is an adapter at the boundary (:ref:`ADR-047`);
constraint validators are core logic, not utilities.

.. _constraint-types-overview:

Constraint Types (MVP Catalog)
------------------------------

The nine frozen MVP types (:ref:`ADR-037`):

#. ``sonority_sequencing`` — Enforces the Sonority Sequencing
   Principle within onset and coda (:ref:`adr-038`); default on,
   visible.
#. ``allow_s_appendix`` — Permits /s/+C onset clusters that
   violate SSP (e.g., /sp/, /st/).
#. ``no_geminate_obstruents`` — Adjacent identical obstruents
   forbidden (domain fixed to ``word``: geminates arise across
   the coda-onset junction, Q35).
#. ``max_onset_length`` — Upper bound on consonant count in
   onset (structural cap).
#. ``max_coda_length`` — Upper bound on consonant count in
   coda (structural cap).
#. ``position_restrictions`` — Forbidden phonemes per position
   (onset/coda/nucleus, plus ``word_initial``/``word_final``
   edge keys, Q37).
#. ``ocp`` — Obligatory Contour Principle: no adjacent
   segments sharing a designated feature.
#. ``harmony`` — Feature agreement within the syllable (MVP
   scope, Q34; parameterized per Q42).
#. ``prohibited_clusters`` — Explicit banned sequences (domain
   defaults to ``syllable``, configurable per Q35).

Realigned to :ref:`ADR-037` 2026-10-31. The 2026-09-16
audit-era draft had silently replaced ``allow_s_appendix``,
``max_onset_length``, and ``max_coda_length`` with
``nucleus_requirements``, ``margin_requirements``, and
``tone_assignment`` — without the superseding ADR that
ADR-037 requires for any catalog change, and with
``tone_assignment`` already among its ten reserved post-MVP
types. The variant names appeared nowhere else in the docs
(sweep, 2026-10-31). Nucleus/margin requirements remain
available through ADR-037's supersession protocol if they
earn a place.

New constraint types are added by defining a new ``type``
identifier and implementing a validator handler (extensibility
protocol per :ref:`ADR-037`).

Field List
----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 10 55

   * - Field
     - Type
     - Required
     - Description
   * - ``type``
     - string
     - Yes
     - Constraint type identifier (catalog strings above).
   * - ``parameters``
     - object
     - Yes
     - Type-specific parameters (per ``parameters`` schema below).
   * - ``domain``
     - string
     - Yes
     - Evaluation scope: ``syllable`` | ``word``. Defaults
       ``syllable``; fixed ``word`` for
       ``no_geminate_obstruents``; configurable for
       ``prohibited_clusters`` (:ref:`q35`).
   * - ``enabled``
     - boolean
     - Yes
     - If false, constraint is excluded from reports
       (:ref:`uc013` SKIPPED semantics).

Parameters Schema (Type-Specific)
---------------------------------

``parameters.feature``
   Controlled-vocabulary feature name. Used by ``harmony``
   (single designated feature per instance, Q42) and ``ocp``
   (the shared feature triggering violation). Validated
   against the pinned PHOIBLE 2.0 feature vocabulary
   (:ref:`adr-033`).

``parameters.targets``
   ``harmony`` only: list of participating category names
   (per Q42; phonemes in absent categories are neutral).

``parameters.forbidden_{position}``
   ``position_restrictions`` only: lists of IPA symbols,
   keyed by ``onset``, ``coda``, ``word_initial``,
   ``word_final`` (edge keys per Q37).

``parameters.max_onset_length`` / ``parameters.max_coda_length``
   Integer upper bound on cluster size (e.g., 3). Conflicting
   pairs (e.g., ``max_onset_length=2`` vs. ``allow_s_appendix``
   implying /spl/) trigger the UC-03 step-4 conflict check.

``parameters.allow_s_appendix``
   List of phonemes permitted to follow /s/ (e.g.,
   ``["p", "t", "k", "m", "n", "l", "ɹ", "w", "j"]``, UC-03).

``parameters.clusters``
   ``prohibited_clusters`` only: list of forbidden sequences
   (e.g., ``[["s", "t"], ["l", "n"]]``, UC-03).

Validation Result Schema
------------------------

Validation output (not constraint storage; cross-referenced here
because UC-03 consumers see it). Per-constraint status is
four-valued: PASSED / FAILED / SKIPPED / ERROR
(:ref:`uc013` audit finding #8):

.. code-block:: json

   {
     "overall": false,
     "results": [
       {
         "constraint_type": "sonority_sequencing",
         "status": "FAILED",
         "reason": "sonority_sequencing (default): /tk/ in onset"
       },
       {
         "constraint_type": "harmony",
         "status": "SKIPPED",
         "reason": "no word context available"
       },
       {
         "constraint_type": "prohibited_clusters",
         "status": "ERROR",
         "reason": "configuration malformed: unknown feature"
       }
     ],
     "tallies": {
       "PASSED": 5,
       "FAILED": 2,
       "SKIPPED": 1,
       "ERROR": 0
     }
   }

Per :ref:`adr-046`: tallies and survival funnel are owned by
the generation run record, not by stored constraints.

Override Semantics
------------------

User overrides of constraint warnings (UC-03 extension 3b3)
are persisted as ``override_acknowledged: true`` on the
constraint instance. The *event* of overriding (GUI toast,
CLI line) is reported through the active interface and is
not persisted (:ref:`adr-047` boundary rule).

Harmony: Implementation Boundary
--------------------------------

MVP scope: within-syllable harmony only (e.g., prohibiting
nasal-obstruent adjacency within onset/coda). The interface
accepts a ``word_context`` parameter (None by default) so
adding cross-syllable harmony later changes the
implementation but not the method signature.

Post-MVP scope: full cross-syllable harmony (Turkish-style
vowel harmony, Guaraní-style nasal spread) requires the
generator to pass word-level context to the validator.
The generation loop may need backtracking — the risk
remains documented.

Relation to Tone
----------------

The ``tone_assignment`` constraint type is among the ten
post-MVP types RESERVED by :ref:`ADR-037` (names must not be
displaced). Tone is configured in a future tone stage
(:ref:`ADR-048`) and enforced by this constraint — the division
of labor is architectural, not temporal.

Implementation Bindings
-----------------------

Planned homes (none implemented as of 2026-10-31; verified —
module absent, no references, no preset file. Semantic rules
above are stable and unaffected):

- ``latticelang.core.constraints`` — ``Constraint`` class,
  per-type handlers, ``TemplateValidator``
- Exceptions: ``ConstraintValidationError``
- Preset example: ``english_ga.json`` (constraint set)

Open Work
---------

- ADR-046's funnel-report schema fields ride with the
  constraints contract finalization.
- Cross-syllable harmony implementation depth (backtracking
  vs. approximation) awaits Q41 corpus inference design.

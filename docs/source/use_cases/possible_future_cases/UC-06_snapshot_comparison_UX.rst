.. _UC-06_snapshot_comparison_ux:
.. _uc06:

Snapshot Comparison UX
======================

:Doc Status: Future / possible-future-cases
:Goal Level: User Goal
:Impl Status: Not started
:Phase: Gamma

Migrated:

**4a:** User wants to compare output before and after a change.
  - System maintains a "previous" snapshot of the word list.
  - User can toggle between current and previous output.
  - Diff highlighting shows added/removed words.
  - Preview regeneration is ephemeral — no seed is recorded
    or exposed; committed generation (:ref:`uc04`) records seeds. See :ref:`q7`.
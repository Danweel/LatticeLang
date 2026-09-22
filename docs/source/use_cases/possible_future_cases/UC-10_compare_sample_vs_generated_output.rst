.. _UC-10_compare_sample_vs_generated_output:
.. _uc10:

UC-10: Compare Sample vs. Generated Output
===========================================

:Doc Status: Parked — see Notes
:Goal Level: User goal
:Impl Status: Not Started
:Phase: Deferred (Delta or later; no commitment)

Goal
----
Let a user who imported real words (:ref:`uc009`) evaluate how
well generated words (:ref:`uc04`) resemble their source material
— the comparative judgment step between "I taught the tool my
sample" and "does the output feel like the same language?"

Notes
-----
**Why this is parked (write-up of the 2026-09-09 disposition):**

Its import-and-infer half was absorbed by the reverse pipeline
(UC-009 + Q41 corpus inference + Q7 frequency calibration): the
tool already extracts inventory, templates, and frequency weights
from imported samples. What remains parked is the
compare-and-judge half — no current use case covers the user
eyeballing (or the tool measuring) resemblance between generated
output and source material.

Honest reason for deferral: until frequency calibration (Q7) and
corpus inference (Q41) are implemented and exercised, there is
nothing meaningful to compare against — any comparison UI would
be judging parameters the tool does not yet compute. MVP
generation validates against *rules*; resemblance is a property
of *statistics*, which arrive later.

Natural evolution, when unparked: manual side-by-side listing
(Phase Delta), then statistical comparison of phoneme/cluster
distributions between sample and output. Depends on Q7/Q41
implementations existing first.

**Label note:** this case stays registered (``_uc10``) and in the
toctree under possible_future_cases so the number is not silently
reused. Renamed file from ``..._vs_generated_ouput.rst`` (typo)
at the same time as this write-up.
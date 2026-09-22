.. _UC-004_select_a_phoneme_for_a_slot:
.. _uc004:

UC-004: Select a Phoneme for a Slot
====================================

:Doc Status: Draft
:Goal Level: Subfunction
:Impl Status: Not Started
:Phase: Beta

Main Success Scenario
---------------------

1. Caller supplies the slot, template constraints, and inventory
   → system assembles the eligible set (category + domain rules,
   ADR-034 / ADR-039)

2. System normalizes frequency weights per-slot over the eligible
   set — ratios only, never persisted (Q7)

3. System derives a deterministic stream from the project seed,
   word position, and slot position (ADR-044)

4. System samples a phoneme with probability proportional to its
   normalized weight → returns the selection

Extensions
----------

* **1a:** Eligible set empty → :class:`GenerationError` with slot




Related
-------


Called by both UC-04 (generation loop) and UC-014 (compose candidate syllable):
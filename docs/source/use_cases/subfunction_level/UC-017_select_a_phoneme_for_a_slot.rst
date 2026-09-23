.. _UC-017_select_a_phoneme_for_a_slot:
.. _uc017:

UC-017: Select a Phoneme for a Slot
====================================

:Doc Status: Draft
:Goal Level: Subfunction
:Impl Status: Not Started
:Phase: Beta

Main Success Scenario
---------------------

1. Caller supplies the slot, template constraints, and
   inventory → system assembles the eligible set:
   category-admitted phonemes (per the slot's
   ``allowed_categories``, :ref:`ADR-034`), intersected with
   the slot's explicit ``allowed_phonemes`` list if present
   (dc_syllable_template eligibility rule 4), filtered by
   domain rules (:ref:`ADR-039`)

2. System normalizes frequency weights over the eligible set
   — ratios only, computed at selection time, never persisted
   (Q7; all-default inventories yield a uniform distribution)

3. System derives a deterministic stream address from the
   project seed, word position, slot domain, and draw index
   (:ref:`adr-049`) — domain ``slot_fill``; the draw index
   advances on retry so failed attempts consume fresh
   coordinates rather than resampling the same phoneme

4. System samples a phoneme with probability proportional to
   its normalized weight → returns the selection to the
   caller

Extensions
----------

* **1a.** Eligible set empty (category populated in the
  inventory but wholly filtered out by ``allowed_phonemes``,
  or vice versa) → :class:`GenerationError` naming the slot,
  the template, and the emptying cause; the failure surfaces
  in the run's survival funnel (:ref:`adr-046`) so the
  starving configuration is diagnosable rather than manifest
  as mysterious silence

* **1b.** (Save-time guard, not runtime): the intersection
  described in step 1 yielding an empty set is a validation
  error at save (UC-02/UC-013) — reaching 1a at generation
  time means the definition changed after validation and is
  itself a bug report

Related
-------

Called by both UC-04 (generation loop) and UC-014 (compose
candidate syllable). Consumes: :ref:`dc_phoneme` (category,
``syllabic`` flag, ``frequency``), :ref:`dc_syllable_template`
(slot definitions, eligibility rules 1–4). Gossip with
:ref:`adr-049` on one point: this case owns only the single
draw — retry loops, attempt limits, and funnel reporting
belong to the callers.

Notes
-----

- **Scope boundary:** this case returns one selection. It does
  not evaluate constraints — the constraint gauntlet runs at
  syllable assembly (UC-014) or word level (UC-04).
- **Tone carve-out (:ref:`adr-048`):** tone features riding on
  candidate phonemes are carried but ignored here; nothing
  downstream of slot filling consumes them until the tone
  stage exists.
- **Custom phonemes:** eligible under the same rules as all
  categories (``custom`` in ``allowed_categories``, checked by
  the ``syllabic`` flag per ADR-034/033) — no special path.
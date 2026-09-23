.. _UC-014_compose_candidate_syllable:
.. _uc014:

UC-014: Compose a Candidate Syllable
=====================================

:Goal Level: Subfunction
:Doc Status: Draft
:Impl Status: Not Started
:Phase: Beta

Goal
----
Produce one candidate syllable that satisfies the selected
template's structure and all syllable-domain constraints, using
rejection sampling with bounded attempts. Called repeatedly by
:ref:`uc04` (word composition) and usable standalone (single-syllable
testing, live preview diagnostics).

Preconditions
-------------
- :ref:`uc01` complete — inventory with features (:ref:`ADR-032`/:ref:`ADR-033`)
  and sonority ranks
- :ref:`uc02` complete — at least one template exists (standalone
  use may pass a template directly)
- :ref:`uc03` constraints loaded (default SSP per :ref:`ADR-038`)

Main Success Scenario
---------------------

1. System selects a syllable template at random (uniform across
   defined templates)

2. For each slot in the selected template, the system delegates to :ref:`uc017`, which derives a per-slot deterministic stream (ADR-044).

3. System removes phonemes disqualified by ``position_restrictions``
   constraints from the eligible set

4. System selects one phoneme from the eligible set. System obtains the slot's
   phoneme via :ref:`uc017`, which applies per-slot frequency weighting (:ref:`Q7`);
   normalization is per-slot, never persisted (see :ref:`uc017`).

5. System assembles the selected phonemes into a candidate
   :class:`~latticelang.core.syllable.Syllable`

6. System validates the candidate against active constraints —
   delegates to :ref:`uc013`, passing ``word_context`` assembled
   from the word-so-far (preceding coda; empty at word start).
   Syllable-domain constraints evaluate in isolation; word-domain
   constraints report SKIPPED when context is unavailable (:ref:`Q37`, :ref:`adr-039`).

7. If validation passes, the syllable is returned to the caller;
   otherwise steps 1–6 repeat (up to 100 attempts per syllable)

Extensions
----------

**2a:** No phonemes eligible for a slot (empty inventory
  category, or all removed by restrictions)
  - 2a1: System raises :class:`~latticelang.core.generator.GenerationError`
  - 2a2: Error: "No phonemes available for [position] slot in template [name] — add phonemes to your inventory or relax restrictions"
  - 2a3: Caller is directed to :ref:`uc01` or :ref:`uc03`

**7a:** 100 attempts exhausted without a valid syllable
  - 7a1: System skips this template
  - 7a2: System reports: "Template [name] produced too many invalid syllables — consider relaxing constraints"
  - 7a3: If all templates are exhausted, system raises :class:`~latticelang.core.generator.NoValidTemplateError`
  - 7a4: Error lists which constraints reject candidates, distinguishing PASSED/FAILED/SKIPPED/ERROR
  - 7a5: Caller is directed to :ref:`uc03`

Related
-------

**Called by:**
- :ref:`uc04` — Generate Words (per word, until syllable count met)
- :ref:`uc08` — Work in GUI with Live Preview (single-syllable diagnostics; anticipated caller)

**Delegates to:**
- :ref:`uc013` — Validate Against Constraints (step 6)

Notes
-----
The 100-attempt bound and the retry policy live HERE, not in the
caller, so the policy has exactly one home. Callers own their own
retry budgets above this level (:ref:`uc04`'s word-sweep and duplicate
limits are separate).

SKIPPED word-domain results from :ref:`uc013` are provisional —
the calling use case (:ref:`uc04` step 3) owns confirming them at
word-completion (Q37). This subfunction never reports a word
valid; only syllables.

.. todo::
   :class: warning

   **Anticipated callers.** :ref:`uc08` (live preview) is an anticipated
   second caller for single-syllable composition. When :ref:`uc08` is
   audited, verify its needs match this contract rather than
   bypassing it.
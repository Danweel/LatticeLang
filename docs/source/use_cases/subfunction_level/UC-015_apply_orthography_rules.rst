.. _UC-015_apply_orthography_rules:
.. _uc015:

UC-015: Apply Orthography Rules
===============================

:Goal Level: Subfunction
:Doc Status: Draft
:Impl Status: Not Started
:Phase: Beta

Goal
----
Render one word (or word list) from IPA into the project's
romanization by applying its orthography rules — the forward
direction of the mapping defined in :ref:`uc11`. Called by UC-04
for every generated word, and available standalone (re-romanize
an existing list after rules change).

Preconditions
-------------
- A word or word list in IPA exists (typically :ref:`uc04`
  output)
- The project's orthography rules are loaded if defined
  (``dc_orthography_rules``); their absence is a handled case,
  not an error

Main Success Scenario
---------------------

1. System loads the project's orthography rules (may be empty)

2. For each IPA word, system scans segments left-to-right,
   matching the longest rule whose phoneme sequence matches at
   the current position (segment-level mapping; see Notes)

3. System substitutes each matched sequence with its grapheme
   string; unmatched phonemes pass through as their IPA
   characters

4. System returns the romanized word list paired with the
   originals

Extensions
----------

* **2a:** Project defines no orthography rules
  - 2a1: Romanization equals the IPA string
  - 2a2: System attaches a note: "No orthography rules defined —
  showing IPA. Define a mapping." See :ref:`uc11`

* **3a:** A phoneme has no mapping rule
  - 3a1: The phoneme passes through as its IPA character
  - 3a2: The word is flagged; the summary reports: "[N] unmapped
  phonemes romanized as IPA — see :ref:`uc11` to map them"
  - Never raises: partial coverage is an expected state while a
  user builds up their rules

Related
-------

**Called by:**
- :ref:`uc04` — Generate Words (step 6, per word)
- :ref:`uc08` — Work in GUI with Live Preview (anticipated; re-romanize on rule change, debounced with generation)

**Inverse of:**
- :ref:`uc009` — Import Words (parses romanized text to IPA using the same rule set, reversed).
The two interpretations MUST remain exact inverses: any rule expressible here must parse
back, or round-tripping breaks. Shared error vocabulary with UC-009's ambiguity cases.

Notes
-----
MVP mapping is segment-level only: each rule maps one phoneme (or
phoneme sequence, for longest-match) to one grapheme string.
Forward mapping (this case, segments → graphemes) and reverse parsing
(UC-009, graphemes → segments) operate on the same rule set in opposite
directions and must remain exact inverses.

Both "no rules" and "partial rules" degrade visibly and
identifiably (warn-and-show, never hide, never raise) — the same
attribution principle as ADR-038's annotated defaults: the user
should always be able to tell WHY they are looking at IPA.

Rule-order-is-semantic (serialization must preserve array order).

.. todo::
   :class: warning

   **Contextual romanization rules (post-MVP)**
   Contextual spelling rules (e.g., "c" → ⟨s⟩ before front
   vowels, ⟨k⟩ elsewhere) are deferred until the segment-level
   forward path and UC-009's reverse parsing are both stable —
   forward application and reverse parsing must be implemented as
   exact inverses of each other or round-tripping breaks.
   Revisit once generation (:ref:`uc04`) and import
   (:ref:`uc009`) are both basically working.
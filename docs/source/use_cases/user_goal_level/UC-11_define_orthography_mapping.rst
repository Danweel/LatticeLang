.. _UC-11_define_orthography_mapping:
.. _uc11:

UC-11: Define Orthography Mapping
==================================

:Doc Status: Draft
:Goal Level: User goal
:Impl Status: Not Started
:Phase: Beta (rules format + UC-015), Delta (editor polish)

Goal
----
Define how the language's phonemes are rendered as romanized
spelling — the writing system a reader of the user's fiction will
actually see. Each mapping rule associates a phoneme (or phoneme
sequence) with a grapheme string. IPA is the internal working
form; the mapping turns generated words (:ref:`uc04`) into words
that read naturally in prose.

Preconditions
-------------
- :ref:`uc01` is complete — phonemes exist to be mapped
- A loaded LanguageDefinition is in memory — see :ref:`uc005`
- Rules are stored in the project file per
  ``dc_orthography_rules``

Default State
-------------
New projects define no orthography rules. Romanization then equals
the IPA string (UC-015 extension 2a) — visible degradation, never
silent. The GUI editor and CLI nudges point here from first
generation onward, since writers generally want to see their
language in spelling, not IPA.

Main Success Scenario
---------------------

1. User opens the Orthography Editor → system shows the current
   rule set (possibly empty), grouped by phoneme category
   (consonants, vowels, additional segments per ADR-032)

2. User creates a mapping rule: selects a phoneme from the
   inventory (IPA symbol and its features shown for reference) and
   enters the grapheme string that represents it
   (e.g., /θ/ → ``"th"``, /ʃ/ → ``"sh"``) → system stores the rule

3. System validates the rule:
   - The phoneme exists in the inventory (else see extension 2a)
   - No other rule already maps the same phoneme sequence (else see extension 2b)
   - The grapheme string is non-empty

4. User previews a sample word → system romanizes it live —
   delegates to :ref:`uc015` — showing IPA and romanized forms
   side by side

5. User repeats steps 2–4 until coverage is satisfactory

6. User saves the project → system serializes the rules — see
   :ref:`uc005`. System reports coverage: "[M] of [N] inventory
   phonemes mapped; [K] unmapped phonemes will romanize as IPA"

Postconditions
--------------

- Orthography rules are stored in the project file, complete with
  any deliberately-unmapped phonemes
- Forward application (:ref:`uc015`) and reverse parsing
  (:ref:`uc009`) read the same rule set — a rule change affects
  both directions consistently
- Generated words display romanized from this point on
  (:ref:`uc04` step 6)

Extensions
----------

* **2a:** Rule references a phoneme not in inventory
  - 2a1: System warns: "Phoneme /x/ is not in your inventory"
  - 2a2: User adds the phoneme — see :ref:`uc01` — or removes the rule
  - TODO: troubleshooting page (phoneme not in inventory)

* **2b:** Another rule already maps the same phoneme
  - 2b1: System warns and shows the existing rule
  - 2b2: User replaces the old rule, or keeps both — in which case
  the longest-match winner is determined by rule order, and the
  system states which rule won ("/t/ → ``t`` (kept) — new rule /t/ → ``tt`` unused")
  - Never ambiguous silently: the winning rule is always named

* **5a:** Unmapped phonemes remain after save
  - 5a1: System reports the count and lists them
  - 5a2: User may continue (they pass through as IPA per :ref:`uc015` extension 3a) or map them now
  - Partial coverage is a supported steady state, not an error

Frequency
---------
Medium — usually one intensive session per language (writers care
deeply about spelling flavor), then touched up when phonemes are
added or words look wrong in preview.

Related
-------

**Consumed by (forward direction):**
- :ref:`uc015` — Apply Orthography Rules (applies these rules to generated words)
- :ref:`uc009` — Import Words (parses romanized text back to IPA
using these rules, reversed — the two interpretations MUST be
exact inverses or round-tripping breaks)

**Adjacent to:**
- :ref:`uc04` — Generate Words (primary consumer of romanized
output; its editor nudges point here)
- :ref:`uc07` — Export to LaTeX (word lists are romanized in exports)

Variations
----------

* **Via CLI (Phase Beta):**

  .. code-block:: bash

     latticelang orthography set --phoneme θ --grapheme th
     latticelang orthography set --phoneme θ --grapheme th --force

  ``--force`` overrides an existing mapping (extension 2b path);
  without it, the conflict is reported and nothing changes.

* **Via GUI (Phase Gamma):**
  Orthography Editor with an inventory browser on the left, rule
  list on the right, and a live two-column preview (IPA /
  romanization) fed by :ref:`uc015` (debounced). Unmapped phonemes
  carry a visible "unmapped" badge — matching the warn-and-show
  principle throughout.

* **Via Python API (Phase Beta):**

  .. code-block:: python

     from latticelang.orthography.rules import OrthographyRules

     rules = definition.orthography_rules
     rules.set(grapheme="th", phonemes=["θ"])
     rules.set(grapheme="sh", phonemes=["ʃ"])
     # Coverage check, same report as step 6
     missing = rules.unmapped_phonemes()

Notes
-----
MVP mapping is segment-level: each rule maps one phoneme (or an
explicit phoneme *sequence*, for digraph source material) to one
grapheme string. Multi-grapheme targets (``"th"``, ``"kh"``,
``"ng"``) are first-class and ordinary — natural orthographies
use them constantly.

Rule application order and tie-breaking live in :ref:`uc015`,
not here — this case defines the rule SET; the subfunction defines
rule INTERPRETATION. Longest-match-wins is the only ordering
semantic guaranteed at definition time.

Coverage is reported at save time (step 6) rather than enforced —
partial inventories are expected during rule-building, and forcing
full coverage would block legitimate work-in-progress.

.. todo::
   :class: warning

   **Contextual romanization rules (post-MVP)**
   Mirror of the :ref:`uc015` todo: when contextual spelling rules
   are added (e.g., "c" → ⟨s⟩ before front vowels), THIS case
   gains the rule-authoring UI for them and BOTH :ref:`uc015`
   (forward) and :ref:`uc009` (reverse) must interpret them as
   exact inverses. Do not add contextual rules to any one of the
   three alone. Revisit once generation (:ref:`uc04`) and import
   (:ref:`uc009`) are both basically working.
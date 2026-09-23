.. _UC-04_generate_words:
.. _uc04:

UC-04: Generate Words
=====================

:Doc Status: Review
:Goal Level: User goal
:Impl Status: Not Started
:Phase: Beta (API), Gamma (GUI); CLI where scheduled

Goal
----
Produce a set of N unique words that conform to the currently loaded
LanguageDefinition — honoring templates, frequency weighting, and
phonotactic constraints — reproducibly via seed.

Preconditions
-------------
- :ref:`uc01` is complete — inventory passes the ``dc_inventory``
  checks (at least one nucleus-capable phoneme; every category a
  template references is populated)
- :ref:`uc02` is complete — at least one syllable template defined
- Constraints always exist in practice: new projects ship with
  ``sonority_sequencing`` enabled (ADR-038)
- Limits: 500 words per batch; 50 in GUI live preview
- Each returned word carries both its IPA and romanization
  (romanization equals the IPA string when no orthography rules
  are defined — see :ref:`uc015`)

Main Success Scenario
---------------------

1. User sets generation parameters (word count, syllable range,
   frequency weighting, seed) → system validates them (count > 0
   and ≤ 500; min syllables ≥ 1; max ≥ min; seed, if given, an
   integer)

   Reproducibility (ADR-044): Reproducibility depends on the
   entire pipeline drawing from deterministic per-slot streams
   (ADR-044): no stage shares an RNG, so downstream edits don't
   perturb upstream draw.

2. System initializes
   :class:`~latticelang.core.generator.WordGenerator` with the
   LanguageDefinition and parameters, seeding its PRNG

3. For each word, the system delegates to :ref:`uc017`, which derives a per-slot deterministic stream (ADR-044).

4. System checks the completed word against the existing word list
   for duplicates → duplicates are regenerated (up to 50 attempts)

5. Steps 3–4 repeat until the requested word count is reached

6. 6. System returns the word list, each entry carrying the IPA
   string with syllable boundaries (e.g., ``"stɹæm.bəl"``) and
   its romanization per the project's orthography rules
   (delegates to :ref:`uc015`) — e.g., ``"strambul"``.

Postconditions
--------------
- A list of N unique words exists, all conforming to the
  LanguageDefinition, including word-domain constraints
- Same parameters + definition + seed reproduce the exact list
- Word list is available for display, export, or further
  processing

Extensions
----------

* **1a:** Invalid generation parameters (count = 0, min > max,
  count > 500)
  - 1a1: System raises :class:`~latticelang.core.generator.ParameterError`
  - 1a2: Error identifies the invalid parameter
  - 1a3: User corrects and retries

* **1b:** Requested count exceeds combinatorial maximum
  - 1b1: System calculates the maximum unique words before generating
  - 1b2: "Requested [N] words but only [M] unique combinations are possible with the current definition"
  - 1b3: System offers to generate the maximum and stop, or cancel

* **3a:** Word-level validation fails repeatedly (10 attempts)
  - 3a1: System reports which word-domain constraint rejects the word and at which junction (e.g., "geminate /b.b/ at syllables 2–3")
  - 3a2: User is directed to :ref:`uc03`
  - 3a3: If a single template's coda-onset combinations are systematically blocked, the system notes this as a likely cause

* **3b:** Change results in zero valid words generated.
  - System displays a warning: "No valid words — constraints may be too restrictive."
  - System reports candidates surviving each filtering stage (template composition, constraint screening)
  - User adjusts and retries.

* **4a:** Duplicate word generated after 50 attempts
  - 4a1: System allows the duplicate with a note
  - 4a2: Indicates the definition may be too constrained (small inventory + few templates → limited word space)
  - 4a3: System reports the combinatorial maximum: "With [X] phonemes and [Y] templates, approximately [Z] unique words are possible"
  - 4a4: User adjusts inventory or templates — see :ref:`uc01`, :ref:`uc02`




Frequency
---------
Very high — once per generation request in batch mode; continuously
(debounced, capped at 50 words) in GUI live preview.

Related
-------

**Calls (delegates to):**
- :ref:`uc014` — Compose a Candidate Syllable (Subfunction; the per-syllable loop, retry policy, and template-exhaustion handling live there)
- :ref:`uc013` — Validate Syllable (called by UC-014 per syllable; the completed-word sweep here uses it with full context)
- :ref:`uc015` — Apply Orthography Rules (Subfunction, called in step 6 to render each generated word in the project's spelling)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview (UC-04 is the generation engine inside the editing loop)
- CLI entry point (``latticelang generate``)
- Test suite

**Adjacent to:**
- :ref:`uc07` — Export to LaTeX (consumes this output)
- :ref:`uc005` — Serialize/Deserialize (loads the input)

Variations
----------

* **Via CLI (where scheduled):**

  .. code-block:: bash

     latticelang generate --preset english_ga --count 50 --seed 42

  Output: one word per line, romanized and IPA separated by a tab
  (``--format ipa|romanized|both`` controls columns). Errors:
  exit code 1, message on stderr. Output capped at 50 words, shown as two columns: romanization / IPA.

* **Via GUI (Phase Gamma):**
  Triggered on rule change (debounced 300ms) or via "Generate".
  Output capped at 50 words in the live preview pane. Errors:
  in-app notification with "Fix" button linking to :ref:`uc01` or
  :ref:`uc03`.

  .. code-block:: python

     from latticelang.core.generator import WordGenerator
     from latticelang.io.language_json import load_project

     definition = load_project("english_ga.json")
     gen = WordGenerator(definition, seed=42)
     words = gen.generate(
         count=50,
         min_syllables=1,
         max_syllables=4,
         frequency_weighted=True,  # default; False for uniform
     )
     for word in words:
         print(word.romanization, word.ipa)  # GeneratedWord objects

Notes
-----
Seeded PRNG (``random.Random``): same definition + same seed
always reproduces the same list — critical for testing and for
reproducing "language snapshots."

Reproducibility depends on the *entire* pipeline being seeded:
UC-014's slot filling and this case's word-level decisions draw
from the same PRNG.

Word-domain validation (step 3, second half) is deliberately a
word-completion sweep rather than inline: syllables are validated
as built with whatever context exists; the finished word gets one
full-context check. SKIPPED results from per-syllable validation
are provisional; a word is never reported valid until word-domain
constraints have run with full context (Q37).

.. todo::
   :class: warning

   **Troubleshooting page for UC-04**
   Page needed under ``user/troubleshooting/``: no output / all
   templates exhausted (surfaced from UC-014's exhaustion
   extension in word context).

.. todo::
   :class: warning

   **Contextual romanization rules (post-MVP)**
   MVP maps single phonemes to grapheme strings only
   (longest-match, left-to-right, within a syllable). Contextual
   spelling rules (e.g., "c" → /s/ before front vowels, "k"
   elsewhere) are deferred until the segment-level forward path
   and the reverse-pipeline parser are both stable — they must be
   implemented as exact inverses of each other or round-tripping
   breaks. Revisit once generation (UC-04) and import (reverse
   pipeline) are both basically working.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Set Generation Parameters] --> B{Parameters Valid?}
       B -->|No| C[Raise ParameterError]
       B -->|Yes| D[Initialize WordGenerator]
       D --> E[For Each Word:]
       E --> F[Compose Word from Syllables - via UC-014]
       F --> G[Word-level Sweep: Word-domain Constraints]
       G --> H{Word Passes?}
       H -->|No| I{Attempts < 10?}
       I -->|Yes| F
       I -->|No| J[Report Rejecting Constraint + Junction]
       H --> K{Duplicate?}
       K -->|Yes| L{Attempts < 50?}
       L -->|Yes| E
       L -->|No| M[Accept Duplicate, Note]
       K -->|No| N[Add to Word List]
       M --> N
       N --> O{Word Count Met?}
       O -->|Yes| P[Return Word List]
       O -->|No| E
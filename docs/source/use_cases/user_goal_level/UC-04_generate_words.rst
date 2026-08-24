.. _uc04:

UC-04: Generate Words
=====================

:Goal Level: User goal
:Priority: MVP — Milestone 1 (Python API), Milestone 2 (CLI), Milestone 3 (GUI)
:Status: Planned

Goal
----
Produce a set of N words that conform to the currently loaded
LanguageDefinition, applying frequency weights and phonotactic
constraints, with optional reproducibility via seed.

Preconditions
-------------
- :ref:`uc01` is complete — phoneme inventory exists with at least one
  vowel and one consonant
- :ref:`uc02` is complete — at least one syllable template is defined
- :ref:`uc03` is optionally complete — constraints improve output
  quality but are not required for generation to function

Main Success Scenario
---------------------

#. User sets generation parameters (word count, syllable range,
   frequency weighting, seed) → system validates parameters:
   - Word count > 0
   - Min syllables ≥ 1
   - Max syllables ≥ min syllables
   - If seed is provided, it must be an integer

#. System initializes :class:`~latticelang.core.generator.WordGenerator`
   with the LanguageDefinition and parameters → generator stores
   the inventory, templates, constraints, and seeds its PRNG
   — see :attr:`~latticelang.core.generator.WordGenerator.seed`

#. For each requested word:

   a. System selects a syllable template at random (uniform across
      defined templates) → calls
      :meth:`~latticelang.core.generator.WordGenerator._select_template`

   b. For each slot in the selected template, system selects a phoneme:
      - Filters inventory by allowed categories for the slot position
      - If frequency weighting is enabled, weights selection by
        :attr:`~latticelang.core.phonology.Phoneme.frequency`
        → calls
        :meth:`~latticelang.core.generator.WordGenerator._select_phoneme`
      - Applies position restrictions (forbidden phonemes per slot)
        from :ref:`uc03` constraints

   c. System assembles the selected phonemes into a candidate syllable
      → creates a :class:`~latticelang.core.syllable.Syllable` object

   d. System validates the candidate syllable against all active
      constraints → delegates to :ref:`uc013`

   e. If validation passes, syllable is accepted; if not, steps (a)–(d)
      repeat with a new candidate (up to 100 attempts per syllable)

   f. Steps (a)–(e) repeat until the word reaches the target syllable
      count (randomly chosen between min and max)

#. System checks the completed word against the existing word list for
   duplicates → if duplicate, the word is regenerated (up to 50
   attempts)

#. Steps 3–4 repeat until the requested word count is reached

#. System returns the word list as a list of IPA strings with
   syllable boundaries marked (e.g. ``"stɹæm.bəl"``)

Postconditions
--------------
- A list of N unique words exists, all conforming to the
  LanguageDefinition
- If a seed was provided, the same parameters + definition + seed
  will reproduce this exact list
- Word list is available for display, export, or further processing

Extensions
----------

* **1a:** Invalid generation parameters
  (e.g., word count = 0, min > max)
  - 1a1: System raises
    :class:`~latticelang.core.generator.ParameterError`
  - 1a2: Error message identifies which parameter is invalid
  - 1a3: User corrects and retries

* **3b:** No phonemes available for a slot
  (e.g., onset allows only consonants but no consonants are defined)
  - 3b1: System raises
    :class:`~latticelang.core.generator.GenerationError`
  - 3b2: Error message: "No phonemes available for [position] slot in
    template [name] — add phonemes to your inventory"
  - 3b3: User is directed to :ref:`uc01`

* **3e:** Syllable fails validation after 100 attempts
  - 3e1: System skips this template for the current word
  - 3e2: System logs warning: "Template [name] produced too many
    invalid syllables — consider relaxing constraints"
  - 3e3: If all templates are exhausted for a word, system raises
    :class:`~latticelang.core.generator.NoValidTemplateError`
  - 3e4: Error message lists which constraints are rejecting candidates
  - 3e5: User is directed to :ref:`uc03` to review constraints
  - → See :ref:`troubleshooting_no_output`

* **4a:** Duplicate word generated after 50 attempts
  - 4a1: System allows the duplicate with a note
  - 4a2: Indicates that the LanguageDefinition may be too constrained
    (small inventory + few templates → limited word space)
  - 4a3: System calculates the combinatorial maximum: "With [X]
    phonemes and [Y] templates, approximately [Z] unique words are
    possible"
  - 4a4: User adjusts inventory or templates — see :ref:`uc01`,
    :ref:`uc02`

* **5a:** Word count exceeds combinatorial maximum
  (e.g., requesting 10,000 words from a 6-phoneme inventory with
  one CV template)
  - 5a1: System calculates the maximum possible unique words before
    generation begins
  - 5a2: System informs user: "Requested [N] words but only [M]
    unique combinations are possible with the current definition"
  - 5a3: System offers to generate the maximum and stop, or cancel

Frequency
---------
Very high — called once per generation request in CLI mode, or
continuously (debounced) in GUI live-preview mode.

Related
-------

**Calls (delegates to):**
- :ref:`uc013` — Validate Syllable Against Constraints (Subfunction,
  called in step 3d)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview (Summary, calls UC-04
  as part of the interactive editing loop)
- CLI entry point (``latticelang generate``)
- Test suite (``test_english_validation.py``)

**Adjacent to:**
- :ref:`uc07` — Export to LaTeX (receives this use case's output)
- :ref:`uc005` — Serialize/Deserialize (loads the input for this use case)

Variations
----------

* **Via CLI (Milestone 2):**

  .. code-block:: bash

     latticelang generate --preset english_ga --count 50 --seed 42

  Output: one word per line on stdout
  Errors: exit code 1, message on stderr

* **Via GUI (Milestone 3):**
  Triggered automatically on rule change (debounced 300ms) or manually
  via "Generate" button. Output: displayed in live preview pane.
  Errors: in-app notification with "Fix" button linking to relevant
  use case (:ref:`uc01` or :ref:`uc03`).

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.generator import WordGenerator
     from latticelang.orthography.json_io import load_project

     definition = load_project("english_ga.json")
     gen = WordGenerator(definition, seed=42)
     words = gen.generate(
         count=50,
         min_syllables=1,
         max_syllables=4,
         frequency_weighted=True,
     )
     for word in words:
         print(word)

Notes
-----
The generator uses a seeded PRNG (Python's ``random.Random`` with
the provided seed). The same LanguageDefinition + same seed always
produces the same word list. This is critical for testing (see
:ref:`testing_strategy`) and for users who want to share a specific
"language snapshot" or reproduce results across sessions.

The generation algorithm prioritizes correctness over speed: it
attempts up to 100 candidate syllables before giving up on a template.
This is acceptable for MVP word counts (≤ 1000 words). Post-MVP
optimization may include precomputing valid clusters per template
to avoid rejection sampling.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Set Generation Parameters] --> B{Parameters Valid?}
       B -->|No| C[Raise ParameterError]
       B -->|Yes| D[Initialize WordGenerator]
       D --> E[For Each Word:]
       E --> F[Select Template at Random]
       F --> G[For Each Slot: Select Phoneme]
       G --> H{Phonemes Available?}
       H -->|No| I[Raise GenerationError]
       H -->|Yes| J[Apply Position Restrictions]
       J --> K[Apply Frequency Weighting]
       K --> L[Assemble Candidate Syllable]
       L --> M{Constraints Pass?}
       M -->|Yes| N{Syllable Count Met?}
       M -->|No| O{Attempts < 100?}
       O -->|Yes| F
       O -->|No| P[Skip Template, Log Warning]
       P --> Q{All Templates Exhausted?}
       Q -->|Yes| R[Raise NoValidTemplateError]
       Q -->|No| F
       N -->|No| F
       N -->|Yes| S{Duplicate?}
       S -->|Yes| T{Attempts < 50?}
       T -->|Yes| E
       T -->|No| U[Accept Duplicate, Note]
       S -->|No| V[Add to Word List]
       U --> V
       V --> W{Word Count Met?}
       W -->|Yes| X[Return Word List]
       W -->|No| E
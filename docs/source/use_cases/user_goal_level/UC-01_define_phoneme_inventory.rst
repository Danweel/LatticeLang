.. _uc01:

UC-01: Define Phoneme Inventory
================================

:Goal Level: User goal
:Priority: MVP — Milestone 1
:Status: In progress

Goal
----
Define which phonemes exist in the constructed language, including IPA
symbols, phonetic features, sonority rank, and relative frequency. The
resulting inventory serves as the foundation for all downstream use
cases: syllable templates, constraint enforcement, and word generation.

Preconditions
-------------
- A project file exists (new or loaded) — see :ref:`uc005`
- The IPA symbol set is available for validation — see :ref:`uc012`

Main Success Scenario
---------------------

1. User adds a phoneme by providing an IPA symbol (e.g. ``"p"``,
   ``"tʃ"``, ``"aɪ"``) → system segments and validates the symbol
   using the segmenter — see :func:`~latticelang.core.phonology.segment_ipa`

2. User selects a phoneme category (consonant, vowel, diphthong, tone)
   → system stores the category as
   :class:`~latticelang.core.phonology.PhonemeCategory`

3. User assigns phonetic features (voiced, place, manner, height,
   backness, etc.) → system stores features as a dictionary on the
   :class:`~latticelang.core.phonology.Phoneme` instance

4. User sets the sonority rank (integer 0–9, where 0 = least sonorous)
   → system validates the rank is within the allowed range and
   consistent with the category — see
   :meth:`~latticelang.core.phonology.Phoneme.__post_init__`

5. User optionally sets a frequency weight (float, default: 1.0)
   → system stores the weight for use in generation — see
   :attr:`~latticelang.core.phonology.Phoneme.frequency`

6. System checks for duplicate symbols in the
   :class:`~latticelang.core.phonology.Inventory` → if unique,
   phoneme is added

7. User repeats steps 1–6 for each phoneme in the language

8. User saves the project → system serializes the inventory — see
   :ref:`uc005`

Postconditions
--------------
- :class:`~latticelang.core.phonology.Inventory` contains all defined
  phonemes with complete feature sets
- Each phoneme has a unique symbol, valid category, and sonority rank
- Project file (``.json``) persists the inventory
- Live preview regenerates word list if any words were previously
  generated (Milestone 3+)

Extensions
----------

* **1a:** IPA symbol not recognized by the segmenter
  - 1a1: System displays warning with closest matches from the IPA
    symbol table
  - 1a2: User selects from suggestions or enters a custom symbol
  - 1a3: If custom, system flags the phoneme for manual review
  - → See :ref:`uc012`, extension 2a
  - → See :ref:`troubleshooting_unrecognized_ipa`

* **1b:** IPA symbol is valid but represents multiple phonemes
  (e.g., ``"ts"`` could be one affricate /t͡s/ or two phonemes /t/+/s/)
  - 1b1: System presents segmentation options
  - 1b2: User confirms interpretation
  - → See :ref:`uc012`, extension 3a

* **4a:** Sonority rank conflicts with assigned features
  (e.g., stop marked as rank 5, or vowel marked as rank 0)
  - 4a1: System warns: "Rank [X] is unusual for [category] with
    features [Y]. Expected range: [A–B]"
  - 4a2: User confirms override or adjusts
  - → See :ref:`reference_sonority`

* **6a:** Duplicate symbol detected
  - 6a1: System shows existing entry with its features and rank
  - 6a2: User chooses: replace existing, merge features, or cancel
  - → See :ref:`troubleshooting_duplicate_phoneme`

* **6b:** Symbol is unique but differs only by diacritic from an
  existing one (e.g., adding ``"pʰ"`` when ``"p"`` exists)
  - 6b1: System notes: "Similar symbol 'p' already exists — is this
    an allophone or a distinct phoneme?"
  - 6b2: User confirms distinction (allophones are post-MVP; for now
    they're treated as separate phonemes)

* **8a:** File I/O error during save
  - 8a1: System displays error with file path and permissions hint
  - 8a2: User retries or saves to alternate location
  - → See :ref:`troubleshooting_file_io`

Frequency
---------
High — typically the first task when creating a new language. Most
users will revisit this step repeatedly as they refine their phonology.

Related
-------

**Calls (delegates to):**
- :ref:`uc012` — Segment IPA Input (Subfunction, called in step 1)
- :ref:`uc005` — Serialize/Deserialize (Subfunction, called in step 8)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview (Summary, UC-01 is one
  of the activities within the editing loop)

**Prerequisite for:**
- :ref:`uc02` — Define Syllable Templates (needs phonemes to fill slots)
- :ref:`uc03` — Define Phonotactic Constraints (needs sonority ranks)
- :ref:`uc04` — Generate Words (needs a complete inventory)

Variations
----------

* **Via CLI (Milestone 2):** User edits the ``.json`` project file
  directly or uses ``latticelang phoneme add --symbol p --category
  consonant --features voiced=false,bilabial,stop --rank 0``

* **Via GUI (Milestone 3):** User interacts with a table widget
  (rows = phonemes, columns = symbol, category, features, rank,
  frequency). Inline editing with dropdown selectors for category
  and features. Add/remove buttons.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.phonology import (
         Phoneme, PhonemeCategory, Inventory,
     )

     inv = Inventory()
     inv.add(Phoneme(
         symbol="p",
         category=PhonemeCategory.CONSONANT,
         features={"voiced": False, "place": "bilabial", "manner": "stop"},
         sonority_rank=0,
         frequency=1.93,
     ))

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Add Phoneme: IPA symbol] --> B{Symbol Valid?}
       B -->|Yes| C{Ambiguous?}
       B -->|No| D[Suggest Closest Matches]
       D --> A
       C -->|No| E[Select Category]
       C -->|Yes| F[Present Segmentation Options]
       F --> E
       E --> G[Assign Features]
       G --> H[Set Sonority Rank]
       H --> I{Rank Consistent?}
       I -->|Yes| J[Set Frequency Weight]
       I -->|No| K[Warn: Unusual Rank]
       K --> J
       J --> L{Duplicate?}
       L -->|No| M[Add to Inventory]
       L -->|Yes| N[Show Existing Entry]
       N --> O{Replace? Merge? Cancel?}
       O -->|Replace| M
       O -->|Merge| P[Merge Features]
       P --> M
       O -->|Cancel| A
       M --> Q{More Phonemes?}
       Q -->|Yes| A
       Q -->|No| R[Save Project]
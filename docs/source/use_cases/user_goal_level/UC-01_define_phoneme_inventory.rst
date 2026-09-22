.. _UC-01_define_phoneme_inventory:
.. _uc01:

UC-01: Define Phoneme Inventory
===============================

:Doc Status: Review
:Goal Level: Summary
:Impl Status: Not Started
:Phase: Beta

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
   ``"t͡ʃ"``, ``"aɪ"``) → system segments and validates the symbol
   using the segmenter — see
   :func:`~latticelang.core.phonology.segment_ipa`.
   Multi-character symbols (affricates, diphthongs, co-articulated
   segments) are validated against the IPA reference table

2. System derives the phoneme category (consonant, vowel, glide,
   diphthong) from the symbol's features: see
   :term:`phoneme category`, user confirms or overrides.
   Override is intended for custom symbols and deliberate
   non-standard analyses (ADR-032).

3. User assigns phonetic features (voiced, place, manner, height,
   backness, etc.) → system shows only the feature fields relevant
   to the derived category → features are stored as a dictionary
   on the :class:`~latticelang.core.phonology.Phoneme` instance

4. System proposes a sonority rank from the phoneme's features
   (integer 0–9, where 0 = least sonorous) → user confirms or
   adjusts → system validates the rank is within the expected
   range for the category and features — see :term:`sonority scale`

5. System pre-fills the frequency weight from PHOIBLE
   attestation data (float, default: 1.0 if unattested) → user
   optionally adjusts → stored for use in generation — see
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
- Each phoneme has a unique symbol, a category (derived or
  overridden), and a sonority rank
- Project file (``.json``) persists the inventory
- Live preview regenerates word list if any words were previously
  generated (Phase Gamma)

Extensions
----------

* **1a:** IPA symbol not recognized by the segmenter
  - 1a1: System displays warning with closest matches from the IPA symbol table
  - 1a2: User selects from suggestions or enters a custom symbol
  - 1a3: If custom, system flags the phoneme for manual review and skips automatic feature, rank, and frequency pre-fill

* **1b:** IPA symbol is valid but represents multiple phonemes
  (e.g., ``"ts"`` could be one affricate /t͡s/ or two phonemes /t/+/s/)
  - 1b1: System applies the longest-match default (ADR-043):
  prefer /t͡s/ if the affricate exists in the inventory, else the /t/+/s/ sequence
  - 1b2: System flags the interpretation with a low-friction
  correction affordance (user can switch to the alternative)
  - 1b3: Batch contexts (:ref:`uc009`) never prompt — longest-match
  commits, uncertain resolutions surface in the batch report (:ref:`q4-ambiguity-confidence`)
  - See :ref:`uc012`, extension 3a

* **2a:** Derived category is unexpected for the user's analysis
  (e.g., glide /j/ that the user wants treated as a consonant)
  - 2a1: User overrides the category
  - 2a2: System records the override but warns if slot placement
  implications follow (glides overridden to consonant may fill
  onset slots, contrary to feature expectations)

* **4a:** Sonority rank conflicts with assigned features
  (e.g., stop marked as rank 5, or vowel marked as rank 0)
  - 4a1: System warns: "Rank [X] is unusual for [category] with
  features [Y]. Expected range: [A–B]"
  - 4a2: User confirms override or adjusts
  - See :term:`sonority scale`

* **6a:** Duplicate symbol detected
  - 6a1: System shows existing entry with its features and rank
  - 6a2: Agreeing fields merge silently; conflicting fields
  collect into one grouped prompt: keep all existing / take all
  new / decide individually (ADR-040)
  - 6a3: ``sonority_rank`` is never merged — recomputed from the
  merged features; ``custom`` is never downgraded
  - 6a4: Pre-merge entry is recoverable (undo stack)
  - 6a5: User may instead replace entirely or cancel

* **6b:** Symbol is unique but differs only by diacritic from an
  existing one (e.g., adding ``"pʰ"`` when ``"p"`` exists)
  - 6b1: Detection runs after normalization (ADR-041): NFD
  base-stripping; tie-bar forms never false-fire
  - 6b2: System notes, enriched by the IPA reference variant
  group when known: "'pʰ' is aspirated /p/ — in many languages
  an allophone. Add as a distinct phoneme?"
  - 6b3: User confirms distinction (allophones are post-MVP; for now
  they're treated as separate phonemes)

* **8a:** File I/O error during save
  - 8a1: System displays error with file path and permissions hint
  - 8a2: User retries or saves to alternate location

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
- :ref:`UC-08_work_in_a_gui_with_live_preview` — Work in GUI with Live Preview (Summary; UC-01 is one of the activities within the editing loop)

**Prerequisite for:**
- :ref:`UC-02_define_syllable_templates` — Define Syllable Templates
(needs phonemes to fill slots)
- :ref:`UC-03_define_phonotactic_constraints` — Define Phonotactic Constraints (needs sonority ranks)
- :ref:`UC-04_generate_words` — Generate Words (needs a complete inventory)

Variations
----------

* **Via CLI (Phase Beta):** User edits the ``.json`` project file
  directly or uses ``latticelang phoneme add --symbol p``

* **Via GUI (Phase Gamma):** User interacts with a table widget
  (rows = phonemes, columns = symbol, category, features, rank,
  frequency). Category column pre-filled and editable. Add/remove
  buttons.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.phonology import (
         Phoneme, Inventory,
     )

     inv = Inventory()
     inv.add(Phoneme(
         symbol="p",
         features={"voiced": False, "place": "bilabial", "manner": "stop"},
         frequency=1.93,
     ))  # category and rank derived from features (ADR-032)

Notes
-----

**Diphthongs** (e.g., /aɪ/, /oʊ/) are single phonemes of category
``diphthong`` occupying the nucleus slot. Input accepts the bare
sequence (``"aɪ"``); the non-syllabic diacritic (aɪ̯) is accepted but
normalized to the bare form. No tie bar is used — the tie bar
exclusively marks consonant-affricate unity (ADR-028). Component
vowels should exist in the inventory; the system warns if they don't.
Storing diphthongs as unit phonemes is a documented deviation from
standard sequence analyses — see :ref:`theoretical_framework`.

**Custom symbols** not present in the IPA reference table are
accepted but flagged, and receive no automatic features, rarity
tier, or frequency data until reviewed.

**Category derivation** follows the major-class feature mapping
([±syllabic] / [±consonantal]) rather than the LCK's manual
selection. See ADR-032 and :term:`phoneme category`.

.. todo::
   :class: warning

   **Create troubleshooting pages for UC-01**
   The following labels are referenced by UC-01 extensions but
   don't exist yet:

   - unrecognized IPA symbol handling (extension 1a)
   - duplicate symbol handling (extension 6a)
   - file I/O errors (extension 8a)

   Create pages under ``user/troubleshooting/``.

.. todo::
   :class: warning

   **Curate IPA reference symbol set**
   The IPA reference table must enumerate all valid phoneme
   symbols including affricates, co-articulated segments,
   diphthongs, and alternate forms, with features for category
   derivation. Target scope: PHOIBLE-attested segments plus
   standard chart symbols (~1,000–2,500 entries).
   See :ref:`dc_ipa_reference`.

.. todo::
   :class: attention

   **Finalize category derivation rules**
   Blockers resolved (Q6, Q24; ADR-033). The mapping table —
   including glide and diphthong handling, and syllabic
   consonants — lands in :ref:`dc_phoneme`. Remove this todo
   when the contract's mapping section is drafted.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Add Phoneme: IPA symbol] --> B{Symbol Valid?}
       B -->|Yes| C{Ambiguous?}
       B -->|No| D[Suggest Closest Matches / Flag Custom]
       D --> A
       C -->|No| E[Derive Category from Features]
       C -->|Yes| F[Present Segmentation Options]
       F --> E
       E --> G{User Confirms or Overrides Category?}
       G --> H[Assign Features: Relevant Fields Only]
       H --> I[Propose Sonority Rank]
       I --> J{Rank Plausible?}
       J -->|Yes| K[Pre-fill Frequency Weight]
       J -->|No| L[Warn: Unusual Rank]
       L --> K
       K --> M{Duplicate?}
       M -->|No| N[Add to Inventory]
       M -->|Yes| O[Show Existing Entry]
       O --> P{Replace? Merge? Cancel?}
       P -->|Replace| N
       P -->|Merge| Q[Merge Features]
       Q --> N
       P -->|Cancel| A
       N --> R{More Phonemes?}
       R -->|Yes| A
       R -->|No| S[Save Project]
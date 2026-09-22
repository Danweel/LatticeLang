.. _UC-009_import_words:
.. _uc009:

UC-009: Import Romanized Word List
===================================

:Doc Status: Draft
:Goal Level: Subfunction
:Impl Status: Not Started
:Phase: MVP — Phase Beta (Core Engine)

Goal
----
Import a list of romanized words from the user's existing work,
convert them to IPA using a selected dialect profile, segment the
IPA into phonemes, and present the results for review. This is the
primary onboarding flow for users who already have words they want
to develop into a full language.

Preconditions
-------------
- A dialect profile (orthography rules) is available — see
  :ref:`dc_orthography_rules`.
- An IPA reference table is available for symbol validation —
  see :ref:`dc_ipa_reference`.

Main Success Scenario
---------------------

1. User initiates import and provides a list of romanized words
   via:
   - Pasting text (one word per line)
   - Uploading a text file
   - Drag-and-drop onto the interface
   → system validates the input is non-empty.

2. User selects a dialect profile (e.g., American English,
   Received Pronunciation) or chooses "Custom/Manual" if no
   existing profile fits.

3. The system converts each romanized word to IPA using the
   selected dialect rules → calls
   :func:`~latticelang.core.orthography.convert_to_ipa`.

4. The system normalizes each IPA string to NFC (Unicode Normalization
   Form C) for consistent diacritic handling.

5. The system segments each IPA string into discrete phoneme
   symbols using longest-match resolution → calls
   :func:`~latticelang.core.segmenter.segment_ipa`.

6. The system presents a side-by-side mapping of:
   - Original romanized word
   - Inferred IPA string
   - Segmented phoneme list
   - Confidence indicators for ambiguous conversions

7. User reviews the conversions and marks any corrections.
   Corrections update the inferred inventory and flag the
   ambiguous case for future reference.

8. User confirms the inferred phoneme inventory → system saves
   the review session → calls :ref:`uc005`.

Postconditions
--------------
- On success: an inferred phoneme inventory exists in memory,
  pending user confirmation. The original romanized word list
  is preserved as source material.
- On failure: the caller receives a descriptive error indicating
  which word(s) failed and why.

Extensions
----------

* **2a:** No appropriate dialect profile is available.
  - 2a1: System offers "Custom/Manual" mode.
  - 2a2: In custom mode, system bypasses dialect conversion
  and expects user to provide IPA directly.
  - 2a3: User may create a new dialect profile (post-MVP) or
  select "I'll correct manually."

* **3a:** A character sequence is unrecognized by the dialect rules.
  - 3a1: System preserves the sequence unchanged (passes through).
  - 3a2: System flags the sequence for manual review.
  - 3a3: Warning indicates: "[N] unrecognized sequences —
  review required."

* **3b:** A character sequence is ambiguous i.e. could map to multiple IPA interpretations.
  - 3b1: System applies heuristic (longest-match by default).
  - 3b2: System marks the ambiguity with a confidence indicator.
  - 3b3: User can select alternative interpretations during review.
  - See :ref:`questions` Q4 for resolution strategy.

* **5a:** A segment is not found in the IPA reference table.
  - 5a1: System flags the segment as invalid.
  - 5a2: System offers closest matches from the reference table.
  - 5a3: User can correct or override.
  - → See :ref:`uc012`, extension 3a.

* **6a:** User finds a systematic error (e.g., all instances of
  "th" were converted incorrectly).
  - 6a1: User can correct one instance.
  - 6a2: System offers to "apply to all" instances of that pattern.
  - 6a3: User may confirm the batch correction.

* **7a:** User rejects the inferred inventory as unreliable.
  - 7a1: System preserves the romanized word list for later
  reference.
  - 7a2: User switches to "Define from Scratch" mode (:ref:`uc01`).
  - 7a3: No inferred inventory is created.

Frequency
---------
One-time (project onboarding) or occasional (when importing
additional words later).

Related
-------

**Calls:**
- :ref:`UC-005_serialize_deserialize_LanguageDefinitions` (saves inferred inventory)
- :ref:`UC-012_segment_ipa_input`
- :ref:`UC-01_define_phoneme_inventory` (user reviews and confirms inferred phonemes)

**Data contracts:** :ref:`dc_orthography_rules`, :ref:`dc_ipa_reference`

Variations
----------

* **Batch mode (recommended):** Import entire word list at once,
  review in bulk. Efficient for large imports.

* **Interactive mode:** Convert and review word-by-word. Slower
  but more immediate feedback.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.importer import import_words

     # Import from file
     results = import_words(
         path="source_words.txt",
         dialect="american_english"
     )

     # Returns: {
     #     "conversions": [
     #         {"roman": "catch", "ipa": "kætʃ", "segments": ["k", "æ", "tʃ"], "confidence": High},
     #         ...
     #     ],
     #     "inferred_phonemes": ["k", "æ", "t", "ʃ", ...],
     #     "warnings": [...]
     # }

Notes
-----

The original romanized word list is **never overwritten**. It's
preserved as source material. Users can add to it later. The
import process only generates a *suggested* IPA transcription —
users must review and correct.

Dialect profiles are currently read-only (American English,
Received Pronunciation). Custom profiles are post-MVP.

Confidence indicators are qualitative (high/medium/low) in MVP,
not statistical probabilities. They flag cases requiring user
review.

Storage normalization (NFC, step 4) and comparison normalization
(NFD, ADR-041) are distinct and both deliberate; they are never unified.

Open Questions (see :ref:`questions`)
--------------------------------------------------

- **Q2:** Dialect rule formalism — what's the right level of
  complexity for orthography conversion rules? Does the current
  "simple substitution" model suffice, or do we need context-
  sensitive rules?

- **Q4:** Ambiguity resolution — should the system surface
  multiple valid segmentations to the user, or just flag
  low-confidence cases?

Flow Diagram
------------

.. mermaid::

   graph TD
       A[User imports word list] --> B{Select dialect profile}
       B -->|Standard| C[Apply dialect rules]
       B -->|Custom/Manual| D[Bypass conversion, expect IPA]
       C --> E[Normalize to NFC]
       D --> F[Validate IPA input]
       E --> G[Segment IPA]
       F --> G
       G --> H[Display mapping: roman → IPA → segments]
       H --> I{Any corrections needed?}
       I -->|Yes| J[User corrects flagged entries]
       J --> K[Update inferred inventory]
       I -->|No| L[Confirm inferred inventory]
       K --> L
       L --> M[Save project — :ref:`uc005`]
       M --> N[Proceed to :ref:`uc01` review]
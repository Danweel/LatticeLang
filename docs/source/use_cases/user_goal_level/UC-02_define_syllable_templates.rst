.. _uc02:

UC-02: Define Syllable Templates
================================

:Goal Level: User goal
:Priority: MVP — Milestone 1
:Status: Planned

Goal
----
Define the allowable syllable structures for the constructed language,
including which phoneme categories may occupy each position (onset,
nucleus, coda) and the minimum/maximum count per slot. The resulting
templates constrain word generation to produce structurally valid
syllables.

Preconditions
-------------
- :ref:`uc01` is complete — a phoneme inventory exists with at least one
  vowel
- The concept of syllable positions (onset/nucleus/coda) is understood
  — see :ref:`reference_syllable_structure`

Main Success Scenario
---------------------

1. User creates a new template by providing a name (e.g. ``"CVC"``,
   ``"CCVCC"``) → system accepts the name without enforcing
   conventional notation (allows custom labels like ``"Heavy"``,
   ``"Light"``)

2. User defines slots in order:
   - Position type: onset, nucleus, or coda → system stores as
     :class:`~latticelang.core.syllable.SlotPosition`
   - Allowed categories: consonant, vowel, diphthong, tone → system
     validates against the inventory from :ref:`uc01`
   - Minimum count (integer, typically 0 or 1) → system validates
     min ≤ max
   - Maximum count (integer, typically 1–3) → system validates
     max ≤ 3 (configurable limit)
   - Each slot is stored as a :class:`~latticelang.core.syllable.Slot`

3. System validates the template → calls
   :meth:`~latticelang.core.syllable.SyllableTemplate.validate`

4. System checks that at least one slot is a nucleus (every syllable
   requires a vowel or syllabic consonant)

5. User repeats steps 1–3 for additional templates as desired

6. User saves the project → system serializes the templates — see
   :ref:`uc005`

Postconditions
--------------
- :class:`~latticelang.core.syllable.SyllableTemplate` objects exist
  with validated slot configurations
- Generator recognizes the templates as valid syllable shapes
- Live preview can generate words using the defined templates

Extensions
----------

* **2a:** Slot allows only categories not in inventory
  (e.g., onset allows only diphthongs but no diphthongs exist)
  - 2a1: System warns: "Slot [position] allows only [category], but
    no such phonemes exist in inventory"
  - 2a2: User adds phonemes (links to :ref:`uc01`) or changes slot
    categories
  - → See :ref:`troubleshooting_empty_category`

* **3a:** No nucleus slot defined
  - 3a1: System rejects template with explanation
  - 3a2: "Every syllable requires a nucleus (typically a vowel)"
  - 3a3: User adds nucleus slot and retries
  - → See :ref:`troubleshooting_missing_nucleus`

* **3b:** Nucleus slot allows only consonants (syllabic consonant
  configuration)
  - 3b1: System warns: "Nucleus allows only consonants — ensure you
    intend syllabic consonants"
  - 3b2: User confirms or revises
  - Note: Syllabic consonants are supported but rare in English-like
    languages; this is documented behavior

* **3c:** Template name already exists
  - 3c1: System prompts to rename or overwrite
  - 3c2: Overwrite replaces the previous template

* **3d:** Min count > max count
  - 3d1: System raises validation error
  - 3d2: "Min count ([X]) cannot exceed max count ([Y])"
  - 3d3: User adjusts and retries

* **3e:** Max count exceeds system limit (3)
  - 3e1: System warns: "Max count exceeds recommended maximum (3).
    Longer clusters are rare in natural languages."
  - 3e2: User confirms override or reduces max
  - → See :ref:`uc013`, extension 4a

* **8a:** File I/O error during save
  - 8a1: System displays error with file path and permissions hint
  - 8a2: User retries or saves to alternate location
  - → See :ref:`troubleshooting_file_io`

Frequency
---------
Medium — set once per language, adjusted occasionally as the user
refines their phonology.

Related
-------

**Calls (delegates to):**
- :ref:`uc005` — Serialize/Deserialize (Subfunction, called in step 8)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview (Summary, UC-02 is one
  of the activities within the editing loop)

**Prerequisite for:**
- :ref:`uc03` — Define Phonotactic Constraints (templates define the
  raw shapes; constraints filter them)
- :ref:`uc04` — Generate Words (consumes templates to build syllables)

**Dependent on:**
- :ref:`uc01` — Define Phoneme Inventory (provides phoneme categories
  for slot validation)

Variations
----------

* **Via CLI (Milestone 2):** User edits the ``.json`` project file
  directly or uses ``latticelang template add --name CVC --slots
  "onset:c:1:1,nucleus:v:1:1,coda:c:1:1"``

* **Via GUI (Milestone 3):** User interacts with a drag-and-drop
  interface. Slots are represented as colored boxes. Drag phoneme
  category icons onto slots. Min/max are sliders. Visual preview
  of template structure updates in real time.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.syllable import SyllableTemplate, Slot, SlotPosition

     cvc = SyllableTemplate(
         name="CVC",
         slots=[
             Slot(
                 position=SlotPosition.ONSET,
                 allowed_categories=["consonant"],
                 min_count=1,
                 max_count=1,
             ),
             Slot(
                 position=SlotPosition.NUCLEUS,
                 allowed_categories=["vowel"],
                 min_count=1,
                 max_count=1,
             ),
             Slot(
                 position=SlotPosition.CODA,
                 allowed_categories=["consonant"],
                 min_count=1,
                 max_count=1,
             ),
         ],
     )

     # Add to project's template list
     project.templates.append(cvc)

Notes
-----
The slot numbering within each position (when min/max > 1) is
implicit: consecutive slots at the same position fill consecutively.
For example, an onset with min_count=2, max_count=2 will always be
filled as [C1, C2] — not [C2, C1] — and SSP validation applies to
the full onset sequence.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Create Template: name] --> B[Define Slot: position, categories, min/max]
       B --> C{Slot Valid?}
       C -->|No| D[Show Validation Error]
       D --> B
       C -->|Yes| E{Add More Slots?}
       E -->|Yes| B
       E -->|No| F{Has Nucleus?}
       F -->|No| G[Reject: Missing Nucleus]
       G --> A
       F -->|Yes| H{Validates?}
       H -->|No| I[Show Errors]
       I --> A
       H -->|Yes| J{More Templates?}
       J -->|Yes| A
       J -->|No| K[Save Project]
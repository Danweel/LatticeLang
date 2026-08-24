.. _uc03:

UC-03: Define Phonotactic Constraints
=====================================

:Goal Level: User goal
:Priority: MVP — Milestone 1
:Status: Planned

Goal
----
Define rules that filter which phoneme combinations are valid within
syllable slots. Constraints operate *after* template filling — the
generator produces a candidate syllable from a template, then
constraints reject or accept it. This separation keeps templates
simple (structural shapes) and constraints focused (phonotactic
legality).

Preconditions
-------------
- :ref:`uc01` is complete — phoneme inventory exists with sonority ranks
- :ref:`uc02` is complete — at least one syllable template exists
- User understands the Sonority Sequencing Principle — see
  :ref:`reference_sonority`

Main Success Scenario
---------------------

#. User accesses the Constraint Editor

#. User selects a constraint type from available built-ins:
   - ``sonority_sequencing`` — enforces SSP within onset and coda
   - ``allow_s_appendix`` — permits /s/ + consonant clusters
     violating SSP in onset position
   - ``no_geminate_obstruents`` — prevents identical obstruent pairs
   - ``max_onset_length`` — limits onset cluster size
   - ``max_coda_length`` — limits coda cluster size
   - ``position_restrictions`` — forbids specific phonemes in onset
     or coda
   → system stores the constraint type as a string identifier on
   :class:`~latticelang.core.sonority.Constraint`

#. User configures constraint parameters (where applicable):
   - ``max_onset_length``: integer (e.g., 3)
   - ``max_coda_length``: integer (e.g., 4)
   - ``allow_s_appendix``: list of phonemes allowed to follow /s/
     (e.g., ``["p", "t", "k", "m", "n", "l", "ɹ", "w", "j"]``)
   - ``position_restrictions``: forbidden phonemes per position
     (e.g., ``{"onset": ["ŋ"], "coda": ["h"]}``)
   → system validates parameters against the current inventory
   — calls :meth:`~latticelang.core.sonority.Constraint.validate`

#. System checks for conflicts with existing constraints
   (e.g., ``max_onset_length=2`` conflicts with ``allow_s_appendix``
   implying 3-consonant onsets like /spl/)

#. System adds the constraint to the project's constraint list

#. User repeats steps 2–5 for additional constraints as desired

#. User saves the project → system serializes the constraints — see
   :ref:`uc005`

Postconditions
--------------
- Project file contains all defined constraints with parameters
- Generator filters generated syllables through all active constraints
  during :ref:`uc04`
- Invalid clusters are rejected before reaching word output

Extensions
----------

* **3a:** Constraint references a phoneme not in inventory
  (e.g., forbidding /x/ when /x/ doesn't exist)
  - 3a1: System warns: "Phoneme /x/ is not in your inventory"
  - 3a2: User adds the phoneme — see :ref:`uc01` — or removes the
    reference
  - → See :ref:`troubleshooting_phoneme_not_in_inventory`

* **4a:** Two constraints conflict
  - 4a1: System warns: "Constraint [A] and constraint [B] may
    conflict — [description]"
  - 4a2: User resolves (adjusts parameters) or acknowledges the
    conflict (system allows both but logs it)
  - 4a3: During generation, if the conflict causes zero valid output,
    system reports which constraints are blocking — see :ref:`uc04`,
    extension 3a

* **3b:** User attempts to disable ``sonority_sequencing``
  - 3b1: System warns: "Disabling SSP will allow unnatural clusters
    like /pt/ or /mk/ in onsets. Are you sure?"
  - 3b2: User confirms — some languages do allow SSP violations,
    and the system should not hard-block this
  - 3b3: System logs the override for troubleshooting context

* **3c:** User defines a constraint with no parameters
  (e.g., ``no_geminate_obstruents`` takes none)
  - 3c1: System accepts the constraint as a boolean-enabled rule
  - 3c2: No further configuration needed

* **8a:** File I/O error during save
  - 8a1: System displays error with file path and permissions hint
  - 8a2: User retries or saves to alternate location
  - → See :ref:`troubleshooting_file_io`

Frequency
---------
Medium — set once per language, refined as the user tests output and
notices invalid clusters appearing. Often adjusted in tandem with
template changes (:ref:`uc02`).

Related
-------

**Calls (delegates to):**
- :ref:`uc005` — Serialize/Deserialize (Subfunction, called in step 8)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview (Summary, UC-03 is one
  of the activities within the editing loop)

**Prerequisite for:**
- :ref:`uc04` — Generate Words (constraints filter generated syllables
  during :ref:`uc013`)

**Dependent on:**
- :ref:`uc01` — Define Phoneme Inventory (provides phonemes and
  sonority ranks that constraints reference)
- :ref:`uc02` — Define Syllable Templates (constraints filter template
  output)

Variations
----------

* **Via CLI (Milestone 2):** User edits the ``.json`` project file
  directly or uses ``latticelang constraint add --type
  sonority_sequencing`` and ``latticelang constraint add --type
  position_restrictions --onset-forbidden ŋ --coda-forbidden h``

* **Via GUI (Milestone 3):** User interacts with a constraint panel.
  Each constraint type has a card with toggle switches and parameter
  fields. Conflicts are highlighted in real time with warning badges.

* **Via Python API (Milestone 1):**

  .. code-block:: python

     from latticelang.core.sonority import Constraint

     # SSP is a built-in, no parameters needed
     project.constraints.append(
         Constraint(type="sonority_sequencing", enabled=True)
     )

     # Position restrictions need parameters
     project.constraints.append(
         Constraint(
             type="position_restrictions",
             enabled=True,
             parameters={
                 "forbidden_onset": ["ŋ"],
                 "forbidden_coda": ["h"],
             },
         )
     )

     # Max onset length
     project.constraints.append(
         Constraint(
             type="max_onset_length",
             enabled=True,
             parameters={"max_length": 3},
         )
     )

Notes
-----
The constraint system is designed to be extensible. The MVP includes
seven built-in constraint types (listed in step 2). Post-MVP, custom
constraints will be expressible through a rule language or plugin
system — see :ref:`uc11` and Planned Features §J (Plugin API).

Constraints are applied as a pipeline: each constraint is checked
in sequence during :ref:`uc013`. If any constraint rejects the
syllable, the syllable is regenerated. The order of constraints does
not affect the outcome (all must pass), but may affect performance
(if an early constraint rejects most candidates, later constraints
are not reached).

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Access Constraint Editor] --> B[Select Constraint Type]
       B --> C[Configure Parameters]
       C --> D{Parameters Valid?}
       D -->|No| E[Show Errors]
       E --> C
       D -->|Yes| F{Conflicts with Existing?}
       F -->|No| G[Add Constraint]
       F -->|Yes| H[Warn: Potential Conflict]
       H --> I{User Resolves?}
       I -->|Yes| C
       I -->|Acknowledges| G
       G --> J{Add More?}
       J -->|Yes| B
       J -->|No| K[Save Project]
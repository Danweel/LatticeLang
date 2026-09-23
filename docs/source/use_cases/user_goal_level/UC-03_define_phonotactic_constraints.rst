.. _UC-03_define_phonotactic_constraints:
.. _uc03:

UC-03: Define Phonotactic Constraints
=====================================

:Doc Status: Review
:Goal Level: Summary
:Impl Status: Not Started
:Phase: Beta

Goal
----
Define rules that filter which phoneme combinations are valid within
syllable slots and across slot boundaries. Constraints operate
*after* template filling — the generator produces a candidate
syllable from a template, then constraints reject or accept it.
This separation keeps templates simple (structural shapes) and
constraints focused (phonotactic legality).

Preconditions
-------------
- :ref:`uc01` is complete — phoneme inventory exists with sonority ranks
- :ref:`uc02` is complete — at least one syllable template exists
- User understands the Sonority Sequencing Principle: See :term:`sonority sequencing principle`

Default State
-------------
Per ADR-038, new projects ship with exactly one constraint,
**visible and toggleable**: ``sonority_sequencing`` enabled. The
default is serialized in the project file and displayed in the
Constraint Editor like any user-added constraint — nothing is
hidden. The editor also carries an informational nudge toward
cluster-length constraints ("Most languages also limit cluster
lengths") that activates nothing on its own.

Main Success Scenario
---------------------

1. User accesses the Constraint Editor — the default
   ``sonority_sequencing`` constraint is visible, toggleable, and
   annotated as a default

2. User selects a constraint type from the nine built-ins
   (authoritative catalog: ADR-037, :ref:`adr-039`):
   - ``sonority_sequencing`` — enforces SSP within onset and coda
   - ``allow_s_appendix`` — permits /s/+C clusters violating SSP in onset position
   - ``no_geminate_obstruents`` — prevents identical adjacent obstruents (domain: word, per Q35)
   - ``max_onset_length`` — limits onset cluster size
   - ``max_coda_length`` — limits coda cluster size
   - ``position_restrictions`` — forbids specific phonemes per position, including word edges (Q37)
   - ``ocp`` — no adjacent segments sharing a designated feature
   - ``harmony`` — feature agreement within the syllable (Q34; parameterized per Q42)
   - ``prohibited_clusters`` — bans specific segment sequences: system stores the constraint type as a string identifier on :class:`~latticelang.core.constraints.Constraint`

In all cases the system stores the constraint as a catalog type identifier (one
of the strings above) plus its type-specific parameter block (:ref:ADR-037). Parameters
are validated against the type's schema at save time (:ref:dc_constraints); unknown or
malformed parameters are rejected at definition time, not discovered at generation time.

3. User configures constraint parameters (where applicable):
   - ``max_onset_length`` / ``max_coda_length``: integer (e.g., 3)
   - ``allow_s_appendix``: list of phonemes allowed to follow /s/ (e.g., ``["p", "t", "k", "m", "n", "l", "ɹ", "w", "j"]``)
   - ``position_restrictions``: forbidden phonemes per position (e.g., ``{"onset": ["ŋ"], "coda": ["h"], "word_initial": ["ŋ"]}``)
   - ``ocp``: the shared feature triggering violation (e.g., ``place``, ``voice``)
   - ``harmony``: one instance per feature — ``feature`` (e.g., ``back``) plus ``targets`` (participating categories; absent categories are neutral)
   - ``prohibited_clusters``: list of forbidden sequences (e.g., ``[["s", "t"], ["l", "n"]]``)
   - ``domain``: ``syllable | word`` where the type permits choice (``prohibited_clusters`` defaults to syllable; ``no_geminate_obstruents`` is fixed word — both per Q35): system validates parameters against the current inventory: calls :meth:`~latticelang.core.constraints.Constraint.validate`

4. System checks for conflicts with existing constraints
   (e.g., ``max_onset_length=2`` conflicts with ``allow_s_appendix``
   implying 3-consonant onsets like /spl/)

5. System adds the constraint to the project's constraint list

6. User repeats steps 2–5 for additional constraints as desired

7. User saves the project → system serializes the constraints: see :ref:`uc005`

Postconditions
--------------
- Project file contains all defined constraints with parameters,
  including domain declarations (Q35)
- Generator filters generated syllables through all active
  constraints during :ref:`uc04`
- Invalid clusters are rejected before reaching word output;
  word-domain constraints report SKIPPED (not PASSED) when word
  context is unavailable (Q37, tri-state results)

Extensions
----------

**3a:** Constraint references a phoneme not in inventory
  (e.g., forbidding /x/ when /x/ doesn't exist)
  - 3a1: System warns: "Phoneme /x/ is not in your inventory"
  - 3a2: User adds the phoneme — see :ref:`uc01` — or removes the reference
  - TODO: troubleshooting page (phoneme not in inventory)

**3b:** User disables the default ``sonority_sequencing``
  - 3b1: System warns: "Disabling SSP will allow unnatural
    clusters like /pt/ or /mk/ in onsets. Are you sure?"
  - 3b2: User confirms — some languages do allow SSP violations,
    and the system does not hard-block this (ADR-035: overrides
    are explicit and allowed; ADR-038: the default is visible,
    so disabling is an informed act, not a hidden one)
  - 3b3: System records the override on the constraint instance
    (persisted as data, dc_constraints); the override event is
    reported through the active interface (GUI/CLI) and is not persisted.

**3c:** User defines a constraint with no parameters (e.g., ``no_geminate_obstruents`` takes none)
  - 3c1: System accepts the constraint as a boolean-enabled rule
  - 3c2: No further configuration needed

**4a:** Two constraints conflict
  - 4a1: System warns: "Constraint [A] and constraint [B] may conflict — [description]"
  - 4a2: User resolves (adjusts parameters) or acknowledges the conflict (system allows both but logs it)
  - 4a3: System displays the survival funnel — candidates composed per template,
    then survivors after each active constraint in evaluation order — and names the
    most-rejected constraint with one rejected candidate as a concrete example.
    "Most-rejected" is a heuristic ranking of where candidates died, not a causal
    claim about unsatisfiability; see :ref:ADR-046.
**7a:** File I/O error during save
  - 7a1: System displays error with file path and permissions hint
  - 7a2: User retries or saves to alternate location
  - TODO: troubleshooting page (file I/O)

Frequency
---------
Medium — set once per language, refined as the user tests output and
notices invalid clusters appearing. Often adjusted in tandem with
template changes (:ref:`uc02`).

Related
-------

**Calls (delegates to):**
- :ref:`uc005` — Serialize/Deserialize (Subfunction, called in step 7)

**Called by:**
- :ref:`uc08` — Work in GUI with Live Preview

**Prerequisite for:**
- :ref:`uc04` — Generate Words (constraints filter generated syllables via :ref:`uc013`)

**Dependent on:**
- :ref:`uc01` — Define Phoneme Inventory (provides phonemes and sonority ranks that constraints reference)
- :ref:`uc02` — Define Syllable Templates (constraints filter template output)

ADR-038 - Default State
ADR-037 - Nine-type catalog
Q42 - parameterization
Q35 - domains
Q37 - tristate

Variations
----------

* **Via CLI (Phase Beta):** User edits the ``.json`` project file
  directly or uses ``latticelang constraint add --type
  sonority_sequencing`` and ``latticelang constraint add --type
  position_restrictions --onset-forbidden ŋ --coda-forbidden h``

* **Via GUI (Phase Gamma):** User interacts with a constraint panel.
  Each constraint type has a card with toggle switches and parameter
  fields. The default SSP constraint carries a "default" badge.
  Conflicts are highlighted in real time with warning badges.

* **Via Python API (Phase Beta):**

  .. code-block:: python

     from latticelang.core.constraints import Constraint

     # SSP is the built-in default (ADR-038), no parameters needed
     project.constraints.append(
         Constraint(type="sonority_sequencing", enabled=True)
     )

     # Position restrictions, including word-edge rules
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

     # Harmony: one instance per feature (Q42)
     project.constraints.append(
         Constraint(
             type="harmony",
             enabled=True,
             parameters={"feature": "back", "targets": ["vowel"]},
         )
     )

     # Prohibited clusters with explicit domain (Q35)
     project.constraints.append(
         Constraint(
             type="prohibited_clusters",
             enabled=True,
             parameters={"clusters": [["s", "t"]]},
             domain="syllable",
         )
     )

Notes
-----
The MVP constraint catalog is frozen at nine types (ADR-037); ten
post-MVP types are reserved there and listed in
``dev/design/constraints.rst``, the authoritative living catalog.
Custom constraints via rule language or plugin system are
post-MVP (possible future case).

Constraints are applied as a pipeline: each constraint is checked
in sequence during :ref:`uc013`. If any constraint rejects the
syllable, the syllable is regenerated. Constraint order does not
affect the outcome (all must pass), but may affect performance.

Domain semantics (Q35): syllable-domain constraints evaluate the
syllable in isolation; word-domain constraints require
``word_context`` (Q37) and report SKIPPED when it is absent —
distinct from PASSED in the validation result.

Extension numbering: extensions are keyed ``[step][letter]`` and
match main-scenario steps exactly; extensions are rewritten whole
when steps change (documentation standards).

.. todo::
   :class: warning

   **Create troubleshooting pages for UC-03**
   Referenced behaviours needing pages under ``user/troubleshooting/``:

   - phoneme not in inventory (extension 3a)
   - file I/O errors (extension 7a)

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Access Constraint Editor] --> B[Select Constraint Type]
       B --> C[Configure Parameters + Domain]
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
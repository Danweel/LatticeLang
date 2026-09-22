.. _UC-005_serialize_deserialize:
.. _uc005:

UC-005: Serialize/Deserialize LanguageDefinition
=================================================

:Doc Status: Audited
:Goal Level: Subfunction
:Impl Status: Not Started
:Phase: Beta

Goal
----
Serialize a ``LanguageDefinition`` object to a JSON file on disk,
and deserialize a JSON file into a validated ``LanguageDefinition``
object. This subfunction enables persistence, sharing, and loading
of preset definitions.

Preconditions
-------------
- For serialization: a ``LanguageDefinition`` object exists in
  memory.
- For deserialization: a valid file path exists on disk.

Main Success Scenario
---------------------
Serialize:

1. The system receives a ``LanguageDefinition`` object and a target
   file path → system validates the output path is writable.

2. The system serializes the ``LanguageDefinition`` to JSON,
   including the ``schema_version`` field → calls
   :func:`~latticelang.orthography.json_io.serialize_definition`.

3. The system writes the serialized data to the specified file path
   → calls :func:`~latticelang.orthography.json_io.save_project`.

4. System confirms the file was written successfully.

Deserialize:

5. The system receives a file path → system reads the file and
   parses it as JSON → calls
   :func:`~latticelang.orthography.json_io.load_project`.

6. The system reads the ``schema_version`` field and confirms it
   is a known version.

7. The system reconstructs a ``LanguageDefinition`` object from
   the parsed data.

8. The system validates structural completeness (required fields
   present, referential integrity holds — e.g., phonemes
   referenced in syllable templates exist in the inventory) →
   delegates to :ref:`dc_language_definition` field checks.

9. The system returns the validated ``LanguageDefinition`` to the
   caller.

Postconditions
--------------
On success:

- **Serialize:** a ``.json`` file exists at the specified path,
  containing a complete, round-trippable representation of the
  ``LanguageDefinition``.
- **Deserialize:** a ``LanguageDefinition`` object exists in
  memory, structurally valid and ready for use by either pipeline.

On failure:

- **Serialize:** no file is written (or partial write is cleaned
  up); the original in-memory object is unchanged.
- **Deserialize:** no ``LanguageDefinition`` is created; the
  caller receives a descriptive error.

Extensions
----------
**1a (Serialize):** Output path not writable.
  - 1a1: System raises a ``SerializationError`` with the path and OS reason.

**5a (Deserialize):** File does not exist.
  - 5a1: System raises ``FileNotFoundError`` with the attempted path.

**5b (Deserialize):** File exists but is not valid JSON.
  - 5b1: System raises ``DeserializationError`` indicating parse failure
    and the position if available.

**6a (Deserialize):** ``schema_version`` field is missing.
  - 6a1: System raises ``DeserializationError``: "Missing schema_version —
    file may be from an older LatticeLang version."

**6b (Deserialize):** ``schema_version`` is newer than the loader supports.
  - 6b1: System raises ``DeserializationError`` with the file's version and
    the highest supported version.
  - 6b2: Message recommends updating LatticeLang.

**6c (Deserialize):** ``schema_version`` is older than the current version.
  - 6c1: System raises ``DeserializationError`` describing the version mismatch.

  .. note:: Automated migration is **post-MVP**. The version field is included now so the hook exists, but the MVP does not implement migration logic.

**8a (Deserialize):** Structurally incomplete — missing a required section (e.g., no phoneme inventory).
  - 8a1: System raises ``ValidationError`` naming the missing section.

**8b (Deserialize):** Referential integrity failure — syllable template references a phoneme not in the inventory.
  - 8b1: System raises ``ValidationError`` naming the orphan reference and its location.

Frequency
---------
High — called by nearly every User Goal use case (UC-01, UC-02, UC-03, UC-04, UC-07) and by the GUI live preview (UC-08).

Related
-------

**Called by:**
- :ref:`uc01` — Define Phoneme Inventory
- :ref:`uc02` — Define Syllable Structure
- :ref:`uc03` — Define Constraints
- :ref:`uc04` — Generate Words
- :ref:`uc07` — Export to LaTeX

**Data contract:** :ref:`dc_language_definition`

Variations
----------

* **Via Python API (Beta):**

  .. code-block:: python

     from latticelang.orthography.json_io import (
         save_project, load_project
     )

     # Serialize
     save_project(definition, "my_language.json")

     # Deserialize
     definition = load_project("my_language.json")

Notes
-----

The serialization format (field names, nesting structure, JSON
schema) is documented in :ref:`dc_language_definition`, not in
this use case. This follows Cockburn's recommendation to keep
interface details in separate field-list documents.

The ``english_ga.json`` preset is an example of a deserialized
``LanguageDefinition``, but the format must accommodate all
fields the core engine requires — not just what the preset
currently exercises.

.. warning::
   The boundary between **structural validation** (UC-005: "does
   the data hang together?") and **phonotactic validation**
   (UC-013: "does a generated syllable obey the rules?") is
   **pending further thought**. See :ref:`note_uc005_vs_uc013`
   in the syllable template data contract for the current working
   assumption and open questions.
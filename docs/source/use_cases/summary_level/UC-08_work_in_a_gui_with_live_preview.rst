.. _UC-08_work_in_a_gui_with_live_preview:
.. _uc08:

UC-08: Work in GUI with Live Preview
====================================

:Doc Status: Draft
:Goal Level: Summary
:Impl Status: Not Started
:Phase: Gamma

Goal
----

The user works in a graphical interface where edits to the
phonology (phonemes, templates, constraints) immediately
regenerate and display sample words. The live preview provides
rapid feedback so the user can iterate toward a language that
matches their intention.

Preconditions
-------------

- A ``LanguageDefinition`` is loaded (either from file or newly
  created).
- Phase Beta core engine is functional (generation, validation,
  serialization all work via Python API).

Main Success Scenario (User Actions)
------------------------------------

User opens LatticeLang GUI and loads or creates a project.

User navigates between editing panels:
   - Phoneme Inventory panel
   - Syllable Template panel
   - Constraint Editor panel
   - Word List panel (generated words)

User makes a change in any panel (adds a phoneme, edits a template, toggles a constraint).

User observes the live preview pane update with newly generated words reflecting the change.

User evaluates whether the output matches their intention.

Preview regeneration is debounced and coalesced — rapid successive changes trigger a single regeneration of the latest state.

User makes further adjustments or proceeds to export.

Frequency
---------
Continuous during active editing sessions.

Related
-------

**Includes:**
- :ref:`UC-01_define_phoneme_inventory` (editing activity)
- :ref:`UC-02_define_syllable_templates` (editing activity)
- :ref:`UC-03_define_phonotactic_constraints` (editing activity)
- :ref:`UC-04_generate_words` (preview regeneration)
- :ref:`UC-005_serialize_deserialize_LanguageDefinition` (project save/load)

**Adjacent to:**
- :ref:`UC-06_snapshot_comparison_UX`
- :ref:`UC-07_export_to_latex` (accessed from GUI)
- :ref:`UC-008_preview_regeneration`
- :ref:`UC-009_import_words` (accessed from GUI)

Variations
----------

* **Dual-pane layout:** Left side shows editing controls, right
  side shows live word preview. Resizable panes.

* **Tabbed layout:** Tabs for each editing activity. Preview pane
  persistent at bottom or right.

* **Minimal layout:** Single pane with collapsible sections.
  Preview inline below the editor.

Notes
-----

This is a **summary use case** — it describes the user's workflow,
not the system's internal behavior. The implementation details
(PySide6 widgets, signal/slot connections, threading model)
belong in a separate interface specification, not here.

The live preview depends on the Phase Beta core engine being
complete. The GUI is a presentation layer on top of the engine —
it does not contain business logic.

The 50-word preview limit and 300ms debounce are practical
defaults. These should be configurable in settings.

Contextual pedagogical help (e.g., "This phoneme is rare in
natural languages — occurs in [N]% of PHOIBLE languages")
appears as non-blocking, dismissible tooltips triggered by
rarity tiers and constraint violations. The pedagogy system's
data structure is not yet designed — see the TODO below.

.. todo::
   :class: warning

   **Design pedagogy data structure**
   UC-08 references contextual help (tooltips, rarity warnings).
   The pedagogy system needs a design covering:

   - How tooltip content is stored (inline strings vs. IPA
     reference metadata)
   - When warnings trigger (rarity tier threshold, constraint
     violation explanations)
   - How users dismiss/disable pedagogical content

   Follows :ref:`adr-015` (engine/UI separation).Blocked by the
   IPA reference data contract (:ref:`Q38`) and rarity tier
   thresholds (:ref:`Q36`). Track for Phase Gamma.

Flow Diagram
------------

.. mermaid::

   graph TD
       A[Open project] --> B[Display editing panels + preview]
       B --> C[User makes change]
       C --> D{Change type?}
       D -->|Phoneme| E[Update inventory]
       D -->|Template| F[Update templates]
       D -->|Constraint| G[Update constraints]
       E --> H[Debounce 300ms]
       F --> H
       G --> H
       H --> I[Regenerate 50 words]
       I --> J[Update preview pane]
       J --> K{User satisfied?}
       K -->|No| C
       K -->|Yes| L[Continue to export or save]
.. _dc_orthography_rules:

Orthography Rules Data Contract
===============================

:data structure: OrthographyRules
:owner: Phonology Tool
:created by: UC-011 (Define Orthography Mapping); consumed by
   UC-009 (Import Words), UC-015 (Apply Orthography Rules)
:status: Draft — canonical orientation confirmed (roman→IPA)

Overview
--------

An ``OrthographyRules`` object defines the mapping between
romanized letter sequences and IPA phoneme representations for
a specific dialect. It is used to convert user-provided
romanized words to IPA during the import workflow (UC-009).

Canonical orientation: rules are stored as **roman→IPA** to
support batch import and automatic inference. The export
workflow (UC-015) displays the inverse mapping; the system
maintains consistency between the two views.

.. _dc_conversion_rule:

Information Nicknames
---------------------

- **orthography profile** — a named set of conversion rules for a
  specific dialect (e.g., "General American")
- **conversion rule** — a single mapping from romanized sequence
  to IPA symbol or sequence (storage orientation: roman→IPA)
- **context condition** — optional conditions that limit when a
  rule applies (post-MVP; MVP uses unconditional rules)

Field List
----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 10 55

   * - Field
     - Type
     - Required
     - Description
   * - ``profile_name``
     - string
     - Yes
     - Identifying name (e.g., ``"american_english"``).
   * - ``description``
     - string
     - Yes
     - Human-readable description.
   * - ``rules``
     - array
     - Yes
     - Array of conversion rule objects. See
       :ref:`dc_conversion_rule`.
   * - ``exceptions``
     - array
     - No
     - Exception list (words that break the normal rules).
       Each exception specifies a romanized word and its
       expected IPA.

Field Details
-------------

``profile_name``
   Lowercase alphanumeric with underscores; unique across
   all profiles. Used as the profile identifier when users
   select a dialect. Default: ``"american_english"``.

``description``
   Brief explanation of the dialect covered. May include notes
   on regional variation or limitations.

``rules``
   Array of conversion rule objects (see `Conversion Rule
   Structure`_ below). **Array order is semantic** — rule
   order determines tie-breaking among same-length mappings,
   and this order must survive serialization round-trips
   (:ref:`uc005`).

   The **default profile** for initial imports is
   ``american_english`` (General American), chosen as the
   largest English speaker population and the one already
   encoded in the reference table. Additional profiles
   inherit from or override it via explicit selection (Q2,
   Q3; dialect inheritance is post-MVP).

``exceptions``
   Array of objects specifying words that break the normal
   rules:

   .. code-block:: json

      {
        "roman": "cello",
        "ipa": "tʃɛloʊ"
      }

   Exceptions take precedence over rules — they're checked
   first. Unconditional exceptions are MVP; contextual
   exceptions (conditions attached to exceptions) are
   post-MVP.

Conversion Rule Structure
-------------------------

Each rule in the ``rules`` array has the following structure:

.. code-block:: json

   {
     "roman": "ch",
     "ipa": "tʃ"
   }

Fields:

- ``roman``: string — the romanized sequence to match
  (e.g., ``"ch"``, ``"sh"``, ``"ea"``).
- ``ipa``: string — the IPA symbol(s) to produce
  (e.g., ``"tʃ"``, ``"i:"``).

Uniqueness: no two rules may share the same ``roman`` value
(UC-03-style conflict; replacement is explicit).

Validation at save: each IPA symbol exists in the inventory
(warn per UC-11 extension 2a; partial coverage is a supported
steady state).

**Interpretation Semantics** (MVP):

1. **Longest-match**: among all rules whose ``roman`` prefix
   matches the input position, the longest matching sequence
   wins (Q1, ADR-043).
2. **Definition order**: among same-length matches, the
   earlier rule in the array wins (ties broken by index).
3. **Left-to-right scan**: the segmenter processes input
   sequentially, consuming matched sequences and advancing
   position.

Contextual rules (grapheme choice conditioned on neighboring
segments) are post-MVP — see the UC-11/UC-015 todo directives.
Adding them requires changing UC-011, UC-015, and UC-009
together.

Inverse View (Export)
---------------------

UC-015 (apply orthography rules) walks the stored rules in
reverse to produce IPA→roman mappings for display. The
inverse view is generated dynamically — it is not stored
separately. Longest-match semantics apply symmetrically,
but the priority order reverses (earlier rules in the
stored array become later in the inverse order).

Field Checks
------------

#. ``profile_name`` is unique across all loaded profiles.
#. No duplicate ``roman`` values in the ``rules`` array.
#. Every IPA symbol in ``rules`` and ``exceptions`` is valid
   per the IPA reference table (:ref:`dc_ipa_reference`).
#. Every IPA symbol in ``rules`` exists in the phoneme
   inventory (:ref:`dc_phoneme`; warn, partial coverage OK).

Relationship to Inverse Workflow
--------------------------------

UC-011 defines the mapping from the user's perspective
("here's how my sounds spell"). UC-015 applies the mapping
to generate romanized output. Both operate on the same
stored rules; the direction (roman→IPA vs. IPA→roman) is
a traversal choice, not a schema choice. This contract's
canonical orientation is roman→IPA because that's the
direction batch import needs (UC-009).

Research Notes
--------------

Dialect Profile Selection
^^^^^^^^^^^^^^^^^^^^^^^^^

Users self-report their dialect at import time (UC-009). The
selected profile is stored in ``LanguageDefinition.import_dialect_profile``
as provenance metadata. This is a one-time decision — after
corpus translation to IPA, the profile doesn't affect subsequent
workflows. MVP ships a single mandatory profile (``american_english``)
with no user choice; expansion to additional profiles is post-MVP
(Q2, Q3).

See :ref:`q2-dialect-rules` for the dialect inheritance architecture
(separate documents with explicit inheritance pointer).

See :ref:`q3-dialect-coverage` for candidate dialect expansion.

References
----------

- :cite:p:`rosenfelder2010`, chapter on Sounds and Orthography
  (workflow shape).
- :ref:`adr-043` (maximal-munch / longest-match).
- :ref:`adr-050` (confidence tiers for ambiguous mappings).
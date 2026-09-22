.. _dc_ipa_reference:

IPA Reference Table Data Contract
=================================

:data structure: IPAReferenceTable
:used by: UC012 (Segment IPA Input), UC009 (Import Words), UC01 (Define Phoneme Inventory)
:status: Draft — per-symbol sonority_rank and tipa landed this round; ready for MVP implementation pending build-script verification

.. note::
   This contract was reviewed during the 2026-09-16 use-case
   and spec-completeness audit. See :ref:`audit-september-2026`
   for the full findings table. Key design decisions:
   :ref:`adr-047` (logical schema vs. adapters),
   :ref:`adr-048` (tone as separate stage),
   :ref:`adr-049` (coordinate-addressed random streams),
   :ref:`adr-050` (qualitative ambiguity tiers).

.. _ipa_reference:

Overview
--------

An ``IPAReferenceTable`` is a comprehensive list of all valid
IPA symbols for consonants and vowels. It serves as the ground
truth for validating IPA input during segmentation and orthography
conversion. Multi-character symbols (e.g., affricates like ``"tʃ"``)
are explicitly listed.

Information Nicknames
---------------------

- **IPA symbol** — a single phoneme representation (may be one or
  multiple Unicode codepoints)
- **diacritic** — a combining character that modifies a base symbol
  (e.g., aspiration ``"ʰ"``, length ``"ː"``)
- **tie bar** — a combining character linking two symbols as a
  single unit (e.g., tie bar in ``"t͡s"``)

Field List
----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 10 55

   * - Field
     - Type
     - Required
     - Description
   * - ``version``
     - string
     - Yes
     - Version of the IPA standard this table reflects
       (e.g., ``"2020"`` for the most recent chart).
   * - ``last_updated``
     - string (ISO date)
     - Yes
     - Date the table was last reviewed/updated.
   * - ``consonants``
     - array
     - Yes
     - Array of consonant symbol objects.
   * - ``vowels``
     - array
     - Yes
     - Array of vowel symbol objects.
   * - ``diacritics``
     - array
     - No*
     - Array of diacritic symbol objects.
   * - ``special_combinations``
     - array
     - No
     - Array of known multi-symbol sequences (e.g., affricates,
       diphthongs) that must be treated as single units.

.. *In MVP, diacritics are handled implicitly via Unicode
   normalization. Explicit diacritics array may be added
   post-MVP for extensibility.

Field Details
-------------

``version``
~~~~~~~~~~~

- IPA chart publication year (e.g., ``"2005"``, ``"2020"``).
- Allows validation against known chart versions.
- Enables migration if the IPA standard changes significantly.

``last_updated``
~~~~~~~~~~~~~~~~

- ISO 8601 date (e.g., ``"2026-08-24"``).
- Indicates when this table was generated/reviewed.
- Useful for detecting stale data.

``consonants``
~~~~~~~~~~~~~~

Array of consonant symbols. Each entry:

.. code-block:: json

   {
     "symbol": "p",
     "description": "Voiceless bilabial plosive",
     "place": "bilabial",
     "manner": "plosive",
     "voicing": "voiceless",
     "sonority_rank": 1,
     "unicode_points": ["U+0070"],
     "canonical_forms": ["p", "p"],
     "aliases": [],
     "tipa": "\\textpm"
   }

Fields:


- ``symbol``: The canonical IPA symbol.
- ``description``: Human-readable description (for tooltips/help).
- ``place``: Place of articulation (e.g., ``"bilabial"``,
  ``"alveolar"``, ``"velar"``).
- ``manner``: Manner of articulation (e.g., ``"plosive"``,
  ``"fricative"``, ``"nasal"``).
- ``voicing``: Voicing (``"voiceless"``, ``"voiced"``).
- ``sonority_rank``: Integer or null. Proposed rank from the
  derivation table (:cite:p:`clements1990` basis,
  :cite:p:`kramer2020` nasal simplification noted in the
  derivation doc). Null means "propose manually" — UC-01 treats
  null as a prompt, not an error.
- ``unicode_points``: Unicode codepoints (array for multi-char
  symbols like ``"tʃ"`` → ``["U+0074", "U+0283"]``).
- ``canonical_forms``: Alternate representations (e.g., precomposed
  vs decomposed).
- ``aliases``: Non-canonical forms users might type (e.g.,
  ``["ch", "tsh"]`` for the affricate).
- ``tipa``: String or null. The TIPA macro for LaTeX rendering
  (e.g., ``"ʃ"`` → ``"\\textesh"``), or null when none exists.
  Populated by ``scripts/derive_ipa_reference.py`` merging a
  curated overrides file (same pipeline as Q38). Consumed by
  UC-07's exporter; null is a handled case (raw Unicode +
  warning), not an error.

.. note::
   The MVP includes only consonants from the standard IPA
   chart. Extended IPA (extIPA) for speech pathology is
   **post-MVP**.

``vowels``
~~~~~~~~~~

Array of vowel symbols. Each entry:

.. code-block:: json

   {
     "symbol": "i",
     "description": "Close front unrounded vowel",
     "height": "close",
     "backness": "front",
     "roundedness": "unrounded",
     "unicode_points": ["U+0069"],
     "canonical_forms": ["i", "i"],
     "aliases": []
   }

Fields:

- ``symbol``: Canonical IPA symbol.
- ``description``: Human-readable description.
- ``height``: Vowel height (``"close"``, ``"close-mid"``,
  ``"open-mid"``, ``"open"``).
- ``backness``: Tongue position (``"front"``, ``"central"``,
  ``"back"``).
- ``roundedness``: Lip rounding (``"rounded"``, ``"unrounded"``).
- ``unicode_points``, ``canonical_forms``, ``aliases``: Same as
  consonants.

``diacritics``
~~~~~~~~~~~~~~

.. warning::
   This field is **optional in MVP**. For MVP, diacritics are
   handled implicitly via Unicode normalization. Post-MVP,
   explicit diacritic support enables features like:
   - Diacritic lookup in help tooltips
   - Custom diacritic combinations
   - Filtering by diacritic type

Array of diacritic objects:

.. code-block:: json

   {
     "symbol": "ʰ",
     "description": "Superscript h (aspiration)",
     "unicode_points": ["U+02B0"],
     "combines_with": ["consonants"],  // categories
     "position": "superscript"          // "superscript", "below", etc.
   }

``special_combinations``
~~~~~~~~~~~~~~~~~~~~~~~~

Array of multi-symbol sequences that must be treated as single
units during segmentation:

.. code-block:: json

   {
     "combination": "tʃ",
     "description": "Voiceless palato-alveolar affricate",
     "constituents": ["t", "ʃ"],
     "category": "affricate",
     "unicode_points": ["U+0074", "U+0283"]
   }

This ensures the segmenter recognizes ``"tʃ"`` as one phoneme,
not two.

``tipa``
   String or null. The ``tipa`` macro string for rendering this
   symbol in LaTeX (e.g., ``"ʃ"`` → ``"\\textesh"``), or null
   when no macro exists (expected for rare segments — clicks,
   some modifier stacks). Populated by
   ``scripts/derive_ipa_reference.py`` merging a curated
   overrides file (same pipeline as Q38). Consumed by UC-07's
   exporter; null is a handled case (raw Unicode + warning), not
   an error.

Field Checks
------------

#. No duplicate ``symbol`` values across all arrays.
#. All ``unicode_points`` are valid Unicode codepoints for IPA
   characters.
#. ``canonical_forms`` includes the ``symbol`` value.
#. ``special_combinations`` entries are consistent with the
   ``unicode_points`` in ``consonants`` and ``vowels``.
#. ``version`` corresponds to an actual IPA chart release.

Location
--------

The reference table is stored as a single JSON file in the data
directory: ``data/ipa_reference.json``. Consonant/vowel subsets
are runtime filters, not separate files — a few hundred entries
load in milliseconds, and one file triples the update surface
of none benefit.

Implementation Notes
--------------------

The reference table should be **read-only** at runtime. It's
loaded once at startup and cached in memory.

The table is maintained separately from the user's phoneme
inventory. The reference table contains **all valid IPA
symbols**; the inventory contains **this language's phonemes**.

For MVP, only **standard consonants and vowels** are included.
Click consonants, and other special categories are
post-MVP additions.

References
----------

- :cite:p:`ipa1999` (the IPA Handbook — chart source).
- :cite:p:`moran2019` (PHOIBLE 2.0 — feature and attestation
  data feeding the derive script, Q38).
- Unicode Consortium. *Unicode Standard*. Codepoint ranges for
  IPA characters; pin the version when the derive script freezes
  its input.
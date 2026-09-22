.. _UC-012_segment_ipa_input:
.. _uc012:

UC-012 Segment IPA Input
========================

:Doc Status: Draft
:Goal Level: Subfunction
:Impl Status: Not started
:Phase: Beta

Goal
----
Convert one IPA string into an ordered list of phoneme segments,
resolving ambiguity by longest-match and inventory preference,
and returning visible ambiguity flags. Pure function: no
randomness, no side effects, no caller knowledge.

Preconditions
-------------
- The IPA reference table is loaded (:ref:`dc_ipa_reference`, :ref:`Q38` artifact)

Inputs
------
- ``ipa_string``: the text to segment
- ``inventory`` (optional): confirmed phoneme symbols; presence
  activates inventory-preferred resolution

Main Success Scenario
---------------------

1. System receives the IPA string; validates it is non-empty
   text

2. System normalizes the string to the reference table's
   canonical form — NFC for storage contexts (:ref:`uc009`
   step 4); normalization is deliberate per context and never
   unified (ADR-041's NFD base-stripping is comparison-only)

3. System scans left-to-right. At each position it computes
   candidate matches against the symbol alphabet — inventory
   symbols first, then the full reference — treating tie-bar
   forms as single segments (ADR-028)

4. Among candidates of different lengths, the longest wins
   (Q1; the lexer's maximal-munch rule, ADR-043)

5. Where alternates remain after steps 3–4 (same-length parses,
   or a reading uncorroborated by inventory), the system
   attaches an ambiguity record: position, chosen reading,
   alternates, confidence tier (high / medium / low — Q4)

6. System returns the segment list plus all ambiguity records;
   callers route flags through their own UX (:ref:`uc009`
   review flow; CLI summary line)

Extensions
----------

* **3a:** No symbol matches at the current position
  - 3a1: The character is flagged invalid; segmentation
  continues from the next position
  - 3a2: Nearest-match suggestions come from the reference
  table (:ref:`dc_ipa_reference`)
  - → See :ref:`uc009` extension 5a for the user-facing path

* **4a:** Same-length alternates, inventory present
  - 4a1: The reading whose segments all exist in the inventory
  wins; tie remains → definition order (deterministic default),
  flagged low

* **4b:** Inventory absent (first-pass import)
  - 4b1: Longest-match and definition order carry the decision;
  every such choice is flagged medium
  - 4b2: Results are provisional — :ref:`uc009` re-segments
  after inventory confirmation (two-pass design, see Notes)

* **5a:** Batch context
  - 5a1: Flags accumulate; the segmenter never interrupts,
  never prompts (:ref:`q4-ambiguity-confidence`), :ref:`adr-050`

Postconditions
--------------
- On success: a segment list exists, each segment either a
  reference symbol or flagged invalid; ambiguity records
  accompany every non-unique decision
- On failure: only for empty/non-string input (caller error);
  ambiguity and unknown symbols are *results*, not failures

Related
-------

**Called by:**
- :ref:`uc009` — Import Words (both passes)

**Consumes:**
- :ref:`dc_ipa_reference` (symbol alphabet, nearest matches)

**Leaf** — delegates to nothing below it.

Variations
----------

.. code-block:: python

   from latticelang.core.segmenter import segment_ipa

   result = segment_ipa("kætʃ", inventory=["k", "æ", "t", "ʃ", "t͡ʃ"])
   result.segments      # ["k", "æ", "t͡ʃ"]
   result.ambiguities   # [{position, chosen, alternates, tier}]

Notes
-----

The segmenter is deterministic: same input, same inventory,
same output. No clock, no randomness — the same guarantee
:ref:`uc013` makes for validation.

Two-pass relationship with :ref:`uc009`: segmentation proposes
an inventory (pass one, no inventory input), the user confirms
or corrects it, and re-segmentation (pass two) uses the
confirmed inventory to settle flagged cases. The chicken-and-egg
problem — segmentation needs an inventory, inventory inference
needs segmentation — is resolved by ordering, not by circularity.

Q1 (resolution mechanics) and Q4 (surfacing and batch policy)
meet here; both now carry answers and this case implements them.

Diphthong vs. glide onset vs. hiatus: where the inventory
contains the tie-bar form (e.g., /a͡ɪ/), a matching string
segments as one diphthong phoneme (:ref:`ADR-028`). Where it
contains /j/ or /w/ as margin phonemes, "ja"-type strings
segment as glide+vowel — two phonemes in two structural
positions (:ref:`ADR-034`). Where neither exists, two vowels in
sequence are hiatus: adjacent syllables, each with its own
nucleus. These are three structurally distinct analyses of
similar-looking input, and the confirmed inventory — not the
segmenter's preference — decides which one applies (step 3).
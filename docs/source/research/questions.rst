.. _questions:

Research Questions
==================

This file is the central registry for all open questions, design decisions,
and their resolution status. Questions move through a lifecycle:
**OPEN → ANSWERED → IMPLEMENTED**.

Status Overview (changes)
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 8 42 20 15 15

   * - Q#
     - Topic
     - Status
     - Blocks
     - Related
   * - Q1
     - Segmenter ambiguity resolution
     - ANSWERED (2026-08-23, longest-match + user override) — ADR backfill pending
     - :ref:`uc012`
     - :ref:`dc_orthography_rules`
   * - Q2
     - Dialect rules architecture
     - OPEN (post-MVP; architecture anticipates)
     - Non-blocking
     - :ref:`q23-universal-override-model`, :ref:`dc_constraints`, :ref:`uc005`
   * - Q3
     - Dialect coverage beyond GA/RP
     - OPEN (post-MVP)
     - Non-blocking
     - :ref:`q2-dialect-rules`, :ref:`q33-profile-based-inference`
   * - Q4
     - Ambiguity confidence and batch processing
     - OPEN
     - MVP scope decision
     - :ref:`q1-segmenter-ambiguity`, :ref:`q31-ipa-normalization-input`
   * - Q5
     - Project file versioning; derived-field persistence
     - Persistence sub-question ANSWERED (2026-09-06, :ref:`ADR-032`); versioning main OPEN (suite-deferred)
     - Suite-level
     - :ref:`ADR-033`, :ref:`adr-035`
   * - Q6
     - Feature system = PHOIBLE 2.0, pinned
     - ANSWERED (2026-08-31, :ref:`ADR-033`)
     - Was blocking MVP
     - :ref:`q24-feature-representation`, :ref:`q26-panphon-integration`, :ref:`uc01`
   * - Q7
     - Generation determinism and seed stability
     - Frequency-weight semantics ANSWERED (2026-09-06); seed stability OPEN
     - MVP
     - :ref:`ADR-011`, :ref:`ADR-024`
   * - Q8
     - Constraint expressiveness beyond MVP types
     - ANSWERED at design level (2026-09-09, :ref:`ADR-037`); interface validation remains open
     - Pre/post-MVP design
     - :ref:`ADR-022`, :ref:`ADR-039`, :ref:`constraints`
   * - Q9
     - Morpheme storage and allomorphy
     - OPEN
     - Phase Delta
     - N/A
   * - Q10
     - Etymology tracking granularity
     - OPEN
     - Phase Epsilon
     - N/A
   * - Q11
     - Syntax rule formalism
     - OPEN
     - Phase Epsilon
     - N/A
   * - Q12
     - Interlinear glossing standard
     - OPEN
     - Phase Epsilon
     - N/A
   * - Q13
     - Semantic field ontology
     - OPEN
     - Phase Epsilon
     - N/A
   * - Q14
     - Unicode and IPA font management
     - OPEN
     - Phase Gamma/Epsilon
     - N/A
   * - Q15
     - Module isolation and testing
     - OPEN
     - Suite-level
     - N/A
   * - Q16
     - Community and language sharing
     - OPEN
     - Phase Delta+
     - N/A
   * - Q17
     - Performance envelope
     - OPEN
     - Phase Gamma benchmarks
     - N/A
   * - Q18
     - Accessibility
     - OPEN (cross-cutting)
     - Deferred
     - N/A
   * - Q19
     - UI internationalization
     - OPEN
     - Phase Delta+
     - N/A
   * - Q20
     - License compatibility (PHOIBLE)
     - ANSWERED (2026-08-24) → IMPLEMENTED
     - Resolved
     - :ref:`adr-029`, :ref:`dc_ipa_reference`, :ref:`bibliography`
   * - Q21
     - CoNLL-U interchange format
     - OPEN
     - Phase Delta
     - N/A
   * - Q22
     - UniMorph integration
     - OPEN
     - Phase Delta
     - N/A
   * - Q23
     - Universal→override model
     - DESIGN (architecture pattern, not implemented)
     - Informs Q2
     - :ref:`q2-dialect-rules`
   * - Q24
     - Feature representation
     - ANSWERED (2026-08-31, :ref:`ADR-033`)
     - Resolved with Q6
     - :ref:`q6-feature-system-adoption`, :ref:`dc_phoneme`
   * - Q25
     - Constraint DSL
     - ANSWERED (2026-09-09, :ref:`ADR-037`) — built-ins only; DSL post-MVP
     - Resolved for MVP
     - :ref:`constraints`
   * - Q26
     - panphon integration
     - ANSWERED (2026-08-31, :ref:`ADR-033`) — downgraded to post-MVP optional
     - Non-blocking
     - :ref:`ADR-010`
   * - Q27
     - GUI state management
     - OPEN (lean: PySide6 signals/slots)
     - Phase Gamma
     - N/A
   * - Q28
     - Test dialect (GA vs RP)
     - OPEN
     - Phase Beta
     - :ref:`adr-009`
   * - Q29
     - Syllable boundary detection
     - OPEN (lean: boundaries by construction)
     - Non-blocking
     - :ref:`q35-prohibited-clusters-domain`
   * - Q30
     - MyST dollarmath in docs
     - ANSWERED → IMPLEMENTED
     - Resolved
     - N/A
   * - Q31
     - IPA normalization for user input
     - OPEN (lean: hybrid)
     - Orthography design
     - :ref:`q1-segmenter-ambiguity`, :ref:`dc_orthography_rules`
   * - Q32
     - Orthography complexity scope
     - OPEN (lean: one-to-one + context pairs)
     - Phase Beta
     - N/A
   * - Q33
     - Profile storage shape
     - OPEN (must fit Q41's ranked mappings)
     - Data-contract design now
     - :ref:`q41-corpus-inference`, :ref:`q3-dialect-coverage`
   * - Q34
     - Harmony constraint MVP scope
     - ANSWERED (2026-09-06, :ref:`ADR-039`)
     - Resolved
     - :ref:`q42-harmony-parameterization`
   * - Q35
     - Prohibited clusters domain parameter
     - ANSWERED (2026-09-06, :ref:`ADR-039`)
     - Resolved
     - :ref:`dc_constraints`
   * - Q36
     - Rarity tier thresholds
     - OPEN (provisional buckets in build script)
     - Blocks tier 6 decision
     - :ref:`q38-ipa-reference-sourcing`
   * - Q37
     - Constraint interface word_context parameter
     - ANSWERED (2026-09-06, :ref:`ADR-039`)
     - Resolved
     - :ref:`UC013`, :ref:`dc_constraints`
   * - Q38
     - IPA reference sourcing
     - ANSWERED (2026-08-31, :ref:`ADR-033`) — hybrid
     - Build script = Phase Beta tooling
     - :ref:`q36-rarity-tier-finalization`, :ref:`adr-029`
   * - Q39
     - Merge semantics for duplicate symbols
     - ANSWERED (2026-09-06, :ref:`ADR-040`)
     - Blocked by UC01 implementation
     - :ref:`UC01`, :ref:`dc_phoneme`
   * - Q40
     - Near-miss symbol similarity
     - ANSWERED (2026-09-06, :ref:`ADR-041`)
     - Blocked by UC01 implementation
     - :ref:`UC01`
   * - Q41
     - Corpus inference strategy
     - OPEN (post-MVP anticipation)
     - Non-blocking; shapes Q33
     - :ref:`q33-profile-based-inference`, :ref:`UC009`
   * - Q42
     - Harmony parameterization
     - ANSWERED (2026-09-09, :ref:`ADR-042`)
     - Resolved
     - :ref:`ADR-033`, :ref:`dc_constraints`
   * - Q43
     - Nasal sonority Split
     - OPEN
     - Deferred — Post-MVP Exploration
     - :ref:`ADR-038`, :term:`sonority`, :ref:`constraint-types-overview`
   * - Q44
     - Maxent Phonotactic Learning
     - OPEN
     - Deferred — Post-MVP Exploration
     - :ref:`q23-universal-override-model`, :ref:`constraint-types-overview`, :term:`optimality theory`, :term:`faithfulness constraint`
   * - Q45
     - OT Learnability Framework
     - OPEN
     - Deferred — Post-MVP Research
     - :ref:`q44-maxent-phonotactic-learning`, :ref:`theoretical_framework`, :term:`optimality theory`

Gap Analysis: MVP Impact
------------------------

Questions that could block MVP progress if unresolved:

.. csv-table::
   :header-rows: 1
   :widths: 10 50 40

   "ID","Why it matters","Action needed"
   "Q1","UC012 (orthography conversion) depends on this","Decide: longest-match with user override"
   "Q6","Feature system affects OCP/harmony constraints","Decide: adopt standard or keep free-form"
   "Q7","Affects live preview usefulness (ADR-011)","Prototype seed stability behavior"
   "Q8","Constraint interface must support post-MVP types","Validate interface against post-MVP constraint list"
   "Q24","Phoneme data contract depends on this","Decide: enum vs strings vs hybrid"
   "Q26","OCP/harmony need feature validation","Decide: panphon or own feature set"
   "Q28","Test language dialect choice","Decide: GA primary, RP secondary"
   "Q29","Word display format","Confirm: boundary marker for generated words"
   "Q32","Orthography data contract scope","Confirm: one-to-one + context pairs"
   "Q34","Harmony constraint scope confirmation","Confirm: within-syllable only for MVP"
   "Q35","Prohibited clusters need domain parameter","Add domain field to constraint data contract"
   "Q36","Rarity tier 6 for unattested sounds","Confirm: add tier 6 to IPA reference"
   "Q37","Constraint interface word_context parameter","Confirm interface accepts optional word context"

Questions
---------

.. _q1-segmenter-ambiguity:

Q1: Segmenter Ambiguity Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: danger

   **Status:**
   Blocks :ref:`UC012`
   Answered :ref:`ADR-014`

   **Question:**
   When segmenting romanized text to IPA, some sequences are ambiguous.
   Does "ts" represent the affricate /t͡s/ or the sequence /t/ + /s/?

   **Options considered:**

   1. Longest-match heuristic (prefer affricate over sequence)
      Prefer affricates when a valid affricate exists in the inventory,
      with user override.
      Consequences - segmenter always commits, batch processing never
      blocks, and it composes cleanly with ADR-028 — since ADR-028
      already normalizes input to tie-bar form internally, "ts"
      typed without a tie bar normalizes to /t͡s/, which is longest-match
      in disguise. The two decisions reinforce each other.
      Override path - user can configure per-language preference
      in the LanguageDefinition.
      Cost - minimal — longest-match is a greedy pass over the
      orthography rules, already sorted by length.

   2. User-configured preference in LanguageDefinition
      Shifts the decision to every user — the "remembering"
      failure mode ADR-035 prohibits.

   3. Context-sensitive rules (e.g., "ts" before vowel = affricate,
      otherwise sequence) More linguistically accurate in some cases
      (English "ts" in "cats" is sequence + affricate-adjacent),
      but requires conditioning context in the data contract,
      is harder to explain in tooltips, and batch mode still
      can't resolve everything. Post-MVP refinement at best.

   4. Require explicit tie bar in input
      Honest but hostile: users can't easily type U+0361,
      and corpus import (UC009) receives romanized text
      with no tie bars at all — this option breaks the
      reverse pipeline entirely.

   **Preferred approach:**
   Longest-match with user override. Default: prefer affricates when a
   valid affricate phoneme exists in the inventory.

   **Dependencies:**
   - Orthography rules data contract
   - User-facing configuration UI

   **Action items:**

   - [x] Decide on default behavior (adr-043)
   - [ ] Document longest-match policy in :ref:`UC012`
   - [ ] Note segmenter behavior in ``dc_orthography_rules``
   - [ ] (Later) Suggest tests: "ts" → /t͡s/ with affricate in inventory;
     "ts" → /t/ + /s/ without

.. _q2-dialect-rules:

Q2: Dialect Rules Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: danger

   **Status:** OPEN (post-MVP, architecture should anticipate)

   **Question:**
   Should dialect variants be separate LanguageDefinition objects, or a
   single object with multiple constraint sets? How do we handle inherited
   features (parent → child dialect)?

   **Options considered:**

   1. Separate documents with inheritance chain (JSON refs)
   2. Single document with "variant" sections
   3. Plugin-based dialect system
   4. Defer entirely to post-MVP

   **Preferred approach:**
   Separate documents with explicit inheritance pointer, inspired by the
   Universal Dependencies universal→override model. See :ref:`q23-universal-override-model`.

   **Dependencies:**
   - :ref:`dc_constraints`
   - Serialization/deserialization (:ref:`UC005`)

   **Impact on MVP:**
   None — dialects are post-MVP. Architecture should support this pattern
   without requiring changes.

.. _q3-dialect-coverage:

Q3: [PHONO] Dialect Coverage Beyond GA and RP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (post-MVP)

   **Question:**
   Beyond General American and Received Pronunciation, which dialects
   should LatticeLang eventually support? Candidates include:

   - Australian English (different vowel shifts)
   - General Indian English (large speaker population, likely L2)
   - Non-English L2 mappings (a Spanish speaker's romanization
     differs from an English speaker's)

   Should dialect profiles be a first-class data type that the
   community can contribute? If so, what format?

   **Context:**
   This is an extensibility question that affects the data contract
   design now, even if we only ship two profiles initially.

   **Related:**
   - :ref:`q2-dialect-rules` (dialect rules architecture)
   - :ref:`q33-profile-based-inference`

   **Action items:**

   - [ ] Decide: community-contributable dialect profiles (post-MVP)
   - [ ] Ensure data contract design doesn't preclude this

.. _q4-ambiguity-confidence:

Q4: [PHONO] Ambiguity Confidence Levels and Batch Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** (partially overlaps :ref:`q1-segmenter-ambiguity`)
   ANSWERED (2026-09-16, UC-012 draft; optional formal record in :ref:`ADR-050`)

   **Question:**
   When the segmenter resolves ambiguity (e.g., "ts" → /t͡s/ or
   /t/+/s/), should the confidence level be surfaced to the user?
   How does this interact with batch processing where asking
   per-word is impractical?

   **Resolution strategies considered:**

   - User's inventory (preferred — does /t͡s/ exist?)
   - Longest-match heuristic (fallback)
   - Frequency statistics (are affricates common in this language?)
   - User disambiguation (ask — tedious for long word lists)

**Resolution:**

   - Confidence is surfaced: qualitative tiers
     (high / medium / low), attached per ambiguity,
     accumulated across a batch. The segmenter never
     interrupts or prompts (batch-mode policy).
   - Resolution order: user inventory → longest-match →
     definition order (deterministic default, flagged low).
   - Frequency-statistics resolution: rejected for MVP —
     statistical learning boundary (:ref:`ADR-045`).
   - Corrections route through UC-009's review flow,
     including apply-to-all (:ref:`uc009` extension 6a).

   **Implemented by:** :ref:`uc012` (steps 5–6, extensions
   4a–5a). **Related:** :ref:`q1-segmenter-ambiguity`
   (mechanics — still owns resolution internals).

   **Related:**
   - :ref:`q1-segmenter-ambiguity` (segmenter ambiguity resolution)
   - :ref:`q31-ipa-normalization-input`

   **Action items:**

   - [x] Decide: should confidence be surfaced in MVP? Yes.
   - [x] Design batch-mode behavior (default to best guess, flag
     uncertain items)

.. _q5-project-file-versioning:

Q5: [SUITE] Project File Versioning Across Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:**
   OPEN (suite-level, deferred)

   **Question:**
   If Module 1 (Phonology) is at schema version 1.3 but Module 2
   (Morphology) is at version 1.0 (added later), how do we handle
   version mismatches?

   **Options:**

   1. Per-module version fields (flexible, complex)
   2. Whole-project version (simple, forces coordinated upgrades)
   3. No versioning (honest but painful for users with existing projects)

   **Current approach:**
   Front-loaded schema versioning into the LanguageDefinition (see
   :ref:`dc_language_definition`). Does that decision scale to a
   multi-module project file?

   **Action items:**

   - [ ] Validate schema versioning design when Module 2 is planned
   - [ ] Consider per-module version fields vs whole-project version

   **Sub-question** (from :ref:`adr-032`)
   Category is now a *derived* field on ``Phoneme``. Should
   serialized JSON store category (denormalized — fast load,
   but can drift from features if hand-edited) or recompute on
   load (clean, but a schema-version change alters derivations
   silently)?

   **Options:**

   1. Store and validate on load (recompute, warn on mismatch)
   2. Recompute always (category is never serialized)
   3. User-configurable strictness

   **Tentative lean:** option 1 — store for transparency and
   hand-editability, recompute on load, warn on divergence.

   **Derived-field persistence (ADR-032 sub-question): ANSWERED
   (2026-09-06).** Serialized JSON **stores** ``category`` and
   ``sonority_rank``; the loader **recomputes** both and **warns
   on divergence**, retaining the stored values. Rationale:
   stored values keep files hand-editable and diffable;
   recompute-with-warning makes drift visible instead of
   corrosive. A mismatch is a soft warning, never a load failure
   (:ref:`adr-035` - never block on best-guess discrepancies).
   Data contracts follow the same separation: field tables describe
   semantics; concrete types, classes, and signatures live in
   an Implementation Bindings section.

   - I believe this is about merging: Divergence indicates either a feature edit was made without refreshing category or the derivation table changed between versions. Should not auto-correct. See :ref:`dc_inventory`.

.. _q6-feature-system-adoption:

Q6: [PHONO] Feature System Standard Adoption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-08-31) → Implemented via :ref:`adr-033`

   **Question:**
   Should LatticeLang adopt a standard feature system for the
   ``Phoneme`` data contract, and if so, which one?

   **Why this matters beyond validation:**
   Adopting a standard feature system has a second consequence:
   **phoneme category becomes derivable from features.** The three
   major class features ([±syllabic], [±consonantal],
   [±sonorant]) partition all speech sounds, so the
   consonant/vowel/glide distinction falls out mechanically:

   .. csv-table::
      :header-rows: 1
      :widths: 25 30 45

      "Category","Feature signature","Notes"
      "consonant","−syllabic, +consonantal","Stops, fricatives, affricates, nasals, liquids"
      "vowel","+syllabic, −consonantal","Monophthongs"
      "glide","−syllabic, −consonantal","/j/, /w/ — feature-wise ambiguous residue"
      "diphthong","(sequence, not features)","Stored as single phoneme with ``components`` — documented deviation"

   This would replace the LCK-style manual category selection
   (Rosenfelder's workflow) with literature-grounded derivation.
   The LCK ordering survives only as the wizard's *presentation
   order*, which is pedagogically sound.

   **Options:**

   1. **SPE features** — the classic system from
      :cite:t:`chomsky1968`. Well-documented, widely taught,
      but notation predates the feature-geometry refinements.
   2. **Feature Geometry (Clementian)** — hierarchical trees
      per :cite:p:`clements1985` :cite:p:`clements1995`.
      Best fit for our OCP/harmony constraints and for future
      autosegmental spreading. More complex data model.
   3. **panphon's feature set** — practical, already encoded,
      but third-party (see :ref:`q26-panphon-integration`).
   4. **Free-form dicts** (current sketch) — maximum flexibility,
      no validation, fragile rules.

   **Preferred approach:**
   Adopt a standard system as the *built-in default* (leaning
   toward Feature Geometry subset for MVP: major class + place +
   laryngeal + manner, without full subscript machinery), keep
   the feature dict open for custom features, and **derive
   category from features** with manual override for syllabic
   consonants, custom symbols, and other edge cases.

   **Dependencies:**
   - :ref:`q24-feature-representation` (enum vs strings — this
   question narrows it: standard features should be controlled
   vocabulary)
   - :ref:`q26-panphon-integration` (panphon's system as a
   shortcut vs rolling our own)
   - :ref:`ADR-022` (extensible constraints — OCP/harmony depend on it)
   - :ref:`UC01` (step 2 changes if we derive category)

   **Consequences if adopted:**
   - :ref:`UC01` step 2 becomes "system derives category → user confirms or overrides"
   - New category value needed: ``glide``
   - Diphthong-as-single-phoneme documented as deviation in :ref:`theoretical_framework`
   - Custom symbols (not in IPA reference) keep manual category

   **Action items:**

   - [ ] Compare SPE vs Feature Geometry subset for MVP scope
   - [ ] Decide before finalizing the Phoneme data contract
   - [ ] Update :ref:`UC01` steps 2–3 to match the decision
   - [ ] Add ``glide`` to category set if derived

   5. **PHOIBLE's feature system** — the system PHOIBLE uses for
      all 3,183 segments, loosely based on :cite:t:`hayes2009` with
      laryngeal additions (:cite:t:`moisik2011`). Already mapped to
      every attested IPA segment; CC-BY 4.0; distributed as a
      parseable TSV. Substantially de-risks
      :ref:`q38-ipa-reference-sourcing` because adopting it
      makes the reference dataset and the feature vocabulary
      the *same* artifact. Caveat: PHOIBLE states the system
      "may change as new languages are added" — we would pin to
      the 2.0 release.

   **Edge cases the decision must cover:**

   - Syllabic consonants (/n̩/): +syllabic, +consonantal breaks
     the clean four-way category table; needs an explicit rule
     (proposal: syllabic beats consonantal → vowel-like
     treatment for slot placement)
   - Clicks (dual-place: coronal front closure + dorsal back
     closure per PHOIBLE's representation) — a flat feature dict
     handles this; a strict place-node tree does not, which
     argues for a *feature set* adoption over a full geometry
     tree for MVP
   - Contour tones (post-MVP category) deferred
   - Custom symbols: manual feature entry, stored as user-defined
     additions to the controlled vocabulary

    The decisive argument is artifact unification: if our feature
    vocabulary is PHOIBLE's system, then the IPA reference dataset
    and the feature ontology are one and the same file, curated once,
    and category derivation (:ref:`ADR-032`), sonority rank proposal,
    OCP/harmony feature matching, and frequency pre-fill all read
    from a single source of truth. :cite:t:`hayes2009` is also pedagogically
    respectable — it's a textbook system, teachable in tooltips,
    unlike raw SPE notation.

    Choosing the feature set (flat-ish Hayes features) over a full
    Clements geometry tree also resolves the clicks edge case gracefully
    — PHOIBLE represents clicks with combined place features that a flat
    dict stores trivially. The geometry tree remains a post-MVP
    refinement (it's already in the theoretical framework as "partial"),
    and our OCP constraint works on shared features either way.

    This narrows :ref:`q24-feature-representation` as well - features are controlled-vocabulary
    strings, with the vocabulary defined by the pinned PHOIBLE feature
    list plus user-defined additions — validated, but stored as strings
    so project JSON stays plain and diffable. That effectively answers
    Q24 as "option 2 with validation" (strings + controlled vocabulary),
    not enums (which would hard-code the vocabulary into Python,
    violating our data-driven approach and complicating the zero-
    dependency core) and not free-form (fragile rules).

    Proposed resolution path: mark :ref:`q6-feature-system-adoption` ANSWERED (pending your sign-off)
    → draft :ref:`ADR-033` "Adopt PHOIBLE-aligned feature system with
    controlled vocabulary" → :ref:`q24-feature-representation` ANSWERED pointing at
    :ref:`ADR-033` → :ref:`q38-ipa-reference-sourcing` ANSWERED (hybrid). Then the Phoneme data contract
    has everything it needs, and per :ref:`ADR-023` that's the last gate
    before :ref:`UC01` implementation.

    Bib note: add Moisik & Esling only if we cite the laryngeal
    additions specifically; otherwise the :cite:t:`moran2019` entry plus
    :cite:t:`hayes2009` suffices for these claims.

**Answer:**
   Adopt **PHOIBLE 2.0's feature system** (loosely based on
   :cite:t:`hayes2009`, with Moisik & Esling laryngeal additions), pinned
   to the 2.0 release, stored as controlled-vocabulary strings in
   a flat dict. See :ref:`ADR-033`.

   **Decisive argument:**
   PHOIBLE ships per-segment feature data for all 3,183 segments
   under CC-BY 4.0. Adopting their system unifies the feature
   ontology and the IPA reference dataset (:ref:`q38-ipa-reference-sourcing` ) into one
   artifact, making category derivation (:ref:`ADR-032`), rank
   proposals, OCP/harmony matching, and frequency pre-fill read
   from a single source of truth.

   **Edge cases ruled on in ADR-033:**
   - Syllabic consonants: [+syllabic] precedence → vowel-like slot treatment
   - Clicks: PHOIBLE's combined-place representation, category = consonant
   - Contour tones: post-MVP
   - Custom symbols: same vocabulary + user additions

   **Follow-on effects:**
   - :ref:`q24-feature-representation` resolved alongside
   - :ref:`q26-panphon-integration` (panphon) downgraded to post-MVP optional
   - Feature-geometry tree remains a post-MVP theoretical
   refinement, documented in :ref:`theoretical_framework`

.. _q7-generation-determinism:

Q7: [PHONO] Word Generation Determinism and Seed Stability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-09-06) (relates to :ref:`ADR-024`, blocked MVP)

   **Question:**
   UC04 specifies a seed for reproducibility. But if the user changes
   one phoneme's frequency weight, should the entire output change?
   Or should the generator be resilient to minor changes (stable
   ordering — same words generated, just weighted differently)?

   **Context:**
   This affects how useful the live preview is. If every small change
   produces a completely different word list, the user can't evaluate
   whether their change helped. If too stable, they might not see
   enough variety.

   **Related:**
   - :ref:`ADR-024` (seeded PRNG)
   - :ref:`ADR-011` (live preview)
   - :ref:`ADR-044` (per-slot deterministic streams)
   - :ref:`ADR-049` (Coordinate-Addressed Streams for All Random Decisions)
   - :ref:`uc04`   (generation algorithm)
   - :ref:`uc015`  (apply orthography rules)
   - :ref:`dc_phoneme`

   **Action items:**

   - [x] Decide: per-slot deterministic streams (adr-044);
     full-reseed fallback documented
   - [ ] Reference per-slot stream derivation in UC04's
     generation algorithm description
   - [ ] Suggest tests: same parameters → same output;
     weight tweak → untouched slots unchanged

   **Answer:** ``frequency`` is a **positive relative weight**,
   opaque to its provenance:

   1. **Storage:** positive float, default ``1.0`` for user-
      added phonemes. PHOIBLE-derived prefill stores the
      segment's attestation rate (fraction of inventories
      containing it, e.g. ``0.93`` for /m/). The two scales
      interoperate because only *ratios* matter (next point).
   2. **Generation:** when filling a slot, the generator samples
      among *eligible* phonemes with probability proportional
      to weight — ``weight_i / Σ(weights of eligible phonemes)``.
      Normalization is computed per-slot, per-generation, never
      persisted.
   3. **Zero and negative weights are invalid** (schema rejects;
      excluding a phoneme is done by removing it or via
      ``position_restrictions`` — exclusion has an explicit,
      ADR-035-friendly path, so the weight field never doubles
      as a kill switch).
   4. **Meaning of the scale:** doubling a phoneme's weight
      doubles its expected share of slots it is eligible for;
      weights never interact across differently-eligible slots.

   **Spec impact:** ``dc_phoneme`` frequency wording finalizes to
   the above; UC04's generation algorithm references the
   per-slot normalization formula.

Notes: Larman's Protected Variations says the thing to protect is
the key structure — the scheme by which any random decision
finds its stream — while the derivation mechanics behind it
stay swappable. Martin's dependency rule says the derivation
function is core, but core-safe (stdlib-only, honoring ADR-010).
And UC-013's determinism note forbids hidden global state — which
rules out sequential spawning (derive word 1's stream, consume it,
derive word 2's from what's left), because then regenerating
word 50 requires replaying words 1–49.


.. _q8-constraint-expressiveness:

Q8: [PHONO] Constraint System Expressiveness Beyond MVP Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** (effectively) ANSWERED (2026-09-09, :ref:`adr-037`) at design level —
   interface accommodates post-MVP types via ``word_context``
   (:ref:`adr-039`); validation against the post-MVP list remains an
   implementation-time action item. See ADR-022/037/039

   **Question:**
   The nine MVP constraint types cover common phonotactic rules. But
   what about:

   - OCP: two identical features cannot be adjacent
   - Harmony: features must agree across a domain
   - Weight-sensitive constraints: heavy syllables cannot appear in
     onset position
   - Positional constraints: certain phonemes only appear
     word-initially or word-finally

   Can the constraint interface accommodate these without a redesign,
   or do they require a fundamentally different evaluation model
   (whole-word vs. per-syllable)?

   **Current status:**
   OCP and harmony are included in the MVP nine (within-syllable
   only). Cross-syllable versions and weight-sensitive constraints
   are post-MVP. The interface design (:ref:`ADR-022`) should anticipate
   whole-word evaluation.

   **Related:**
   - :ref:`ADR-022` (extensible constraint system),
   - :ref:`ADR-037`
   - :ref:`ADR-039`
   - :ref:`constraints`

   **Action items:**

   - [ ] Validate constraint interface against post-MVP types
   - [ ] Ensure ``word_context`` parameter is in the interface

.. _q9-morpheme-allomorphy:

Q9: [SUITE] Morpheme Storage and Allomorphy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Delta — morphology)

   **Question:**
   When morphology is implemented, morphemes may have multiple
   allomorphs (e.g., English plural: /-s/, /-z/, /-ɪz/ depending on
   the preceding sound). How should allomorphy be represented?

   **Options:**

   1. Separate morpheme entries with conditioning rules
   2. One morpheme with a rule that selects the form
   3. A phonological rule applied after concatenation (morphophonology)

   The Language Construction Kit treats this as a phonological rule,
   suggesting it belongs in the phonology module. But it's triggered
   by morphology. Where does the logic live?

   **Action items:**

   - [ ] Track for Phase Delta (morphology module)
   - [ ] Consider: phonology module exposes a rule application API
     that morphology can call

.. _q10-etymology-tracking:

Q10: [SUITE] Etymology Tracking Granularity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Epsilon — sound change)

   **Question:**
   For the sound change module, etymologies form a tree
   (proto-language → daughter → granddaughter). But we also need:

   - Regular inheritance (parent → child via sound change)
   - Borrowing (external source → target language)
   - Analogy (existing word reshaped by paradigm pressure)
   - Compounding (two roots → new word)

   Should the etymology model distinguish these derivation types?
   Tracking them separately gives richer historical information but
   complicates the data model.

   **Action items:**

   - [ ] Track for Phase Epsilon
   - [ ] Design etymology data contract when sound change module
     is planned

.. _q11-syntax-formalism:

Q11: [SUITE] Syntax Rule Formalism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Epsilon — syntax)

   **Question:**
   Natural language syntax is formalized in many competing frameworks
   (CFG, HPSG, LFG, Minimalism, Construction Grammar). For a conlang
   tool, which formalism is:

   - Expressive enough to capture common syntactic patterns
   - Simple enough for a non-linguist to understand
   - Computable (can we generate and validate sentences?)

   Context-Free Grammars (CFG) are the simplest and most widely
   understood, but can't handle agreement, long-distance dependencies,
   or discontinuous constituents without extensions. Is CFG enough?

   **Action items:**

   - [ ] Track for Phase Epsilon
   - [ ] Survey conlanging community for desired syntax features

.. _q12-interlinear-glossing:

Q12: [SUITE] Interlinear Glossing Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Epsilon — lexicon/syntax)

   **Question:**
   The LCK recommends Leipzig Glossing Rules for interlinear glosses.
   Should the lexicon/syntax modules enforce this standard, or allow
   free-form glosses?

   Enforcing a standard enables automatic gloss generation but
   constrains users who want non-standard annotations.

   **Action items:**

   - [ ] Track for Phase Epsilon
   - [ ] Evaluate: Leipzig Glossing Rules as default with opt-out

.. _q13-semantic-field-ontology:

Q13: [SUITE] Semantic Field Ontology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Epsilon — lexicon)

   **Question:**
   Should the lexicon module ship with a predefined semantic field
   hierarchy (body parts, kinship, colors, animals, etc.), or let
   users create their own?

   A predefined hierarchy (based on a standard like the
   Intercontinental Dictionary Series or Haspelmath's typological
   categories) would enable cross-linguistic comparison but might
   not fit all conlangers' needs.

   **Action items:**

   - [ ] Track for Phase Epsilon
   - [ ] Survey existing semantic field ontologies for suitability

.. _q14-unicode-font-handling:

Q14: [SUITE] Unicode and IPA Font Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Gamma — GUI)

   **Question:**
   IPA rendering depends on fonts that support the IPA Unicode block.
   The project bundles Junicode. But if we support custom scripts
   (Module 6), we need a font management system.

   Should the program bundle fonts, rely on system fonts, or
   integrate with a font manager?

   **Action items:**

   - [ ] Track for Phase Gamma (font bundling strategy)
   - [ ] Track for Phase Epsilon (custom script font management)

.. _q15-module-isolation-testing:

Q15: [SUITE] Module Isolation and Testing Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (suite-level, deferred)

   **Question:**
   Each module should be testable independently. But if Module 2
   (Morphology) depends on Module 1 (Phonology), how do we test
   Module 2 in isolation?

   **Options:**

   1. Mock the phonology interface (fast, but tests don't catch integration issues)
   2. Use a minimal phonology fixture (a small test inventory)
   3. Require the full phonology module for integration tests

   Likely answer: "all three" at different testing levels. But the
   interface contract between modules must be well-defined for
   mocking to work.

   **Action items:**

   - [ ] Define module interface contracts when Module 2 is planned
   - [ ] Establish testing pyramid: unit (mocked) → integration (fixture) → system (full)

.. _q16-community-sharing:

Q16: [SUITE] Community and Language Definition Sharing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Delta+)

   **Question:**
   Should LatticeLang support sharing language definitions? If sharing
   is a goal (even post-MVP), the data format should be designed for it now:

   - Are language definitions portable across installations?
   - Can a user import another user's phoneme inventory without importing their entire project?
   - Should dialect profiles be shareable separately from language definitions?

   **Action items:**

   - [ ] Ensure LanguageDefinition format is self-contained and portable
   - [ ] Track sharing infrastructure for Phase Delta+

.. _q17-performance-envelope:

Q17: [SUITE] Performance Envelope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Gamma)

   **Question:**
   The 500-word generation limit and 50-word live preview are (current arbitrary)
   practical constraints. But what about:

   - Large lexicons (10,000+ words in the dictionary)?
   - Complex constraint sets (dozens of rules)?
   - Sound change applied to an entire lexicon?
   - Sentence generation with recursive syntax rules?

   At what point does the system need async processing, progress
   bars, or caching?

   **Action items:**

   - [ ] Benchmark generation performance during Phase Beta
   - [ ] Set performance budgets for Phase Gamma GUI work

.. _q18-accessibility:

Q18: [SUITE] Accessibility
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (cross-cutting, deferred)

   **Question:**
   The tool is text-heavy and IPA is inherently visual. How do we
   make it accessible to:

   - Screen reader users (IPA symbols don't read well aloud - but we have clickable ones)
   - Users with dyslexia (?)
   - Users who can't hear audio (if we add click-to-hear - we have sound descriptions? edge case probably)
   - Colorblindness
   - High Contrast (more for GUI)

   This is a cross-cutting concern that should be noted early, even
   if implementation is deferred.

   **Action items:**

   - [ ] Document accessibility considerations in architecture.rst
   - [ ] Research: IPA-to-description mapping for screen readers
   - [ ] Track for Phase Gamma (GUI accessibility audit)

.. _q19-i18n-ui:

Q19: [SUITE] Internationalization of the UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (Phase Delta+)

   **Question:**
   The program teaches linguistics in English. But if a user's
   native language is not English, should the pedagogical content be
   translatable? The LCK is English-only; translating linguistic
   pedagogy is a significant effort. But refusing to internationalize
   limits the audience.

   **Action items:**

   - [ ] Track for Phase Delta+
   - [ ] Ensure UI strings are separated from logic (i18n-ready)
     even if translations aren't provided initially

.. _q20-license-compatibility:

Q20: License Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-08-24) → IMPLEMENTED

   **Question:**
   The project uses MIT for code and OFL for the Junicode font. If we
   incorporate IPA data from PHOIBLE, we need to verify license
   compatibility.

   **Answer:**
   PHOIBLE 2.0 is licensed under CC-BY 4.0, which is compatible with MIT.
   The IPA symbol set itself is factual (not copyrightable), but the
   compilation retains CC-BY. Attribution required in documentation.

   **Implementation:**
   Updated ``ipa_reference.json`` with license metadata. See
   :ref:`dc_ipa_reference` and :ref:`bibliography`.

.. _q21-conllu-interchange:

Q21: CoNLL-U Interchange Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: danger

   **Status:** OPEN (Phase Delta — syntax/morphology)

   **Question:**
   Should LatticeLang support CoNLL-U as an interchange format when it
   expands beyond phonology into morphology and syntax?

   **Background:**
   CoNLL-U is the standard plain-text format for Universal Dependencies
   treebanks. It encodes tokens with 10 tab-separated fields: ID, FORM,
   LEMMA, UPOS, XPOS, FEATS, HEAD, DEPREL, DEPS, MISC. :cite:p:`forkel2018`

   **Relevance:**
   - Not useful for phonology (MVP)
   - Potentially useful as an export format when morphology/syntax modules exist
   - Design lesson: keep our JSON format simple, extensible, with a
   "misc"/"custom" escape hatch like CoNLL-U's MISC field

   **Action items:**

   - [ ] Consider adding ``custom`` or ``metadata`` field to data contracts
   - [ ] Track for Phase Delta roadmap
   - [ ] Add CoNLL-U reference to bibliography

.. _q22-unimorph-integration:

Q22: UniMorph Integration
~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: danger

   **Status:** OPEN (Phase Delta — morphology)

   **Question:**
   Should LatticeLang integrate with UniMorph (cross-linguistic
   morphological feature database) when the morphology module is built?

   **Background:**
   UniMorph provides standardized morphological features across languages,
   similar to how PHOIBLE provides phonological data. If we add morphology,
   UniMorph could serve as a reference data source, just as PHOIBLE serves
   for phonology.

   **Action items:**

   - [x] Add UniMorph to bibliography
   - [ ] Track for Phase Delta
   - [ ] Evaluate UniMorph license compatibility when the time comes

.. _q23-universal-override-model:

Q23: Universal→Override Model (from UD patterns)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** DESIGN (architecture pattern, not yet implemented)

   **Question:**
   Should LatticeLang adopt the Universal Dependencies pattern of defining
   universal defaults with language-specific overrides?

   **Background:**
   Universal Dependencies defines all annotation universally first, then
   languages override only what differs. This keeps the universal layer
   clean and makes adding new languages incremental.

   **Proposed mapping to LatticeLang:**

   .. code-block:: json

      {
        "defaults": {
          "max_onset_length": 3,
          "max_coda_length": 3,
          "sonority_sequencing": true
        },
        "overrides": {
          "max_onset_length": 2,
          "prohibited_clusters": ["pk", "bg"]
        }
      }

   This also informs :ref:`q2-dialect-rules` (dialect architecture) - dialects would be
   overrides on top of a parent language definition.

   **Action items:**

   - [ ] Validate this pattern against all 9 MVP constraint types
   - [ ] Document in architecture.rst
   - [ ] Ensure JSON schema supports this pattern


.. _q24-feature-representation:

[PHONO] Q24: Feature Representation — Enum vs Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-08-31) → Implemented via :ref:`adr-033`

   **Question:**
   Should phoneme features use a fixed enum (e.g.,
   ``PlaceOfArticulation.VELAR``) or free-form strings?

   **Options:**

   1. **Enums** — type-safe, IDE autocomplete, catches typos at compile
      time. But inflexible: adding new features requires code changes.
   2. **Strings** — flexible, easy to extend, no code changes needed.
      But error-prone: typos aren't caught until runtime.
   3. **Hybrid** — enums for standard IPA features, strings for
      user-defined custom features.

   **Context:**
   This affects the ``Phoneme`` data contract and all constraint
   implementations that inspect features (OCP, harmony).

   **Dependencies:**
   - :ref:`dc_phoneme` (needs to be finalized)
   - :ref:`adr-022` (extensible constraint system)

   **Action items:**

   - [ ] Decide before implementing :ref:`UC01`

 **Answer:**
   **Controlled-vocabulary strings** — with validation.

   - Feature values are plain strings (``"coronal"``, ``"-"``,
     ``"+"``), validated against a pinned vocabulary list derived
     from PHOIBLE 2.0's feature system (:ref:`adr-033`)
   - User-defined feature names may be added per project;
     validated for identifier syntax only, not semantics
   - Enums were rejected: they hard-code the vocabulary into
     Python, breaking the data-driven approach and complicating
     the zero-dependency core (ADR-010), and every PHOIBLE update
     would require a code change
   - Pure free-form strings were rejected: unvalidated names make
     constraint rules (OCP, harmony) fragile

   This gives enum-like safety at runtime while keeping project
   JSON plain, diffable, and hand-editable — and the vocabulary
   file, not the code, is the source of truth.

.. _q25-constraint-dsl:

[PHONO] Q25: Constraint DSL — Python Callables vs Declarative Mini-Language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** ANSWERED (2026-09-09, :ref:`adr-037`) — MVP ships the
   nine built-in constraint types only; DSL is post-MVP
   (ADR-037 freezes the nine types and reserves ten, doesn't explicitly
   say "no DSL in MVP" - despite Q25's own preferred approach)

   **Question:**
   Should phonotactic constraints be Python callables (powerful,
   requires coding) or a declarative mini-language (accessible,
   limited)?

   **Preferred approach:**
   MVP ships with the nine built-in constraint types only (see
   :ref:`constraints`). A constraint DSL is post-MVP. Users
   configure built-in constraints via JSON parameters, not by writing
   code.

   **Action items:**

   - [ ] Confirm: no DSL in MVP
   - [ ] Track DSL design for Phase Delta

.. _q26-panphon-integration:

[PHONO] Q26: panphon Integration vs Lightweight Feature Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** ANSWERED (2026-08-31, :ref:`adr-033`) — downgraded to
   post-MVP convenience (panphon may power optional *phonetic*
   validation later; not needed for feature vocabulary)

   **Question:**
   Should LatticeLang depend on the `panphon <https://github.com/dmort27/panphon>`_
   library for feature validation, or maintain its own lightweight
   feature set?

   **Trade-off:**
   - **panphon** — comprehensive, well-maintained, covers all IPA features. But adds a dependency (conflicts with ADR-010: zero-dependency core).
   - **Our own** — no dependency, full control. But requires maintaining accuracy against IPA standards.

   **Possible compromise:**
   panphon as an optional dependency for advanced feature validation,
   with a built-in fallback for the core layer.

   **Dependencies:**
   - :ref:`adr-010` (zero-dependency core)
   - :ref:`q24-feature-representation` (feature representation — if we use enums, panphon's stringfeatures need mapping)

   **Action items:**

   - [ ] Evaluate panphon license compatibility
   - [ ] Decide before implementing OCP/harmony constraints

.. _q27-gui-state-management:

[PHONO] Q27: GUI State Management — MVC vs Reactive Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (likely answered: PySide6 signals/slots)

   **Question:**
   Should the GUI use simple MVC, or a proper reactive framework?

   **Preferred approach:**
   PySide6 has signals/slots (observer pattern) built in — likely
   sufficient for MVP. No additional framework needed.

   **Context:**
   This is a Phase Gamma concern. No action needed until GUI
   development begins.

   **Action items:**

   - [ ] Confirm during Phase Gamma architecture work

.. _q28-test-dialect:

[PHONO] Q28: Multi-Dialect English — Which Dialect to Model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN

   **Question:**
   Which dialect of English should be used as the test/validation
   language?

   **Options:**
   - **General American (GA)** — more widely recognized, especially by international users
   - **Received Pronunciation (RP)** — cleaner phonology, fewer rhotic complications, well-documented in the literature
   - **Both** — more comprehensive but doubles test maintenance

   **Suggested approach:**
   Use GA as the primary test language (recognition), with RP as
   a secondary profile (simplicity).

   **Dependencies:**
   - :ref:`adr-009` (English as validation language)

   **Action items:**

   - [ ] Decide before creating dialect profiles in Phase Beta

.. _q29-syllable-boundary-detection:

[PHONO] Q29: Syllable Boundary Detection for MVP?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN

   **Question:**
   Do we need to syllabify generated words (insert syllable
   boundary markers between syllables), or just generate syllable
   sequences?

   **Context:**
   The generator produces syllables. If it concatenates them into
   words, should it mark where one syllable ends and the next begins?

   **Arguments for:**
   - Useful for display (users want to see syllable breaks)
   - Needed for stress assignment (post-MVP)
   - Needed for cross-syllable constraints (post-MVP)

   **Arguments against:**
   - Syllabification of arbitrary consonant sequences is complex
   (ambiguity in onset/coda assignment)
   - For generated words, we already *know* the syllable boundaries
   (we generated each syllable separately)

   **Likely answer:**
   For generated words, boundaries are known by construction —
   just concatenate with a marker (e.g., "."). For imported words
   (reverse pipeline), syllabification is harder and may be
   deferred.

   **Action items:**

   - [ ] Confirm: generated words use simple concatenation with boundary marker
   - [ ] Imported words: defer syllabification to post-MVP

.. _q30-myst-dollarmath:

[SUITE] Q30: MyST Dollarmath in Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED

   **Question:**
   Should we enable MyST dollarmath (``$...$`` for inline LaTeX math)
   in documentation, or stick with literal Unicode IPA in backticks?

   **Answer:**
   Enabled. Dollarmath is useful for phonological notation that
   requires subscripts, superscripts, or formal mathematical
   expressions in theoretical sections.

   **Implementation:**
   Add to ``conf.py``:

   .. code-block:: python

      myst_enable_extensions = ["dollarmath"]

   IPA symbols in running text still use backticks (e.g., ``/t͡s/``)
   rather than math mode. Dollarmath is reserved for formulas and
   theoretical notation.

.. _q31-ipa-normalization-input:

[PHONO] Q31: IPA Normalization for User Input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN

   **Question:**
   How should the system handle users typing Latin approximations
   of IPA (e.g., typing "sh" for /ʃ/)?

   **Options:**

   1. **Hardcoded heuristics** per user profile (fast to implement,
      limited coverage)
   2. **Machine learning model** trained on common patterns (requires
      training data, overkill for MVP)
   3. **Hybrid:** defaults with manual overrides (best balance, medium
      complexity)
   4. **Defer to post-MVP** — design the scaffold now, implement later

   **Preferred approach:**
   Hybrid (option 3) for MVP. Default mappings for common Latin
   approximations, with user-configurable overrides in the
   LanguageDefinition.

   **Dependencies:**
   - :ref:`q1-segmenter-ambiguity` (segmenter ambiguity — related but distinct)
   - :ref:`dc_orthography_rules` Orthography data contract

   **Action items:**

   - [ ] Decide scope: which Latin approximations to support in MVP
   - [ ] Design override mechanism in orthography data contract

.. _q32-orthography-complexity:

[PHONO] Q32: Orthography Complexity Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (likely answered: one-to-one + context pairs)

   **Question:**
   At what point do spelling rules become too complex to manage in
   a simple editor?

   **Options:**

   1. **Simple one-to-one mappings only** (easy, limited expressivity)
   2. **Context-sensitive rules** with visual editor (medium,
      expressive)
   3. **Full regular expressions** (hard, overkill for most users)

   **Preferred approach:**
   MVP: one-to-one mappings plus context pairs (e.g., "s before i =
   /ʃ/"). Post-MVP: visual rule editor for context-sensitive rules.
   Full regex is out of scope.

   **Action items:**

   - [ ] Confirm scope for Phase Beta
   - [ ] Design orthography data contract accordingly

.. _q33-profile-based-inference:

[PHONO] Q33: Profile-Based Inference — Persistent vs Transient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (likely answered: project-local for MVP)

   **Question:**
   Should user profiles (for orthography inference) be persistent
   per user, or transient per project?

   **Persistent profiles** could learn from the user's corrections
   over time, but raise privacy concerns and require account
   management.

   **Transient/project-local profiles** reset per project but are
   simpler and have no privacy implications.

   **Preferred approach:**
   Start with project-local profiles. Consider user-level profiles
   post-MVP if there's demand.

   **Action items:**

   - [ ] Confirm: project-local for MVP
   - [ ] Design profile storage in LanguageDefinition


.. _q34-harmony-mvp-scope:

Q34: [PHONO] Harmony Constraint — MVP Scope Confirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (:ref:`adr-039`)

   **Question:**
   The ``harmony`` constraint type is in the MVP nine, but how far
   does it operate? Within a single syllable only, or across
   syllable boundaries?

   **Answer:**
   MVP: within-syllable only. Cross-syllable harmony (e.g., vowel
   harmony spreading across an entire word) requires the
   autosegmental tier model described in
   :ref:`theoretical_framework` and is deferred to
   post-MVP.

   This means the MVP ``harmony`` constraint checks feature
   agreement between adjacent segments *within the same syllable*
   (e.g., onset consonant to nucleus vowel).

   **Related:** Q8 (constraint expressiveness),
   :ref:`constraints`

   **Action items:**

   - [ ] Document scope explicitly in constraint data contract
   - [ ] Add test case: within-syllable harmony passes
   - [ ] Add test case: cross-syllable harmony not evaluated (not an error, just ignored)

.. _q35-prohibited-clusters-domain:

Q35: [PHONO] Prohibited Clusters — Domain Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:**  ANSWERED (2026-09-06) — per-constraint domain
   parameter; cluster constraints default to syllable, gemination
   is word-adjacency (Blocked MVP) :ref:`adr-039`

   **Question:**
   The ``prohibited_clusters`` constraint bans specific consonant
   sequences (e.g., /pk/, /bg/). But what is its evaluation domain?

   **Options:**

   1. **Within syllable only** — checks onset and coda clusters
      (e.g., bans /st/ in onset)
   2. **Across syllable boundaries** — checks sequences spanning
      coda-onset boundaries (e.g., bans /pk/ where /p/ is coda of
      one syllable and /k/ is onset of next)
   3. **Configurable** — user chooses the domain per constraint
      instance

   **Preferred approach:**
   Configurable (option 3). Default: within-syllable. This makes
   the constraint maximally useful without forcing a choice.

   **Dependencies:**
   - Constraint data contract (``domain`` parameter)
   - :ref:`q29-syllable-boundary-detection` (syllable boundary detection — if we don't mark boundaries, cross-syllable checking is harder)

   **Action items:**

   - [ ] Add ``domain`` field to constraint data contract
   - [ ] Default value: ``"syllable"``
   - [ ] Implement cross-syllable check when :ref:`q29-syllable-boundary-detection` is resolved
   - [ ] Suggest tests - geminate /ab.ba/ triggers across the coda-onset junction; /st/ onset ban fires within syllable by default; explicit ``domain: "word"`` extends cluster check across the boundary

   **Answer:** The constraint carries an explicit ``domain``
   field rather than a global rule:

   - ``prohibited_clusters`` (e.g., no /kn/ onsets) - default
     ``domain: "syllable"``. Cluster well-formedness in natural
     languages is overwhelmingly a syllable-internal affair
     (onset/coda structure); word-edge combinations that look
     like clusters (/n.s/ in "cousin-say") are not the same
     phenomenon and shouldn't be policed by it.
   - ``no_geminate_obstruents`` (and any identical-adjacent-
     segment constraint) - fixed ``domain: "word"`` — geminates
     in natural languages arise precisely *across* the coda-
     onset junction (/ab.ba/), so a syllable-domain check would
     miss every actual gemination site.
   - ``harmony`` (:ref:`q34-harmony-mvp-scope`) - already ruled within-syllable for MVP;
     its future word-domain expansion is post-MVP.

   **Rationale (ADR-035):** the defaults are the naturalistic
   ones — languages that ban clusters police syllables; the
   geminate constraint can't do its job in any smaller domain.
   Users wanting word-edge policing for regular clusters may
   set ``domain: "word"`` explicitly.

   **Spec impact:** ``dc_constraints`` gains a ``domain`` field
   (enum: ``syllable | word``, default ``syllable``) with
   per-type constraints on which values are permitted.

.. _q36-rarity-tier-finalization:

Q36: [PHONO] Rarity Tier System — Finalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN

   **Question:**
   The IPA reference data includes a ``rarity_tier`` field (1–5:
   universal to rare). Should tier 6 be added for unattested sounds
   (sounds that are theoretically possible but not found in any
   documented language)?

   **Context:**
   PHOIBLE documents attested sounds only. But conlangers may want
   to use sounds that exist in the IPA chart but are unattested in
   PHOIBLE. These need a distinct tier so users understand they're
   choosing something with no natural language precedent.

   **Proposed tiers:**

   .. csv-table::
      :header-rows: 1

      "Tier","Label","Description"
      "1","Universal","Found in nearly every language (e.g., /m/, /a/)"
      "2","Common","Found in most language families"
      "3","Moderate","Found in several language families"
      "4","Uncommon","Found in few languages"
      "5","Rare","Found in very few languages"
      "6","Unattested","In IPA chart but not in PHOIBLE database"

   **Action items:**

   - [ ] Confirm: add tier 6 to IPA reference JSON
   - [ ] Update :ref:`dc_ipa_reference`
   - [ ] Add UI warning when user selects tier 5–6 phonemes

.. _q37-word-context-parameter:

Q37: [PHONO] Constraint Interface — Word Context Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-09-06) — optional, minimal,
   constraint-declared requirements (architecture decision,
   not a research question, blocked MVP) :ref:`adr-039`

   **Question:**
   The constraint validation interface currently takes a
   ``Syllable`` object. Should it also accept an optional
   ``WordContext`` parameter for post-MVP constraints that need
   word-level information (cross-syllable harmony, stress,
   positional faithfulness)?

   **Proposed interface:**

   .. code-block:: python

      def validate(
          self,
          syllable: Syllable,
          word_context: WordContext | None = None
      ) -> ValidationResult:
          ...

   MVP constraints ignore ``word_context`` (it defaults to
   ``None``). Post-MVP constraints use it for cross-syllable
   evaluation.

   **Related:**
   - :ref:`q8-constraint-expressiveness` (constraint expressiveness)
   - :ref:`q29-syllable-boundary-detection` (syllable boundaries)
   - :ref:`adr-032` (extensible constraint system)

   **Action items:**

   - [ ] Confirm interface design in :ref:`architecture`
   - [ ] Define ``WordContext`` data structure (minimal: position
     in word, neighboring syllables)
   - [ ] Ensure MVP constraints work with ``word_context=None``

   **Answer:** :ref:`UC013` 's validation API takes an **optional**
   ``word_context`` argument carrying the *minimum* the
   word-domain constraints need — not the whole word:

   - ``preceding_coda``: the coda of the previous syllable, if any (empty at word start)
   - ``following_onset``: the onset of the next syllable, if known (empty at word end)

   **Semantics:**

   1. Each constraint declares its ``domain`` (:ref:`q35-prohibited-clusters-domain`). Word-domain constraints read from ``word_context``; syllable-domain constraints ignore it entirely.
   2. If ``word_context`` is omitted (bare-syllable validation,
      as in live single-syllable preview), word-domain
      constraints are **reported as SKIPPED, never as PASSED**.
      The validation result distinguishes passed / failed /
      skipped — a skipped check is honest, a false pass is
      silent corruption.
   3. Word start/end edges: an empty preceding coda means the
      syllable's onset sits at a word edge — this enables
      word-edge ``position_restrictions`` (e.g., "no /ŋ/
      word-initially") without a separate parameter.
   4. ERROR needs to be included as a legitimate state.

   **Rationale:** syllable validation stays cheap and
   self-contained for preview; word validation composes from the
   same primitive plus context. UC04 :ref:`UC04` 's generation loop owns
   assembling ``word_context`` from the syllables it has already
   built — the generator always knows the preceding coda, and
   the final syllable's constraint sweep happens once the word
   completes.

   **Spec impact:** ``dc_constraints`` documents the domain
   declaration; :ref:`UC013` 's result schema gains the four-valued
   (passed/failed/skipped/error) outcome. :ref:`adr-046`

.. _q38-ipa-reference-sourcing:

Q38: [PHONO] IPA Reference Data Sourcing Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-08-31) → Design recorded; build
   script is Phase Beta tooling

   **Question:**
   How should we build the IPA reference dataset (~3,183 PHOIBLE
   segment types exist; we estimated 1,000–2,500 curated entries)?
   The sourcing strategy determines effort by an order of
   magnitude and gates: custom-symbol flagging, category
   derivation (:ref:`adr-032`), sonority rank proposals, frequency
   pre-fill, rarity tiers, and the pedagogy layer.

   **Options:**

   1. **Hand-curated from the IPA chart** — ~107 core symbols plus
      affricates and alternates, manually entered with features.
      High quality control, weeks of data entry, gaps in
      coverage for rare segments.

   2. **Programmatically derived from PHOIBLE** — take
      ``phoible-segments-features.tsv``, aggregate per-segment
      frequency across 3,020 inventories, compute rarity tiers,
      emit ``ipa_reference.json`` via a build script. Near-total
      coverage with minimal manual effort.

   3. **Hybrid** — PHOIBLE-derived base + hand curation pass for:
      the ~107 core chart symbols (guaranteed present even if
      unattested in PHOIBLE), display metadata (descriptions,
      aliases), alternate forms, and tier 6 (unattested) entries
      from the IPA chart's extensions.

   **Key facts from research:**

   - PHOIBLE 2.0: 3,020 inventories, 3,183 segment types, 2,186
     languages (:cite:p:`moran2019`)
   - PHOIBLE includes distinctive features for **every** segment,
     in a system loosely based on :cite:t:`hayes2009` with additions from
     Moisik & Esling's laryngeal features
   - The feature file maps each IPA segment to a feature set, with
     IPA as the interoperability pivot — i.e., the exact
     symbol→features mapping :ref:`adr-032` needs already exists
   - License: CC-BY 4.0, compatible (:ref:`q20-license-compatibility` / :ref:`adr-029` )
   - PHOIBLE documents *attested* segments only — tier 6
     (unattested, e.g., IPA chart extensions like voiceless
     lateral fricative variants beyond what corpora record) still
     needs hand curation

   **Preferred approach:**
   Hybrid (option 3). Rationale: programmatic derivation kills
   95% of the data-entry burden and gives us real PHOIBLE
   frequencies for free; hand curation covers exactly the things
   automation can't — pedagogical descriptions, alias lists,
   alternate forms, and unattested symbols.

   **Build pipeline sketch (Phase Beta tooling, not runtime):**
   a script reads the TSV, aggregates per-segment frequency
   (count of inventories containing the segment / total
   inventories), assigns rarity tiers by frequency buckets,
   merges a hand-written overrides file, and emits
   ``ipa_reference.json``. The script is reproducible and
   re-runnable when PHOIBLE updates.

   **Dependencies:**
   - :ref:`adr-029` (PHOIBLE license compatibility)
   - :ref:`q38-ipa-reference-sourcing` (rarity tier thresholds — bucketing must be decided)
   - :ref:`q6-feature-system-adoption` (feature system — PHOIBLE's Hayes-based system is now a strong candidate, making :ref:`q6-feature-system-adoption` and :ref:`q38-ipa-reference-sourcing` converge)
   - :ref:`dc_ipa_reference`

   **Action items:**

   - [ ] Decide sourcing strategy
   - [ ] Decide rarity tier frequency buckets (feeds :ref:`q36-rarity-tier-finalization`)
   - [ ] Check PHOIBLE's tie-bar/affricate conventions against :ref:`adr-028` normalization
   - [ ] Write the derivation script as part of Phase Beta tooling

     Programmatic derivation from PHOIBLE's phoible-segments-features.tsv
     gives us every attested segment with features and computable frequencies
     under a license we've already cleared (:ref:`adr-029`). Hand curation then
     only has to cover what automation structurally can't: the ~107 core chart
     symbols (some may be unattested in PHOIBLE but indispensable to conlangers),
     descriptions and aliases for pedagogy, alternate forms per :ref:`adr-028`, and
     tier 6 unattested symbols. Estimated manual effort drops from weeks to days.

     One genuine wrinkle to check during implementation: PHOIBLE's segment
     conventions may not match our tie-bar normalization (e.g., how it encodes
     affricates), so the derivation script needs a normalization pass — which
     is the same normalization code the segmenter needs, so it's not wasted work.

   **Answer:**
   **Hybrid**, per :ref:`adr-033`:

   1. **Derive programmatically** from PHOIBLE 2.0's
      ``phoible-segments-features.tsv``: per-segment features,
      frequency aggregation across the 3,020 inventories,
      rarity-tier bucketing (thresholds feed :ref:`q36-rarity-tier-finalization`), emission of
      ``ipa_reference.json`` plus the pinned feature-vocabulary
      file. The script is reproducible Phase Beta tooling;
      re-running it against a newer PHOIBLE requires an ADR.

   2. **Hand-curate** on top: the ~107 core IPA chart symbols
      (guaranteed present even if unattested), descriptions and
      aliases for pedagogy, alternate forms per :ref:`adr-028`, and
      tier 6 (unattested) symbols from the IPA chart's
      extensions.

   **Normalization caveat:** PHOIBLE's affricate/tie-bar
   conventions may differ from our :ref:`adr-028` normalization; the
   derivation script includes a normalization pass, reusing the
   segmenter's normalization code.

   **License:** CC-BY 4.0, attribution in JSON metadata and
   bibliography (:ref:`adr-029`, :ref:`q20-license-compatibility`)

.. _q39-merge-semantics:

Q39: [PHONO] Merge Semantics for Duplicate Symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-09-06) — interactive grouped-prompt
   merge; bulk first-wins-plus-report (blocked :ref:`UC01` implementation)
   :ref:`adr-040`

   **Question:**
   When a user adds a phoneme whose normalized symbol already
   exists in the inventory (:ref:`UC01`, extension 6a), the system
   offers: replace, merge, or cancel. What do "replace" and
   "merge" actually do — and what happens when there is no user
   present to decide (bulk corpus import)?

   **Options:**

   1. **Strict reject** — no merge exists. Duplicates must be
      removed and re-added explicitly. Simplest and most
      predictable; tedious, and refuses to help when the duplicate
      was accidental (e.g., "ts" normalizing to an existing "t͡s").

   2. **Whole-entry replace (last-wins)** — the new entry silently
      overwrites the existing one. Simple, but silent data loss
      and pedagogically misleading ("what happened to my /t/?").

   3. **First-wins (ignore new)** — equally silent; the user's
      correction attempt appears to fail.

   4. **Per-field prompting** — system diffs existing vs. new and
      prompts on each differing field (feature value, rank,
      frequency). Most careful; unacceptable in batch contexts
      (importing a 5,000-word corpus cannot prompt per symbol).

   5. **Union with grouped conflict prompt** — fields that agree
      merge silently; conflicting fields are collected into ONE
      prompt offering: keep all existing / take all new /
      decide individually. Interactive without being tedious.

   6. **Mode-dependent policy** — interactive sessions use option
      5; bulk ingestion (:ref:`adr-009` corpus import, reverse pipeline)
      uses a project-level policy: ``first-wins | last-wins |
      skip-duplicates | report-only``. Mirrors Q4's batch-mode
      design (default to best guess, flag uncertain items).

   **Field participation rules (for whichever merge variant):**

   - ``features``: merge per-field; conflicting values follow the
     chosen resolution (this is the core of "merge")
   - ``sonority_rank``: **not merged** — recomputed from the
     merged feature set (rank derives from features per
     :ref:`adr-032` & :ref:`adr-033`; a merge that changes features but keeps the
     old rank is internally inconsistent)
   - ``frequency``: keep existing, UNLESS the existing value is
     the unedited default (1.0) and the incoming value is
     reference-sourced — then take the reference value
   - ``components`` (diphthongs): conflicts here should prompt,
     since components define the phoneme's identity
   - ``custom`` flag: never downgraded — a merged phoneme is
     custom if either source was

   **Safety net (all options):** any destructive resolution keeps
   the pre-merge entry recoverable (undo stack or merge-preview
   diff before committing). For pedagogy, the merge dialog
   explains what changed: "Your /t/ had manner=stop; the new
   entry says fricative — this changes which constraints see it."

   **Preferred approach:**
   Option 5 for interactive use + option 6 for bulk, with the
   field-participation rules above baked into a single
   ``merge_phonemes()`` core function so both paths share
   semantics. Undo retention mandatory in both.

   **Relevance to the reverse pipeline:**
   Corpus ingestion (:ref:`UC009`) will frequently re-encounter existing
   symbols. A silent first-wins default there would mask
   transcription inconsistencies — the report-duplicates policy
   doubles as a data-quality signal for rule inference.

   **Dependencies:**
   - :ref:`q4-ambiguity-confidence` (batch behaviour generally)
   - :ref:`UC01` extension 6a; ``dc_phoneme`` merge-semantics flag

   **Action items:**

   - [ ] Confirm interactive vs bulk policy split
   - [ ] Specify ``merge_phonemes()`` in ``dc_phoneme``
   - [ ] Design corpus-import duplicate reporting (009)
   - [ ] Suggest tests: merge unions features and recomputes
     ``sonority_rank`` (stale rank never survives); bulk import defaults to
     first-wins and records collisions to the report; merged ``custom`` flag
     never downgrades

   **Answer (interactive):** Union merge with a **single grouped
   conflict prompt** (option 5). Fields that agree merge
   silently; conflicting fields collect into one prompt offering:
   keep all existing / take all new / decide individually.

   **Answer (bulk — UC009 corpus import):** Project-level policy,
   default **first-wins + duplicate report** (option 6). Existing
   entries are presumed reviewed; incoming collisions are recorded
   to the import report as data-quality signals. Configurable:
   ``first-wins | last-wins | skip-duplicates | report-only``.

   **Field participation rules (normative, both modes):**

   - ``features``: union per-field; conflicts resolved by the
     chosen policy — this is the substance of "merge"
   - ``sonority_rank``: never merged — **recomputed** from the
     merged feature set (rank derives from features; carrying a
     stale rank through a features-changing merge violates the
     :ref:`adr-032` invariant)
   - ``frequency``: keep existing, unless existing is the untouched
     default (1.0) and incoming is reference-sourced — then take
     the reference value
   - ``components`` (diphthongs): conflicts always prompt in
     interactive mode; in bulk, keep existing and report
   - ``custom``: never downgraded — merged phoneme is custom if
     either source was

   **Safety net:** pre-merge entry is recoverable (undo stack);
   merge-preview diff shown before committing. The dialog
   teaches: "Your /t/ had manner=stop; the incoming entry says
   fricative — this changes which constraints see it."

   Why this fits :ref:`adr-035` - the bulk default never blocks and
   never destroys (first-wins is the best guess per Q4 :ref:`q4-ambiguity-confidence`); the
   report is the flag-the-uncertain surface.

.. _q40-near-miss-similarity:

Q40: [PHONO] Near-Miss Symbol Similarity Rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-09-06) — layered: NFD detector +
   reference-enriched messaging (blocked :ref:`UC01` implementation)
   :ref:`adr-041`

   **Question:**
   UC01 extension 6b warns when a new symbol "differs only by
   diacritic" from an existing one (adding "pʰ" when "p" exists):
   "allophone or distinct phoneme?" What concrete comparison
   implements "differs only by diacritic"?

   **Options:**

   1. **Unicode NFD decomposition** — decompose both symbols to
      base character + combining marks (standard-library
      ``unicodedata.normalize("NFD", ...)``); strip combining
      marks; equal bases → near-miss. Pure standard library,
      covers arbitrary diacritics the reference table never
      anticipated (pʷ, p̰, p̴ ...). Fragile edge: some diacritics
      have precomposed exceptions; and the tie bar is itself a
      combining character (U+0361) — so the normalizer (ADR-028)
      MUST run first, or "tʃ" vs "t͡ʃ" would falsely surface as
      a diacritic variant rather than resolving as the same
      affricate.

   2. **Reference-table variant groups** — precompute, in
      ``ipa_reference.json``, groups of symbols sharing a base
      form (aspiration, rounding, velarization variants...).
      Authority-based: known pairs get rich messaging ("pʰ is
      aspirated /p/ — commonly an allophone of /p/"). Coverage
      limited to curated variants; misses unlisted diacritic
      stacks and all custom symbols.

   3. **Feature-distance comparison** — flag phonemes whose
      feature sets differ in exactly one feature (t vs d differ
      only in voice). Linguistically principled, but it flags
      legitimate contrasts — /t/ vs /d/ is a minimal pair, not
      a near-miss mistake. Wrong tool for extension 6b's job;
      better placed as an inventory-level soft warning
      (``dc_phoneme`` already flags identical feature sets; a
      distance-of-1 note is its sibling).

   4. **User-configurable sensitivity** — off / diacritics-only
      (option 1) / diacritics + curated pairs (1+2) / plus
      feature-distance notes (1+2+3). Default: diacritics-only,
      on.

   **Preferred approach:**
   Layered: normalization first (:ref:`adr-028`), then NFD
   base-stripping as the general detector (option 1) for ALL
   symbols including customs; reference-table groups (option 2)
   upgrade the *message* for known pairs (naming the diacritic
   and the common allophony relationship is the pedagogical
   payoff). Feature-distance is explicitly NOT a similarity
   trigger — it belongs to inventory-level validation instead.

   **Order of operations (critical):**
   1. Segment + normalize input (tie bar, diphthong forms)
   2. Exact-match check → duplicate path (6a)
   3. NFD near-miss check → allophone prompt (6b)
   4. Inventory-level checks (identical/1-off feature sets) → soft warnings, separate mechanism

   **Messaging for the prompt (pedagogy):**
   "You already have /p/. /pʰ/ differs only by aspiration — in
   many languages this is an allophone of /p/, not a separate
   phoneme. Add as distinct phoneme anyway?" — with a link to
   the ``allophone`` glossary entry (post-MVP concept, but the
   term should be teachable now).

   **Dependencies:**
   - Q38 (reference-table variant groups come from the same derivation pipeline)
   - Segmenter normalization (:ref:`UC012`) — must precede similarity
   - ``dc_phoneme`` near-miss flag

   **Action items:**

   - [ ] Decide NFD-first ordering with the normalizer
   - [ ] Specify detector in ``dc_phoneme`` (validation rules)
   - [ ] Draft the pedagogical message text
   - [ ] Ensure customs (unknown symbols) still get NFD check
   - [ ] Suggest tests: "pʰ" added alongside "p" prompts; "tʃ" vs "t͡ʃ" resolves via normalization (no false near-miss); custom symbols still get the NFD check

   **Answer:** Layered, with a strict order of operations:

   1. Segment + normalize input (tie-bar, diphthong forms,
      ADR-028) — MUST precede comparison
   2. Exact-match check → duplicate path (:ref:`UC01` ext. 6a → :ref:`q39-merge-semantics`)
   3. **NFD base-stripping detector** — ``unicodedata.normalize``
      decomposition, strip combining marks, compare base
      characters. Runs for ALL symbols including custom ones.
      This is the general, zero-curation mechanism
   4. Reference-table variant groups upgrade the *message* for
      known pairs: "pʰ is aspirated /p/ — in many languages an
      allophone of /p/" (pedagogical payoff from the Q38 pipeline)

   **Explicitly rejected:** feature-distance as a similarity
   trigger. /t/ vs /d/ is a legitimate minimal pair, not a
   probable mistake; 1-off feature sets belong to
   inventory-level validation warnings, not the 6b prompt.

   **Messaging template (pedagogy):** "You already have /p/.
   /pʰ/ differs only by [diacritic description]. In many
   languages this is an allophone of /p/, not a separate
   phoneme. Add as a distinct phoneme anyway?"

   Why this fits :ref:`adr-035` - the near-miss prompt fires rarely
   and only ever *asks* — naturalistic curiosity, no blocking,
   no silent reinterpretation.


.. _q41-corpus-inference:

Q41: [PHONO] Corpus Inference Strategy — Orthographic Profiles vs Cross-linguistic Priors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: warning

   **Status:** OPEN (design anticipation for :ref:`UC009` — post-MVP, but
   profile architecture affects Q33's data contract now)

   **Problem:**
   Imported corpora (:ref:`UC009`) are *romanized*, not IPA — writers
   approximate sounds through their L1's spelling habits, which
   mischaracterize the target phonology the way English spelling
   mischaracterizes English phonology. "Sh", "kh", "j" mean
   different things depending on the writer's orthographic background.

   **Layered inference design (proposed):**

   1. **Profile layer (curated, small).** Orthographic profiles
      per language community — "English-orthography speaker",
      "Spanish-orthography speaker", etc. Each maps romanization
      strings → ranked IPA candidates with prior probabilities.
      Hand-curated but bounded: ~50–100 mappings each. The
      "what is your mother tongue?" question is the *selector*
      for the profile — it is not a lesser fallback, it is the
      cheapest high-information query available.

   2. **Corpus self-consistency layer.** Distributional evidence
      from the corpus itself: if "sh" appears in complementary
      distribution with "s", that's signal; if the same digraph
      maps inconsistently across the corpus, flag for review.
      The corpus is its own best disambiguation training data.

   3. **Cross-linguistic prior layer (PHOIBLE).** Rank competing
      interpretations by cross-linguistic attestation; use L1
      inventory (from PHOIBLE) to model *expected interference
      substitutions* — writers approximate through their L1
      inventory, constraining plausible substitutions.

   4. **Plausibility audit.** Compare the fully inferred
      inventory against PHOIBLE: proportion of common vs rare
      segments, phoneme-count ranges. Outliers flag broken
      mappings. Doubles as a data-quality report feeding rule
      inference (per :ref:`q39-merge-semantics`'s bulk policy).

   5. **Confirmation loop.** Low-confidence segments surface in
      a batch report (:ref:`q4-ambiguity-confidence`), user corrects, corrections persist in
      the project-local profile (:ref:`q33-profile-based-inference`).
      Pedagogical payoff: the  correction dialog explains the mapping ("in English
      orthography 'th' usually means /θ/...").

   **MVP boundary:**
   Layers 1 + 5 only if/when corpus import lands; layers 2–4
   are post-MVP refinements. Crucially: the *profile data
   shape* (orthographic community → ranked mappings) must fit
   into whatever Q33 decides now, so we don't retrofit.

   **Note:** profiles are community-candidate (:ref:`q3-dialect-coverage`) - L1 orthographic
   habits matter, not just phoneme inventory. A Spanish-speaker
   profile and a Mexican-Spanish profile may differ ("x" → /ks/
   vs /x/ in loanwords).

   **Dependencies:**
   - :ref:`q31-ipa-normalization-input`, :ref:`q33-profile-based-inference`, :ref:`q4-ambiguity-confidence`, :ref:`q3-dialect-coverage`
   - :ref:`q38-ipa-reference-sourcing` (profile priors could be seeded from PHOIBLE-derived data)

   **Action items:**

   - [ ] Record layered design in :ref:`UC009` when drafted
   - [ ] Ensure :ref:`q33-profile-based-inference`'s profile storage accommodates ranked mappings
   - [ ] Curate the first profile (English) as pilot when corpus work begins

.. _q42-harmony-parameterization:

Q42: [PHONO] Harmony Constraint Parameterization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Click to expand
   :color: success

   **Status:** ANSWERED (2026-09-09) — designated single feature
   per constraint instance

   **Question:**
   What does the ``harmony`` constraint's ``feature`` parameter
   take, and how are participating phonemes determined?

   **Answer:**
   One ``harmony`` constraint instance per agreed feature:

   .. code-block:: json

      {
        "type": "harmony",
        "enabled": true,
        "parameters": {
          "feature": "back",
          "targets": ["vowel"]
        }
      }

   - ``feature`` - a single controlled-vocabulary feature name (``back``, ``round``, ``atr``, ``nasal`` are the attested harmony features cross-linguistically; backness and rounding are the prototypes — Turkish, Finnish, Hungarian; ATR dominates Niger-Congo/Nilo-Saharan; nasal harmony: Guaraní)
   - ``targets`` - which categories participate. A phoneme absent from ``targets`` is **neutral** — transparent to the constraint. This gives us the typologically essential neutral-vowel concept (Turkish /i, e/ don't undergo backness harmony) for free, via exclusion
   - A language with back+round harmony adds TWO constraint instances, mirroring AGREE([back]) + AGREE([round]) in the OT literature

   **Rejected options:**
   - *Total agreement* (all shared features must agree) - typologically wrong — real harmony is feature-class-selective, and a default that natural languages don't have violates :ref:`adr-035`
   - *Full OT ranked-constraint system:* the theoretically complete answer; requires a ranking engine and faithfulness machinery — parked with the reserved post-MVP types

   **Caveat (recorded honestly):** with :ref:`q34-harmony-mvp-scope`'s within-syllable
     scope, MVP harmony's practical bite is small (diphthong
     components, adjacent nucleus segments). The parameterization
     is the durable design; the scope is deliberately narrow
     until ``cross_syllable_harmony`` (reserved, :ref:`adr-037`).

   **Upgrade paths:**
   - Feature lists per instance (if multi-feature agreement proves common in practice)
   - Directionality/dominance (root-controlled harmony — which value wins disagreements) — deferred; requires morphological roots
   - Autosegmental spreading representation — deferred with the tier model; relevant mainly once cross-syllable scope exists

   **Dependencies:**
   - :ref:`adr-033` (controlled-vocabulary features)
   - :ref:`q34-harmony-mvp-scope`
   - Feeds: ``dc_constraints``.

   - [ ] Suggest tests: two instances implement back+round harmony
     independently; phoneme excluded from ``targets`` is transparent
     (neutral), not a violation

.. _q43-nasal-sonority-split:

Q43: Do Nasals Form a Single Natural Class for Sonority?
--------------------------------------------------------

**Status:** Deferred — Post-MVP Exploration

**Motivation:** Krämer & Zec (2020) present phonotactic evidence that
nasal consonants don't behave as a unified sonority class — their
behavior splits by place, with higher-place nasals (velar, pharyngeal)
pattern as more sonorant than lower-place ones (bilabial, alveolar).
This contradicts LatticeLang's current assumption of a fixed sonority
scale where nasals occupy a single contiguous rank.

**Current Assumption:** The ``sonority_rank`` field (uc01 step 4) assigns
a single integer to all nasal segments, and the
``sonority_sequencing`` constraint enforces the SSP using that fixed
ranking (Clements 1990).

**Challenge:** If Krämer & Zec's hypothesis is correct, a single
``sonority_rank`` per phoneme is insufficient. Possible remedies:

1. Place-dependent ranking: nasals inherit rank based on place feature
2. Context-sensitive rank: nasal sonority varies by following segment
3. Dual nasal hypothesis implementation: split nasals into two
   natural classes in the SSP logic

**Dependencies:** Q4 (SSP implementation), ADR-029 (IPA data source)

**Sources:**

- :cite:p:`kramer2020` — primary source
- Levick et al. (follow-up work on phonetic/phonotactic alignment)

**See Also:** :ref:`ADR-038`, glossary entry ``sonority``,
:ref:`constraint-types-overview` (sonority_sequencing constraint)


.. _q44-maxent-phonotactic-learning:

Q44: Could LatticeLang Learn Constraint Weights from User Choices?
------------------------------------------------------------------

**Status:** Deferred — Post-MVP Exploration

**Motivation:** :cite:p:`hayes2011` demonstrates that experimental evidence
for an "innate" Sonority Sequencing Principle can largely be explained
by learners extracting patterns from ambient phonotactics rather than
assuming Universal Grammar constraints. This suggests LatticeLang
might infer constraint strength/weights from user-generated languages
instead of hardcoding default weights.

**Related Tools:**

- :cite:p:`hayeswilson2008` — maxent phonotactic learner
  (*Linguistic Inquiry* 39:379–440)
- george-steel/maxent-learner — open-source reimplementation
- Hayes Phonotactics Manual & EnglishFeatures.txt — data/examples

**Potential Application:** Users could supply example words, and
LatticeLang would infer which constraints are active and how strongly
they weight them. This mirrors Tesar & Smolensky's learnability
framework for OT ranking induction.

**Technical Scope:** Significant — requires statistical learning
infrastructure, not MVP.

**Sources:**

- :cite:p:`hayes2011` — theoretical motivation
- :cite:p:`hayeswilson2008` — algorithmic foundation
- :cite:p:`tesar2000` — learnability framework
- george-steel/maxent-learner — reference implementation

**See Also:** :ref:`q23-universal-override-model`,
:ref:`constraint-types-overview` (gradient_probabilistic), glossary
entries ``optimality theory``, ``faithfulness constraint``


.. _q45-ot-learnability-framework:

Q45: Does OT Learnability Theory Inform Our Constraint Design?
--------------------------------------------------------------

**Status:** Deferred — Post-MVP Research

**Motivation:** Tesar & Smolensky's work on learnability in Optimality
Theory addresses how a grammar learner induces constraint rankings
from exposure to data. If LatticeLang eventually supports user-driven
constraint tuning (see Q44), this framework might inform how we
represent and expose constraint weights to users.

**Relation to MVP:** None — current MVP uses designer-fixed,
hand-weighted constraints (per ADR-044, ADR-042).

**Potential Future Use:** If users request "this conlang learned
constraints from X example corpus," the learnability framework
provides the theoretical backing for that feature.

**Sources:**

- Tesar & Smolensky (1998/2000) — learnability algorithms
- Prince & Smolensky (2004) ``prince2004`` — foundational OT text

**See Also:** :ref:`q44-maxent-phonotactic-learning`,
:ref:`theoretical_framework`, glossary entry ``optimality theory``
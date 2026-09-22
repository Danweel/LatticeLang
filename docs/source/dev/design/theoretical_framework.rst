.. _theoretical_framework:

Theoretical Framework
======================

:date: 2026-08-24
:status: Static
:audience: Developers and contributors
:purpose: What linguistic theory are we using?

LatticeLang's core engine uses a **rule-based, declarative constraint
system** inspired by Generative Phonology. This document explains the
theoretical choices, alternatives considered, and how the architecture
accommodates future expansion.

Understanding the theoretical basis matters because different theories
make different predictions about what is "natural" or "marked" in
language. Conlangers who understand these predictions can make informed
choices about their phonology; those who don't may accidentally create
patterns that no human language would ever produce.

.. contents::
   :local:
   :depth: 2


Primary Framework: Generative Phonology
----------------------------------------

**Core principles:**

- Underlying forms are transformed to surface forms via ordered rules
- Constraints are hard filters — a candidate either passes or fails
- Derivation is serial and deterministic

**Why we chose this for MVP:**

- Simpler to implement and debug than ranked/violable systems
- More intuitive for non-linguists (true/false vs. "how badly violated?")
- Faster generation loops (no candidate comparison needed)
- Clearer pedagogical value (rules can be explained one at a time)

**Mapping to LatticeLang:**

- ``LanguageDefinition`` = underlying form specification
- Constraints (UC-03) = rule/filter definitions
- Generator (UC-04) = derivation engine
- Output = surface form

**Key reference:** Chomsky & Halle, *The Sound Pattern of English*
(1968) :cite:p:`chomsky1968` — the foundational text of Generative
Phonology, often abbreviated "SPE."

Alternative Frameworks Considered
----------------------------------

Optimality Theory (OT)
~~~~~~~~~~~~~~~~~~~~~~~

**Core principle:** Constraints are violable and ranked. The "optimal"
candidate is the one that best satisfies the hierarchy :cite:p:`prince2004`.

In OT, every input generates a large set of candidate outputs. Each
candidate is evaluated against a ranked list of constraints. The
candidate that violates the fewest high-ranked constraints wins. No
constraint is absolute — any constraint can be violated if a higher-ranked
constraint would be violated worse by the alternative.

**Strengths:**

- Captures cross-linguistic variation elegantly (different rankings
  produce different languages from the same universal constraint set)
- Handles exceptions naturally (lower-ranked constraints can be violated)
- Well-developed theoretical foundation with decades of literature

**Weaknesses:**

- Constraint ranking UI is complex (users must understand and manage
  a total ordering of constraints)
- Computationally expensive (must evaluate many candidates per word)
- Less intuitive for beginners ("why is this word wrong?" → "because
  it violates constraint X which outranks constraint Y")
- Requires a candidate generator that produces *many* possibilities,
  including implausible ones, then filters them

**Status:** Post-MVP option. The architecture supports upgrading
constraints to weighted/violable without breaking changes. When
implemented, users would gain a "Theory Mode" toggle:

- **Generative mode** (default): constraints are hard filters
- **OT mode:** constraints are ranked and violable; best candidate wins

Autosegmental Phonology
~~~~~~~~~~~~~~~~~~~~~~~~

**Core principle:** Features operate on separate tiers (melody, tone,
syllable structure). Spreading and association happen between tiers
:cite:p:`goldsmith1976` :cite:p:`goldsmith1990`.

In standard (linear) phonology, a word is a single sequence of
segments. In autosegmental phonology, a word has multiple parallel
layers — a melody tier (the consonants and vowels), a tonal tier
(the pitch patterns), a skeletal tier (the timing slots), and so on.
Features can "spread" from one segment to adjacent segments along
a tier.

**Strengths:**

- Handles tone, nasal harmony, and feature spreading elegantly
- Accurate representation of long-distance phenomena (e.g., vowel
  harmony across an entire word)
- Foundation for modern work in feature geometry

**Weaknesses:**

- Complex data model (multi-tier structures require special
  representation)
- Overkill for syllable-level phonotactics (which is our MVP scope)

**Status:** Partially implemented. The ``harmony`` constraint type uses
autosegmental concepts (feature agreement across segments) but operates
within a single syllable. Cross-syllable harmony — where a feature
spreads across syllable boundaries — requires the full autosegmental
model and is deferred to post-MVP.

Feature Geometry
~~~~~~~~~~~~~~~~~

**Core principle:** Features are hierarchically organized in trees :cite:p:`clements1985` :cite:p:`clements1995`.

In feature geometry, phonological features are not a flat list but a
tree. For example, the place feature hierarchy might look like:

.. code-block:: text

   Place
   ├── Labial
   │   └── [±round]
   ├── Coronal
   │   ├── [±anterior]
   │   └── [±distributed]
   └── Dorsal
       ├── [±high]
       ├── [±low]
       └── [±back]

Natural classes emerge naturally: all sounds sharing a node in the tree
form a class. Assimilation typically involves spreading a node (and
everything beneath it) from one segment to another.

**Strengths:**

- Predicts natural classes precisely (e.g., "coronal" = /t, d, n, s, z,
  θ, ð, ʃ, ʒ, .../ — all share the Coronal node)
- Explains assimilation patterns (e.g., nasal place assimilation spreads
  the Place node, not individual features)
- Well-established in the literature

**Weaknesses:**

- Very abstract representation (users must understand feature trees)
- Requires a feature tree data model, not just flat feature lists

**Status:** Partially implemented. The ``ocp`` constraint uses
feature-based matching (checking whether adjacent segments share a
specified feature like place or voicing). The full hierarchical tree
model is not yet implemented. When it is, OCP constraints could target
entire subtrees (e.g., "no two adjacent coronals" rather than "no two
adjacent [+anterior] segments").

Natural Phonology
~~~~~~~~~~~~~~~~~~

**Core principle:** Phonologies emerge from natural articulatory and
perceptual biases. Some sound patterns are "natural" because they're
easier to produce or perceive; others are "unnatural" and require
extra effort :cite:p:`hayes2009`.

**Strengths:**

- Explains universals well (why certain patterns appear in nearly every language)
- Psychologically plausible (reflects actual human cognition and physiology)

**Weaknesses:**

- Hard to formalize in deterministic rules (naturalness is gradient, not binary)
- Less developed as a formal framework

**Status:** Not implemented. The concept of "markedness" (some sounds
are rarer or harder) influences our rarity tier system in the IPA
reference, but we don't use Natural Phonology as a constraint evaluation
framework.

Dependency Phonology
~~~~~~~~~~~~~~~~~~~~~

**Core principle:** Phonological elements are organized in
head-dependent relationships. Some elements are heads (structurally
dominant), others are dependents :cite:p:`ladefoged2014`.

**Strengths:**

- Explains asymmetries (e.g., onset vs. coda behave differently because
  onset is the head of the syllable)

**Weaknesses:**

- Less common in conlanging literature
- Not as well-supported by computational tools

**Status:** Not implemented.

Summary Comparison
~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :header-rows: 1
   :widths: 25 35 25 15

   "Theory","Core Idea","Our Use","Status"
   "Generative Phonology","Rule-based derivations; underlying → surface","Primary framework","**MVP**"
   "Optimality Theory","Ranked violable constraints; best candidate wins","Post-MVP option","Planned"
   "Autosegmental Phonology","Feature tiers; spreading between tiers","Partially (harmony)","Partial"
   "Feature Geometry","Hierarchical feature trees; natural classes","Partially (OCP)","Partial"
   "Natural Phonology","Articulatory/perceptual biases drive patterns","Conceptual influence","Not implemented"
   "Dependency Phonology","Head-dependent relationships","Not used","Not implemented"

Warning: Mixing Theories
-------------------------

Combining frameworks without clarity can produce unintuitive results.
For example:

- An OCP constraint (Feature Geometry) combined with ranked violability
  (OT) may behave differently than expected — the OCP was designed as an
  absolute constraint, not a violable one
- Autosegmental spreading assumes parallel evaluation across tiers,
  which is incompatible with serial generative derivation (where rules
  apply one at a time in sequence)
- Feature Geometry's hierarchical features may not map cleanly onto
  OT's flat constraint set

**System safeguard:** The ``Constraint`` data contract includes a
``theory_origin`` field. Each constraint is tagged with its theoretical
origin (e.g., ``"generative"``, ``"OT"``, ``"autosegmental"``). When
the GUI detects mixed-theory constraint sets, it displays a warning
explaining potential conflicts.

This tagging is **documented but not yet enforced** in the MVP. For now,
all constraints operate in Generative mode regardless of their
``theory_origin`` tag.

Architecture Accommodation
---------------------------

The current design anticipates future theoretical modes without
implementing them:

.. code-block:: python

   class Constraint:
       type: str                          # "sonority_sequencing", "ocp", etc.
       params: dict                       # Constraint-specific parameters
       mode: str = "generative"           # "generative" | "OT" | "autosegmental"
       weight: float | None = None        # Only used in OT mode
       theory_origin: str = "generative"  # Tags the theoretical basis

   class ConstraintEngine:
       def validate(
           self,
           syllable: Syllable,
           constraints: list[Constraint],
           word_context: WordContext | None = None
       ) -> ValidationResult:
           # Mode-specific validation logic dispatched here
           pass

This allows switching constraint interpretation modes without changing
the data contract. The constraint *types* remain stable; only the
*evaluation algorithm* changes.

For example, in Generative mode, ``sonority_sequencing`` is a hard
filter — candidates that violate it are eliminated. In a future OT mode,
the same constraint would assign violation marks, and candidates would
be ranked by total violations across all constraints.

Novel Components and Deviations from the Literature
----------------------------------------------------

Most of LatticeLang's theoretical apparatus is borrowed from
established phonology. However, several components are **novel
design decisions** made for usability, data modelling, or
pedagogical reasons. These deviations are listed explicitly so
contributors can distinguish borrowed theory from project
invention.

.. csv-table::
   :header-rows: 1
   :widths: 30 45 25

   "Component","Origin","Grounding"
   "Phoneme Category enum","Novel UI/engine field; derived from features, not manually chosen","Major class features (SPE tradition); see :cite:p:`hayes2009`"
   "Sonority as integer 0–9","Novel flattening of the sonority hierarchy into a single scale","Sonority hierarchy literature via :cite:p:`hayes2009`"
   "Rarity tiers 1–6","Novel bucketing of PHOIBLE frequencies","Data: :cite:p:`moran2019`; bucketing is ours"
   "Tie-bar policy","Novel engineering policy on standard IPA practice","ADR-028"
   "MVP constraint catalog (9 types) and grouping","Novel selection and scoping of textbook constraints","Constraint theory via :cite:p:`prince2004`"
   "``allow_s_appendix`` as a distinct constraint","Semi-novel framing of a well-documented exception","s-cluster exception literature (s-extrametricality)"
   "Diphthong as single phoneme","**Documented deviation** — standard analyses treat diphthongs as vowel sequences; we store them as unit phonemes for slot-filling","Design choice; see note below"
   "Universal→override pattern","Borrowed from Universal Dependencies design, applied to phonology","Tracked in :ref:`q23-universal-override-model`"
   "Pedagogy layer","Novel — engine/UI separation per ADR-015","ADR-015, ADR-019"
   "Seed-shareable language snapshots","Novel UX framing of PRNG seeding","ADR-024"
   "Romanization inference profiles","Novel profile-based approach to Latin-approximation handling",":ref:`q31-ipa-normalization-input`, :ref:`q33-profile-based-inference`"

**Note on diphthongs:** Standard phonological analyses treat /aɪ/
as two segments (/a/ + /ɪ̯/) that pattern together. LatticeLang
deliberately stores diphthongs as single phonemes with a
``components`` field so that one segment fills one nucleus slot.
This is a data-modelling convenience, not a theoretical claim.
The ``glide`` category exists for similar pragmatic reasons:
/j/ and /w/ are feature-wise ambiguous (−syllabic, −consonantal),
and the literature does not force them into the consonant or
vowel bucket.


References
-----------

:cite:p:`chomsky1968` — Foundational text of Generative Phonology
:cite:p:`prince2004` — Foundational text of Optimality Theory
:cite:p:`goldsmith1976` — Autosegmental Phonology (original)
:cite:p:`goldsmith1990` — Autosegmental and Metrical Phonology (textbook)
:cite:p:`clements1985` — Feature Geometry (original)
:cite:p:`clements1995` — Internal Organization of Speech Sounds (feature system)
:cite:p:`hayes2009` — Introductory Phonology (naturalness and markedness)
:cite:p:`ladefoged2014` — A Course in Phonetics (general reference)

See Also
--------

:ref:`constraints` — The constraint type catalog
:ref:`architecture` — How the constraint engine fits in the module layout
:ref:`questions` — Open questions about theoretical commitments
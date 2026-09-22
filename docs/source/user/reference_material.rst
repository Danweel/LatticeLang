.. _reference_material:

Reference Material
==================

Concepts used throughout the use cases. This section explains linguistic
terminology and system behavior that may be unfamiliar to users without
background in phonology.

.. _reference_sonority:

Sonority Sequencing Principle (SSP)
-----------------------------------

**What it is:** A universal constraint on consonant clusters that requires
sonority (relative loudness/resonance) to rise toward the syllable nucleus
and fall away from it.

**Why it matters:** Natural languages overwhelmingly obey SSP. Clusters
that violate it sound "unnatural" to most speakers (e.g., English speakers
find */ptak/* or */mblo/* unnatural). LatticeLang enforces SSP by default
but allows you to disable it if you're modeling a language with systematic
SSP violations (e.g., Georgian).

**Sonority Hierarchy for English-like languages:**

.. csv-table::
   :header-rows: 1
   :widths: 10 30 60

   "Rank","Category","Examples"
   "0","Stops","p, b, t, d, k, g"
   "1","Affricates","tʃ, dʒ"
   "2","Voiceless fricatives","f, θ, s, ʃ"
   "3","Voiced fricatives","v, ð, z, ʒ"
   "4","Nasals","m, n, ŋ"
   "5","Liquids","l, ɹ"
   "6","Glides","w, j"
   "7+","Vowels","i, ɪ, ɛ, æ, …"

Ranks increase with sonority. Within a syllable:

- **Onset:** Sonority must *rise* from left to right toward the nucleus
- **Coda:** Sonority must *fall* from left to right away from the nucleus

**Examples of valid vs. invalid:**

- ✅ Valid: /spl/ (0→2→5: rising)
- ✅ Valid: /lnt/ (5→4→0: falling)
- ❌ Invalid: /pt/ in onset (0→0: flat)
- ❌ Invalid: /lm/ in coda (5→4: rising when it should fall)

**Special cases:**
- **S-appendix exception:** English permits /s/ before any voiceless stop
in the onset despite violating SSP (e.g., /sp/, /st/, /sk/). This is
modeled as a separate constraint that can be toggled.
- **SSP violations allowed:** Some languages systematically break SSP
(Georgian */ptk/*, Polish */ktstʂ/*). Disable SSP enforcement for these.

**Related use cases:** :ref:`uc01` (assign sonority ranks),
:ref:`uc03` (enable/disable SSP constraint)

**References:**
- Clements, G. N. (1990). "The Role of the Sonority Cycle in Core Syllabification." *Phonologica 1988*.
- Hayes, B. (2009). *Introductory Phonology.* Chapter 4.

.. _reference_syllable_structure:

Syllable Structure
------------------

**What it is:** The organization of a syllable into three positions:

.. csv-table::
   :header-rows: 1
   :widths: 15 45 40

   "Position","Function","Typical contents"
   "Onset","Initial consonants before nucleus","Consonants (optional)"
   "Nucleus","Peak sonority (mandatory)","Vowels or syllabic consonants"
   "Coda","Final consonants after nucleus","Consonants (optional)"

**Template notation:** Each position is represented as a slot with constraints:

- **Position type:** ``onset``, ``nucleus``, or ``coda``
- **Allowed categories:** Which phoneme categories (consonant, vowel, diphthong)
- **Min/Max count:** How many phonemes can occupy this slot

**Standard templates:**

.. csv-table::
   :header-rows: 1
   :widths: 15 55 30

   "Template","Structure","Example words"
   "V","nucleus","eye, owe"
   "CV","onset+nucleus","pa, go"
   "VC","nucleus+coda","am, in"
   "CVC","onset+nucleus+coda","pat, dog"
   "CCVC","double-onset+nucleus+coda","stop, flag"
   "CCVCC","double-onset+nucleus+double-coda","splint"
   "CCCVC","triple-onset+nucleus+coda","splash"

**Constraints on templates:**
- At least one nucleus per syllable
- Min count ≤ max count for all slots
- Max count typically ≤ 3 (longer clusters are rare in natural languages)

**Related use cases:** :ref:`uc02` (define templates), :ref:`uc04` (generate from templates)

.. _reference_phonotactic_constraints:

Phonotactic Constraints
-----------------------

**What they are:** Rules that filter which phoneme combinations are valid
within a template's structural shape. Templates define *where* phonemes
can go; constraints define *which* phonemes are allowed.

**MVP constraint types:**

.. csv-table::
   :header-rows: 1
   :widths: 25 40 35

   "Constraint","Description","Example"
   "sonority_sequencing","Enforce SSP within onset/coda","Rejects /pt/ in onset"
   "allow_s_appendix","Permit /s/ before voiceless stops","Allows /sp/, /st/, /sk/"
   "no_geminate_obstruents","Prevent identical obstruent pairs","Rejects /pp/, /tt/, /ss/"
   "max_onset_length","Limit onset cluster size","Rejects /splst/"
   "max_coda_length","Limit coda cluster size","Rejects /kstsθ/"
   "position_restrictions","Forbid specific phonemes in slots","No /ŋ/ in onset, no /h/ in coda"

**Configuration examples:**

.. code-block:: python

   # Disable SSP (allows unnatural clusters)
   Constraint(type="sonority_sequencing", enabled=False)

   # Set max onset length to 3
   Constraint(
       type="max_onset_length",
       enabled=True,
       parameters={"max_length": 3}
   )

   # Forbid /ŋ/ in onset and /h/ in coda
   Constraint(
       type="position_restrictions",
       enabled=True,
       parameters={
           "forbidden_onset": ["ŋ"],
           "forbidden_coda": ["h"],
       }
   )

**Related use cases:** :ref:`uc03` (define constraints), :ref:`uc04` (apply during generation)

**References:**
- Goldsmith, J. (1990). *Autosegmental and Metrical Phonology.*
- Zec, D. (2007). "The Sonority Controversy." *Phonology at Santa Cruz.*

.. _reference_frequency_weighting:

Frequency Weighting
-------------------

**What it is:** When selecting phonemes for a syllable slot, the generator
can weight choices by their relative frequency in the language. High-frequency
phonemes appear more often in generated output.

**Why it matters:** Without frequency weighting, all phonemes are equally
likely. This produces artificial-looking output (e.g., equal numbers of
/r/-words and /ʒ/-words in English). With weighting, /r/ appears ~6% of
the time while /ʒ/ appears ~0.2%.

**Configuration:**

- Each :class:`~latticelang.core.phonology.Phoneme` has a ``frequency``
  attribute (float, default: 1.0)
- The generator normalizes frequencies to probabilities
- Frequency weighting can be disabled per generation request

**Example:**

.. code-block:: python

   from latticelang.core.generator import WordGenerator

   gen = WordGenerator(definition, seed=42)
   words = gen.generate(count=100, frequency_weighted=True)
   # Or: frequency_weighted=False to ignore frequency

**Related use cases:** :ref:`uc01` (set frequency weights), :ref:`uc04` (configure during generation)

.. _reference_ipa_segmentation:

IPA Segmentation
----------------

**What it is:** The process of parsing a string of IPA symbols into
discrete phoneme units. Multi-character symbols (e.g., ``"tʃ"``, ``"aɪ"``)
must be recognized as single phonemes rather than split into constituent
characters (``"t"`` + ``"ʃ"``).

**How it works:** LatticeLang uses a **longest-match algorithm**:

1. Read characters from left to right
2. Attempt to match the longest symbol from the IPA table
3. If no match, fall back to the next-longest
4. Continue until the entire string is segmented

**Examples:**

.. csv-table::
   :header-rows: 1
   :widths: 20 30 50

   "Input","Segmentation","Explanation"
   "``'tʃaɪn'``","[tʃ, aɪ, n]","Affricate + diphthong + consonant"
   "``'tʃain'``","[tʃ, a, i, n]","Affricate + 3 monophthongs"
   "``'straɪk'``","[s, t, ɹ, aɪ, k]","Consonants + diphthong + consonant"

**Ambiguities:** Some inputs can be segmented multiple ways:

.. csv-table::
   :header-rows: 1
   :widths: 15 40 45

   "Input","Interpretation 1","Interpretation 2"
   "``'ts'``","[t͡s] (affricate)","[t, s] (stop+fricative)"
   "``'pj'``","[p, j] (consonant+glide)","[pʲ] (palatalized p)*"

*Palatalization is post-MVP — currently treated as separate phonemes.*

**Related use cases:** :ref:`uc01` (validate IPA input), :ref:`uc012` (segmentation subroutine)

.. _reference_cross_language_coverage:

Cross-Language Constraint Coverage
----------------------------------

**What it is:** The MVP includes seven constraint types sufficient for
English-like and simple CV languages. Other phonological phenomena are
documented here for future implementation.

**Supported in MVP:**
- Sonority Sequencing Principle (toggleable)
- S-appendix exceptions
- Obstruent geminate prohibition
- Max onset/coda length
- Position restrictions (forbidden phonemes per slot)

**Scaffolded but not implemented:**
- Tone assignment (category exists, logic deferred)
- Non-pulmonic consonants (representable as phonemes, no special rules)
- Gemination (representable as separate phonemes, no length feature)

**Requires new architecture (post-MVP):**
- Vowel harmony (cross-syllable feature agreement)
- Syllable weight (per-syllable calculation affecting stress)
- Nasal harmony (feature spreading across phonemes)
- SSP violations as positive constraints (require specific clusters)

**Research Note:** These gaps are tracked as research notes, not blockers.
Each can be added as a new constraint type without modifying the existing
pipeline — constraints are checked sequentially, so new types slot in
without refactoring. See :file:`docs/source/dev/research_notes.rst` for
details.

**Related use cases:** :ref:`uc03` (constraint system)

.. _reference_reproducibility:

Reproducibility and Seeds
-------------------------

**What it is:** LatticeLang uses a seeded pseudo-random number generator
(PRNG) for word generation. If you provide a seed value (integer), the
same LanguageDefinition + same parameters + same seed will always produce
the exact same word list.

**Why it matters:**
- Sharing a specific "language snapshot" with collaborators
- Reproducing results across sessions
- Testing — the test suite uses fixed seeds to verify output
- Debugging — if a generated word looks wrong, the seed lets you reproduce it exactly

**How to use it:**

.. code-block:: bash

   # CLI
   latticelang generate --preset english_ga --seed 42 --count 50

.. code-block:: python

   # Python API
   gen = WordGenerator(definition, seed=42)
   words = gen.generate(count=50)

If no seed is provided (``seed=None``), the system uses a random seed
and output is non-reproducible.

**Related use cases:** :ref:`uc04` (generation parameters)

.. _reference_syllable_boundaries:

Syllable Boundary Notation
--------------------------

**What it is:** Generated words include syllable boundaries marked with
a dot (``.``) separator, following standard linguistic convention.

**Example:**

::

   stɹæm.bəl    →  two syllables: "stram" + "bel"
   kændi.ɛs     →  two syllables: "candy" + "es"

**Display options:**
- With boundaries (default): ``stɹæm.bəl``
- Without boundaries: ``stɹæmbəl``
- With hyphens instead: ``stɹæm-bəl``

Boundary display is a presentation choice — the internal representation
always preserves syllable structure regardless of display format.

**Related use cases:** :ref:`uc02` (templates define syllable structure),
:ref:`uc04` (output format)

.. _reference_exception_hierarchy:

Error Types
-----------

**What it is:** LatticeLang uses a hierarchy of custom exceptions to
signal different failure modes during generation. Understanding these
helps diagnose why generation failed.

**Exception hierarchy:**

::

   LatticeLangError (base)
   ├── ParameterError        — Invalid generation parameters
   ├── GenerationError       — Structural impossibility
   └── NoValidTemplateError  — All templates rejected by constraints

**Common scenarios:**

.. csv-table::
   :header-rows: 1
   :widths: 25 40 35

   "Exception","Cause","Fix"
   "ParameterError","word_count=0, min > max","Correct parameters"
   "GenerationError","No phonemes for a slot","Add phonemes (see :ref:`uc01`)"
   "NoValidTemplateError","Constraints reject all candidates","Relax constraints (see :ref:`uc03`)"

**Related use cases:** :ref:`uc04` (extensions 1a, 3b, 3e)

**Verified background research (attested, not yet cited in LatticeLang):**

- Zec (2007), "The Syllable," in de Lacy (ed.), *Cambridge Handbook of
  Phonology*, pp. 161–194 — syllable-theory survey. Relevant to Delta
  (TBU/tone) and Epsilon (allomorphy conditioning). Provenance:
  attested via reference lists 2026-09-11; chapter not read in full.
- McCarthy & Prince (1993), *Prosodic Morphology: Constraint Interaction
  and Satisfaction*, RuCCS-TR-3 (ROA-companion to OT TR-2) — related
  report on the same problem space; prosodic morphology is post-MVP.
  Provenance: verified via Prince's Rutgers publication list 2026-09-11.
- Evans & Levinson (2009), "The Myth of Language Universals," BBS 32(5),
  429–448 — diversity counterweight: affects interpretation of ADR-035
  and ADR-033 ("typologically common," not "universal"). Provenance:
  bibliographic record verified (Cambridge Core, Semantic Scholar,
  Glottolog) 2026-09-11; article not read in full.
- Keuleers & Brysbaert (2010), "Wuggy," BRM 42(3), 627–633 —
  computational prior art for UC-04/UC-013 (phonotactic-constrained
  generation, statistical rather than declarative). Provenance:
  verified (Springer, PubMed, Macquarie) 2026-09-11.
- UPSID (UCLA Phonological Segment Inventory Database) — typological
  ancestor of the PHOIBLE frequency approach; credited via
  Maddieson (1984), *Patterns of Sounds* (in refs.bib).

UniMorph, UD, CoNLL-U
---------------------

**UniMorph ↔ UD**: sibling standards from different communities covering
different linguistic layers. UD annotates syntax — dependency trees
of sentences (~200 languages of treebanks). UniMorph annotates
inflectional morphology — paradigm cells as lemma-form-feature
triples, with a schema of semantic "atoms" for features. Orthogonal
and complementary rather than rivalrous, with bridging efforts existing
to enrich UD treebanks with UniMorph-derived lemmas/features. For
LatticeLang, the relevance splits cleanly: UD's value is the
architectural pattern (universal→override — already captured in ud2024
and q23); UniMorph's value is as a future morphology-module feature
schema (q22); PHOIBLE is the one actually feeding MVP data.

**CoNLL-U vs CoNLL-X**: CoNLL-X was the 2006 shared-task format for
dependency parsing; CoNLL-U is UD's format, descended from it with
deliberate upgrades — multiword token lines (ID ranges like 1-2 for
contractions, which CoNLL-X simply can't represent), empty nodes
with decimal IDs (8.1, for ellipsis/gapping in the enhanced
representation), mandatory comment conventions (# sent_id, # text),
strict validity constraints (single root, acyclic, connected), and
a DEPS column for the enhanced graph. CoNLL-U is better
specified for treebank-scale annotation — CoNLL-X was fit for its
2006 purpose; CoNLL-U is fit for representing linguistic reality
that CoNLL-X had no syntax for.
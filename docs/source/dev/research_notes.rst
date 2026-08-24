
Research Notes
==============

Open questions, proposed solutions, and references for future
development. These are developer-facing notes, not user documentation.

.. note::

   This file tracks unresolved design questions. Each note should have
   a date, status (open/closed), and enough context to resume the
   discussion after a break.

## Cross-Language Constraint Coverage

**Date:** 2026-08-23
**Status:** Open
**Priority:** Post-MVP

### Problem
The seven MVP constraint types cover English-like and simple CV
languages but miss several major phonological phenomena:

1. **Vowel harmony** (Turkish, Finnish, Hungarian): Requires
   cross-syllable vowel feature agreement. Current architecture
   validates syllables independently — a vowel harmony constraint
   would need access to the previous syllable's nucleus features.

2. **Syllable weight** (Latin, Arabic, Japanese): Heavy vs. light
   syllables (based on nucleus length or coda presence) affect
   stress assignment and poetic meter. Requires per-syllable weight
   calculation and a stress assignment module.

3. **Nasal harmony** (Guaraní, Terena): Nasality spreads from a
   trigger to subsequent segments. Requires feature-spreading rules
   that operate across phoneme boundaries.

4. **Positive SSP violation constraints** (Georgian, Polish): Some
   languages systematically allow clusters that violate SSP. The
   current system can *disable* SSP but cannot *require* specific
   violating clusters.

### Proposed Approach
Each phenomenon requires a new constraint type with a broader scope
than current constraints (which operate per-syllable). Two options:

**Option A: Contextual constraints** — constraints that receive the
full word context (previous syllables, neighboring phonemes), not just
the current syllable. This is more powerful but changes the constraint
pipeline signature.

**Option B: Post-generation filtering** — generate freely, then filter
the complete word against contextual constraints. Simpler to implement
but less efficient (may reject many candidates).

### Recommendation
Defer until post-MVP. Document the constraint interface as receiving
both the syllable and optional word context, so adding contextual
constraints later doesn't change the method signature.

### References
- Hayes, B. (2009). *Introductory Phonology.* Chapter 4 (Syllables)
  and Chapter 5 (Features).
- Goldsmith, J. (1990). *Autosegmental and Metrical Phonology.*
  Chapters on harmony.

Combinatorial Maximum Calculation
---------------------------------

:Date: 2026-08-23
:Status: Open
:Priority: MVP (UC-04, extension 5a)

Problem
~~~~~~~

UC-04 extension 5a requires the system to calculate the maximum possible
unique words before generation begins, so it can warn users when their
request exceeds the combinatorial space.

Proposed Formula
~~~~~~~~~~~~~~~~

::

   template_combinations(T) = Π(slot_i_available_phonemes)
   where slot_i_available_phonemes = count of phonemes matching
   slot i's allowed categories minus forbidden phonemes

   unique_words ≈ Σ(T ∈ templates) template_combinations(T) ^
                    avg_syllable_count

This is an upper bound — constraints (SSP, geminate prohibition)
reduce the actual number below the theoretical maximum.

Open Questions
~~~~~~~~~~~~~~

1. Should we compute exact valid combinations by brute-force checking
   all permutations against constraints? Accurate but potentially
   expensive for large inventories.

2. Should we use the theoretical upper bound (fast but optimistic)?
   May mislead users into expecting more words than constraints allow.

3. Should we sample (generate 1000 candidates, count valid, extrapolate)?
   Middle ground but statistically noisy.

Recommendation
~~~~~~~~~~~~~~

Use the theoretical upper bound for the MVP warning. It's fast and
correct as an upper bound ("at most N words are possible"). Post-MVP,
implement exact counting for smaller inventories (< 30 phonemes).

Generation Performance
-----------------------

:Date: 2026-08-23
:Status: Open
:Priority: Post-MVP optimization

Problem
~~~~~~~

The MVP generator uses rejection sampling: generate a candidate syllable,
check it against constraints, discard if invalid, retry. With strict
constraints and complex templates, this may waste many attempts.

Current Limits
~~~~~~~~~~~~~~

- MAX_SYLLABLE_ATTEMPTS = 100 (per syllable)
- MAX_DUPLICATE_ATTEMPTS = 50 (per word)

Acceptable for MVP (≤ 1000 words, ≤ 30 phonemes).

Future Optimization
~~~~~~~~~~~~~~~~~~~

Precompute valid clusters per template:
1. For each template, enumerate all valid onset/nucleus/coda combinations
2. Store as a lookup table
3. During generation, sample directly from valid combinations

Trade-off: startup cost (precomputation time) vs. generation speed
(no rejection needed). Worth it for repeated generation (GUI live
preview where the same definition generates many times).

Bibliography
------------

Phonology
~~~~~~~~~

- Clements, G. N. (1990). "The Role of the Sonority Cycle in Core
  Syllabification." *Phonologica 1988*.
- Goldsmith, J. (1990). *Autosegmental and Metrical Phonology.*
  Chapters on harmony.
- Hayes, B. (2009). *Introductory Phonology.* Chapter 4 (Syllables)
  and Chapter 5 (Features).
- Ladefoged, P. & Johnson, K. (2014). *A Course in Phonetics.*
  Chapter on English phonology.
- Mines, M., Hanson, B., & Shoup, J. (1978). "Frequency of Occurrence
  of Phonemes in Conversational English." *Language and Speech.*
  (Source for phoneme frequency weights.)
- Zec, D. (2007). "The Sonority Controversy." *Phonology at Santa Cruz.*

Conlang Pedagogy
~~~~~~~~~~~~~~~~

- Rosenfelder, M. (2009). *The Language Construction Kit.*
  Online at https://www.zompist.com/ccc.htm
- Rosenfelder, M. (2011). *Advanced Language Construction Kit.*

Software
~~~~~~~~

- SIL FieldWorks: https://fieldworks.sil.org/
- Vulgar: https://www.vulgarlang.com/
- Awkwords: https://github.com/phylovisualization/awkwords

Use Case Methodology
~~~~~~~~~~~~~~~~~~~~~

- Cockburn, A. (2000). *Writing Effective Use Cases.* Addison-Wesley.


.. _how-latticelang-works:

How LatticeLang Works: A Plain-English Guide
============================================

:date: 2026-10-01
:type: Tutorial
:audience: Linguists, conlangers (minimal programming jargon)

This guide explains the internal workings of LatticeLang - the decisions
made and linguistic theories used to make it work. Like all sciences,
they're theories, and they don't all perfectly mesh, either. Similarly,
a small program like this can't accurately depict all of linguistics either
so outliers also had to be scoped out at some arbitary line as well.

At a High Level
---------------

LatticeLang is a tool for designing phonological inventories — the
sounds of a language. You tell it which sounds exist, what features
they have, and how they fit together. It then generates syllable
structures, validates your constraints, and exports everything in
consistent formats.

That's pretty standard for phonology generators - there's a lot of
them out there. Enough that it's a bit tough to write out a list of them,
I usually just send people to Rosenfelder's, Gen.

What I wanted specifically was a program with authors in mind, less-so
conlangers with a hobby. Writers don't have time to make conlang a
full hobby. They might be interested in the things that a basic conlang
might bring to their worlds, but struggle with the ins and outs that
you get a sense of when you take it up as a full hobby. Writing is already
the hobby for a lot of people. Also, it should be a touch more accessible
for people curious also, than some of the Gens out there.

The main thing I wanted it to do is be able to take a 'corpus', or already
existing set of words (authors including myself often start making things
up and then realize they can't think of any more stuff that feels
consistent), and extrapolate patterns from it, in order to make
more words of similar design. A lot more complicated than it sounds of
course, which is why it doesn't really exist as far as I know. (I think
there is one set of linguist-scientists that worked on a much more serious
and rigorous program in this vein meant for Serious Science Stuff, as far
as I could tell - it would not be friendly enough to use, nor was in a
familiar, download-and-runnable format. It certainly wasn't about my
use-case, anyway.)

Because a tiny corpus doesn't hold enough information to actually fully
inform generation, some decisions need to be made and the program will
hand-hold that to a certain degree. Ideally, you can change rules and
see how that changes the output. This will help people choose the right
rules for what they want, and hopefully learn something too. It should
function alright as a toy for learning about lingustics basics
as well, hopefully.

The Five-Step Pipeline
----------------------

Here's what happens internally, translated from technical terms:

**1. Load PHOIBLE Data**
PHOIBLE is a global database of 3,020 phonological inventories from
real languages. LatticeLang starts with this data, not from scratch.
This ensures the sounds suggested are plausible and can even tell you
by how much. In this lang-gen you're constrained by what
actually occurs in human languages. But if you were using IPA before,
you already were anyway. This program puts a special emphasis on it though.

**2. Derive Sonority Ranks**
Every sound gets a "sonority rank" — a number indicating how sonorous
(vowel-like) it is. Stops (p, t, k) score lowest; vowels score highest.
This ranking determines which sounds can fill which slots in syllables.
This was one of the initial rules I wanted to include - most generators
really only focus on CVC, sometimes the overall likelyhood of a pattern
appearing - but don't give any hints on what's already likely.

**3. Build IPA Reference Table**
The tool generates a master table, mapping every IPA symbol to its
properties: features, rarity in world languages, Unicode codepoints,
canonical forms, and aliases. This becomes the lookup table for all
subsequent operations. This is what actually ships with the program,
but it's specifically PHOIBLE-based, with the information codified
in a way more useful to the program to read.

**4. Validate Against Rules**
The user's inventory passes through six validation checks:
- Unique symbols (no duplicates)
- No forbidden vowel gaps (define what forbidden means at this juncture - forbidden by the user or the data?)
- Required diphthong components present (define more clearly)
- Feature vocabulary consistency (define)
- Unicode codepoint correctness (which should already be part of the table?)

Failures abort the build — you can't create impossible phonologies.

**5. Instantiate Phonemes**
Individual Phoneme objects are created, each carrying:
- The IPA symbol itself
- A feature set (consonantal+, syllabic-, etc.)
- Derived category (consonant, vowel, glide, diphthong)
- Sonority rank
- Generation frequency weight

The user can also assign Orthography, or the spelling, to each phoneme.
For now, this is somewhat simplistic, but I'd like to add rules to this as well,
such as sound changes when next to other set phonemes, etc., which causes
inconsistencies in spellings, potentially.

Why This Matters
----------------

Most tools let users create anything, including linguistically
impossible combinations or other 'interesting' edge cases. That's
great for play and to experiment with lingustics. But for novelists
too much adventure can be just difficult to read, or tempting to put
on display when the words should really be serving the story - sometimes
that's just flavor.
LatticeLang prevents this *before* it happens,
not after. You're nudged toward naturalistic patterns without being
explicitly forbidden. It'll still allow you to make whatever, but there's
fundamentals that appear by default, especially when it's making
assumptions about what you are feeding it.

This is the "Naturalistic Defaults" principle (:ref:`ADR-035`).
It's easier to remember what's forbidden than what's required — so
the tool is lifting that weight for you. It might be #35, but this
was a ground-level principle behind the tool and why I'm not just using
an existing generator.

The Phoneme Unit
----------------

Every sound in your inventory is a ``Phoneme``. Here's what each field
means in plain English:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Field
     - What It Means
   * - Symbol
     - The IPA character (e.g., ``p``, ``ɑ``, ``k͡p``)
   * - Features
     - A bundle of attributes (consonantal+, syllabic-,
       voiceless, bilabial, etc.) — think of these as the "DNA"
       that determines behavior
   * - Category
     - Automatically derived: consonant, vowel, glide, or
       diphthong. The tool figures this out from features
   * - Sonority Rank
     - A number (0–9) indicating where this sound falls on the
       sonority scale. Vowels are highest.
   * - Frequency Weight
     - How often this sound appears in world languages (from
       PHOIBLE data). Rare sounds get lower weights.

Categories Are Derived, Not Assigned
------------------------------------

In LatticeLang, you don't *assign* a phoneme to a category.
The tool derives it from features using decision rules:

- **Consonant**: consonantal=+, syllabic=-
- **Vowel**: syllabic=+
- **Glide**: consonantal=+, syllabic=+
- **Diphthong**: two-vowel combination

If you mark something as consonantal but also syllabic, it
automatically becomes a glide, not a contradiction.

About Step 4 - Validation Gates
-------------------------------

When you build your inventory, six checks run:

**INV-1: Unique Symbols**
No duplicate IPA characters allowed. The table can't have two ``p``
entries — that would make lookups ambiguous.

**INV-2: Syllable Template Compatibility**
Your inventory must support at least one valid CV structure. Empty
inventories or inventories with only tones fail here.

**INV-3: Vowel Absence Warning**
Languages almost always have at least one vowel. If yours has none,
you'll get a warning — but it won't block the build (some languages
lack underlying vowels on certain analyses).

**INV-4: Diphthong Component Presence**
If you declare a diphthong, both component vowels must exist as
standalone phonemes. ``ai`` can't be a diphthong if ``i`` doesn't
exist in your inventory.

**INV-5: Feature Vocabulary Consistency**
All feature values must come from the controlled PHOIBLE vocabulary.
You can't invent arbitrary feature names.

**INV-6: Diphthong Structural Check**
Diphthongs must contain exactly two vowel elements. Three-vowel
clusters aren't supported at this phase, but its on the table.

The Special Combinations Case
-----------------------------

Some IPA symbols aren't single characters — they're combinations:

- Tie bars (``k͡p`` — labial-velar double articulation)
- Length marks (``aː`` — long vowel)
- Syllabic diacritics (``l̩`` — syllabic consonant)

These (from the PHOIBLE data) route to a separate ``special_combinations`` bucket in the
output JSON. They're still considered valid 'phonemes', just handled differently
during segmentation. When we complicate things at a later stage, they'll have more uses.

Frequency and Rarity Tiers
--------------------------

PHOIBLE provides raw inventory counts (e.g., ``p`` appears in 1,873 of
the 2,155 inventories in PHOIBLE 2.0's gold-standard set). LatticeLang
converts this to a frequency weight (count divided by the total number
of inventories, calculated at build time from the pinned data), then
labels it with a rarity tier. The tiers are display labels for humans;
the continuous frequency is what the tool actually uses as a weight, so
tiers never gate anything.

- **Tier 1**: Extremely common (at least 80% of languages have this sound)
- **Tier 2**: Common (at least 50%)
- **Tier 3**: Moderately common (at least 25%)
- **Tier 4**: Uncommon (at least 5%)
- **Tier 5**: Rare (at least 1%)
- **Tier 6a**: Isolate — attested in exactly one inventory of the sample
- **Tier 6b**: Attested, but below 1% and not an isolate

A caveat on 6a: "isolate" means "appears in exactly one inventory of
this 2,155-inventory sample," not "rare in a linguistic sense" —
sampling gaps and source quirks can strand a sound in tier 6a that
isn't actually unusual. Sounds that aren't in the reference table at
all aren't forbidden — they're custom symbols, usable freely for
speculative conlangs.

What Happens Next?
------------------

This pipeline feeds into the next phase: syllable templates and
constraints. Once you've defined your phonemes:

1. You specify valid syllable shapes (CV, CVC, CCVC, etc.)
2. You set constraints (no final clusters, max onset of 2, etc.)
3. LatticeLang validates whether your phonemes support those shapes
4. It generates candidate words that obey all constraints

You never see invalid candidates. The validation happens
at the constraint layer, not the output layer.

Limitations (Current Phase)
---------------------------

For transparency, here's what *doesn't* work yet (Post-MVP items):

- Tone and stress marking (planned for Delta phase)
- Harmonic processes (velar harmony, nasal harmony)
- Morphology (prefixes, suffixes, roots)
- Sound change simulation (historical phonology)
- Export to writing systems beyond IPA

The roadmap tracks these as Epsilon-phase features or even a
different potential module of language construction. For now, LatticeLang
focuses on the core: phoneme inventories, syllable structures, and
constraint validation, all of which are useful for a "Naming Language",
the thing most useful for authors.

Further Reading
---------------

- :ref:`dc_phoneme` — Technical phoneme contract (developers)
- :ref:`dc_inventory` — Validation rules in detail
- :ref:`how_the_program_processes_things` — (placeholder: expand with flow diagrams when available)
- :ref:`glossary` — Technical terminology explained

Feedback Welcome
----------------

This guide is intentionally jargon-light. If you're a linguist
reading this and thinking "wait, that's not how sonority works,"
please open an issue on GitHub. Your expertise helps keep the
tool accurate.

Conversely, if you're a programmer thinking "that's hand-wavy,"
please check :ref:`dc_phoneme` for the technical specifications.
This page is the friendly front door; the docs behind it hold
the rigorous details.
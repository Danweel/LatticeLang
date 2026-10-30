.. _how-latticelang-works:

How LatticeLang Works:
======================

:date: 2026-10-01
:type: Tutorial
:audience: Linguists, conlangers (minimal programming jargon)

This guide explains the internal workings of LatticeLang - the decisions
made and linguistic theories used to make it work. Like all sciences,
they're theories, and they don't all perfectly mesh, either. Similarly,
a small program like this can't accurately depict all of linguistics either
so outliers also had to be scoped out at some arbitrary line as well.

At a High Level
---------------

LatticeLang is a tool for designing phonological inventories — the
sounds of a language. You tell it which sounds exist, what features
they have, and how they fit together. It then generates syllable
structures, validates your constraints, and exports everything in
consistent formats.

That's pretty standard for phonology generators - there's a lot of
them out there. Enough that it's a bit tough to write out a list of them,
I usually just send people to Rosenfelder's "Gen". Zompist's Gen <https://www.zompist.com/gen.html>.
What I wanted specifically was a program with fiction authors in mind, less-so
conlangers with a hobby. Writers don't have time to make conlanging a
full hobby. They might be interested in the things that a basic conlang
might bring to their worlds, but struggle with the ins and outs that
you get a sense of when you take it up as a full hobby. Writing is already
the hobby for a lot of people. Also, it should be a touch more accessible
for people curious about language than some of the Gens out there.

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
see how that changes the output (we'll see if I can get that working).
This will help people choose the right rules for what they want, and
hopefully learn something too. It should function alright as a toy for
learning about linguistics basics as well, hopefully.


Here's what happens internally, translated from technical terms:

**PHOIBLE curation**
This is in the GitHub repo but not included for end users. PHOIBLE is
a collection of data from real world languages that contains 2,155 inventories
spanning 2,104 language names (1,673 distinct ISO codes), as counted
from the pinned PHOIBLE 2.0 release that the authors of
the database were able to collate. They already did the work of removing
duplicates and normalizing the data itself. It's open-source, so I've
been able to make use of their hard work for less-than-scientific purposes.
I ran scripts that didn't take PHOIBLE for granted: it compares it to the
IPA list. This way certain kinds of complex entries are set aside - an
example is clicks. Clicks only ever appear with another sound - something
not reflected in the IPA chart. You just have to know that. I can't assume
users will be able to apply that if they don't know, not to mention that
in PHOIBLE, the click glyphs themselves have 0 rows where they appear alone.
These exceptions are placed aside and marked - they have to be handled
in a different way than the rest. (See :ref:`phoible_use_methodology`)
(PHOIBLE never lists the bare click letters at all — it documents clicks
only in accompanied forms, and those rows are complete and usable. The
problem is the mismatch between what the chart lists and what the
database attests, not missing data.)

**Data Stuff**
LatticeLang starts with this data, not from scratch. This ensures the sounds
suggested are plausible and can even tell you by how much compared to real
languages. In this lang-gen you're somewhat more informed about what actually occurs in
human languages. This program puts a special emphasis on it because that's
usually what people are actually doing. It does allow for overrides, though.

**The IPA Reference Table**
The tool generates a master table, mapping every IPA symbol to its
properties: features, rarity in world languages, Unicode codepoints,
canonical forms, and aliases. This becomes the lookup table for all
subsequent operations. This is what actually ships with the program,
with the information codified in a way more useful to the program to read.

**Derive Sonority Ranks**
Every sound gets a "sonority rank" — a number indicating how sonorous
(vowel-like) it is. Stops (p, t, k) score lowest; vowels score highest.
This ranking determines which sounds tend to fill which slots in syllables.
This was one of the initial rules I wanted to include - most generators
really only focus on CVC, sometimes the overall likelyhood of a pattern
appearing - but don't give any hints on what's already likely. I had
to keep track of sonority myself, which was difficult.

**Validate Against Rules**
The user's inventory passes through six validation checks, detailed under Validation Gates below.

**Instantiate Phonemes**
Individual Phoneme objects are created, each carrying:
- The IPA symbol itself
- A feature set (consonantal+, syllabic-, etc.)
- Derived category (consonant, vowel, glide, diphthong)
- Sonority rank
- Generation frequency weight

The user can also assign **Orthography**, or the spelling, to each phoneme.
For now, this is somewhat simplistic, but I'd like to add rules to this as well,
such as sound changes when next to other set phonemes, etc., which causes
inconsistencies in spellings, potentially, as in English.

Why This Matters
----------------

Most tools let users create anything, including linguistically
impossible combinations or other 'interesting' edge cases. That's
great for play and to experiment with lingustics,, but for novelists
too much adventure can be just difficult to read, or tempting to put
on display when the words should really be serving the story - sometimes
this work's just flavor.

LatticeLang prevents this *before* it happens, not after. You're
nudged toward naturalistic patterns without being
explicitly forbidden. It'll still allow you to make whatever, but there's
fundamentals that appear by default, especially when it's making
assumptions about what you are feeding it.

This is the "Naturalistic Defaults" principle (:ref:`ADR-035`).
It's easier to be flagged for what's unusual than remember what
you don't know you have to put in there — so the tool is lifting
that weight for you. It might be Ref 35, but this was a ground-level
principle behind the tool and why I'm not just using
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

In LatticeLang, you don't assign a phoneme to a category
by hand. The tool derives the sound's recorded attributes using
decision rules. Two features do most of the sorting:

- **Consonantal**: whether the sound obstructs the airflow
  enough to pattern with consonants
- **Syllabic**: whether it can serve as the heart of a
  syllable (as the nucleus)

The rules:

- **Consonant**: consonantal+, syllabic−
- **Vowel**: consonantal−, syllabic+
- **Glide** (j, w): consonantal−, syllabic− — essentially the
  close vowels i and u in non-syllabic form; languages treat
  them almost like consonants in where they're allowed to
  appear
- **Diphthong**: a two-vowel combination, stored as a single
  phoneme with its components recorded

Marking a sound as both consonantal and syllabic (like n̩,
the "n" of "button") can also come up — it's a syllabic
consonant. The tool will keep it in the consonant category
but allows it to fill a syllable's nucleus.

Meaning, these are derived automatically under normal circumstances
based on naturalistic languages' usual patterns. However, this
can be overridden in LatticeLang for a conlanger who knowingly wants
an analysis that departs from the linguistic default.

The user could invent a sound the PHOIBLE database doesn't know and
supplies its features by hand, and the category derives from those
hand-entered features (so even here, it's derived — just from user
data rather than reference data), or such a user-defined entry
could represent sounds that resist the clean partition that happens
to be outside PHOIBLE's dataset.

Validation Gates
----------------

When you build your inventory, six checks run:

**INV-1: Nucleus Capacity**
(blocking error) At least one phoneme must be able to serve as
a syllable nucleus — a vowel, a diphthong, or a syllabic
consonant. Without one, no template can produce a word, so
this is the only check that stops the build, with a hint to
add a vowel or a syllabic consonant.

**INV-2: Consonant Absence**
(warning) An inventory with zero consonants is flagged. It is
allowed — nothing blocks — but it is typologically rare
enough to be worth naming.

**INV-3: Vowel Absence**
(warning) Vowelless languages do exist (Nuxalk famously), so
a missing vowel is not an error. The warning fires only when
one of your templates requires a vowel in its nucleus slot —
an inventory of syllabic-consonant nuclei with matching
templates passes silently.

**INV-4: Identical Feature Sets**
(warning) Two phonemes with identical features but different
symbols are either allophones recorded as separate phonemes
or an entry mistake — the warning names the pair so you can
decide which.

**INV-5: Minimal Feature Sets**
(note) Two phonemes differing in exactly one feature, like
/t/ and /d/, are a normal minimal pair — unremarkable, and
nothing fires on its own. This note only ever surfaces
alongside symbol-similarity detection, which is not yet
implemented.

**INV-6: Diphthong Component Presence**
(warning) A diphthong's component symbols must themselves be
in the inventory: ``ai`` cannot be a diphthong if ``i`` is not
a phoneme. Non-blocking, but the gap is named so it can be
fixed.

Duplicate symbols are deliberately not a check: adding a
phoneme whose symbol already exists triggers a deterministic
merge per the contract's merge rule rather than an error.
Checks on the phonemes themselves — feature vocabulary
conformance and diphthong structure — happen when each
phoneme is built; see the technical specification
(:ref:`dc_phoneme`).

The Special Combinations Case
-----------------------------

Some IPA symbols aren't single characters — they're combinations:

- Tie bars (``k͡p`` — labial-velar double articulation)
- Length marks (``aː`` — long vowel)
- Syllabic diacritics (``l̩`` — syllabic consonant)

These (from the PHOIBLE data) route to a separate ``special_combinations`` bucket in the
output. They're still considered valid 'phonemes', just handled differently
during segmentation. When we complicate things at a later stage, they'll have more uses.

Frequency and Rarity Tiers
--------------------------

PHOIBLE provides raw inventory counts. LatticeLang
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
- **Tier 6a**: Attested, but below 1% and not an isolate
- **Tier 6b**: Isolate — attested in exactly one inventory of the sample

They're not completely arbitrary - I chose break points by hand where there
were slightly-larger-than-average gaps between deltas. Those happened
to be fairly round numbers, but that's coincidence and sometimes just
because the gap was so large I could choose a round number within it.

A caveat on 6b: "isolate" means "appears in exactly one inventory of
this 2,155-inventory sample," not "rare in a linguistic sense" —
sampling gaps and source quirks can strand a sound in tier 6b that
isn't actually "unique" (though, it can still be assumed to be a **little**
unusual). Sounds that aren't in the reference table at
all aren't forbidden — they're custom symbols, usable freely for
speculative conlangs. While the PHOIBLE data is impressive, it shouldn't
be mistaken for "complete". Authors can add whatever they like and know
how unusual it really is.

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
- Cross-syllable harmony (backness/rounding, nasal harmony)
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
- :ref:`phoible_use_methodology`
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

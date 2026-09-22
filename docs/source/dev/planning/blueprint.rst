.. _blueprint:

LatticeLang Blueprint: Full Suite Vision
========================================

:date: 2026-08-24
:type: Static
:audience: Developers and contributors
:purpose: What are we building and why?

Overview
--------

LatticeLang is not a language generator. It is a **language
construction helper** — a suite of tools that helps conlangers
form, track, and validate the rules of their constructed language.
Its design draws on two traditions: the conlanging community's
practice, codified in Rosenfelder's Language Construction Kit
:cite:p:`rosenfelder2010`, and the theoretical linguistics literature
(see :ref:`theoretical_framework` and the :ref:`bibliography`),
which grounds the phonological machinery.

The program helps with the algorithmic and organizational aspects
of language construction: generating words that obey phonotactic
rules, managing inflectional paradigms, tracking etymologies,
simulating sound change. The **creative and linguistic decisions**
remain with the user. The program enforces consistency, generates
examples, flags contradictions, and teaches the principles as it
goes.

Philosophy
----------

**The user decides; the program assists.** Every rule in the
language is a human decision. The program helps the user express
those rules formally, validates that they're internally consistent,
and generates output that lets the user see whether the results
match their intention.

**Each module is independently useful.** A conlanger who only wants
help with phonology should get value from the phonology module
alone. The suite composes, but does not require, all modules.

**Changes propagate by notification, not auto-correction.** If a
user changes their phoneme inventory after building morphology,
the morphology module flags affected entries — it does not silently
rewrite them. The user makes the correction, learning what changed
and why.

**Pedagogy is a layer, not a feature.** The program teaches by
explaining choices, flagging concerns, and linking to reference
material (LCK chapters, Wikipedia, academic sources). This guidance
appears at decision points, not as a separate "tutorial mode."

Modules
-------

The suite is organized into modules that correspond roughly to the
chapters of a reference grammar, following the LCK's recommended
order. Each module has its own data model, user interface, and test
suite. Modules communicate through a shared project file.

:Organization: Reference grammar, ch. N (Section Name)
:Conlanging sources: :cite:p:`rosenfelder2010`, ch. "Chapter Title"
:Theory sources: To be determined when this module enters design

.. _module_phonology:

Module 1: Phonology (PhonoBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: In Progress (Phase Beta)
:Organization: Reference grammar
:Conlanging sources: :cite:p:`rosenfelder2010`, ch. "Sounds"
:Theory sources: :cite:p:`hayes2009`, :cite:p:`clements1990`
:Depends on: Nothing (foundation module)
:Independent utility: High — word generation alone is valuable

What it does:

- Define or import a phoneme inventory
- Define syllable templates (onset-nucleus-coda patterns)
- Define phonotactic constraints (nine MVP types, extensible)
- Generate words that obey the rules
- Design orthography (romanization) for the inventory
- Import romanized words and infer IPA (reverse pipeline)
- Export phoneme charts, word lists, LaTeX tables

Data model: :ref:`dc_language_definition`

Key challenge: Orthography → IPA conversion is dialect-specific
and inherently ambiguous. The program makes educated guesses;
the user corrects.

What "done" looks like for this module:

- User can define a phonology from scratch or import romanized words
- User can generate words that obey all constraints
- User can export to LaTeX
- All edge cases in :ref:`uc005`, :ref:`uc012`, :ref:`uc013` are handled
- Test suite is comprehensive

.. _module_morphology:

Module 2: Morphology (MorphoBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Future (Phase Epsilon+)
:Organization:
:Conlanging sources: :cite:p:`rosenfelder2010`, ch. "Grammar", "Word Building"
:Theory sources:
:Depends on: Module 1 (Phonology) — morphemes are made of phonemes
:Independent utility: Medium — most useful with lexicon

What it does:

- Define inflectional paradigms (conjugation, declension)
- Define derivational rules (prefix, suffix, infix, compounding)
- Manage a morpheme library (roots, affixes, clitics)
- Generate inflected word forms from roots + rules
- Validate that morphemes use only phonemes in the inventory
- Apply morphophonological rules (e.g., vowel harmony, lenition)

Data model: MorphemeDefinition, Paradigm, InflectionRule

Key challenge: Morphophonology — the rules that govern how sounds
change when morphemes combine (e.g., English "cats" /kæts/ vs
"dogs" /dɔgz/ — the plural marker is /s/ or /z/ depending on
voicing). This requires the phonology module's feature system.

Forward-compatibility: If the user changes their phoneme inventory,
the morphology module flags morphemes that reference removed
phonemes. It does not auto-fix them.

.. _module_syntax:

Module 3: Syntax (SyntaxBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Future
:Organization:
:Conlanging sources: :cite:p:`rosenfelder2010`, ch. "Syntax"
:Theory sources:
:Depends on: Module 2 (Morphology) — words have inflected forms
:Independent utility: Low — requires morphology to be meaningful

What it does:

- Define word order rules (SVO, SOV, VSO, free)
- Define phrase structure rules
- Define agreement and government rules
- Generate example sentences
- Validate sentences against the grammar rules
- Interlinear glossing (align words with morpheme-by-morpheme translations)

Data model: GrammarRule, PhraseStructure, Sentence

Key challenge: Syntax is where the "algorithm" becomes most complex.
Natural language syntax has recursion, movement, and long-distance
dependencies. For a conlang, the user defines the rules — but
the program needs to parse and generate sentences that obey them.

.. _module_lexicon:

Module 4: Lexicon (LexiconManager)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Future
:Organization:
:Conlanging sources: :cite:p:`rosenfelder2010`, ch. "Lexicon", "Semantic Fields"
:Theory resources:
:Depends on: Module 1 (Phonology) — words are made of phonemes
:Independent utility: High — a dictionary with etymology tracking is useful even without generation

What it does:

- Manage a dictionary (headwords, definitions, part of speech)
- Track etymologies (derived from root X via rule Y)
- Organize by semantic field (body parts, kinship, colors, etc.)
- Search and browse
- Import/export (CSV, JSON, custom formats)
- Detect gaps (e.g., "you have a word for 'father' but not 'mother'")

Data model: LexicalEntry, Etymology, SemanticField

Key challenge: Keeping the lexicon synchronized with phonology
changes. If a phoneme is removed, words containing it are flagged.

.. _module_sound_change:

Module 5: Sound Change (HistoriaBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Future
:Organization: :cite:p:`rosenfelder2010`, ch. "Language Families, Sound Changes"
:Conlanging sources:
:Theory sources:
:Depends on: Module 1 (Phonology), Module 4 (Lexicon)
:Independent utility: Medium — useful for worldbuilders creating language families

What it does:

- Define sound change rules (e.g., "p → f before s or t")
- Apply rules to a lexicon to produce a daughter language
- Layer multiple rule sets chronologically
- Compare parent and daughter languages
- Generate etymological chains

Data model: SoundChangeRule, LanguageFamily, ChronologicalLayer

Key challenge: Sound change rules operate on phonemes with
features, so they need the full phonological feature system. Rules
like "voiceless stops → voiced between vowels" require querying
features (voiced, manner) across word boundaries.

.. _module_writing:

Module 6: Writing System (GraphoBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Future
:Organization: :cite:p:`rosenfelder2010`, ch. "Writing Systems"
:Conlanging sources:
:Theory sources:
:Depends on: Module 1 (Phonology) — scripts represent phonemes
:Independent utility: Low — mostly presentation

What it does:

- Design a custom script (assign glyphs to phonemes)
- Define direction (LTR, RTL, boustrophedon)
- Map between IPA, romanization, and native script
- Export font mappings (for use with font editors)
- Render text in the custom script

Data model: ScriptMapping, Glyph

Key challenge: Font generation is outside the scope of a Python
tool. The program can output mapping tables (glyph → phoneme)
that a user takes to a font editor (FontForge, etc.).

.. _module_pedagogy:

Module 7: Pedagogical Companion (DidactoBuilder)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Status: Cross-cutting (developed incrementally alongside all modules)
:Organization: :cite:p:`rosenfelder2010`, ch. All chapters (suite integration)
:Conlanging sources:
:Theory sources:
:Depends on: All modules (as a layer)
:Independent utility: None (it's an overlay)

What it does:

- Provides context-sensitive help at decision points
- Links to relevant LCK chapters and references
- Flags common mistakes (e.g., "your phonology has no fricatives
  — most natural languages have at least one")
- Suggests alternatives (e.g., "consider adding a lateral
  approximant")
- Explains linguistic terms when introduced

This is not a separate module but a **cross-cutting concern** woven
into each module's interface. It grows as each module is developed.

Shared Architecture
-------------------

Project File Format
~~~~~~~~~~~~~~~~~~~

All modules read and write to a single LatticeLang project file
(``.llp`` — a directory containing JSON files, one per module)::

    my_language.llp/
    ├── project.json          # Metadata (name, author, created)
    ├── phonology.json        # Module 1
    ├── morphology.json       # Module 2
    ├── syntax.json           # Module 3
    ├── lexicon.json          # Module 4
    ├── sound_changes.json    # Module 5
    ├── writing_system.json   # Module 6
    └── source_words.txt     # Original romanized input (preserved)

Each module owns its file. Cross-module references use stable IDs
(e.g., a morpheme references a phoneme by symbol, not by index).

Change Propagation
~~~~~~~~~~~~~~~~~~

When a module's data changes, affected entries in other modules
are **flagged** — not auto-corrected::

    [Phonology] Removed phoneme /ʔ/ from inventory.
    [Lexicon] 3 words contain /ʔ/: "maʔa", "ʔili", "paʔu"
    [Morphology] 1 morpheme references /ʔ/: glottal stop infix
    → Review affected entries? [Y/N]

The user decides what to do. The program ensures they *know* what
broke, but doesn't guess how to fix it.

Backup Plans
------------

If the full suite is never completed, each module is still useful:

+----------------------+------------------------------------------+
| Module(s) Completed  | What the user gets                       |
+======================+==========================================+
| Phonology only       | Word generator, phoneme inventory        |
|                      | manager, orthography designer, IPA       |
|                      | importer, LaTeX export                   |
+----------------------+------------------------------------------+
| + Morphology         | Above + inflection paradigm builder,     |
|                      | derivational rule engine                 |
+----------------------+------------------------------------------+
| + Lexicon            | Above + searchable dictionary with       |
|                      | etymology tracking                       |
+----------------------+------------------------------------------+
| + Sound Change       | Above + daughter language generator,     |
|                      | historical layering                      |
+----------------------+------------------------------------------+
| + Syntax             | Above + sentence generator, grammar      |
|                      | validator, interlinear glossing          |
+----------------------+------------------------------------------+
| + Writing System     | Above + script designer, font mapping    |
+----------------------+------------------------------------------+

Even **Phonology alone** is more than most existing conlang tools
offer. The reverse pipeline (romanized words → IPA → inferred
inventory) is, to our knowledge, not available in any existing
tool.

Research Questions
------------------

1. Phonology module questions — orthography conversion, segmentation, constraint system extensibility
2. Cross-module architecture questions — project file format, change propagation, dependency management
3. Morphology questions — morphophonology interface, paradigm handling
4. Syntax questions — grammar rule formalism, parsing approach
5. Lexicon questions — synchronization, etymology tracking
6. Sound change questions — rule formalism, feature querying
7. Writing system questions — font mapping approach
8. Pedagogy questions — how to surface guidance
9. Engineering questions — testing strategy, module isolation, versioning
.. _phoible_use_methodology:

PHOIBLE use methodology
=======================

:date: 2026-10-11
:type: Reference essay
:audience: Curious readers — no programming or linguistics
   background assumed

How LatticeLang turns PHOIBLE, a large database of sounds
documented from real languages, into the reference data the
program actually ships. Technical terms are glossed where
they first appear.

We never "generate" combinations
--------------------------------

Partly error-proneness, but the deeper reason is invented data.
The project has a doctrine written into the chart-membership
filter rationale: transcription is curation, not invention —
zero invented values. Here's what breaks if we tried to generate
the click roster combinatorially (by multiplying every companion
sound by every click letter), say k/ɡ/ŋ/q/ɢ/ɴ × 5 click letters:

1. **We'd invent symbols PHOIBLE never documented.** The census
shows the real families are lopsided — 50 velar-prefixed
rows but only 5 ɢ-prefixed ones, and the two ʼŋ-prefixed
glottalized rows exist for only two of the five letters.
A product of prefixes × letters would produce combinations
that occur in no natural language (in the sample), and we'd
have no features, frequency, or rarity data for them — we'd
be fabricating a reference table.
2. **We'd miss real ones.** ʼŋǀ and qʘʰ come from no prefix × letter
rule — they're layered accompaniments (glottal closure,
aspiration stacks). A combinatorial generator structurally
wouldn't predict these; only reading them off the hand-
collected data can.
3. **Features can't be composed.** Each of the 156 rows carries
a hand-curated 38-column feature vector describing that
specific accompaniment. "Velar + alveolar click features"
isn't an arithmetic sum — merging feature vectors by guesswork
produces plausible-looking-but-wrong entries.
4. **Traceability.** Every stored glyph is byte-for-byte
traceable to the pinned, checksummed copy of PHOIBLE the
repository carries. Generated spellings could break the audit
trail; there's no row in the vendor data you can point at
and say "that's where this came from."

Anything that ships either came from PHOIBLE spelled exactly
as the database spells it, or is explicitly hand-curated by
us, visibly, in a small file a human reviewed.

What our plumbing actually does
-------------------------------

The pipeline looks like this:

.. mermaid::

   flowchart TD
     A["PHOIBLE phonemes listing<br>(which symbols exist, how often)"]
     B["PHOIBLE features table<br>(38-columns of feature vectors)"]
     C{"JOIN - NFC Normalized"}
     D["Shared-symbol set (~2,100)"]
     E["Drop-log: Featureless 62,<br>Features-only 66"]
     F{"CHART MEMBERSHIP FILTER<br>data/ipa_chart.json"}
     G["ASCII romanization rows,<br>Accompanied click clusters"]
     H["Derive classifications, ranks,<br>tiers, frequencies"]
     I["Curated overrides.json<br>(descriptions, aliases)"]
     J["data/ipa_reference.json<br>ships with the wheel"]

     A --> C
     B --> C
     C --> D
     C -.-> E
     D --> F
     F -->|on chart| H
     F -.->|off chart| G
     H --> J
     I --> J

The **JOIN step** compares two PHOIBLE files against each other.
"NFC normalized" means the spellings were first standardized
to one Unicode form (by us), so the same sound spelled two
different ways on the byte level still match. The **drop-log**
is a build-time repport of everything that got excluded and
why. Exclusions here are visible and counted, never silent.

The **chart-membership filter** asks, "Is this symbol on the IPA chart?"

So the affricate "ts", double articulations like "kp", aspirates
like "pʰ" are all kept, because they're chart-sanctioned
segments that happen to be spelled with multiple glyphs (spelled
here the way PHOIBLE spells them, without the tie-bar you might see
elsewhere). But a single-glyph symbol that's off-chart would drop if
it doesn't appear on the chart. This is for ease of use with what
people are most familiar with, and is just one way to sort the raw data.
We use tie-bars a slightly different way than the chart does later in
the program.

There's also an other route into the output: the
"special_combinations"/ **Curated overides** route. Things the chart
filter structurally can't express (long vowels "aː", syllabic marks "m̩",
tone letters, tie-barred spellings) enter through "overrides.json".
Two doors total: intersection for ordinary chart segments,
curation for everything else.

For example:
Clicks fall through a gap specific to them: the chart lists
only the five bare letters/symbols (ǀ ǁ ǂ ǃ ʘ), but PHOIBLE attests only
**accompanied** clusters (kǀ, ŋǃ...), and the bare letters have
zero rows. There's no overlap for clicks — the intersection
is empty, and the bare letters are parked in the chart's
"deferred" map with stated reasons rather than crashing the build.

How the data reaches you
------------------------

As data climbs from the build scripts toward what the user sees,
it transforms through what we're calling "layers" or "floors":

- **Floor 0**: *The derivation layer*. the repository's copy
  of PHOIBLE, the derive script, the NFC join, the drop-log,
  the chart file, and the test fixtures. Developers only; end
  users never run this.
- **Floor 1**: *The reference table* ``ipa_reference.json``,
  shipped with the program, read-only. Machine-shaped:
  verbatim spellings, feature sets, sonority ranks, frequencies.
- **Floor 2**: *The user's inventory*. The user assembles a
  set of phonemes. Whatever they pick or type gets enriched from
  the reference (features, a proposed sonority rank, pre-filled
  real-world frequency. Typed input goes through the input splitter
  ("segmenter"), with aliases ("ch" for "t̠ʃ") and near-miss detection;
  typing "p" when "pʰ" already exists (in most languages these are
  not usually distinct).
- **Floor 3**: *Phonotactics*. Syllable templates and constraints consult
  phoneme objects — data structure, not spelling. This is ADR-052's
  core insight: whether ts is one phoneme or two is represented by
  the object graph, never by the glyphs.
- **Floor 4**: *Generation*. The engine assembles words from those objects.
- **Floor 5**: *Display*. Only here do tie bars get added, tooltips
  render descriptions, rarity tiers become human-facing common-ness
  labels. The verbatim spelling below, user-centric rendering above.

Suggesting click clusters to the user would live at
Floor 2, pulling from Floor 1's reference.
The emission decision and the eventual interface are linked:
the install package (wheel) only ships Floor 1.

A note on Floor 0
-----------------

- It's "done on demand, never at runtime." The pipeline is deliberately
  re-runnable. A PHOIBLE update requires a recorded decision (ADR), then
  a re-run and diff review (ADR-033). So Floor 0 is a workshop, not a one-time event.
  Its product, "ipa_reference.json", is frozen and shipped, but the
  workshop stays in the repo for development.

- It also ships unevenly. The repository and source distribution (sdist)
  carry everything — vendor data, scripts, tests — so developers and CI
  can verify derived artifacts from source. The installable package carries
  only the product. So "Floor 0 never ships" is true for end users, but
  not for the repository.

The distinction matters for the click ruling (Q48): decisions about what the
workshop admits are methodology decisions, while decisions about what the
product contains are user-facing. That's why the ruling can exclude clusters
from emission while allowing for a curated batch later — the workshop is
still in place to make more.

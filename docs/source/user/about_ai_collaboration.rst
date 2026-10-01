.. _ai-collaboration-methodology:

AI Collaboration Methodology: An Experiment in Specification-Led Development
===========================================================================

:date: 2026-10-01
:type: Essay
:audience: Linguists, conlangers, developers curious about AI-assisted projects

This document describes how LatticeLang was developed using AI assistants,
why this approach differs from typical "AI-generated code," and what
we learned about documentation as a safety mechanism. It's transparent
about what worked, what didn't, and why this methodology matters for
future projects.

Introduction
------------

LatticeLang is a phonology-based conlanging tool for writers and linguists.
What makes this project unusual is how it was built: every feature was
specified in documentation *before* any code was written, and an AI
assistant helped translate those specifications into implementation.

This reversed the typical AI-assisted development pattern, where code
comes first and documentation follows (often poorly). In LatticeLang,
the documentation was the primary artifact; code was the secondary
derivation.

Why This Matters
----------------

AI in software development has been polarized between hype and fear. I'm an
AI is a tool kind of person. As a tool, it has impressive pitfalls and
a few genuine uses - but like all things, this takes experimentation to
tease apart.

This project demonstrates one concrete case:
- A solo developer with beginner Python skills, not enough to tackle a project of this size
- Using AI systematically for 12+ months. Mostly as an artist and writer concerned and interested about what AI can do.
- Producing working, tested software (with tests written first, per tech standards)
- Without hallucinated features, broken contracts, or technical debt (ideally-speaking).


The last is a crucial point for me. Software already was kind of bad lately, there's no advantage in
just speeding up already bad software design. But, when it comes to small batches of code, a
word-predictor can do well. It's not about doing more faster, it's about being more organized,
maybe having a second brain that can read text from anywhere at a moment's notice.

The project works through explicit constraints and verification
mechanisms — documented here so others can evaluate, replicate, or improve on them.

Methodology Overview
--------------------

Some of this is just mirroring best practices I've read about for real, human developers,
others come from my background in technical writing/documentation. I find when working with
LLMs, it's crucial to always already be an expert in the thing it's trying to help you with -
that way you can catch its mistakes - which are frequent. But you can't tell when you
don't understand the nuances of your topic and what it's missing in the responses. NEVER
interact with an AI on a topic you know NOTHING about. Create a bibliography of citations
and look each one up by hand. Read the sources themselves, not just that it cited something - same as Wikipedia.
I bought a lot of the books it decided to cite, where I could afford them. Found PDFs of
others. I tried not to cite anything I couldn't read myself.

**Documentation-first development**.

Rather than asking the AI "how do I implement X?" we established:

1. **Data Contracts**: Formal specifications of what data structures must look like
   (e.g., :ref:`dc_phoneme`, :ref:`dc_inventory`). The AI couldn't invent
   fields that weren't contractually specified.

2. **Use Cases**: Behavior specifications written in Cockburn format,
   describing what the user observes, not how the code achieves it.

3. **Test-First Discipline**: Every function required a test before
   implementation. The AI proposed tests; failures guided implementation.

4. **Provenance Tags**: Every factual claim in documentation carried
   inline sourcing: [record], [inference], [uncertain], [verified: output].

5. **Verification Discipline**: The assistant never asserted repository
   state without proposing a `grep` command to check it. Both parties
   trusted command output over memory.

This prevented the most common failure modes: feature drift, hallucinated
capabilities, and specification rot.

Tech Stack
----------

I refuse to give big companies any money, let alone for tokens. Furthermore,
the 'free token' era we have recently been experiencing is certain to dry
up sooner or later, making it a "dependancy" I wanted to avoid in this project
in general (not just as housekeeping but also just to help me maintain the project).
What I did do for a lot of the heavy lifting was give Proton 10$ a month for access
to it's Lumo 2.0 Max model. I was not able to figure out what "Lumo" is based on
which is a bit important to me. --Not yet, anyway. The rest of my AI use is entirely
local, using text-generation-webui and my fairly normal PC hardware. The models used
were from Hugging-Face, pre aquisition.

I do everything on Linux (Ubuntu Studio), with just VS-Codium piped to my Github
account. I don't use Microsoft's VSCode, nor any AI inside it. Currently, I'm not
even using automation like linting. When a change needs doing, I open it and edit
it myself. It's a bit backwards, but as a beginner it's sometimes
best not to overcomplicate things. Just writing the program itself is a bit
over my head at times. There's a lot of asking very basic questions as new concepts
come up. It eats a lot of context to explain everything that's happening, so having
a way to clear out the context but not lose progress or knowlege became something the
docs definately helped with.

Lumo's internal organization is a bit unhelpful. It has a memory feature, but it
remembers way too much and calls ancient files into the context sometimes. You can't
edit knowlege out from the LLM by hand - you can tell it not to refer to a file, but
every paste is just a date, so looking at every file is tedious. It was crucial to be
able to start from scratch in a predictable way in part because it was so easy for Lumo
to go off track with an old paste.

What Worked Well
----------------

**Documentation Standards**
A single file (`documentation_standards.rst`) encoded formatting,
cross-referencing, and hygiene rules. This ensured consistent output
across 20+ documentation files. When the AI violated a standard,
the Sphinx build caught it immediately.

**Verification Commands**
The `grep -rn 'pattern' docs/source/` discipline was the single most
effective safeguard. Both parties proposed commands rather than
asserting facts. When memory contradicted grep output, the grep
won — always. This caught drift in five separate sessions.

**Paste-Check Discipline**
After pasting any code block: `python -m py_compile <file>` before
running pytest. This separated paste-placement errors from logic
errors in under a second. Critical for catching unsaved-buffer
issues (where the editor shows fresh code but disk contains stale
code).

**Session Rituals**
Cold-start kit (AGENTS.md + Status Overview + ADR Index), epoch
line at session start (commit hash + test count), doc-contact
rotation (one planning/design doc checked against reality each
session). These prevented the "slow fade into wrong assumptions"
that happens in long collaborations.

What Didn't Work
----------------

**Initial Label Naming Confusion**
Early sessions used lowercase ADR labels (`adr-032`) contrary to
the documented convention (`ADR-032`). This broke cross-references
silently for weeks. The fix: stricter label hygiene in the
documentation standards, plus the label-check audit command.

I was learning what worked best with sphinx and the auto-complete in
VS-Codium. This is just me messing around with what things should look
like - that uncertainty made the AI produce choose randomly for a
while. That's fine but always define anything that's going to be in
a codeblock explicitly - preferably before you write a lot. If you
develop it organically, stop at some point, make a firm decision and
change everything to match it. Once that's done, the LLM follows this
really well.

**Over-Eager Implementation**
Sometimes the AI proposed features not in the use cases, motivated
by "this would be helpful." The cure: explicit scope creep flags
("that's post-MVP" as an explicit thing to watch for against the docs).
The LLM folled instructions to distinguish between
MVP (Beta phase) and future phases (Gamma, Delta, Epsilon).

I experimented early with OMP - it basically tried to build everything
all at once, and I could barely keep up with what it was generating, even
WITH docs. I switched to copy and pasting individual code blocks one at a time
with Lumo. It's very slow by comparison, but I imagine it's still faster
than typing everything out by hand. That's still a meaningful improvement.

**Vacuous Tests**
One test (`test_aliases_resolve_to_symbol`) initially passed
because it never executed its loop body (empty alias arrays in
the fixture). The test "worked" while testing nothing. Lesson:
tests require negative assertions (what *shouldn't* happen)
as well as positive ones.

This would be helped enormously if I had any experience in auto-testing.
You get used to poking the LLM to check itself. With no guardrails written
at all, you could probably "pushback" on an LLM all day, getting it to
double back on itself and agree to whatever you seem to want - the idea
here was to ground the LLM to a "souce of truth" as it likes to call it -
that being the docs, ADRs and the documentation_standards (and previous
files in general). That way, when I do a 'pushback', the LLM 

AI's Role (and Limits)
----------------------

The AI assistant performed three distinct functions:

1. **Specification Reviewer**: Reading drafts, flagging contradictions,
   suggesting additions, checking against existing decisions.

2. **Code Translator**: Turning approved specifications into
   implementation, including test harnesses.

3. **Debugging Partner**: Interpreting error messages, proposing
   hypotheses, suggesting grep/pytest commands.

The AI did *not*:

- Make binding decisions (ADR authorship remained human)
- Modify production code - I did that, peice by peice.
- Assume repository state without verification. Or assume anything, really.
- Persist memory across sessions (all context was re-injected)

Greps were super important and explicitly ruled for. If it didn't know something, it got greped.
Double checking states around git as well. In addition, I have a rule about social softening words,
stuff like "honestly" and other qualifiers that are designed to 'reassure' - basically, when it comes
to statements, anything that seemed to be qualified in such a manner gets double-checked. It now responds
with statements that end in what it calls "provenance tags" - it's almost like a citation but to the
project itself. Easily checkable.

Lessons Learned
---------------

**Specification Thickness Matters**
Vague specs ("handle IPA input") produce hallucinated implementations.
Thick specs ("PHOIBLE 2.0 TSV with 13 columns, validated per
:ref:`dc_phoible_source`") constrain the AI to the contractual
boundary. The thickness of the spec predicts the reliability
of the implementation.

**Drift Accumulates Without Audits**
Without forced full-build audits, incremental Sphinx builds hide
warnings indefinitely. The `-E` flag (discard cache) became
non-negotiable for end-of-session hygiene.

I did a lot of this by hand and some of that is vibes - I had to
have a sense for which documents "felt" most out of date. At intervals
I decided "we've made a lot of decisions since then" and forced a
doc by doc review. This is where a lot of documentation standards
and some non-linguistic ADRs come from. As the project solidified
and I wanted certain things to be remembered, it became meta-information
that got recorded. This is just something about managing use-case
documents, and definately best done by hand. The AI helped out
by reading and comparing quickly and offering suggested changes. By
changing the lines myself I can keep some 'sense' of the project
overall, even if I can't fully follow every technical decision.

**Human Expertise Still Essential**
Linguistic domain knowledge remained entirely human. The AI
couldn't invent phonological rules; it could only implement
what was specified.

Though, I'm not a linguist either. Much of the raw research
was done by the AI (and then hand-checked by me once found).
I didn't know about foundational texts much of LatticeLang
hinges on. I have a passing knowlege (primarily through Rosenfelder's
conglanging books) - but he isn't citing textbooks either.
I then made the best decisions I could based on what I wanted
the program to do.

**Tooling Over Trust**
Command output trumps both parties' memories. Provenance tags
on every claim. The system is resilient precisely because it
doesn't trust anyone — not even itself.

I have an extremely poor memory myself - I don't remember much better
than it does - part of what lead me to documentation in the first place.
This means that I have a pretty good understanding of the things
most likely to get forgotten about, I suppose. Fail-safes are
things I have built into my personal life and work at all levels
anyway. Extending it to help the LLM wasn't too much of a stretch.
The lack of trust is something an LLM also doesn't personally mind
as much as a fellow human either. It's just good sense. The constant
assumption that we will make mistakes at every turn helped keep
adding rules and auditing top of mind, and a key aspect of development.

Replicability
-------------

If you want to try this methodology:

1. Start with documentation, not code. Even rough drafts. (I recommend being as thorough as possible - see Cockburn)
2. Establish one (or more) "standard of truth" file(s). AGENTS.md are LLM-specific rulings, documentation_standards is for everyone. Use Cases keep the scope and architecture helps the LLM navigate. All of this info needs triggers, sometimes right in the file, so the LLM remembers to use them.
3. Require tests for every new function. (Though, I would recommend this for all development anyway, generally)
4. Use grep-style verification for all state claims. (Helps to also tell the LLM how to avoid placating language in general.)
5. Never let the AI make binding decisions alone. (You have to have an iron grip and thorough understanding of your ADRs and other 'truth' files.)

You don't need our exact stack (Sphinx, Poetry, pytest). You need
the discipline: spec → test → implement → verify. The tools are
secondary.

Meaning, if you build enough of a structure around the LLM and treat
it as a generation machine that can't run by itself any more than any
machine should, the results are pretty good. Be generous with the caution
tape around a big dangerous machine that moves fast. Table saws come to mind.
Be careful what you feed it and how.

Transparency Note
-----------------

This methodology is being documented openly because the AI-assisted
development space suffers from all kinds of nonsense - sometimes the AI
is credited with stuff that was mostly human-led. Other times it's left
to its own devices and puts out atrocious code that adds to overhead and
really would have been better served by not involving LLMs at all.

Between the two, there's reasonable uses. I'm learning a lot about how
Python works at the project level, excercising my doc skills,
practicing managing a project, learning how to work with data, and of
course furthering a dream project of mine. Glad to have access to
these foundational linguistics texts and reading fairly early papers.
I didn't want "AI" (llms) to pass me by as a creator - I prefer
investigating things that might cause me consternation, and this was
a productive experiment into how they work, what they're good for
and where they fall short, especially in epistimology and
"knowlege management".

Related Work
------------

- :ref:`uc01` — Phoneme inventory definition (primary use case)
- :ref:`ADR-033` — PHOIBLE 2.0 feature system pinning
- :ref:`dc_phoible_source` — PHOIBLE versioning policy
- :ref:`documentation_standards` — Full formatting standards

Changelog entry for this methodology: 0.3.0 (AI collaboration
methodology documented, `CHANGELOG.md`).

See Also
--------

- :ref:`how-latticelang-works` — This covers the decisions made that were implemented by the code. Should be readable for linguists.
- :ref:`glossary` — Technical terminology
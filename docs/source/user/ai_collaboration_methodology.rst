.. _ai-collaboration-methodology:

AI Collaboration Methodology: An Experiment in Specification-Led Development
============================================================================

:date: 2026-10-01
:type: Essay
:audience: Linguists, conlangers, developers curious about AI-assisted projects

This document describes how LatticeLang was developed with LLMs, how my
approach appears to differ from typical "AI-generated code," and what
was learned about documentation as a safety mechanism. I can then report
about what worked, what didn't, and why this methodology might be useful
as an experiment.

Introduction
------------

LatticeLang is a phonology-based conlanging tool for writers and linguists.
What makes this project build different from LLM-generated code is that
every feature was specified in traditional documentation *before* any code
was written, and an AI assistant helped translate those specifications
into implementation.

This reversed the typical AI-assisted development pattern, where code
comes first and documentation follows (often poorly). In LatticeLang,
the documentation was the primary go-to; code was dependant on adhering to it.

Transparency
------------

This methodology is being documented openly because the AI-assisted
development space suffers from all kinds of nonsense - sometimes the AI
is credited with stuff that was mostly human-led. Other times it's left
to its own devices and puts out atrocious code that adds to overhead and
really would have been better served by not involving LLMs at all.

Between the two, there's reasonable uses. I'm learning a lot about how
Python works at the project level, exercising my doc skills,
practicing managing a project, learning how to work with data, and of
course furthering a dream project of mine. Glad to have access to
these foundational linguistics texts and reading fairly early papers.
I didn't want "AI" (llms) to pass me by as a creator - I prefer
investigating things that might cause me consternation, and this was
a productive experiment into how they work, what they're good for
and where they fall short, especially in epistemology and
"knowledge management". They're an okay tool for some
applications - like most tools. A lot of caveats.

Why This Matters
----------------

AI in software development has been polarized between hype and fear. I'm an
AI is a tool kind of person. As a tool, it has impressive pitfalls and
a few genuine uses - but like all things, this takes experimentation to
tease apart.

This project demonstrates one concrete case:
- A solo developer with beginner Python skills, not enough to tackle a project of this size (but still somewhat small)
- Background with local LLMs for 12+ months. Mostly as an artist and writer concerned and interested about what AI can do.
- Producing working, tested software (but with tests written first, per tech standards)
- Without hallucinated features, broken contracts, or technical debt (ideally-speaking). It was specifically planned against to the best of my ability, anyway.


The last is a crucial point for me. Software already was kind of bad lately, there's no advantage in
just speeding up already bad software design. But, when it comes to tiny batches of code, a
word-predictor can do well. It's not about doing more faster, it's about being more organized,
maybe having a second brain that can read text from anywhere at a moment's notice.

The project works through explicit constraints and verification
mechanisms — documented here so others can evaluate, replicate, or just improve on them.

Methodology Overview
--------------------

Some of this is just mirroring best practices I've read about for real, human developers,
others come from my background in technical writing/documentation. I find when working with
LLMs, it's crucial to always already be an expert in the thing it's trying to help you with -
that way you can catch its mistakes - which are frequent. But you can't tell when you
don't understand the nuances of your topic and what it's missing in the responses. NEVER
interact with an AI on a topic you know NOTHING about. Even then, create a bibliography of citations
and look each one up by hand. Read the sources themselves, not just that it cited something - same as Wikipedia.
I bought a lot of the books it decided to cite, where I could afford them. Found PDFs of
others. I tried not to cite anything I couldn't read myself. I have some familiarity with linguistics and code
but less than I'm usually comfortable engaging with an LLM on. I went in skeptical.

**Documentation-first development**.

Rather than asking the AI "how do I implement X?" we established:

1. **Data Contracts**: Formal specifications of what data structures must look like
   (e.g., :ref:`dc_phoneme`, :ref:`dc_inventory`). The AI couldn't invent
   fields that weren't contractually specified. Sometimes it helped define
   these based on technical considerations, sometimes these were defined by me.

2. **Use Cases**: Behavior specifications written in Cockburn format,
   describing what the user observes and how the program responds, not how the code achieves it.

3. **Test-First Discipline**: Every function required a test before
   implementation. The AI proposed tests; failures guided implementation.

4. **Provenance Tags**: Every factual claim in documentation carried
   inline sourcing: [record], [inference], [uncertain], [verified: output].

5. **Verification Discipline**: The assistant never asserted
   state without proposing a `grep` command to check it. Both parties
   trusted command output over memory. There was more of this than I think a vibe coder
   would put up with, but it was crucial and prevented a ton of mistakes LLMs introduce
   by 'introspection'.

This prevented the most common failure modes: feature drift, hallucinated
capabilities, and specification rot. Every single movement and problem was recorded.
Greps for subjects and sometimes even vectorization could surface related issues.

Tech Stack
----------

I refuse to give big companies any money, let alone for tokens. Furthermore,
the 'free token' era we have recently (2025-2026) been experiencing is certain to dry
up sooner or later, so making it a "dependancy" is something I wanted to avoid in this project
in general (not just as housekeeping but also just to help me maintain the project).
What I did do for a lot of the heavy lifting was give Proton 10$ a month for access
to it's Lumo 2.0 Max model. I was not able to figure out what "Lumo" is based on
which is a bit important to me. --Not yet, anyway. The rest of my AI use is entirely
local, using text-generation-webui and my fairly normal PC hardware. The models used
were from Hugging-Face, pre-acquisition.

I do everything on Linux (Ubuntu Studio), with just VS-Codium piped to my Github
account. I don't use Microsoft's VSCode, nor any AI inside it. Currently, I'm not
even using automation either. It's a bit slow and basic: I open VSCodium and edit
the files by hand. It's a bit backwards, but as a beginner it's sometimes
best not to overcomplicate things. Just writing the program itself is a bit
over my head at times. There's a lot of asking very basic questions as new concepts
come up. It eats a lot of context to explain everything that's happening, so having
a way to clear out the context but not lose progress or knowlege became something the
docs definitely helped with.

Lumo's internal organization is a bit unhelpful. It has a memory feature, but it
remembers way too much and calls ancient files into the context sometimes. You can't
edit knowlege out from the LLM by hand - you can tell it not to refer to a file, but
every paste is just a date, so looking at every file is tedious. It was crucial to be
able to start from scratch in a predictable way in part because it was so easy for Lumo
to go off track with old files. What I ended up working with was an extremely strict
set of documents.

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

What didn't work at first
-------------------------

Writing and revising working systems is something I've done professionally,
at the highest level for the UN. Surfacing working rough spots and writing
methods that eliminate them, or at least reduce their impact is basically
what I have the most professional experience doing at this point. I came
into the job a bit by accident, from the software testing side of things,
managing teams of testers. I wrote tests then, but often more important was
how those teams were organized internally to interact with data collection.

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
The LLM followed instructions to distinguish between
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
as well as positive ones. This would be helped enormously if I had
any experience in auto-testing, but I had to stumble over it as
I learned.

You get used to poking the LLM to check itself. With no guardrails written
at all, you could probably "pushback" on an LLM all day, getting it to
double back on itself and agree to whatever you seem to want - the idea
here was to ground the LLM to a "souce of truth" as it likes to call it -
that being the docs, ADRs and the documentation_standards (and previous
files in general). That way, when I 'pushback' on something, the LLM is
triggered to re-verify, not make a best guess on 'memory'.

AI's Role (and Limits)
----------------------

The LLM performed three distinct functions:

1. **Specification Reviewer**: Reading drafts, flagging contradictions,
   suggesting additions, checking against existing decisions. It had a
   better capacity to remember what I'd previously decided than I could
   without a lot of re-reading.

2. **Code Translator**: Turning approved specifications into
   implementation, including test harnesses. Also explaining what each
   code block was doing and why, referring back to previous ADRs or Use Cases.

3. **Debugging Partner**: Interpreting error messages, proposing
   hypotheses, suggesting grep/pytest commands. It shined at this, I
   never would have gotten anywhere with this otherwise.

The AI did not:

- Make binding decisions (ADR authorship remained human) - This had some exceptions at the data-level, as I didn't understand that stuff entirely at first. Each decision is marked with who decided it. Almost always I fought to understand it before a real decision was recorded though.
- Modify production code - I did that, piece by piece. This sometimes meant writing scripts that lifted data from one source into json, since copy pasting ASCII sometimes goes awry.
- Assume repository state without verification. Or assume anything, really. An excessive amount of checks were eventually running, to make sure everything was in freshest context. Changes were usually written against the previous turn.
- Persist memory across sessions. All context was re-injected by hand. This gave me a chance to oversee exactly what it was going to remember for the session and vet issues. I wrote extra rules between sessions based on difficulties I encountered.

Greps were super important and explicitly ruled for. If it didn't know something, it got greped.
Double checking states around git as well. In addition, I have a rule about social softening words,
stuff like "honestly" and other qualifiers that are designed to 'reassure' - basically, when it comes
to statements, anything that seemed to be qualified in such a manner gets double-checked. It now responds
with statements that end in what it calls "provenance tags" - it's almost like a citation but to the
project itself. Easily checkable, though often I could remember the source when it was listed to me.

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
Eventually a rotation of docs evolved, and this ran itself. Each
session usually involved looking over a doc just in case.

**Domain Knowlege**
Linguistic domain data was entirely human-sourced. The AI
couldn't invent phonological rules; it could only implement
what was specified so that helped in terms of being able to lock
it to immutible sources - I wasn't asking it to be creative. It
had to work with the data that was already there.

Though, I'm not a linguist. I didn't know about foundational
textbooks that much of LatticeLang hinges on. I have a passing
knowlege (primarily through Rosenfelder's conlanging books)
- but he isn't citing textbooks at that level. When it came to
linguistic fundamentals and how to manage the data itself, I
relied on the LLM's 'reasearch' and then hand-checked by
me once found. I then made the best decisions I could based on
what I wanted the program to do. I bought the textbooks I could
afford, and was able to find PDFs of a lot of the papers themselves.
Some of it is old enough it's well shared.

**Tooling Over Trust**
Command output trumps both parties' memories. Provenance tags
on every claim. The system is more resilient because it doesn't
trust either party.

I have an extremely poor memory myself - I don't remember much better
than it does - part of what lead me to documentation in the first place.
This means that I have a pretty good understanding of the things
most likely to get forgotten about, I suppose. Fail-safes are
things I have built into my personal life and work, at all levels.
Extending it to help the LLM wasn't too much of a stretch.
The lack of trust is something an LLM also doesn't personally mind
as much as a fellow human either. It's just good sense. The constant
assumption that we will make mistakes at every turn helped keep
adding rules and auditing top of mind, and a key aspect of development.

Replicability
-------------

If you want to try this methodology:

1. Start with documentation, NOT CODE. Even rough drafts. (I recommend being as thorough as possible - see Cockburn. Write the basics yourself even if that's just in design-doc format)
2. Establish one (or more) "standard of truth" file(s). AGENTS.md are LLM-specific rulings, documentation_standards is for everyone. Use Cases keep the scope and architecture helps the LLM navigate. All of this info needs triggers, sometimes right in the file, so the LLM remembers to use them.
3. Require tests for EVERY new function. (Though, I would recommend this for all development anyway, generally)
4. Use grep-style verification for ALL state claims. (Helps to also tell the LLM how to avoid placating language as well.)
5. NEVER let the AI make binding decisions alone. (You have to have an iron grip and thorough understanding of your ADRs and other 'truth' files. Review and read them often.)

You don't need the stack (Sphinx, Poetry, pytest). You need
the discipline: spec → test → implement → verify. The tools are
secondary.

If you build enough of a structure around the LLM and treat
it as a generation machine that can't run by itself any more than any
machine should, the results are pretty good. Be generous with the caution
tape around a big dangerous machine that moves fast. Table saws come to mind.
Be careful about the quality of what you feed it and how - safety first,
or it'll bite too fast to fix.

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

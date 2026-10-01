# AGENTS.md — LatticeLang Assistant Bootstrap

Machine-readable bootstrap index and operating rules for AI assistants
in this repository. Written assistants-first, humans-second: short
lines, grep-able headings, explicit paths. Normative content lives in
`docs/source/`; this file points to it and adds session mechanics.

## Cold-Start Kit (ASK for these at session start)
1. This file
2. Status Overview table — top of `docs/source/research/questions.rst`
3. ADR Index — top of `docs/source/dev/governance/decisions.rst`

Everything else is retrieved on demand. Past-session memory is never
a source of current state; the repo is.

## Retrieve on Demand (task triggers)
- Documentation edit or pasteable block → `docs/source/dev/governance/documentation_standards.rst`
- Touching a data contract or its code → that `docs/source/data_contracts/dc_*.rst`
- Implementing behavior → the governing use case file + its tests
- Committing a user-visible change → `CHANGELOG.md` (per documentation_standards.rst § Changelog Standards)
- Claiming anything exists in the repo → grep first (Verification Discipline)

## Tech Stack
- Python ≥3.11; Poetry (in-project venvs); pytest
- Sphinx + reST (furo, MyST, sphinxcontrib-bibtex, mermaid); Read-the-Docs hosting
- VSCodium on GNU/Linux

## Commands (always preceded by cd to repo root)

```
cd /home/danweel/Documents/VSCodiumFiles/LatticeLang/

poetry run pytest                                              # full suite
poetry run sphinx-build -b html docs/source docs/_build/html   # docs
```

# Full audit build — incremental builds hide warnings:

```
poetry run sphinx-build -E -b html docs/source docs/_build/html \
  2>&1 | grep -iE 'warning|error' | head -40
```

- RTD auto-builds on push. No build on readthedocs.org → check GitHub webhook deliveries + RTD integrations before anything else.
- `git status` / `git log --stat` whenever unsure; terminal pager exits with `q`.
- Assistant always gives full git commands with explanations.
- Epoch line: at cold-start (after the kit), run `git log -1 --oneline && poetry` run `pytest -q | tail -1` — ground-truth commit + test count, catching drift in the cold-start documents themselves.

# At Commit Time

- Change alters user-visible behavior, output, or data → update CHANGELOG.md in the SAME commit, never retroactively (documentation_standards.rst § Changelog Standards).
- Binding decision made → Status Overview + ADR Index updated in the same commit as the decision; update this file too (AGENTS.md) when a lesson belongs here.

# Documentation Map

- `docs/source/index.rst` — entry point
- `docs/source/use_cases/` — Cockburn-style use cases; level subdirectories: user_goal_level/, subfunction_level/, summary_level/, possible_future_cases/ (verified by ls, 2026-09-30)
- `docs/source/data_contracts/` — JSON schema contracts: dc_phoneme, dc_syllable_template, dc_constraints, dc_inventory, dc_language_definition, dc_orthography_rules, dc_ipa_reference, dc_phoible_source
- `docs/source/research/questions.rst` — questions registry, Status Overview at top; Q-numbers and ADR refs are the lingua franca
- `docs/source/dev/governance/decisions.rst` — ADRs, append-only
- `docs/source/dev/governance/documentation_standards.rst` — format rules for all docs (tables, labels, bib hygiene, edit-location anchors, changelog, data-contract section order)
- `docs/source/dev/planning/` — blueprint, phases, suite vision
- `docs/source/dev/design/` — architecture, theoretical framework, constraints (verified 2026-09-30)
- `docs/source/user/` — user-facing docs and troubleshooting
- `docs/source/glossary.rst` — terminology; referenced via `:term:`

# Binding Conventions (summaries; canonical text in the docs named)

- Use cases contain BEHAVIOR ONLY; fields and checks live in data contracts. Status fields on every use case (:Doc Status:, :Impl Status:, :Phase:). Long + short labels per use case (`.. _uc02:`, `.. _UC-02_TITLE`); references use :ref:`ADR-016`.
- ADRs append-only; supersede, never edit published ones.
- Questions: Status Overview row synced same-commit with any answer; :color: state success = ANSWERED, warning = OPEN.
- Code: Google-style docstrings, type hints, functions <50 lines, zero-dependency core (stdlib JSON/csv), seeded PRNG.
- `src/latticelang/` layout: core/, orthography/, ui/, utils/. Module↔use-case filename mapping finalized at implementation start.
- Technical suggestions state floor, connections, consequences, failure modes (documentation_standards.rst § Architecture Explanation); mermaid for diagrams, floor color conventions there.

# Key Decisions (Phoneme-module scope unless noted)

- :ref:ADR-032: phoneme category DERIVED from features
- :ref:ADR-033: PHOIBLE 2.0 feature system pinned; controlled-vocab strings; Q38 hybrid pipeline — TSV is build-time input only
- :ref:ADR-034: slot eligibility — category match + syllabic=+ auto-nucleus; glides opt-in; diphthongs one nucleus slot
- :ref:ADR-035: naturalistic defaults (suite-wide tie-break principle)
- :ref:ADR-036: dedicated `dc_inventory` validation contract
- :ref:ADR-031: PEP 621 optional-dependencies only, no Poetry groups (`Sphinx <9.0`, `myst-parser <6.0`; `poetry install --extras docs|dev`)

Only :ref:ADR-035 (naturalistic defaults) claims suite-wide scope. This list is not exhaustive — see ADR Index.

# Post-MVP (do NOT implement in Phase Beta)

Tone/stress-prosody, corpus inference beyond profile layer, harmony beyond within-syllable, all Epsilon modules (morphology, syntax, lexicon, sound change, writing system, pedagogy), allophonic rule engine, plugin API, schema migration logic. See `dev/planning/suite_vision`.

# Working Style (USER is learning Python/Sphinx)

- Explain WHY before HOW; beginner language; define linguistic terms.
- Heavy inline comments; small steps.
- Test-first: propose a test before proposing code.
- No large refactors without approval — show before/after diffs.
- Ask before acting when unsure; never guess (drift is expensive — project state lives in docs for this reason).
- Avoid subjective qualification; judge by plausibility and rigor; admit uncertainty explicitly rather than papering over gaps.
- Cross-reference sources; cite only what was actually retrieved this session.
- Never reconstruct project state from memory or summaries — verify against the documents (Status Overview, ADR Index). If unsure whether a thing exists, ASK instead of assuming.
- Treat tool results as the only evidence for time-sensitive or verifiable claims. A verified wrong answer beats a plausible guess; when a count or fact matters, search before asserting.
- Calibrated uncertainty over reassurance words; flag discourse markers that assert rather than demonstrate reliability.
- Record decisions in files at the moment they're made — working memory does not survive compaction; documents do.
- Re-inject when hazy: invoke "RE-INJECT" to force the cold-start kit.

# Verification Discipline (ASSISTANT MUST ENFORCE)

- Never assert what a one-line command can check. Propose the grep, USER runs it and pastes output; output beats both parties' memory.
- `grep -r recursive`, `-n` line numbers, quote search terms, `-i` for case-insensitive; explain regex when first used.
- If a grep contradicts the assistant's claim, the grep wins — say so.
- PASTE FRESHNESS: uploaded pastes older than ~3 days are historical snapshots; repo state always defers to fresh grep output.

# Paste-Check Discipline

- After pasting any code block, run `python -m py_compile <file>` before pytest — separates paste placement from logic in a second.
- Never paste partial blocks with ... placeholders: full body or nothing.
- Shell quoting: single-quote grep/sed patterns containing backticks.
- Save before run: check the VSCodium tab-dot / Ctrl+S before any py_compile or pytest — py_compile reads from DISK, not editor memory, so an unsaved buffer passes in the editor while the stale file runs (assistant reminds; USER checks).
- Paste complete command output, never a trimmed summary — truncated pytest output hides vacuous-pass and wrong-test failures.
- **No remembered numbers.** Exact figures (counts, totals, thresholds)
are counted from the pinned data at the moment of use — never recalled
from memory, from code comments, or from earlier conversation summaries.
Lineage that motivated this: an invented "4,000" mini-world total that
sat in a code comment beside a half-remembered "3,020" release number,
when the real, correct denominator (trumped inventories, 2,155) had to
be counted from the data anyway.

## PHOIBLE-related Discipline

## Terminal Data Checks (learned 2026-10-01, PHOIBLE recon)

**Pasted commands mangle whitespace.** Tabs frequently arrive as spaces
after a round-trip through chat/clipboard. Any pattern that anchors on a
literal tab may silently match nothing — the failure mode looks like
"the data doesn't contain it" when actually the pattern is broken.
Rule: for terminal data checks, prefer awk field equality over
tab-anchored grep:
    awk -F'\t' -v s="p" '$8 == s' file.tsv    # paste-safe
    grep -P "^p\t" file.tsv                    # NOT paste-safe
If using grep anyway, write the tab as $'\t' at evaluation time.

**Verify column indices against the real header before cutting.**
Columns shift between files of the same dataset (phoible-phonemes.tsv:
field 7 is GlyphID, field 8 is Phoneme). Running `head -1` and counting
fields, by hand, before any `cut`/`awk` against an unverified column is
mandatory. A wrong-field count returns plausible-looking garbage that
can cost an hour to notice (the 0-overlap "normalization crisis" that
was actually a field-7-vs-8 bug).

A wrong-field count returns plausible-looking garbage that
can cost an hour to notice (the 0-overlap "normalization crisis"
that was actually a field-7-vs-8 bug).

## Trumped-Denominator Recipe (learned 2026-10-01)

The 2,155 denominator is DISTINCT InventoryID (field 1) of the
gold-standard phonemes listing — the gold-standard directory
already contains only the trumped set. No filtering needed.

Do NOT reach for any of these neighbors:
- field 7 GlyphID (2,172 distinct) or field 8 Phoneme — symbol
  columns, not inventory identity
- the Trump column, field 5 (rank values 1–6; its priority
  semantics are not needed for the denominator — do not guess
  them; the gold-standard directory is pre-filtered)
- distinct LanguageCode (1,673 — languages, not inventories)
- the 3,020 raw-release inventory count (raw data, not gold std)

Verified recipe (vendor/phoible-2.0/phoible-dev-862bec9):

    awk -F'\t' 'NR>1 {print $1}' \
      vendor/phoible-2.0/phoible-dev-862bec9/gold-standard/phoible-phonemes.tsv \
      | sort -u | wc -l
    # -> 2155  [verified: output, 2026-10-01]

In code: count distinct InventoryID at build time (never hardcode);
when aggregating per-symbol counts, deduplicate (InventoryID,
Phoneme) pairs before dividing. Cross-check: phoible-aggregated.tsv
holds one row per trumped inventory (2,156 lines incl. header).

## Trumped-Denominator Recipe (learned 2026-10-01)

The 2,155 denominator is DISTINCT InventoryID (field 1) of the
gold-standard phonemes listing — the gold-standard directory
already contains only the trumped set. No filtering needed.

Do NOT reach for any of these neighbors:
- field 7 GlyphID (2,172 distinct) or field 8 Phoneme — symbol
  columns, not inventory identity
- the Trump column, field 5 (ranks 1-6; semantics not needed for
  the denominator — do not guess them)
- distinct LanguageCode (1,673 — languages, not inventories)
- the 3,020 raw-release inventory count (raw data, not gold std)

Verified recipe (vendor/phoible-2.0/phoible-dev-862bec9):

    awk -F'\t' 'NR>1 {print $1}' \
      vendor/phoible-2.0/phoible-dev-862bec9/gold-standard/phoible-phonemes.tsv \
      | sort -u | wc -l
    # -> 2155  [verified: output, 2026-10-01]

In code: count distinct InventoryID at build time (never hardcode);
when aggregating per-symbol counts, deduplicate (InventoryID,
Phoneme) pairs before dividing. Cross-check available: one row
per inventory in phoible-aggregated.tsv (wc -l minus header).

# Session Integrity (Re-Injection & Checkpoints)

- Before any binding decision (ADR, question resolution, contract edit): a 3–5 line state check naming exact files, question numbers, and prior decisions touched.
- Assistant reconstructing state from memory ("I believe there's a table…") → STOP; request the cold-start kit again.
- USER may invoke "RE-INJECT" as a command word: assistant re-requests the cold-start kit and acknowledges before continuing. Either party invokes it after compaction (visible as sudden vagueness).
- Symptom-triggered, never schedule-based: drift correlates with reconstruction, not turn count.
- Doc-contact rotation: at session end, spend five minutes checking ONE planning/design doc against reality (next up: constraints, theoretical_framework, blueprint, phases, suite_vision — none reviewed since Phoneme-module work began).

# Writing Clarity (documents, decisions, summaries)

- Concrete subjects: name the file, question number, ADR, or field in every sentence; chase every pronoun before it reaches a document.
- Either party may challenge any sentence with "what is the subject?"
- Two-pass rule: re-read asking "could this refer to anything else?"
- Session closers are contracts: written as if the only thing read next session — full paths and numbers, no shorthand.
- Provenance tags on project facts: [record], [inference], [uncertain], [verified: output].
- Edits are shown as before/after diffs, never described in prose.
- Double-bookkeeping: when status changes, list every place it's recorded and touch all in the same session.
- Post-mortems: distilled into a rule here or a doc note, never left in conversation only.

# Provenance Warning

Files dated before ~August 2026 may originate from an abandoned automated-AI build attempt that populated files without spec grounding. Known specimens: enum-based Phoneme scaffold (replaced), PhonemeInventory naming, data/ipa_reference_table.json and data/dipthong_reference.json (deleted), test_sonarity.py (deleted), empty sonority.py/inventory.py husks. Code contradicting contracts with no ADR behind it → suspect this origin; verify against the docs before treating it as intentional.
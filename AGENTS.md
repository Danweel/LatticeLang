# AGENTS.md — LatticeLang Assistant Bootstrap

Machine-readable bootstrap index and operating rules for AI assistants
in this repository. Written assistants-first, humans-second: short
lines, grep-able headings, explicit paths. Normative content lives in
`docs/source/`; this file points to it and adds session mechanics.
Collaboration process detail lives in
docs/source/dev/governance/collaboration_protocol.rst — this file
keeps summaries and pointers only.

## Cold-Start Kit (ASK for these at session start)
1. This file (AGENTS.md)
2. Status Overview table — top of docs/source/research/questions.rst
3. ADR Index — top of docs/source/dev/governance/decisions.rst
4. documentation_standards.rst
5. collaboration_protocol.rst
6. Session bootstrap: run the epoch check (see collaboration_protocol.rst) before any work

Everything else is retrieved on demand. Past-session memory is never
a source of current state; the repo is. Warn if any of these files are missing.

## Retrieve on Demand (task triggers)
- Documentation edit or pasteable block → docs/source/dev/governance/documentation_standards.rst
- Touching a data contract or its code → that docs/source/data_contracts/dc_*.rst
- Implementing behavior → the governing use case file + its tests
- Committing a user-visible change → CHANGELOG.md (per documentation_standards.rst § Changelog Standards)
- Claiming anything exists in the repo → grep first (Verification Discipline)
- Adding or changing to existing Qs or ADRs → determine if cross referencing applies
- Process/paste/verification rules in doubt → docs/source/dev/governance/collaboration_protocol.rst
- Resuming mid session → docs/operational/session_log.rst (newest entry first; operational, not published)

## Tech Stack
- Python ≥3.11; Poetry (in-project venvs); pytest
- Sphinx + reST (furo, MyST, sphinxcontrib-bibtex, mermaid); Read-the-Docs hosting
- VSCodium on GNU/Linux

## Commands (always preceded by cd to repo root)
```bash
cd /home/danweel/Documents/VSCodiumFiles/LatticeLang/

poetry run pytest                              # full suite
poetry run sphinx-build -b html docs/source docs/_build/html   # docs
```
## Full audit build — incremental builds hide warnings:
```
poetry run sphinx-build -E -b html docs/source docs/_build/html \
  2>&1 | grep -iE 'warning|error|critical' | head -40
```

## Broken-role sweep

A :ref: missing its backticks renders as plain text with NO warning (silent dead reference). Runs with the pre-commit verification:

```
grep -rnE ':ref:[A-Za-z]' docs/source/
grep -rnE ':cite:[a-z]?:[A-Za-z]' docs/source/
```

- RTD auto-builds on push. No build on readthedocs.org → check GitHub webhook deliveries + RTD integrations before anything else.
- `git status` / `git log --stat` whenever unsure; terminal pager exits with "q".
- Assistant always gives full git commands with explanations.
- Epoch line: at cold-start (after the kit), run `git log -1 --oneline && poetry run pytest -q | tail -1` — ground-truth commit + test count, catching drift in the cold-start documents themselves.

# At Commit Time

- Change alters user-visible behavior, output, or data → update CHANGELOG.md in the SAME commit, never retroactively (documentation_standards.rst § Changelog Standards).
- Binding decision made → Status Overview + ADR Index updated in the same commit as the decision; update this file too (AGENTS.md) when a lesson belongs here.
- Verify BEFORE committing, commit LAST: run the full sphinx audit build and pytest; only when both are clean does a commit happen.

# Documentation Map

- `docs/source/index.rst` — entry point
- `docs/source/use_cases/` — Cockburn-style use cases; level subdirectories: user_goal_level/, subfunction_level/, summary_level/,   possible_future_cases/ (verified by ls, 2026-09-30)
- `docs/source/data_contracts/` — JSON schema contracts: dc_phoneme, dc_syllable_template, dc_constraints, dc_inventory, dc_language_definition, dc_orthography_rules, dc_ipa_reference, dc_phoible_source
- `docs/source/research/questions.rst` — questions registry, Status Overview at top; Q-numbers and ADR refs are the lingua franca
- `docs/source/dev/governance/decisions.rst` — ADRs, append-only
- `docs/source/dev/governance/documentation_standards.rst` — format rules for all docs (tables, labels, bib hygiene, edit-location anchors, changelog, data-contract section order, fixture doctrine)
- `docs/source/dev/governance/collaboration_protocol.rst` — verification, paste-check, and fix-response process rules (moved here 2026-10-05)
- `docs/source/dev/planning/` — blueprint, phases, suite vision
- `docs/source/dev/design/` — architecture, theoretical framework, constraints (verified 2026-09-30)
- `docs/source/user/` — user-facing docs and troubleshooting
- `docs/source/glossary.rst` — terminology; referenced via :term:

# Binding Conventions (summaries; canonical text in the docs named)

- Use cases contain BEHAVIOR ONLY; fields and checks live in data contracts. Status fields on every use case (:Doc Status:, :Impl Status:, :Phase:). Long + short labels per use case (.. _uc02:, .. _UC-02_TITLE); references use :ref:`ADR-016`.
- ADRs append-only; supersede, never edit published ones.
- Questions: Status Overview row synced same-commit with any answer; :color: state success = ANSWERED, warning = OPEN.
- Code: Google-style docstrings, type hints, functions <50 lines, zero-dependency core (stdlib JSON/csv), seeded PRNG.
- src/latticelang/ layout: core/, orthography/, ui/, utils/. Module↔use-case filename mapping finalized at implementation start.
- Technical suggestions state floor, connections, consequences, failure modes (documentation_standards.rst § Architecture Explanation); mermaid for diagrams, floor color conventions there.
- In questions.rst and decisions.rst, always update the index at the top as well as the entry.
- Fail loud, never plausible-silent: functions validate inputs and raise on mismatch; a plausible-but-wrong return is a defect even when tests pass around it.

# Key Decisions (summaries; ADR Index is canonical and complete)

Cross-cutting:
- :ref:`ADR-035` — naturalistic defaults (the only SUITE-wide design principle)

Load-bearing for the Phoneme/Q38 phase (derive script, reference table):
- :ref:`ADR-033`: PHOIBLE 2.0 feature system pinned; controlled-vocab strings; Q38 hybrid pipeline — TSV is build-time input only
- :ref:`ADR-036`: dedicated dc_inventory validation contract
- :ref:`ADR-041`: near-miss symbol similarity (tie-bar forms excluded)
- :ref:`ADR-048`: tone not a slot category; tonemes carried with null rank
- :ref:`ADR-051`: merge field-class duplicates (supersedes ADR-040 field merge rules in part)
- :ref:`ADR-052`: segment spelling — PHOIBLE-verbatim storage; tie bar display-layer only (supersedes ADR-028)

This list is a phase view, not the record; see the ADR Index.

# Post-MVP (do NOT implement in Phase Beta, but design in anticipation of)

Tone/stress-prosody, corpus inference beyond profile layer, harmony beyond within-syllable, all Epsilon modules (morphology, syntax, lexicon, sound change, writing system, pedagogy), allophonic rule engine, plugin API, schema migration logic. See dev/planning/suite_vision.

# Working Style (USER is learning Python/Sphinx)

- Explain WHY before HOW; beginner language; define linguistic terms (glossary.rst is the accumulator: new terms become :term: entries).
- Heavy inline comments; small steps.
- Test-first: propose a test before proposing code.
- No large refactors without approval — show before/after diffs.
- Ask before acting when unsure; never guess (drift is expensive — project state lives in docs for this reason).
- Cross-reference sources; cite only what was actually retrieved this session.
- Never reconstruct project state from memory or summaries — verify against the documents (Status Overview, ADR Index). If unsure whether a thing exists, ASK instead of assuming.
- Treat tool results as the only evidence for time-sensitive or verifiable claims. A verified wrong answer beats a plausible guess; when a count or fact matters, search before asserting.
- Record decisions in files at the moment they're made — working memory does not survive compaction; documents do.
- Re-inject when hazy: invoke "RE-INJECT" to force the cold-start kit.

# Process Rules (summaries; full text: collaboration_protocol.rst)

- Verification Discipline: never assert what a one-line command can check;
  USER runs the grep and pastes output; output beats both parties' memory;
  if a grep contradicts the assistant, the grep wins;
  literal patterns need grep -F (backslash-escapes invoke regex anchors);
  combining-mark renderings are not evidence — codepoint dumps adjudicate.
- Paste-Check Discipline: py_compile after paste;
  scan for duplicated defs; never paste partial blocks;
  save-and-sentinel (unsaved buffer edits do not exist;
  grep the disk for a paste token);
  no remembered numbers;
  RST targets get markdown-remnant sentinels (grep -c '^## '; fences via grep -F) — legal-parse garbage never warns;
  JSON edits validated (json.tool);
  no Unicode via clipboard (use chr()/escapes).
- Fix Response Protocol: every fix = diagnosis with evidence, before/after with file path, verification command with expected output, what's next;
  all diagnoses cite exact lines;
  all fixes include sentinels.

# PHOIBLE Terminal Checks (paste-safe data access)

Tabs mangle through clipboards — use awk field equality, never tab-anchored grep:
    `awk -F'\t' -v s="p" '$8 == s' file.tsv`    # paste-safe
    `grep -P "^p\t" file.tsv`                    # NOT paste-safe
Verify column indices against `head -1` by hand before any cut/awk.
Trumped-denominator recipe and counting verification: see
dc_phoible_source.rst Implementation Bindings (the canonical home).
Fixture doctrine: see documentation_standards.rst § Fixture Doctrine.

# Development vs. Runtime Artifacts

The repository contains all data and tools required to regenerate
derived artifacts from first principles (the pinned PHOIBLE 2.0
release), INCLUDING the vendored data — committed to the repo per
the 2026-10-04 bundling decision. Distribution policy:

- Repository/sdist (via ``MANIFEST.in`` graft): everything — vendor/
  data, tests, scripts, docs. Developers and CI can verify derived
  artifacts from source.
- Wheel (end users): runtime library + pre-computed
  ``ipa_reference.json`` only; vendor data excluded.

Boundaries:
- ``vendor/phoible-2.0/`` — vendored raw data; IN the repo and sdist,
  excluded from wheels; read only by derivation scripts
- ``tests/`` and ``scripts/`` — development-only; excluded from wheels
- ``src/latticelang/`` — the library package; distributed as-is
- ``ipa_reference.json`` (committed, regenerated) — runtime data;
  included in distributions

# Session Integrity (Re-Injection & Checkpoints)

- Before any binding decision (ADR, question resolution, contract edit): a 3–5 line state check naming exact files, question numbers, and prior decisions touched.
- Assistant reconstructing state from memory ("I believe there's a table…") → STOP; request the cold-start kit again or specific file.
- USER may invoke "RE-INJECT" as a command word: assistant re-requests the cold-start kit and acknowledges before continuing. Either party invokes it after compaction (visible as sudden vagueness).
- Symptom-triggered, never schedule-based: drift correlates with reconstruction, not turn count.
- Doc-contact rotation: at session end, spend five minutes checking ONE planning/design doc against reality (next up: constraints, theoretical_framework, blueprint, phases, suite_vision — none reviewed since Phoneme-module work began).

# Writing Clarity (documents, decisions, summaries)

- Concrete subjects: name the file, question number, ADR, or field in every sentence; chase every pronoun before it reaches a document.
- Either party may challenge any sentence with "what is the subject?"
- Two-pass rule: re-read asking "could this refer to anything else?"
- Session closers are contracts: written as if the only thing read next session — full paths and numbers, no shorthand.
- Provenance tags on project facts: [record], [inference], [uncertain], [verified: output].
- Edits are shown as before/after diffs, never described as or in prose.
- Double-bookkeeping: when status changes, list every place it's recorded and touch all in the same session.
- Post-mortems: distilled into a rule in a governance doc or this file, NEVER left in conversation only.

# Provenance Warning

Files dated before ~August 2026 may originate from an abandoned automated-AI build attempt (OMP - removed) that populated files without enough spec grounding. Known specimens: enum-based Phoneme scaffold (replaced), PhonemeInventory naming, data/ipa_reference_table.json and data/dipthong_reference.json (deleted), test_sonarity.py (deleted), empty sonority.py/inventory.py husks. Code contradicting contracts with no ADR behind it → suspect this origin if very old; verify against the docs before treating it as intentional. Delete or replace when encountered.

## Phase: derive-script rewrite (Q38) — planned 2026-10-04

Foundation (done): chart-membership binding (curated
data/ipa_chart.json, intersection semantics), classification
derivation scope, overrides minimal scope, glossary.rst,
stale field-check-6 note struck.

Task order (each test-first, one-story commits):
1. Author data/ipa_chart.json — curated chart transcription,
   provenance block, ~100 entries, PHOIBLE-verbatim spellings.
2. Parsing layer — reuse read_tsv/require_header (shared or
   imported from regenerate_mini_fixture.py; do not fork the
   validators). Full-scale two-source join, pair-dedup,
   drop-log for: featureless-attested, off-chart (counts
   computed, never asserted; documented 2,077/83/85 are dated
   comments, not assertions).
3. Category + classification derivation — toneme routing
   (tone '+' branch), consonant/vowel sort, classification
   vocabulary per the Classification derivation scope binding.
   Null, never nearest-fit.
4. Overrides merge + Field Checks — curated-wins merge, then
   the nine Field Checks as acceptance tests (grow
   tests/test_ipa_reference.py into its contracted role).
5. Emission — data/ipa_reference.json, load-time sanity
   check, RTD green.

Deferred (recorded, not scheduled): KNOWN_FEATURE_KEYS comment
cleanup (ledger (d)); reverse-IPA corpus philosophy note
("tens deep, art not science, suggestions with confidence"
— becomes a constraint clause when the UC is specified).

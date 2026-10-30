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
6. Session bootstrap: run the epoch check (see collaboration_protocol.rst) before any work, including branch/PR sweep: `git branch -a` and `gh pr list`

Everything else is retrieved on demand. Past-session memory is never
a source of current state; the repo is. Warn if any of these files are missing.

## Retrieve on Demand (task triggers)

- Documentation edit or pasteable block → docs/source/dev/governance/documentation_standards.rst
- Touching a data contract or its code → that docs/source/data*contracts/dc*\*.rst
- Implementing behavior → the governing use case file + its tests
- Committing a user-visible change → CHANGELOG.md (per documentation_standards.rst § Changelog Standards)
- Claiming anything exists in the repo → grep first (Verification Discipline)
- Adding or changing to existing Qs or ADRs → determine if cross referencing applies
- Process/paste/verification rules in doubt → docs/source/dev/governance/collaboration_protocol.rst
- Resuming mid session → docs/\_operational/session_log.rst (newest entry first; operational, not published)

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
- When a session adopts or rejects a new tool/service, update the AGENTS.md tooling
  inventory in the same session.

# At Commit Time

- Change alters user-visible behavior, output, or data → update CHANGELOG.md in the SAME commit, never retroactively (documentation_standards.rst § Changelog Standards).
- Binding decision made → Status Overview + ADR Index updated in the same commit as the decision; update this file too (AGENTS.md) when a lesson belongs here.
- Verify BEFORE committing, commit LAST: run the full sphinx audit build, pytest, and `poetry run ruff check .`; only when all three are clean does a commit happen. (Lineage: 2026-10-15 — CI's lint gate failed on 30 accumulated ruff errors never caught locally; the local ritual had no ruff step.)

# Documentation Map

- `docs/source/index.rst` — entry point
- `docs/source/use_cases/` — Cockburn-style use cases; level subdirectories: user_goal_level/, subfunction_level/, summary_level/, possible_future_cases/ (verified by ls, 2026-09-30)
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

- Use cases contain BEHAVIOR ONLY; fields and checks live in data contracts. Status fields on every use case (:Doc Status:, :Impl Status:, :Phase:). Long + short labels per use case (.. \_uc02:, .. \_UC-02_TITLE); references use :ref:`ADR-016`.
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
- Fix Response Protocol: every fix = diagnosis with evidence,
  before/after with file path, verification command with expected output, what's next;
  all diagnoses cite exact lines;
  all fixes include sentinels.
  Tool findings imply, they do not conclude. Investigate unknowns of any kind.
- warnings.warn in library code (src/) always sets
  stacklevel=2 so the warning points at the caller's line;
  scripts/**main** leave the default. (Why: default points
  at the library's own interior — useless to the user.)

# PHOIBLE Terminal Checks (paste-safe data access)

Tabs mangle through clipboards — use awk field equality, never tab-anchored grep:
`awk -F'\t' -v s="p" '$8 == s' file.tsv` # paste-safe
`grep -P "^p\t" file.tsv` # NOT paste-safe
Verify column indices against `head -1` by hand before any cut/awk.
Trumped-denominator recipe and counting verification: see
dc_phoible_source.rst Implementation Bindings (the canonical home).
Fixture doctrine: see documentation_standards.rst § Fixture Doctrine.

# Development vs. Runtime Artifacts

The repository contains all data and tools required to regenerate
derived artifacts from first principles (the pinned PHOIBLE 2.0
release), INCLUDING the vendored data — committed to the repo per
the 2026-10-04 bundling decision. Distribution policy:

- Repository/sdist (via `MANIFEST.in` graft): everything — vendor/
  data, tests, scripts, docs. Developers and CI can verify derived
  artifacts from source.
- Wheel (end users): runtime library + pre-computed
  `ipa_reference.json` only; vendor data excluded.

Boundaries:

- `vendor/phoible-2.0/` — vendored raw data; IN the repo and sdist,
  excluded from wheels; read only by derivation scripts
- `tests/` and `scripts/` — development-only; excluded from wheels
- `src/latticelang/` — the library package; distributed as-is
- `ipa_reference.json` (committed, regenerated) — runtime data;
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

Files dated before ~October 2026 might originate from the
removed automated-AI build attempt (OMP) or later unreviewed
LLM batches (e.g. the 2026-09-22 contract stack in PR #1,
closed unmerged 2026-10-28; the "Docs roundup" commit 32449c6
landed on main the same night). Known specimens: enum-based
Phoneme scaffold (replaced), PhonemeInventory naming,
data/ipa_reference_table.json and data/dipthong_reference.json
(deleted), test_sonarity.py (deleted), empty sonority.py /
inventory.py husks. Code contradicting contracts with no ADR
behind it → suspect this origin if old; verify against the
docs before treating it as intentional. Delete or replace
when encountered. Attributed, reviewed-session commits from
2026-10 onward are the reliability boundary.

Clock time is weak attribution in both directions: a solo dev
may work late (2026-10-01 04:45 is not itself proof of machine
work), and rebase-organized commits naturally share identical
timestamps. The reliable signal is corroboration — session
records, protocol checks, and follow-on work depending on the
content. Treat content as unverified when it lacks
corroboration, never merely because of its clock time.

## Tooling Inventory

What LatticeLang uses, and what it deliberately doesn't. Two
purposes: (1) so a newcomer doesn't "fix" a deliberate choice,
(2) so service banners can be triaged without re-investigation.
Update in the same session a tool is adopted or rejected (see
collaboration_protocol.rst, service-banner rule).

### In use

- **Runtime & packaging**: Python ≥3.11 (CI matrix 3.11 + 3.12);
  Poetry with PEP 621 metadata and the poetry-core build backend,
  in-project venvs; `src/` layout; console entry point
  `latticelang = latticelang.cli:main`; license GPL-3.0-or-later.
- **Testing**: pytest 8 (`-v --tb=short`); pytest-cov is available
  but no coverage threshold is enforced.
- **Lint**: ruff (rules E, W, F, I, B; line-length 88; target
  py311; one per-file ignore for `docs/source/conf.py` E501).
  Part of the pre-commit ritual since 2026-10-15.
- **Docs**: Sphinx 8 + MyST 5, furo theme; extensions: autodoc,
  napoleon, viewcode, intersphinx, todo, mermaid (11.13.0),
  notfound, copybutton, design, togglebutton, bibtex
  (`research/refs.bib`). Built with `make docs SPHINXOPTS=-W` —
  warnings are errors in CI.
- **Hosting**: Read the Docs is the CANONICAL public
  documentation. GitHub Pages is an incidental secondary build
  with fewer features — redundancy, not parity.
- **CI/CD**: GitHub Actions — `ci.yml` (matrix test + lint + docs,
  artifact upload) and `deploy-pages.yml`. First-party actions plus
  `snok/install-poetry`. Runs on GitHub's runners; nothing local.
- **Dependency upkeep**: Dependabot for the `github-actions`
  ecosystem, weekly (adopted 2026-10-28).
- **Version control**: git, trunk-based on `main` only; SSH auth;
  `gh` CLI with a keyring-stored token.
- **Editor**: VSCodium; `settings.json` is the editor-config
  source of truth.
- **Data**: vendored PHOIBLE 2.0, pinned and checksummed.

### Deliberately not in use

- **Editor AI / GitHub Copilot**: AI collaboration is external and
  chat-based, with a verification-heavy protocol (see
  collaboration_protocol.rst). A design choice — please don't
  "fix" it.
- **GitHub Apps / marketplace integrations**: no third-party
  services in CI, review, or deployment.
- **GitHub Issues / Projects**: `research/questions.rst` plus the
  ADR registry are the issue system.
- **Long-lived branches**: no `develop`, no feature branches; PRs
  are exceptions, not workflow.
- **Issue/PR templates, CODEOWNERS, release automation, tags**:
  scale-dependent; revisit if outside contributors arrive.
- **`.editorconfig`**: VSCodium `settings.json` instead.
- **Dependabot for Python packages**: dependency review is manual
  via Poetry. Revisit anytime; the actions ecosystem is the
  automated exception.

### Project shape

Solo, hobby-scale, trunk-based development. Radically different
approaches are welcome as forks rather than in-tree changes.

### Banners seen and resolved

Kept so the same notice is never investigated twice.

- `ghs_` token format change (2026-05-15 changelog): GitHub Apps
  only; we consume `GITHUB_TOKEN` via first-party actions — no
  action.
- Node 20 deprecation: resolved 2026-10-28 by the actions major
  bump.
- `ubuntu-latest` → Ubuntu 26 (2026-10-19): migration occurred;
  first green run post-migration confirmed.

## Current Work

Derive-script rewrite (Q38) in progress. Task order and progress marks live in the repo:
docs/source/dev/planning/derive_rewrite_plan.rst. Deferred items and
wake-up conditions live there and in the question registry (questions.rst),
not here.

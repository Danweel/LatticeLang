.. _design-principles:

Design principles — the books, mapped to working checks
=========================================================

Prose principles don't fire; checks consulted at decision
points do. Each entry: principle, source, how LatticeLang
enforces it. Invoke principles BY NAME in ADR/contract
rationales so decisions cite their lineage.
Add here as principles are discovered/implemented.

- **Zero invented values / transcription is curation**
  (data-first doctrine) — enforced by ADR-052 and the
  chart-membership binding: PHOIBLE-verbatim or visibly
  hand-curated, never generated.
- **Deep modules — narrow interface, rich behavior**
  (Ousterhout, *Philosophy of Software Design*) — the derive
  script is a dumb comparator; all variation lives in reviewable
  data files (ipa_chart.json, overrides.json). CHECK for any
  new module: "state its contract in one sentence; if the
  interface needs a paragraph, widen the data, not the code."
- **One master, never copies** (DRY, Pragmatic Programmer) —
  enforced by the similar-blocks rule (collaboration_protocol).
- **Fail loud, never silent-inert** (Pragmatic Programmer) —
  drop-log with counts, -W builds, sentinel greps, epoch checks.
  The session's recurring failure class (inert settings,
  untracked dirs, missing stacklevel) is what this rule hunts.
- **Atomic, one-story commits** (Clean Code, applied to
  history) — the task order's "each test-first, one-story
  commits"; batch-then-organize via staging/rebase is the
  sanctioned workflow.
- **Boy Scout rule — leave it cleaner** (Clean Code) — the
  fix-response protocol: diagnosis, before/after, verification,
  plus drift sweeps like the broken-role grep.
- **Strategic programming — invest in tooling**
  (Ousterhout) — ~10-20% of effort goes to guards and sentinels
  rather than features. (Dependabot, branch sweep, banner triage, etc.)
- **Make the change easy, then make the easy change**
  (Beck, via Fowler's *Refactoring*) — contract-first, then
  implementation; the task order is this principle serialized.
- **Tests define done** (TDD canon) — the pre-commit gauntlet
  and "suggest a test before suggesting code."

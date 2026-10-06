2026-10-06 — non-pulmonic batch 1 (implosives) + Q46 ruling
------------------------------------------------------------
Landed: four attested implosives (U+0253, U+0257, U+0284,
U+0260) in data/ipa_chart.json non_pulmonic_consonants, +1
test (exact-group membership incl. deferral), suite 109.
Voiced uvular implosive U+029B parked in new chart "deferred"
map — PHOIBLE attests only the voiceless variant U+029B
U+0325 (substring probe 2026-10-06; verbatim-storage ADR-052
bars diacritic stripping). Anti-abuse guard active: vendor-
gated tests fail if PHOIBLE gains the row (promotion trigger).
Q46 ANSWERED (questions.rst, entry + Status Overview row):
one Unicode spelling per glyph, PHOIBLE-verbatim; ASCII variant
rows drop via intersection with counting — evidence: 88-row
ASCII romanization family in FEATURES (LC_ALL=C awk probe; [
[:print:]] is Unicode-aware in UTF-8 locales). Clause in
dc_ipa_reference.rst Implementation Bindings ("Spelling
variants" subsection); deferred route documented in Chart
membership filter. Glossary: romanization term. CHANGELOG:
[Unreleased] batch incl. Oct 5 backfill (NFC corrections,
vendoring/PROVENANCE) + Dependencies section. Doc standards
grew: question-entry format, glossary format, changelog
triggers/granularity/backfill. Process lessons banked
(collaboration_protocol.rst): sentinel flags (-F; uniqueness),
glossary-indent sentinels, wrap-immune phrase checks
(tr '\n' ' '), closing files before sentinel runs.
Park note: poetry run discipline (bare pytest ran system
Python — 6 import errors, 31 collected vs 108).

NEXT: non-pulmonic batch 2 — clicks (Q46 settles spelling;
watch U+01C0-U+01C3 vs ASCII lookalikes), then vowel
quadrilateral, completeness-floor test. Then task 2:
derive-script rewrite (NFC join at input seam, pair-dedup,
drop-log). Doc-contact rotation due (constraints,
theoretical_framework, blueprint, phases, suite_vision).
Deferred: F-4 (ejectives), F-5 prep (source-database trace —
N kin of the 88 family; upstream heads-up idea), F-6 (aspirate
alias), audit_featureless ASCII-family annex.

2026-10-05 — derive phase, task 1 (chart pass-list)
---------------------------------------------------
Landed: data/ipa_chart.json (pulmonic + affricates groups,
vendored decomposed spellings per ADR-052), 6 tests, suite 108.
Discovered and corrected the PHOIBLE encoding seam (F-5):
NFC join required — featureless 83->62, features-only
unattested 85->66, emitted shared 2,077->2,098
(dc_ipa_reference dated Correction; probe evidence in
research/q36_featureless_audit.rst, regenerable via
scripts/audit_featureless.py). The 62 decompose mostly into
voiced-aspirate spelling variants (F-6 alias question);
legacy-artifact row (ASCII N, 10 attestations) provenance
open — N/A-parser split hypothesized, unverified; fold the
source-database trace into F-5 prep. New follow-ups F-4
(ejectives deferred), F-6 (aspirate alias). Empty placeholder
data/ipa_reference.json REMOVED — it is the task-2 derive
OUTPUT, distinct from the curated chart INPUT; the rewrite
emits it fresh. docs/Operational/ instituted for tracked-but-
unpublished operator docs (session log lives here; scratch
scripts relocated from root — dangling-reference check done).
Vendor zip stays gitignored; vendor pinned by PROVENANCE.txt
hash. Stray docs/source/_build removed (only docs/_build is
canonical; always the recorded build command). Process rules
banked: json.tool gate, no clipboard Unicode, codepoint-dump
evidence, completion prints, save-and-sentinel.

NEXT: COMMIT the task-1 batch (message drafted in chat;
stage by name, receipt via git log -1 --stat). Then:
non-pulmonic batch (clicks, implosives), vowel quadrilateral,
completeness-floor test. Then task 2: derive-script rewrite —
NFC join mandatory at input seam.
Deferred (small, standalone): setup_contrib.sh content review
(likely stubs; undocumented); .gitignore template tidy
(irrelevant framework blocks). Committed as two stories:
program work (task 1) then repo housekeeping.

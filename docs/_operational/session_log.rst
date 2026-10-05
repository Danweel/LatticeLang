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

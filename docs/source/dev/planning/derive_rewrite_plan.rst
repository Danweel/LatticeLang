.. _derive-rewrite-plan:

Derive-script rewrite — task order (Q38)
=========================================

:Recorded: 2026-10-04; moved from AGENTS.md 2026-10-29 (bootstrap
   files carry how-to-work, not what's-next). Progress marks
   update as tasks land.

Foundation (done): chart-membership binding (curated
``data/ipa_chart.json``, intersection semantics), classification
derivation scope, overrides minimal scope, glossary.rst,
stale field-check-6 note struck.

Task order (each test-first, one-story commits):

1. [DONE — landed before the non-pulmonic batches] Author
   ``data/ipa_chart.json`` — curated chart transcription,
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
   ``tests/test_ipa_reference.py`` into its contracted role).
5. Emission — ``data/ipa_reference.json``, load-time sanity
   check, RTD green. Governed by the Q48 accompanied-cluster
   admission ruling: chart cells only, categorical drop-log.

Deferred (recorded, not scheduled): KNOWN_FEATURE_KEYS comment
cleanup; reverse-IPA corpus philosophy note ("tens deep, art
not science, suggestions with confidence" — becomes a
constraint clause when the UC is specified).

Click-cluster curation — gated by UC-01 cluster-extension
amendment; see Q48.

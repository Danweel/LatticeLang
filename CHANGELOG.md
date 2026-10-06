# Changelog

All notable changes to LatticeLang will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Add the curated IPA chart pass-list (`data/ipa_chart.json`):
  pulmonic consonants and affricates in vendored PHOIBLE-verbatim
  spellings (ADR-052), with a provenance block and vendor-gated
  curation tests. IPA-reference chart membership is intersection
  with this list — never heuristics.
- Add the four attested non-pulmonic implosives (U+0253, U+0257,
  U+0284, U+0260) to the chart pass-list, with an exact-group
  membership test.

### Changed
- Institute the `deferred` map in `data/ipa_chart.json` for
  chart-canonical symbols lacking a PHOIBLE features row; park
  the voiced uvular implosive (U+029B) — only the voiceless
  variant (U+029B U+0325) is attested. Vendor-gated tests flag
  promotion if PHOIBLE gains a row.
- Correct the derive-pipeline join figures after fixing the NFC
  normalization seam: shared emitted symbols 2,077 → 2,098;
  attested-but-featureless 83 → 62; features-only unattested
  85 → 66. The join normalizes both sides to NFC for matching;
  emitted spellings stay PHOIBLE-verbatim (ADR-052).
- Record the ASCII/homoglyph spelling-variant ruling (Q46) in
  the dc_ipa_reference Implementation Bindings: one Unicode
  spelling per glyph, ASCII variant rows drop via intersection
  with drop-log counting, typed-lookalike input tolerance
  delegated to the near-miss layer (ADR-041).

### Dependencies
- Vendor the pinned PHOIBLE 2.0 release into the repository
  (dev-862bec9, hash pinned in PROVENANCE.txt; bundling
  decision 2026-10-04): repository and sdist carry all data,
  tests, scripts, and docs; the wheel distributes the runtime
  library plus the precomputed ipa_reference.json only.

### Tests
- 109 passing

### Removed
- Remove the empty placeholder `data/ipa_reference.json`: it is
  the derive script's OUTPUT, emitted fresh; the curated chart
  file is the INPUT.

## [0.3.0] — 2026-09-30

### Added
- Add Q38 IPA Reference derive pipeline (`scripts/derive_ipa_reference.py`)
  - Build in five steps: parse → filter → derive → merge → validate → emit
  - Share sonority rank derivation with runtime prefill (one derivation, two consumers)
  - Cover with 14 tests in `tests/test_derive_ipa_reference.py`
- Add mini-scale fixtures: `tests/fixtures/phoible_mini.tsv` (6 rows, 13 columns,
  PHOIBLE-style TSV) and `tests/fixtures/overrides_mini.json` (curated overlay sample)
- Add DC-PHOIBLE-01 data contract (`docs/source/data_contracts/dc_phoible_source.rst`)
- Emit `pinned_sources` block in `data/ipa_reference.json` output schema
- Implement Field Check 4 (alias/symbol collision detection)

### Changed
- Harden `tests/test_derive_ipa_reference.py`: replace vacuous alias test with
  real assertion; pin pipeline boundaries with negative assertions (step-1 shape
  ≠ step-3 shape)

### Fixed
- Fix column alignment in PHOIBLE-style TSV (inventory_count / features / vowel
  columns previously slid by one slot)
- Fix placeholder ellipsis in `derive_category` (previously returned `None` for
  all categories)

### Removed
- Remove legacy AI debris: `PhonemeCategory(Enum)`, `PhonemeInventory` naming,
  orphaned test files
- Remove stale comments referencing "script doesn't exist yet"
- Remove unused `tempfile` import

### Dependencies
- Pin PHOIBLE 2.0 via Zenodo DOI (`10.5281/zenodo.2626687`, 2019)
- Adopt annual-review upgrade cadence (January each year, per DC-PHOIBLE-01)

### Tests
- Grow suite to 71 passing:
  - `test_derive_ipa_reference`: 14
  - `test_ipa_reference`: 10
  - `test_phonome_contract`: 15
  - `test_phoneme_derivation`: 18
  - `test_inventory`: 14

(Changelog/dc_phoible_source.rst changes landed across both 272cbf6 and 13e49f6. The other items committed are better-dogfooded.)

---

## [0.2.0] — September 2026

### Added
- UC-01 data layer (Phoneme, Inventory, Merge per ADR-014, ADR-033, ADR-051)
- `core/phonology.py`: Phoneme dataclass, Inventory validation view
- `core/sonority.py`: `propose_sonority_rank`, band-floor ranks
- Category divergence warnings (load-time only)
- 57 tests passing (prior to IPA reference work)

### Documentation
- `docs/source/data_contracts/dc_phoneme.rst`
- `docs/source/data_contracts/dc_inventory.rst`
- Implementation Bindings recorded for module homes and merge semantics

---

## [0.1.0] — April-August 2026

### Initial Release
- Project scaffolding
- Poetry configuration
- Sphinx/RTD setup
- Basic test infrastructure

[Unreleased]: https://github.com/Danweel/LatticeLang/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/Danweel/LatticeLang/releases/tag/v0.3.0
[0.2.0]: https://github.com/Danweel/LatticeLang/releases/tag/v0.2.0
[0.1.0]: https://github.com/Danweel/LatticeLang/releases/tag/v0.1.0

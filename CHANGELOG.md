# Changelog

All notable changes to LatticeLang will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### To Be Added
- Real PHOIBLE 2.0 TSV vendoring (mini-scale fixture currently in place)
- Rarity-tier finalization per Q36 (thresholds currently assumed)
- ADR-028 normalization pass for special combinations (naive `_split_constituents` currently in use)

---

## [0.3.0] — 2026-09-30

### Added
- Add Q38 IPA Reference derive pipeline (`scripts/derive_ipa_reference.py`)
  - Five-step build: parse → filter → derive → merge → validate → emit
  - 14 tests in `tests/test_derive_ipa_reference.py`
  - Shared sonority rank derivation with runtime prefill
- Add Mini-scale fixtures:
  - `tests/fixtures/phoible_mini.tsv` (6 rows, 13 columns, PHOIBLE-style TSV)
  - `tests/fixtures/overrides_mini.json` (curated overlay sample)
- Data contract for source pinning (`docs/source/data_contracts/dc_phoible_source.rst`)
- Output schema with `pinned_sources` in `data/ipa_reference.json`

### Changed
- `tests/test_derive_ipa_reference.py` hardened:
  - Vacuous alias test replaced with real assertion
  - Negative assertions added to pin pipeline boundaries (step-1 ≠ step-3 shape)
- Field Check 4 implementation (alias/symbol collision detection)

### Fixed
- Column alignment in PHOIBLE-style TSV (inventory_count / features / vowel columns)
- Placeholder ellipsis removal in `derive_category` (previously returning `None` for all categories)

### Removed
- Legacy AI debris: `PhonemeCategory(Enum)`, `PhonemeInventory` naming, orphaned test files
- Stale comments referencing "script doesn't exist yet"
- Unused `tempfile` import

### Dependencies
- PHOIBLE 2.0 pinned via Zenodo DOI (`10.5281/zenodo.2626687`, 2019)
- Annual-review upgrade cadence established (January each year, per DC-PHOIBLE-01)

### Tests
- Total: 71 passing
  - `test_derive_ipa_reference`: 14
  - `test_ipa_reference`: 10
  - `test_phoneme_contract`: 15
  - `test_phoneme_derivation`: 18
  - `test_inventory`: 14

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
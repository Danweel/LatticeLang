.. _dc_phoible_source:

Data Contract: PHOIBLE Source Pinning (DC-PHOIBLE-01)
=====================================================

Date established: 2026-09-30
Related components: scripts/derive_ipa_reference.py, data/ipa_reference.json

Purpose
-------

LatticeLang consumes PHOIBLE 2.0 as a *static derivation oracle* — one source,
two consumers (runtime ``Phoneme`` prefill via :func:`latticelang.core.sonority.propose_sonority_rank`
and build-time IPA reference generation). Deterministic outputs take priority
over freshness to ensure conlangers relying on LatticeLang receive repeatable
category/rank results across installations and CI runs.

Canonical Source
----------------

**PHOIBLE 2.0** (Zenodo archival snapshot)

- DOI: ``10.5281/zenodo.2626687``
- Publication: Moran, Steven & McCloy, Daniel (eds.) 2019. *PHOIBLE 2.0*.
  Jena: Max Planck Institute for the Science of Human History.
- Availability: Zenodo (archival) + phoible.org (browse/live)

Gold-Standard Trumping Semantics (added 2026-10-01)
---------------------------------------------------

PHOIBLE 2.0 resolves overlapping source inventories (multiple
databases describing the same language) through *trumping*: each
language contributes one winning "trumped" inventory, and the
vendored ``gold-standard/`` directory contains only those winners.

- The trumped denominator — distinct ``InventoryID`` (field 1)
  of ``gold-standard/phoible-phonemes.tsv`` — is **2,155**
  (counted 2026-10-01; cross-checked against the row count of
  ``phoible-aggregated.tsv``, which lists one row per trumped
  inventory). The derive script counts it at build time; it is
  never hardcoded.
- The ``Trump`` column (field 5) carries rank values 1–6; its
  exact priority semantics are not established here and are not
  needed for the denominator (the gold-standard directory is
  pre-filtered). Do not filter on it.
- The raw-data directories retain the unfiltered universe
  (~3,020 inventories per the 2.0 release notes); frequency
  derivations that consume raw-data files would compute a
  different denominator and are not supported.

Per-symbol frequency is computed over the trumped denominator
with ``(InventoryID, Phoneme)`` pairs deduplicated before
division, so repeated rows within one inventory cannot inflate
a symbol's count.

Implementation Bindings
-----------------------

The derived output file ``data/ipa_reference.json`` must include:

.. code-block:: json

    {
      "schema_version": "1.0",
      "pinned_sources": {
        "phoible_release": "2.0",
        "ipa_chart_year": "2015"
      }
    }

The ``parse_phoible_tsv`` function in the derive pipeline validates that the vendored
TSV matches the expected column set from the canonical release. Mismatched
headers cause immediate build failure.

Terminal Data Checks (learned 2026-10-01, PHOIBLE recon)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pasted commands mangle whitespace. Tabs frequently arrive as spaces
after a round-trip through chat/clipboard. Any pattern that anchors
on a literal tab may silently match nothing — the failure mode
looks like "the data doesn't contain it" when actually the pattern
is broken. Rule: for terminal data checks, prefer awk field
equality over tab-anchored grep:

.. code-block:: bash

    awk -F'\t' -v s="p" '$8 == s' file.tsv    # paste-safe
    grep -P "^p\t" file.tsv                    # NOT paste-safe

If using grep anyway, write the tab as ``$'\t'`` at evaluation time.

Verify column indices against the real header before cutting.
Columns shift between files of the same dataset (phoible-phonemes.tsv:
field 7 is GlyphID, field 8 is Phoneme). Running ``head -1`` and
counting fields, by hand, before any ``cut``/``awk`` against an
unverified column is mandatory. A wrong-field count returns
plausible-looking garbage that can cost an hour to notice (the
0-overlap "normalization crisis" that was actually a
field-7-vs-8 bug).

Trumped-Denominator Recipe (learned 2026-10-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 2,155 denominator is DISTINCT InventoryID (field 1) of the
gold-standard phonemes listing — the gold-standard directory
already contains only the trumped set. No filtering needed.

Do NOT reach for any of these neighbors:

- field 7 GlyphID (2,172 distinct) or field 8 Phoneme — symbol
  columns, not inventory identity
- the "Trump" column, field 5 (rank values 1–6; its priority
  semantics are not needed for the denominator — do not guess
  them; the gold-standard directory is pre-filtered)
- distinct LanguageCode (1,673 — languages, not inventories)
- the 3,020 raw-release inventory count (it is raw data, not the Gold Standard file)

Verified recipe (vendor/phoible-2.0/phoible-dev-862bec9)::

    awk -F'\t' 'NR>1 {print $1}' \
      vendor/phoible-2.0/phoible-dev-862bec9/gold-standard/phoible-phonemes.tsv \
      | sort -u | wc -l
    # -> 2155  [verified: output, 2026-10-01]

In code: count distinct InventoryID at build time (never hardcode);
when aggregating per-symbol counts, deduplicate (InventoryID,
Phoneme) pairs before dividing. Cross-check available: phoible-aggregated.tsv
holds one row per trumped inventory (2,156 lines incl. header).

Upgrade Cadence
---------------

**Annual review** — January of each year. (Probably unnecessary, but ideally.)

An upgrade requires:

1. Download the new PHOIBLE release (Zenodo or GitHub tag)
2. Compare inventory totals (row count, segment count, language count)
3. Run ``scripts/derive_ipa_reference.py`` with the new TSV
4. Execute full test suite (expect 71+ tests passing)
5. Document deltas in ``CHANGELOG.md`` under the relevant release
6. Update ``pinned_sources.phoible_release`` in the emitted JSON
7. Commit with semantic version bump (minor version increment)

Rationale
---------

The PHOIBLE project follows a "live website + stable Zenodo snapshot" model.
Between 2019–2026, the maintainers have issued bugfixes and additions via GitHub
but have not minted a new numbered release (no 2.0.1 exists as an official
archive; see CLLD technical discussion on dataset semantic versioning).

For LatticeLang, stability outweighs recency: a phonologist deriving categories
in 2026 should receive the same output as one running LatticeLang in 2027,
provided both vendor from the same PHOIBLE snapshot.

References
----------

- PHOIBLE 2.0 Zenodo record: https://zenodo.org/record/2626687
- PHOIBLE Online: https://phoible.org
- CLDF Data Format Specification: https://cldf.clld.org
- Cross-linguistic Linked Data Project: https://clld.org

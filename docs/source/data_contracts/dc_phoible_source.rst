.. _dc-phoible-source:

===========================================
Data Contract: PHOIBLE Source Pinning (DC-PHOIBLE-01)
===========================================

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

Implementation Bindings
-----------------------

The derived output file ``data/ipa_reference.json`` must include:

.. code-block:: json

    {
      "schema_version": "1.0",
      "pinned_sources": {
        "phoible_release": "2.0",
        "ipa_chart_year": "2015"
      },
      ...
    }

The ``build_step_1`` function in the derive pipeline validates that the vendored
TSV matches the expected column set from the canonical release. Mismatched
headers cause immediate build failure.

Upgrade Cadence
---------------

**Annual review** — January of each year. (Probably unnecessary, but ideally.)

An upgrade requires:

1. Download the new PHOIBLE release (Zenodo or GitHub tag)
2. Compare inventory totals (row count, segment count, language count)
3. Run ``scripts/derive_ipa_reference.py`` with the new TSV
4. Execute full test suite (expect 71+ tests passing)
5. Document deltas in ``CHANGES.md`` under the relevant release
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
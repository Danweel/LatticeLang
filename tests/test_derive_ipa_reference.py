"""Tests for the Q38 derive script (test-first, dc_ipa_reference.rst).

Written RED against the contract's Build Pipeline section — the
derive script is a build-time pipeline that regenerates
data/ipa_reference.json from a PHOIBLE-format TSV plus curated
overrides (Q38 hybrid: derived base, hand-curated overlay).

Targets the Field Checks from dc_ipa_reference.rst plus the
intermediate pipeline steps for granular failure messages.

Sources of truth:
- Field Checks 1-9: dc_ipa_reference.rst (Field Checks section)
- Build Pipeline:   dc_ipa_reference.rst (five-step sequence)
- Rank proposal:    latticelang.core.sonority.propose_sonority_rank
  (shared runtime/build-time derivation — one home, two callers)

Fixtures: tests/fixtures/phoible_mini.tsv (6 hand-made rows,
assumed PHOIBLE shape: one column per feature — assumption
flagged in scripts/derive_ipa_reference.py's docstring) and
tests/fixtures/overrides_mini.json (curated overlay sample).
"""

from pathlib import Path

from scripts.derive_ipa_reference import (
    parse_phoible_tsv,
    filter_to_ipa_chart,
    derive_rank_and_frequency,
    merge_overrides,
    run_field_checks,
    generate_ipa_reference_json,
)

FIXTURE = Path(__file__).parent / "fixtures" / "phoible_mini.tsv"
OVERRIDES = Path(__file__).parent / "fixtures" / "overrides_mini.json"

# --- Step 1: parse_phoible_tsv ---------------------------------------

def test_parse_returns_list_of_dicts():
    """Each TSV row becomes one dict; 6 rows in the fixture."""
    parsed = parse_phoible_tsv(FIXTURE)
    assert isinstance(parsed, list)
    assert len(parsed) == 6

def test_parsed_row_has_required_keys():
    """Step 1 emits RAW rows: flat columns, raw inventory_count.
    The features sub-dict and computed phoible_frequency are
    born in step 3 (derive_rank_and_frequency) — pipeline
    boundary ruled 2026-09-30; don't test step-3 shape here."""
    parsed = parse_phoible_tsv(FIXTURE)
    for row in parsed:
        for column in ("symbol", "syllabic", "consonantal",
                       "inventory_count"):
            assert column in row
        # Raw stage invariant: no enrichment has leaked in early.
        assert "features" not in row
        assert "phoible_frequency" not in row

# --- Step 2: filter_to_ipa_chart --------------------------------------

def test_filter_removes_non_chart_segments():
    """The filter keeps IPA-chart segments; the fixture is small
    enough that all 6 chart-plausible rows pass through."""
    filtered = filter_to_ipa_chart(parse_phoible_tsv(FIXTURE))
    assert len(filtered) == 6

# --- Step 3: derive_rank_and_frequency ----------------------------

def test_derived_entry_has_sonority_rank_or_null():
    """Field Check 2: rank value or explicit null — never absent."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    for entry in enriched:
        assert "sonority_rank" in entry
        assert (entry["sonority_rank"] is None
                or isinstance(entry["sonority_rank"], int))

def test_rank_matches_proposer_for_known_features():
    """Shared derivation: build-time rank equals
    propose_sonority_rank on the same features."""
    from latticelang.core.sonority import propose_sonority_rank
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    for entry in enriched:
        proposed = propose_sonority_rank(entry["features"])
        assert entry["sonority_rank"] == proposed

def test_phoible_frequency_in_0_to_1():
    """Field Check 9 half: frequency is a decimal 0-1."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    for entry in enriched:
        freq = entry["phoible_frequency"]
        assert 0 <= freq <= 1

# --- Step 4: merge_overrides ----------------------------------------

def test_override_wins_on_conflict():
    """Build step 4: curated overrides beat derived values."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    merged = merge_overrides(enriched, OVERRIDES)
    by_symbol = {e["symbol"]: e for e in merged}
    # overrides_mini.json supplies p's description — the
    # curated text must be present after the merge.
    assert by_symbol["p"]["description"] == "Voiceless bilabial plosive"

def test_override_absent_leaves_derived_value():
    """Entries with no override keep their derived fields."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    merged = merge_overrides(enriched, OVERRIDES)
    by_symbol = {e["symbol"]: e for e in merged}
    # 't' has no override entry; it must survive untouched.
    assert "t" in by_symbol
    assert by_symbol["t"]["phoible_frequency"] == 3700 / 4000

# --- Step 5: field checks + emission ------------------------------

def test_all_symbols_unique_across_table():
    """Field Check 1: no duplicate symbols anywhere."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    symbols = [e["symbol"] for e in enriched]
    assert len(symbols) == len(set(symbols))

def test_unicode_points_concatenate_to_symbol():
    """Field Check 3: codepoints concatenate to the symbol."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    for entry in enriched:
        concat = "".join(chr(int(p.replace("U+", ""), 16))
                         for p in entry["unicode_points"])
        assert concat == entry["symbol"]

def test_aliases_resolve_to_symbol():
    """Field Check 4 territory: aliases arrive via overrides and
    survive the merge attached to their entry (guards against a
    vacuous pass — the fixture now carries a real alias)."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    merged = merge_overrides(enriched, OVERRIDES)
    by_symbol = {e["symbol"]: e for e in merged}
    assert by_symbol["k͡p"]["aliases"] == ["kp"]
    for entry in merged:
        for alias in entry.get("aliases") or []:
            assert isinstance(alias, str) and alias

def test_run_field_checks_raises_on_violation():
    """Build step 5: field-check violations abort the build."""
    table = generate_ipa_reference_json(
        merge_overrides(
            derive_rank_and_frequency(parse_phoible_tsv(FIXTURE)),
            OVERRIDES))
    # Valid fixture must pass cleanly (no raise)...
    run_field_checks(table)
    # ...and a corrupted table must raise (duplicate symbol).
    table["consonants"].append(dict(table["consonants"][0]))
    try:
        run_field_checks(table)
        raised = False
    except Exception:
        raised = True
    assert raised, "duplicate symbol must fail the build"

def test_generate_json_contains_top_level_fields():
    """schema_version, pinned_sources, attribution, consonants,
    vowels, special_combinations."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    merged = merge_overrides(enriched, OVERRIDES)
    json_obj = generate_ipa_reference_json(merged)
    for key in ("schema_version", "pinned_sources", "attribution",
                "consonants", "vowels", "special_combinations"):
        assert key in json_obj

def test_generate_json_preserves_entry_count():
    """Round-trip: no rows lost or invented on the way out."""
    enriched = derive_rank_and_frequency(parse_phoible_tsv(FIXTURE))
    merged = merge_overrides(enriched, OVERRIDES)
    json_obj = generate_ipa_reference_json(merged)
    total = (len(json_obj["consonants"]) + len(json_obj["vowels"])
             + len(json_obj["special_combinations"]))
    assert total == len(merged)
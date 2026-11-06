.. _testing_standards:

Testing Standards
=================

:date: 2026-10-31
:type: Static (Append-only without an ADR)
:audience: Test authors, reviewers, AI assistants
:purpose: Test taxonomy, authority hierarchy, and authorship order

This file documents the **methodology** for writing and
evaluating tests in LatticeLang. It complements
:ref:`documentation_standards` (prose and formatting) and
:ref:`collaboration_protocol` (process rules). The binding
rulings live in :ref:`ADR-054`; this file carries the detail.

Test Taxonomy
-------------

.. csv-table::
   :header-rows: 1
   :widths: 18 42 40

   "Type","Trigger","Examples in the suite"
   "interface-first","Contract or interface documented before implementation exists","test_derive_ipa_reference.py, test_inventory.py, test_phoneme_contract.py"
   "data-batch","Curated artifact whose roster is verified from a spec","test_ipa_chart.py: test_implosives_group_exact, test_clicks_all_deferred"
   "audit","Post-implementation bug hunt against real data","test_sonority_real_features.py"
   "vendor-gated","Authority check against pinned source data","test_regenerate_mini_fixture.py: test_full_trumped_denominator_is_2155"

Interface-First Tests
~~~~~~~~~~~~~~~~~~~~~

Written RED, before any implementation, against a documented
interface. The interface is the specification; the test
enforces the contract rather than the current behavior.

Data-Batch Tests
~~~~~~~~~~~~~~~~

For a curated artifact whose roster is known and verified:

#. Verify the roster against its spec (contract, chart artifact).
#. Write the exact-match test using ``\uXXXX`` escapes with
   codepoint comments.
#. Run it — it fails, because the data is not yet populated.
#. Populate the artifact until the test passes.
#. Commit test and data together, as one story.

When the roster is itself under verification (parenthesized
cells, unresolved deferrals), the test waits until the roster
is verified — not until the data is populated. That is the
declared exception in :ref:`ADR-054`; the commit message names
it and the test cites its source.

Audit Tests
~~~~~~~~~~~

Written after code exists, to hunt defects against real data.
Expectations cite the ruling (ADR or Q-number), never the
current behavior — otherwise the test ratifies the bug.

Vendor-Gated Tests
~~~~~~~~~~~~~~~~~~

Verify constants against pinned source data when it is
present. Skip visibly when it is absent:

.. code-block:: python

   requires_vendor = pytest.mark.skipif(
       not VENDORED,
       reason="vendored PHOIBLE data absent",
   )

A skip is always visible and named. A vendor-gated test never
fails silently and never disappears.

Fixture Authority
-----------------

.. csv-table::
   :header-rows: 1
   :widths: 30 40 30

   "Layer","Role","Authority"
   "Vendor-gated tests","Assertions against pinned real data","Ultimate"
   "Committed fixtures","Portable exports, regenerable","Delegated to the regeneration script"
   "In-memory mocks","Isolation for a single test","None (isolation only)"

Rules:

- Never hand-author fixture values; fixtures are exports.
- Never assert a fixture count; compute it from real rows.
- A pinned golden number carries a provenance comment and a
  "data changed" failure message. A tripped pin means re-run
  the PROVENANCE checks, never edit the number.
- Fresh-clone principle: ``git clone && poetry install
  --extras docs --with dev && poetry run pytest`` is green on
  any machine, with vendor-gated skips visible.

Symbol-Escape Discipline
------------------------

IPA symbols in JSON and test files are written as ``\uXXXX``
escapes with a codepoint comment naming each symbol. Glyphs
are never pasted through chat — the clipboard mangles
codepoints and invites homoglyph substitution
(:ref:`Q46`, :ref:`ADR-052`).

.. code-block:: python

   IMPLOSIVES = ["\u0253", "\u0257", "\u0284", "\u0260"]
   # ɓ U+0253, ɗ U+0257, ʄ U+0284, ɠ U+0260

Group-Based Testing
-------------------

Chart groups mirror the chart's own sections, one test
function per group, with the group's members held as an
uppercase constant:

.. code-block:: python

   def test_implosives_group_exact():
       """Non-pulmonic batch 1: the four PHOIBLE-attested
       implosives, exactly, plus the fifth chart symbol parked
       in deferred. List equality pins membership and order."""
       chart = load_chart()
       assert chart["non_pulmonic_consonants"] == IMPLOSIVES
       assert "\u029B" in chart["deferred"]

**Absence must be declared.** A group may be empty only if
named in the pending-groups constant; a deferred symbol gets
its own assertion line rather than vanishing from the list:

.. code-block:: python

   PENDING_GROUPS = {"vowels", "other_symbols"}  # shrink as batches land

   def test_no_group_silently_empty():
       chart = load_chart()
       empty = {g for g in EXPECTED_GROUPS if not chart.get(g)}
       assert empty <= PENDING_GROUPS, (
           f"undeclared empty groups: {empty - PENDING_GROUPS}")

Naming
------

.. csv-table::
   :header-rows: 1
   :widths: 35 65

   "Element","Convention"
   "Test function","test_<group>_<property>"
   "Group constant","UPPERCASE, with \u escape comments"
   "One test per group","A group's membership is pinned by one function"
   "Skip marker","requires_vendor, with a named reason"

Accessors and Assertion Targets
-------------------------------

Chart access lives in the test module itself — there is no
production ``ipa_chart`` module:

.. code-block:: python

   ROOT = Path(__file__).resolve().parents[1]
   CHART_FILE = ROOT / "data" / "ipa_chart.json"

   def load_chart() -> dict:
       with open(CHART_FILE, encoding="utf-8") as f:
           return json.load(f)

   def chart_symbols(chart: dict) -> list[str]:
       return [s for g in EXPECTED_GROUPS for s in chart.get(g, [])]

PHOIBLE columns are read **by position**, never by a
remembered name; verify against ``head -1`` before any
``cut`` or ``awk``:

.. code-block:: python

   def vendor_feature_symbols() -> set[str]:
       with open(VENDOR_FEATURES, encoding="utf-8", newline="") as f:
           reader = csv.DictReader(f, delimiter="\t")
           symbol_col = reader.fieldnames[0]
           return {row[symbol_col] for row in reader}

Commit-Time Verification
------------------------

.. csv-table::
   :header-rows: 1
   :widths: 25 60 15

   "Step","Command","Gate"
   "Tests","poetry run pytest -q","All pass"
   "Lint","poetry run ruff check .","Clean"
   "Docs","poetry run sphinx-build -E -b html docs/source docs/_build/html 2>&1 | grep -iE 'warning|error' | head -40","No output"
   "Changelog","CHANGELOG.md entry when output is user-visible","Same commit"

All three gates pass before a commit happens. A declared
exception is cited in the commit message.

See Also
--------

- :ref:`ADR-054` — the binding rulings this file details
- :ref:`collaboration_protocol` — verification and paste-check discipline
- :ref:`documentation_standards` — prose and formatting standards
- :ref:`fixture-doctrine` — fixture doctrine (in documentation_standards.rst)
- :ref:`ADR-052` — segment spelling, vendored-canonical
- :ref:`Q46` — ASCII and homoglyph spelling variants

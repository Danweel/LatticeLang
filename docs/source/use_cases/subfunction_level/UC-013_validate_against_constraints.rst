.. _UC-013_validate_against_constraints:
.. _uc013:

UC-013: Validate Against Constraints
====================================

:Doc Status: Draft
:Goal Level: Subfunction
:Impl Status: Not Started
:Phase: Beta

Goal
----
Evaluate a segment sequence (a candidate syllable, or a completed
word) against the project's active constraints and return a
``ValidationReport``: an overall verdict plus one four-value result
per constraint (PASSED / FAILED / SKIPPED / ERROR), each FAILED result
carrying a human-readable reason string. Pure evaluation — no
regeneration, no side effects, no knowledge of the caller. Retry
policy lives with callers (:ref:`uc014`, :ref:`uc04`); this case
only judges.

Preconditions
-------------
- The candidate sequence exists in memory (:class:`~latticelang.core.syllable.Syllable` or word assembly)
- The constraint list is loaded; every constraint is an enabled instance of a catalog type (:ref:`adr-037`)

Inputs
------
- ``sequence``: the segment sequence to evaluate
- ``constraints``: the active constraint list
- ``word_context`` (optional): surrounding context — for
  incremental syllable validation, the preceding coda (empty at
  word start); for a completed-word sweep, full context

Main Success Scenario
---------------------

1. System receives the sequence, active constraints, and
   optional ``word_context``

2. System dispatches each constraint by domain (Q35):
   syllable-domain constraints and word-domain constraints are
   routed to their respective evaluation paths; fixed-domain types
   (``no_geminate_obstruents`` = word) and configurable types
   (``prohibited_clusters``, default syllable) resolve their
   domain from the constraint instance

3. For each syllable-domain constraint, system evaluates the
   sequence in isolation → PASSED or FAILED with a reason string

4. For each word-domain constraint:
   - If ``word_context`` is available, system evaluates across
   segment boundaries (the coda-onset junctions where
   geminates and word-domain clusters live)
   - If ``word_context`` is unavailable, the result is SKIPPED —
   reported as such, distinct from PASSED (Q37 four-value, :ref:`adr-039`)

5. System aggregates the results into an overall verdict:
   PASSED if and only if no constraint FAILED. SKIPPED results do
   not block the verdict but are recorded as provisional — the
   caller owning full context (UC-04's word sweep) must eventually
   confirm them

6. System returns the ``ValidationReport``: overall verdict,
   per-constraint results, and reason strings

Reason strings name the constraint, the offending segments, and —
for constraint instances shipped as defaults — their default
status (ADR-038 attribution): e.g., "sonority_sequencing (default):
/tk/ in onset — sonority falls before rising".

Extensions
----------

**2a:** Constraint type not in the catalog (schema from a newer or older project version)
  - 2a1: System refuses to evaluate that constraint and marks its result ERROR with reason "unknown constraint type [name]"
  - 2a2: Overall verdict is never PASSED while an ERROR result exists — validation does not silently skip what it cannot interpret
  - 2a3: Caller surfaces the error to the user with the schema version note (schema versioning is front-loaded by design)

**3a:** A constraint raises an internal error during evaluation* (implementation defect or malformed parameters)
  - 3a1: That constraint's result is ERROR with the exception summary; remaining constraints still evaluate
  - 3a2: Overall verdict is not PASSED — fail-closed, never fail-silent

  * System displays the survival funnel — candidates composed per
  template, then survivors after each active constraint in evaluation order
  — and names the most-rejected constraint with one rejected candidate as a
  concrete example. "Most-rejected" is a heuristic ranking of where candidates
  died, not a causal claim about unsatisfiability; see :ref:ADR-046.

**4a:** Two constraints in known conflict (per UC-03 extension 4a) both FAIL the sequence
  - 4a1: Both results are reported with their reasons
  - 4a2: The report does not adjudicate conflicts — the caller directs the user to :ref:`uc03` for resolution

Related
-------

**Called by:**
- :ref:`uc014` — Compose a Candidate Syllable (step 6, per candidate, with partial context)
- :ref:`uc04` — Generate Words (word-level sweep, full context; the only caller that can convert provisional SKIPPED results into final ones)

**Consumes:**
- Constraint instances defined by :ref:`uc03` (:class:`~latticelang.core.constraints.Constraint`)

**Leaf** — delegates to nothing below it.

Notes
-----

Disabled constraints are excluded from the report entirely.
SKIPPED is reserved for *enabled* word-domain constraints that
could not run for lack of context — the distinction matters for
debugging, so conflating them is forbidden.

Evaluation order follows definition order; order does not affect
the verdict (all constraints must pass) but stabilizes report
ordering for users and tests.

The function is deterministic: same inputs, same report, no
clock, no randomness. This is what makes UC-04's seed
reproducibility achievable at all — the validation layer must not
be a hidden source of nondeterminism.

Implementation home: ``latticelang/core/validation.py``
(:class:`~latticelang.core.validation.ValidationReport`).

Variations
----------
No CLI or GUI variations — subfunctions have no user-facing
entry points. Invoked programmatically via:

.. code-block:: python

   from latticelang.core.validation import validate

   report = validate(sequence=syllable,
                     constraints=definition.constraints,
                     word_context=ctx)
   report.overall          # bool
   report.results[0].status  # "PASSED" | "FAILED" | "SKIPPED"
   report.results[0].reason  # str, populated on FAILED
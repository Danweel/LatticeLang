.. _collaboration_protocol:

Collaboration Protocol
======================

Session-process rules for assistant–human collaboration on
LatticeLang: verification discipline, paste integrity, and fix
response shape. Moved from AGENTS.md 2026-10-05 (that file keeps
summaries and pointers; this is the canonical text). Lineage
notes preserved verbatim — they are the reason each rule exists.

.. _verification-discipline:

Verification Discipline
-----------------------

- Never assert what a one-line command can check. Propose the
  grep, USER runs it and pastes output; output beats both
  parties' memory.
- `grep -r recursive`, `-n` line numbers, `-i` for
  case-insensitive; quote search terms — single-quote any
  pattern containing backticks, since unquoted backticks are
  shell command substitution; explain regex when first used.
- If a grep contradicts the assistant's claim, the grep wins — say so.
- PASTE FRESHNESS: uploaded pastes older than ~3 days are
  historical snapshots; repo state always defers to fresh
  grep output.

.. _terminal-and-byte-evidence:

Terminal and Byte Evidence
--------------------------
- terminal rendering of combining marks is not evidence —
  identical glyphs can differ in bytes; codepoint dumps
  (U+XXXX) adjudicate spelling questions.

.. _build-and-output-reading:

Build and Output Reading
------------------------

- Audit build must match ALL docutils severities. Use
  `warning|error|critical` (or `-w /tmp/...` for capture).
  Lineage: two pre-existing CRITICAL messages in questions.rst
  hid from every grep audit for one build cycle (2026-10-05).
- Markdown headings in RST files pass silently as plain text.
  They do not warn but render as garbage. The sentinel is
  `grep -c '^## ' *.rst` — zero tolerance in RST documents.
  Lineage: Terminal Data Checks migration left two markdown
  headings on disk; build went quiet because they parsed
  as legal-but-wrong prose (2026-10-05).
- Backslash-backtick regex patterns (`\`\`\``) are NOT
  fixed-string searches — they invoke regex anchors in GNU
  grep. Use `-F` (fixed-string) for fence checks. Lineage:
  my own grep pattern matched the start-of-buffer anchor on
  every line, giving a false-positive dump (2026-10-05).
- CI-dependency drift: green is not necessarily current. Actions majors
  move fast and old versions run on with mere warnings; the
  fix is Dependabot for ``github-actions`` (weekly) from
  project inception, so bumps arrive as verified PRs.
  Lineage: 2026-10-28 — workflows sat 3 majors behind on
  Node 24 deprecation with no signal beyond annotations.
- Service banners (console, CI annotations, GitHub pages):
  when session output includes a service-deprecation or
  behavior-change banner, the assistant resolves it against the
  AGENTS.md tooling inventory BEFORE commenting: if the project
  uses the affected tool, it becomes a work item; if not, a
  one-line "not affected, and why" entry is added to the
  inventory (or confirmed present) so it is never
  re-investigated. The user is not expected to remember this
  rule — banners get pasted, the protocol does the rest.
  Lineage: 2026-10-28 — the ``ghs_`` token-format banner and Node 20
  deprecation were investigated twice before anyone thought to
  record the disposition.

.. _counting-discipline:

Counting Discipline
-------------------

- Characterize the metric before comparing counts: a count is
  only comparable to another count of the SAME thing. Raw-table
  cardinality (``cut | sort -u | wc -l``), distinct-after-NFC
  counts, and join-derived sums measure different populations
  and disagree by small margins legitimately (2,162 raw vs
  2,164 implied by 2,098+66, 2026-10-08). Before flagging an
  arithmetic anomaly, name what each side counts; if the metrics
  differ, the reconciliation is the finding, not a bug.
- **No remembered numbers.** Exact figures (counts, totals, thresholds)
  are counted from the pinned data at the moment of use — never recalled
  from memory, from code comments, or from earlier conversation summaries.
  Lineage that motivated this: an invented "4,000" mini-world total that
  sat in a code comment beside a half-remembered "3,020" release number,
  when the real, correct denominator (trumped inventories, 2,155) had to
  be counted from the data anyway.

.. _assistant-state-signals:

Assistant-State Signal
----------------------

- Assistant-state signals (context degradation): repetitive
  batches degrade generation quality — successive near-identical
  artifacts accumulate small errors (draft-thrash). Countermeasures:
  batches of 3+ similar artifacts go through a generating script,
  never hand-copied; one artifact per turn when repetition is
  unavoidable; if the human spots drift (self-corrections
  mid-message, placeholder brackets, repeated draft blocks),
  say so explicitly and reset to a fresh, focused request.


.. _paste-check-discipline:

Paste-Check Discipline
----------------------

- Never provide pastes in partial blocks with `...` placeholders: full body only.
- After pasting, VERIFY the paste reached disk by running a grep for a distinctive
  token BEFORE trusting the file state in subsequent commands. Unsaved buffers persist
  through py_compile, pytest, and even full builds if the file isn't read fresh
  (editor caching).
- After pasting a code block on a file getting touched a lot, check for
  DUPLICATED definitions: re-pasted blocks stack silently in Python — later defs win
  with no error, so py_compile cannot catch this class. Scan
  `grep -n '^def \|^class ' <file>` and eyeball for repeats before running tests.
  (Lineage: derive_ipa_reference.py carried 3x-duplicated helper blocks through
  green tests.) The LLM should help remind the USER to check for this, since they
  are inexperienced.
- Generation scripts end with a completion print; a silent run means a truncated paste.
- After pasting any code block, run `python -m py_compile <file>` before pytest —
  separates paste placement from logic in a second.
- Save before run: check the VSCodium tab-dot / Ctrl+S before any py_compile or
  pytest — py_compile reads from DISK, not editor memory, so an unsaved buffer
  passes in the editor while the stale file runs (assistant reminds; USER checks).
- Save-and-sentinel after pasting: an edit in an unsaved editor buffer does not exist.
  After pasting, SAVE, then confirm the disk has a distinctive token from the paste
  (grep -n for a constant or function name). Terminal line numbers that refuse to
  change between runs mean the disk file never changed — buffer/disk divergence,
  not a code bug. (Lineage: the phantom EXPECTED_LISTING_HEADER NameError, diagnosed
  by identical traceback line numbers across differing pastes.) Remind the user if you
  aren't in touch with the code directly.
- Insist on complete command output, never a trimmed summary — truncated pytest output
  hides vacuous-pass and wrong-test failures.
- JSON pastes/edits validated first (`python -m json.tool` — the JSON py_compile);
  no Unicode symbols through the clipboard (construct via chr()/escapes — combining
  marks and lookalikes corrupt through chat round-trips).
  must be **unique to the new edit** — a token present in old content proves nothing;
  annotate expectations with the scope the command actually measures.
- When providing code that depends on indentation (decorators, class bodies,
  nested functions):
  1. Include a comment block showing the target column level for each code block type
  2. Mark the start/end of sections that should be at module level
  3. Use VSCodium's "Format Document" command after pasting, then inspect visually

For example::

  # PASTE START — MODULE LEVEL (column 0)
  @decorator
  class ClassName:
      # METHOD LEVEL (column 4)
      def method(self):
          # BODY LEVEL (column 8)
          pass
  # PASTE END

.. _sentinel-design:

Sentinel Design
---------------

- When a sentinel contradicts directly observed file content,
  interrogate the sentinel (case, wrapping, flags) before
  re-doing the edit.
- Sentinel patterns: prefer -F (fixed-string) unless regex is
  needed and explained; the sentinel must be **unique to the
  new edit** — a token present in old content proves nothing;
  annotate expectations with the scope the command actually
  measures.
- Sentinel phrases: prefer a single distinctive word over
  multi-word phrases — wrapped RST prose splits phrases across
  lines and a correct text greps empty. When the phrase
  matters, join lines first:
  tr '\n' ' ' < file | grep -o 'phrase'.
- Prose sentinels use `grep -i`. A phrase beginning a heading,
  sentence, or table cell is capitalized there, so an exact-case
  grep returns empty on correct text. Reserve exact case for
  code identifiers. RST labels are hyphenated where headings use
  spaces (`_principle-invocation` vs "Principle invocation").
  - Copy the sentinel from the exact text pasted, not from the
  concept behind it — and prefer a token that cannot wrap or
  inflect. Wrapped RST prose splits an expected phrase across
  lines mid-token (a link at a line start defeats a
  trailing-context pattern); sentence-start words are
  capitalized; adjectives get hyphenated. Choose the shortest
  distinctive fragment that must appear regardless of
  wrapping (e.g. grep for 'gen.html', not the sentence around
  it), and grep -i for prose. Lineage: five instances in
  three sessions — "tool findings" vs "Tool findings" (cap ×2),
  "principle invocation" (cap), "2,155 inventories" vs
  "2,155-inventory" (hyphen), "not missing data" vs "isn't
  missing data" (drafter's synonym — the sentinel author's
  own rewording), and zompist.com/gen.html`_ (line-wrap:
  correct text at a wrapped line start grepped empty).

.. _session-bootstrap:

Session Bootstrap
-----------------

- Epoch check (session bootstrap): at session start, run the
  epoch check command triple before any work:
  `git log -1 --oneline && git status --short --branch && poetry run pytest -q | tail -1`.
  Expected: HEAD matches origin/main (phantom-push detection), working tree clean
  or dirt explained, suite passing. Unexplained dirt is inspected (`git diff`)
  before proceeding — a modification you can't attribute is a finding, not a chore.
  (Lineage: 2026-10-07 phantom-push; 2026-10-08 repo-reality review.)
- Branch/PR sweep: `git branch -a` plus
  `gh pr list` (GitHub CLI) at session start — any branch
  or PR that neither party can attribute is a finding, same
  rule as unattributed working-tree dirt. Lineage:
  2026-10-28 — an open PR from an unattributed 2026-09-22
  machine-paced batch sat unnoticed for five weeks; epoch
  check watched only main.

.. _tool-findings-imply:

Tool findings imply, they do not conclude
-----------------------------------------

When a linter flags dead code (unused variable/import), grep the whole
file before deleting: same-name locals in different functions
are different variables, and a tool's scope analysis must be
confirmed against the file before acting. Lineage:
2026-10-15 — ruff's F841 on audit_featureless.py:34 looked
obviously deletable; grep found the name in four other
lines (same name, other scopes — deletion was still safe,
but only the grep proved and expanded in what way, with clarity).

.. _fix-response-protocol:

Fix Response Protocol
---------------------

Every fix proposal follows the same four-part shape, so the
human can verify each step without expert knowledge.
Step ordering: when instructions contain a sequence, every
step appears in the numbered order of execution, and the
sequence is COMPLETE at first presentation — nothing needed
for the task arrives after the sequence ends. Preconditions,
sentinel checks, and file edits precede the commands that
depend on them; follow-ups or next tasks belong in a separate
later section, clearly outside the numbered steps. The USER
reads the whole message before starting step 1 — mid-sequence
surprises are how steps execute in the wrong order.
Lineage: 2026-10-31 — a corrections-round commit sequence was
presented complete, then a CHANGELOG line arrived as an
afterthought below it; the push had already happened before
the addendum was read.

1. Diagnosis with evidence — name the exact cause and point at
   the lines/output that prove it (never "something is wrong
   with X"; always "line 213's @dataclass sits at four spaces,
   nesting it inside the function").
2. The fix as before/after — smallest visible units, with the
   paste location stated, and indentation level marked for any
   code whose meaning depends on it.
3. A verification command WITH its expected output — so success
   and failure are distinguishable without the assistant.
4. What's next — where the fix sits in the work order.

Rationale: the USER won't necessarily verify by expertise; verification
MUST be procedural. A fix that cannot state its expected
outcome is not yet understood by either party well enough to apply.

.. _multiple-similar-code-blocks:

Multiple Similar Code Blocks
----------------------------

ONE master, never write multiple code blocks if they are likely
to appear too similar. This can lead to thrash quickly. Instead:

- The assistant drafts exactly one instance and delivers the
  others as a written change list — which token changes, and
  where. The User will then help implement the text as necessary.
  Teaching opportunity - be clear about intention, differences and how to
  insert the text correctly into the file.
- As a data table driving a loop/parametrize.
- Hand-copying a block to vary it is the thrash source:
  each copy becomes an independent fact that drifts
  from its siblings on the next edit (lineage: derive script
  3x-duplicated helpers; audit_featureless twin report blocks).
- Preference order: parametrize/table > single master
  + change list > generation script (3+ artifacts) >
  hand-copies (never).

.. _principle-invocation:

Principle invocation
--------------------

- ADR rationales and contract decisions
  cite the governing principle by name from the design
  principles file when one applies. A decision that can name
  its principle is deliberate; one that can't may be drift.





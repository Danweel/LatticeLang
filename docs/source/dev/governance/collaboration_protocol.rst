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
- `grep -r recursive`, `-n` line numbers, quote search terms,
  `-i` for case-insensitive; explain regex when first used.
- If a grep contradicts the assistant's claim, the grep wins — say so.
- PASTE FRESHNESS: uploaded pastes older than ~3 days are
  historical snapshots; repo state always defers to fresh
  grep output.
- Audit build must match ALL docutils severities. The grep
  pattern `warning|error` misses CRITICAL-severity messages;
  use `warning|error|critical` (or `-w /tmp/...` for capture).
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


.. _paste-check-discipline:

Paste-Check Discipline
----------------------

- After pasting any code block, run `python -m py_compile <file>` before pytest — separates paste placement from logic in a second.
- After pasting a code block on a file getting touched a lot, check for DUPLICATED definitions:
  re-pasted blocks stack silently in Python — later defs win
  with no error, so py_compile cannot catch this class. Scan
  `grep -n '^def \|^class ' <file>` and eyeball for repeats
  before running tests. (Lineage: derive_ipa_reference.py
  carried 3x-duplicated helper blocks through green tests.) The LLM should help remind the USER to check for this, since they are inexperienced.
- Never paste partial blocks with `...` placeholders: full body or nothing.
- Shell quoting: single-quote grep/sed patterns containing backticks.
- Save before run: check the VSCodium tab-dot / Ctrl+S before any py_compile or pytest — py_compile reads from DISK, not editor memory, so an unsaved buffer passes in the editor while the stale file runs (assistant reminds; USER checks).
- Paste complete command output, never a trimmed summary — truncated pytest output hides vacuous-pass and wrong-test failures.
- **No remembered numbers.** Exact figures (counts, totals, thresholds)
  are counted from the pinned data at the moment of use — never recalled
  from memory, from code comments, or from earlier conversation summaries.
  Lineage that motivated this: an invented "4,000" mini-world total that
  sat in a code comment beside a half-remembered "3,020" release number,
  when the real, correct denominator (trumped inventories, 2,155) had to
  be counted from the data anyway.
- When pasting code that depends on indentation (decorators, class bodies, nested functions):
  1. Include a comment block showing the target column level for each code block type
  2. Mark the start/end of sections that should be at module level
  3. Use VSCodium's "Format Document" command after pasting, then inspect visually

For example:
```
# PASTE START — MODULE LEVEL (column 0)
@decorator
class ClassName:
    # METHOD LEVEL (column 4)
    def method(self):
        # BODY LEVEL (column 8)
        pass
# PASTE END
```

- Save-and-sentinel after pasting: an edit in an unsaved editor
  buffer does not exist. After pasting, SAVE, then confirm the
  disk has a distinctive token from the paste (grep -n for a
  constant or function name). Terminal line numbers that refuse
  to change between runs mean the disk file never changed —
  buffer/disk divergence, not a code bug. (Lineage: the
  phantom EXPECTED_LISTING_HEADER NameError, diagnosed by
  identical traceback line numbers across differing pastes.)
  Remind the user if you aren't in touch with the code directly.
- After pasting, VERIFY the paste reached disk by running
  a grep for a distinctive token BEFORE trusting the file
  state in subsequent commands. Unsaved buffers persist
  through py_compile, pytest, and even full builds if
  the file isn't read fresh (editor caching).

.. _fix-response-protocol:

Fix Response Protocol
---------------------

Every fix proposal follows the same four-part shape, so the
human can verify each step without expert knowledge:

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

#!/usr/bin/env python3
"""Write-mode deferred-entry adder for data/ipa_chart.json.

The chart file is never hand-edited and glyphs never transit the
clipboard: this script reads and writes the JSON directly. Aborts
if any target key already exists (double-run protection);
--dry-run prints prospective entries and writes nothing.

Click-family usage (hex=name pairs):
    poetry run python scripts/add_deferred.py 298=bilabial 1C0=dental
"""
import json
import sys
from pathlib import Path

CHART_PATH = Path("data/ipa_chart.json")

CLICK_TEMPLATE = (
    "{label} click (U+{cp:04X}): chart-canonical bare letter; "
    "PHOIBLE 2.0 attests only accompanied clusters (velar-closure "
    "voicing/nasality plus release modifiers), 0 bare rows in both "
    "the listing and the features table (probes 2026-10-08). "
    "Cluster admission policy: Q48."
)


def build_click_entries(pairs):
    entries = {}
    for pair in pairs:
        hexcode, label = pair.split("=", 1)
        cp = int(hexcode, 16)
        entries[chr(cp)] = CLICK_TEMPLATE.format(label=label, cp=cp)
    return entries


def main(argv):
    args = [a for a in argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in argv
    if not args:
        print(__doc__)
        return 1

    entries = build_click_entries(args)
    chart = json.loads(CHART_PATH.read_text(encoding="utf-8"))

    already = [k for k in entries if k in chart.get("deferred", {})]
    if already:
        print("ABORT: already deferred:",
              [f"U+{ord(k):04X}" for k in already], file=sys.stderr)
        return 1

    if dry:
        for k, v in entries.items():
            print(json.dumps({k: v}, indent=2, ensure_ascii=True))
        print(f"-- dry run: {len(entries)} entries, nothing written --")
        return 0

    chart.setdefault("deferred", {}).update(entries)
    CHART_PATH.write_text(
        json.dumps(chart, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"-- deferred now: {len(chart['deferred'])} entries --")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

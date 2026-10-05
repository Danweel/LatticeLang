"""Audit the attested-but-featureless symbol set under the NFC join.

Generates docs/source/research/q36_featureless_audit.rst from the
vendored data — generated, never authored (fixture doctrine).
Records EVERY symbol in the set with its codepoints, attestation
count, and a provisional problem class, including extraenious(?) rows.

Classification is codepoint-heuristic and provisional; classes
feed F-3/F-6 rulings, they do not replace them.
"""

from __future__ import annotations

import csv
import unicodedata
from collections import Counter
from pathlib import Path

V = Path("vendor/phoible-2.0/phoible-dev-862bec9")
OUT = Path("docs/source/research/q36_featureless_audit.rst")

H_ASPIRATE = chr(0x02B0)   # modifier letter h
H_VOICED = chr(0x02B1)     # modifier letter h with hook
BREATHY = chr(0x0324)      # combining diaeresis below
GLOTTAL = chr(0x02C0)      # modifier letter glottal stop

def symbols(path: Path, col: int) -> Counter:
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        return Counter(row[col] for row in reader)

def classify(sym: str, features: set[str]) -> str:
    cps = [ord(c) for c in sym]
    if sym == "N":
        return "legacy artifact (ASCII capital N — investigate provenance)"
    if BREATHY in sym:
        return "breathy-voiced (partially modeled in features)"
    if GLOTTAL in sym:
        return "click/glottal accompaniment (unmodeled)"
    if H_ASPIRATE in sym:
        # would swapping for the voiced aspirate mark find features?
        if sym.replace(H_ASPIRATE, H_VOICED) in features:
            return "voiced-aspirate variant (F-6 alias candidate)"
        if sym.startswith(H_ASPIRATE):
            return "preposed aspiration (order variant)"
        return "other aspiration variant"
    return "unclassified"

listing = symbols(V / "gold-standard/phoible-phonemes.tsv", 7)
features = symbols(V / "raw-data/FEATURES/phoible-segments-features.tsv", 0)
nfc_feat = {unicodedata.normalize("NFC", s) for s in features}

the62 = {s: listing[s] for s in listing
         if unicodedata.normalize("NFC", s) not in nfc_feat}
rescued21 = {s: listing[s] for s in listing
             if s not in features
             and unicodedata.normalize("NFC", s) in nfc_feat}
unattested66 = {s for s in features
                if unicodedata.normalize("NFC", s)
                not in {unicodedata.normalize("NFC", t)
                        for t in listing}}

lines = [
    ".. _q36-featureless-audit:",
    "",
    "Featureless-Symbol Audit (Q36 evidence: F-3, F-6)",
    "=================================================",
    "",
    "GENERATED FILE — do not edit by hand; regenerate with",
    "``poetry run python -m scripts.audit_featureless``.",
    "Source: vendored PHOIBLE 2.0 (dev-862bec9); probe date",
    "2026-10-05. Method: NFC-normalized join between the",
    "gold-standard listing (field 8) and the features matrix",
    "(field 1); see dc_phoible_source.rst counting recipes.",
    "",
    f"Counts: {len(listing)} attested symbols; "
    f"{len(the62)} featureless under NFC join "
    "(naive join reported 83); "
    f"{len(rescued21)} rescued by NFC from encoding variance; "
    f"{len(unattested66)} features-only unattested "
    "(naive: 85).",
    "",
    "Every featureless symbol, with codepoints, attestations,",
    "and provisional class:",
    "",
    ".. list-table::",
    "   :header-rows: 1",
    "",
    "   * - Symbol - Attested - Codepoints - Class",
]
for sym, n in sorted(the62.items(), key=lambda kv: -kv[1]):
    cps = " ".join(f"U+{ord(c):04X}" for c in sym)
    lines.append(f"   * - ``{sym}`` - {n} - {cps}"
                 f" - {classify(sym, set(features))}")

lines += [
    "",
    "Rescued by NFC join (21) — precomposed/decomposed variance:",
    "",
]
for sym in sorted(rescued21):
    cps = " ".join(f"U+{ord(c):04X}" for c in sym)
    lines.append(f"- ``{sym}`` ({cps}), {listing[sym]} attestations")

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {OUT}: 62={len(the62)} rescued={len(rescued21)}"
      f" unattested={len(unattested66)}")

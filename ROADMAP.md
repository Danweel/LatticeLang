Post-MVP features (corpus inference, orthography mapping, allophonic engine, etc.) are tracked separately under [Planned Features].
I'll move it to here if we get that far.

| Milestone | Focus | Definition of Done | Status |
|-----------|-------|--------------------|--------|
| 0 | Infrastructure | RTD builds clean, CI passes, 0 ruff errors | Complete |
| 1 | Core engine | `test_english_validation.py` passes; generator produces valid English-like words from `english_ga.json` | In progress |
| 2 | CLI | `latticelang generate --preset english` produces valid words; `latticelang export --format latex` writes `.tex` | Pending |
| 3 | GUI shell | PySide6 window with phoneme editor; live preview updates on rule change | Pending |
| 4 | Export | `.tex` compiles with `pdflatex + tipa`; JSON round-trip (save → load → identical output) | Pending |
| 5 | Release prep | `pip install latticelang` works; README has quickstart; 2+ presets shipped; CONTRIBUTING tested | Pending |
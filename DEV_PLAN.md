# LatticeLang — Design Document
**Version:** 0.1.0-draft

**Author:** Danweel

**Date:** 2026-04-04

**License:** GPL-3.0-or-later

---

## Table of Contents

1. [Purpose and Scope](#purpose-and-scope)
   - Problem Statement
   - Core Goals
   - Core Philosophy / Observations on Current Programs
   - Target User
   - Core (MVP) Features
   - Planned Features (Post-MVP)
   - Out of Scope
   - Success Criteria
2. [Technical Architecture](#technical-architecture)
   - Tech Stack
   - Architecture Pattern / Key Principles
   - Data Model
   - Constraints
   - Directory Structure
   - Key Architectural Decisions
3. [Development Approach](#development-approach)
   - Methodology
   - Phases
   - Git Branching Strategy
   - Coding Workflow (with AI)
   - Commit Message Convention
4. [Research and References](#research-and-references)
   - Linguistics References
   - Phonotactic References (English-Specific)
   - Software References
   - Python Ecosystem
5. [Dependencies and Environment](#dependencies-and-environment)
   - Runtime Environment
   - Runtime Dependencies
   - Development Dependencies
   - System / Hardware
6. [Security Considerations](#security-considerations)
7. [Error Handling and Logging](#error-handling-and-logging)
   - Strategy
   - Graceful Fails
8. [Backup and Data Integrity](#backup-and-data-integrity)
9. [Performance Considerations](#performance-considerations)
   - Target Performance
   - Optimization Guidelines
10. [Deployment and Distribution](#deployment-and-distribution)
    - Initial Deployment (Personal)
    - Future Distribution
11. [Issue Tracking and Project Organization](#issue-tracking-and-project-organization)
    - Tools
    - Label Scheme
    - Commit Message Convention
12. [Risk Assessment](#risk-assessment)
13. [Open Questions](#open-questions) *(now resolved — see Decisions Log)*
14. [Decisions Log](#decisions-log)

## Purpose and Scope

### Problem Statement
Existing conlanging tools fall into two extremes: simple generators that produce
user-guided syllable strings with no linguistic grounding, or heavyweight professional
tools (e.g., SIL FieldWorks) designed for field documentation rather than creative
language construction. There is no libre, accessible, programmatically-extensible
tool that sits in the middle — for serious conlangers who want naturalistic output
without needing to bring most of a linguistics course with them.

### Core Goals
1. Generate phonologically valid, naturalistic words from user-defined phoneme
   inventories, syllable templates, and phonotactic rules.
2. Provide a real-time visual preview of generation results (the "live preview"
   pane — a feature absent from competing tools).
3. Export linguistic data to standard formats: LaTeX (with IPA support), JSON,
   and human-readable tables.
4. Remain fully FOSS, cross-platform, and extensible via plugins or scripting.

### Core Philosophy / Observations on Current Programs
- **Hobbyist tools** (e.g., Vulgar, Awkwords) are easy to use but produce
  mechanical, repetitive output. Their rule systems are too simple for
  naturalistic allophony, assimilation, or sonority-driven syllabification.
- **SIL FieldWorks** is powerful but oriented toward language documentation,
  not creative construction. Its UI is dense and its learning curve is steep.
- **LatticeLang's niche:** Programmatic control over phonological generation
  with an intuitive UI. Think "REPL for phonology" with a GUI on top.

### Target User
Conlangers and hobbyist linguists who want:
- Control over phoneme inventories and features
- Naturalistic output (not just CV syllable repetition)
- An interface that shows results immediately as rules change
- Export to formats they can use in worldbuilding documents, papers, or zines

### Core (MVP) Features
1. **Phoneme editor:** Define phonemes by IPA symbol, features, sonority rank,
   and frequency weight. UI-driven (table view with inline editing).
2. **Syllable template builder:** Compose syllable structure patterns (CV, CVC,
   CCVC, etc.) with positional constraints.
3. **Word generator:** Produce N words from the defined phonology, respecting
   SSP, phonotactics, and frequency weighting.
4. **Live preview:** Generated words update in real time as rules are modified.
5. **LaTeX export:** Emit a compilable `.tex` document with phoneme charts and
   wordlists, using `tipa` for IPA symbols.
6. **JSON serialization:** Save/load entire language definitions as `.json` or
   `.yaml` project files.

### Planned Features (Post-MVP)
- Allophonic rule engine (contextual sound changes)
- Morphological layering (affixes, compounding)
- Historical sound-change simulation (apply ordered rulesets over time)
- Intonation and prosody hints
- Comparison mode (overlay two language definitions)
- Plugin API for custom generation strategies
- Internationalization (i18n) for the UI itself

### Out of Scope (For Now)
- Full text-to-speech synthesis
- Corpus analysis of existing natural languages (that's FieldWorks' job)
- Orthography font rendering (depends on user-supplied fonts; we output Unicode
  and LaTeX, not rendered glyphs)
- Web deployment (desktop-first; web is a future possibility)

### Success Criteria
- **MVP complete when:** The "English test language" (defined below) produces
  words that a linguistically informed reader would accept as English-like.
- **Architecture validated when:** A second language (e.g., Japanese — simple
  CV phonology, very different constraints) can be defined without code changes.
- **Docs green when:** Read the Docs builds with zero warnings and zero errors.

---

## Technical Architecture

### Tech Stack

| Layer          | Technology                              | Rationale                                    |
|----------------|-----------------------------------------|----------------------------------------------|
| Language       | Python 3.11+                            | Linguistics ecosystem (NLTK, IPA libraries)  |
| Packaging      | Poetry                                  | Already in use; reproducible locks           |
| GUI            | PySide6 (Qt for Python)                 | FOSS Qt binding; shared expertise with other  project; rich text rendering for LaTeX/HTML  |
| TUI (optional)  | `rich` library                          | Terminal tables, progress bars, pretty output|
| Docs           | Sphinx + Furo + MyST + Mermaid          | Already configured                           |
| Docs hosting   | Read the Docs                           | Already configured                           |
| Linting        | Ruff                                    | Fast, replaces flake8 + isort + black        |
| Testing        | pytest + pytest-cov                     | Standard Python testing stack                |
| CI             | GitHub Actions                          | Already in use                               |
| LaTeX (docs)   | `sphinx.ext.imgmath` or MathJax via     | Render IPA/formulas in documentation         |
|                | MyST `dollarmath` extension             |                                              |
| LaTeX (export) | Raw string templating → `.tex` files    | Simpler than a LaTeX AST; user compiles      |
|                | (future: `pylatex` or `pylatexenc`)    |                                              |

### Architecture Pattern / Key Principles

**Separation of concerns — three layers:**

1. **Core (pure logic):** Phoneme definitions, syllable templates, sonority
   hierarchy, generation engine, constraint validation. No UI, no I/O. This is
   the testable heart of the project. If you run it headless in a script, it
   works identically to the GUI.

2. **Orthography / Export:** Transliteration mappers, LaTeX export, JSON/YAML
   serialization. Converts core data structures into output formats.

3. **UI (presentation):** PySide6 windows, widgets, the live-preview pane. Reads
   from and writes to the core layer via a controller/mediator. Never contains
   phonological logic.

**Key principle: The core layer knows nothing about LaTeX, Qt, or files.**
It operates on Python dataclasses. The export/UI layers translate.

### Data Model

The fundamental data structures (to be implemented as `dataclasses` or
`pydantic` models):

```python
@dataclass
class Phoneme:
    symbol: str            # IPA symbol, e.g. "k", "æ", "ʃ"
    category: str          # "consonant" | "vowel"
    features: set[str]     # e.g. {"velar", "plosive", "voiceless"}
    sonority_rank: int     # Position in the sonority hierarchy (0 = lowest)
    frequency: float       # Relative frequency weight (0.0–1.0, normalized)

@dataclass
class SyllableSlot:
    position: str          # "onset" | "nucleus" | "coda"
    allowed_categories: list[str]  # Which phoneme categories fit here
    min_count: int         # Minimum phonemes in this slot (nucleus = 1)
    max_count: int         # Maximum phonemes in this slot

@dataclass
class SyllableTemplate:
    name: str              # e.g. "CVC", "CCVC"
    slots: list[SyllableSlot]
    constraints: list[str] # Language-specific rules (e.g., "allow_s_appendix")

@dataclass
class LanguageDefinition:
    name: str
    phonemes: list[Phoneme]
    syllable_templates: list[SyllableTemplate]
    phonotactic_constraints: list[str]  # Named rules, evaluated by the engine
    generation_settings: dict           # word_count, min/max_length, etc.
```

**Serialization format:** JSON by default, with YAML as an alternative. Example project file:

```json
name: "English (Test)"
phonemes:
  - symbol: "k"
    category: "consonant"
    features: ["velar", "plosive", "voiceless"]
    sonority_rank: 3
    frequency: 0.85
  - symbol: "æ"
    category: "vowel"
    features: ["near-open", "front", "unrounded"]
    sonority_rank: 9
    frequency: 0.72
syllable_templates:
  - name: "CVC"
    slots:
      - position: "onset"
        allowed_categories: ["consonant"]
        min_count: 1
        max_count: 1
      - position: "nucleus"
        allowed_categories: ["vowel"]
        min_count: 1
        max_count: 1
      - position: "coda"
        allowed_categories: ["consonant"]
        min_count: 0
        max_count: 1
phonotactic_constraints:
  - "sonority_sequencing"
  - "allow_s_appendix"
  - "no_geminate_obstruents"
generation_settings:
  word_count: 100
  min_syllables: 1
  max_syllables: 4
```

### Constraints

- Must run on Linux (primary), macOS, and Windows.
- Python 3.11+ (matches RTD build environment and Poetry config).
- No compiled C extensions required (pure Python for portability).
- LaTeX export produces valid .tex — compilation is the user's responsibility (we don't bundle a TeX distribution).

### Directory Structure

```
LatticeLang/
├── src/
│   └── latticelang/
│       ├── __init__.py
│       ├── __main__.py              # python -m latticelang
│       ├── cli.py                   # CLI entry point
│       ├── core/                    # --- Pure logic layer ---
│       │   ├── __init__.py
│       │   ├── phonology.py         # Phoneme dataclass, inventory management
│       │   ├── syllable.py          # SyllableTemplate, syllabification
│       │   ├── sonority.py          # Sonority hierarchy, SSP enforcement
│       │   ├── generator.py         # Word generation engine
│       │   └── constraints.py       # Phonotactic constraint evaluators
│       ├── orthography/             # --- Export / mapping layer ---
│       │   ├── __init__.py
│       │   ├── transliteration.py   # Phoneme ↔ glyph mapping
│       │   ├── mapper.py            # Rule-based transcription
│       │   ├── latex_export.py      # .tex document generation
│       │   └── json_io.py           # Serialization (save/load project files)
│       ├── ui/                      # --- Presentation layer ---
│       │   ├── __init__.py
│       │   ├── app.py               # Main PySide6 window
│       │   ├── phoneme_editor.py    # Table widget for phoneme editing
│       │   ├── template_editor.py   # Syllable template builder widget
│       │   ├── live_preview.py      # Real-time word list display
│       │   └── latex_preview.py     # Rendered LaTeX/MathJax preview pane
│       └── utils/
│           ├── __init__.py
│           └── validators.py        # Input validation helpers
├── data/
│   └── presets/                     # Built-in language presets
│       ├── english_test.json        # Validation language
│       └── japanese_simple.json     # Second validation language
├── docs/
│   ├── source/
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── installation.rst
│   │   ├── usage.rst
│   │   ├── design/
│   │   │   └── DESIGN.md            # This document
│   │   ├── api/
│   │   │   └── ...                  # Autodoc-generated
│   │   └── roadmap.rst
│   └── Makefile
├── tests/
│   ├── __init__.py
│   ├── test_phonology.py
│   ├── test_sonority.py
│   ├── test_syllable.py
│   ├── test_generator.py
│   └── test_english_validation.py   # The "English test" acceptance tests
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── .readthedocs.yaml
├── .gitignore
├── README.md
└── LICENSE                         # GPL-3.0-or-later
```

### Key Architectural Decisions

    1. PySide6 over PyQt6: LGPL vs GPL licensing. PySide6's LGPL is more permissive for distribution. Also: shared expertise with another project, reducing context-switching cost. [Decided: 2026-04-04]

    2. Dataclasses over Pydantic (initially): Keep the core layer dependency-free. If validation complexity grows, migrate to Pydantic later — the interface stays the same. [?] — revisit if constraint validation becomes unwieldy.

    3. LaTeX as export target, not input format: LaTeX is for presentation, not storage. The canonical data format is JSON/YAML. This avoids the "parse LaTeX" nightmare. [Decided: 2026-04-04]

    4. Sonority hierarchy as a ranked list, not a tree: Simpler to reason about, sufficient for SSP checking. Trees become relevant if we need feature-based distance calculations (future feature). [Decided: 2026-04-04]

    5. English as the validation language: If we can model English phonology accurately enough to generate convincing pseudo-English, the architecture is proven. English is chosen because its phonology is well-documented and its complexity (clusters, s-appendix, vowel reduction) exercises most engine features. [Decided: 2026-04-04]

---

## Development Approach

### Methodoloy

Iterative, milestone-driven. No formal sprint schedule (solo developer), but each milestone has a definition-of-done:

    Milestone 0: Infrastructure Green — RTD builds clean, CI passes, lint clean.
    Milestone 1: Core Engine — Phoneme, SyllableTemplate, Generator working in pure Python (no UI). English test language validates.
    Milestone 2: CLI — Command-line access to generation and export.
    Milestone 3: GUI Shell — PySide6 window with phoneme editor and live preview.
    Milestone 4: LaTeX Export — .tex generation with IPA tables.
    Milestone 5: Polish — Error handling, documentation, presets, packaging.

### Phases
| Phase	| Focus	| Exit Criteria |
| --- | --- | ---|
| 0 | Infra & docs | RTD green, CI green, 0 ruff errors |
| 1	| Core engine | test_english_validation.py passes |
| 2	| CLI | latticelang generate --preset english produces valid words |
| 3	| GUI (PySide6) | Live preview updates on rule change |
| 4	| Export (LaTeX/JSON) | .tex compiles with pdflatex + tipa |
| 5	| Release prep | pip-installable, documented, 2+ presets |

### Git Branching Strategy
```
    main — stable, always builds green.
    dev — integration branch for features.
    feat/<name> — individual features (e.g., feat/phoneme-editor).
    fix/<name> — bug fixes.
    docs/<name> — documentation work.
```

Tag releases as v0.1.0, v0.2.0, etc.

### Coding Workflow (with AI)

   Use Lumo or equivalent AI assistant for:

    - Scaffolding boilerplate (dataclasses, widget skeletons)
    - Exploring unfamiliar APIs (PySide6, Sphinx internals)
    - Reviewing logic in constraint evaluation
Do not rely on AI for:

    - Linguistic correctness of phonological rules (verify against references)
    - Final architectural decisions (human judgment required)

An AGENTS.md file at repo root can codify conventions for AI-assisted contributions if the project accepts external collaborators.

### Commit Message Convention

Conventional Commits:

```
feat(core): implement sonority sequencing enforcement
fix(docs): resolve sphinxcontrib-mermaid import in RTD build
docs(design): draft initial design document
chore(deps): pin sphinx <9.0 to prevent breaking changes
refactor(generator): extract constraint evaluation to separate module
```

---

## Research and References
### Linguistics References

    - Goldsmith, J. A. (1995). The Handbook of Phonological Theory. — Comprehensive reference for phonological frameworks.
    - Clements, G. N. (1990). "The role of the sonority cycle in core syllabification." — Foundational paper on the Sonority Sequencing Principle.
    - Hayes, B. (2009). Introductory Phonology. — Accessible textbook with English-specific examples.
    - Ladefoged, P. & Johnson, K. (2014). A Course in Phonetics. — IPA reference and articulatory descriptions.

### Phonotactic References (English-Specific)

    - English permits: /s/ + voiceless stop + liquid/glide in onsets (spr-, str-, skw-).
    - English prohibits: nasal + voiced stop in onset (mb-, nd- — unlike Swahili).
    - English coda clusters max out at ~4 consonants (sixths = /ksθs/).

### Software References

    - Vulgar (vulgarlang.com) — Proprietary conlang generator. Reference for features to improve upon (limited sonority awareness, no live preview).
    - Awkwords — Free regex-based generator. Good for understanding what a minimal interface looks like, but no linguistic grounding.
    - SIL FieldWorks — Open-source, but documentation-oriented. Reference for comprehensiveness, not UX.

### Python Ecosystem

    - panphon — Feature-based phoneme comparison library. Useful for validating that user-defined features align with standard IPA feature systems. [?] Evaluate whether to depend on it or implement a lightweight feature set.

---

## Dependencies and Environment
### Runtime Environment

- **OS**: Linux (primary development: Ubuntu Studio 24.04, KDE Plasma 5.27)
- **Python**: 3.11+ (3.12 preferred; matches RTD)
- **Qt**: PySide6 (bundled via pip, no system Qt required)

### Runtime Dependencies
`PySide6 >= 6.6`

(Launcher-only dependency. The core engine has zero runtime dependencies beyond the standard library — by design, for testability and headless use.)

### Development Dependencies
```
sphinx >=8.0, <9.0
furo >=2024.8.6
sphinxcontrib-mermaid >=2.0.0
sphinx-notfound-page >=1.0.0
sphinx-copybutton >=0.5.2
myst-parser >=3.0.0
sphinx-design >=0.6.0
ruff >=0.6
pytest >=8.0
pytest-cov >=5.0
```

### System / Hardware

- Development machine: FOXHOUND-X570 (Ubuntu Studio 24.04.3 LTS, KDE Plasma 5.27.12, kernel 6.14, X11, bash, VSCodium).
- No special hardware requirements. PySide6 GPU acceleration is optional; software rendering is sufficient for the UI complexity envisioned.

---

## Security Considerations

- Input sanitization: Language definition files (JSON/YAML) are loaded from disk. Use json.load() (safe) and a vetted YAML parser (avoid yaml.load() without Loader= — use yaml.safe_load()).
- No network access required: The application is fully offline. LaTeX compilation is a separate user-initiated step.
- No user data collection: No telemetry, analytics, or phone-home behavior. Consistent with FOSS philosophy.
- Plugin security [?]: If a plugin API is added post-MVP, define a sandboxing strategy. Python's importlib has no native sandbox; consider restricting plugins to a declarative rule format rather than executable code.

---

## Error Handling and Logging
### Strategy

- Core layer: Raise typed exceptions. No silent failures. No catching Exception broadly. Example: PhonemeValidationError, ConstraintViolationError, TemplateSyntaxError.
- UI layer: Catch core exceptions at the boundary, display user-friendly messages (QMessageBox or status bar), and log the traceback.
- Logging: Python logging module, configured at app startup. Debug logs to ~/.latticelang/logs/. Rotating file handler (1MB, 3 backups).

### Graceful Fails

- If a language definition file is corrupted: load what's parseable, warn about the rest, offer to revert to last known good save.
- If a constraint conflicts with a syllable template: mark the template as "invalid" in the UI (red highlight) rather than crashing generation.
- If LaTeX export produces invalid .tex: include a comment in the file indicating the error location. The user can debug manually.

### Backup and Data Integrity

- Language project files are user-owned and stored wherever the user chooses. No cloud sync (privacy-first).
- Auto-save: project state saved to ~/.latticelang/autosave/ every 30 seconds if changes are detected. Cleared on successful manual save.
- Version control is the backup mechanism for source code. Users are responsible for backing up their .json/.yaml language files.
- [?]: Consider a .latticelang/ project directory format (like .git/) that bundles the language definition, generation history, and export cache.

---

## Performance Considerations
### Target Performance

- Generating 1,000 words: < 500ms (pure Python, no multiprocessing).
- UI responsiveness during live preview: < 100ms regeneration debounce.
- Loading a language definition file: < 50ms for typical inventories (~50 phonemes, 5 templates).

### Optimization Guidelines

- Premature optimization is the enemy. Profile first, optimize second.
- The generator is CPU-bound but lightweight — phoneme lookup and random selection are O(n) per phoneme, where n is inventory size (~50).
- If generation becomes slow (unlikely at MVP scale): precompute valid onset/ coda clusters as a lookup table per template, rather than validating constraints per generation attempt.
- PySide6 live preview: use a QTimer debounce (100-150ms) so rapid editing doesn't trigger generation on every keystroke.

---

## Deployment and Distribution
Initial Deployment (Personal)

- Clone repository, poetry install, poetry run latticelang.
    No packaging required for personal use.

Future Distribution

- PyPI: pip install latticelang (core + CLI, no GUI dependency). Optional extra: pip install latticelang[gui] pulls PySide6.
- Flatpak: Native Linux packaging (fits Ubuntu Studio workflow). PySide6 apps package well as Flatpaks.
- AppImage: Portable single-file binary. Lower effort than Flatpak.
- Windows/macOS: PyInstaller or Nuitka for frozen binaries. Lower priority.
- Versioning: Semantic versioning. 0.x.x during development, 1.0.0 at first stable release.

---

## Issue Tracking and Project Organization
### Tools

- Issue tracking: GitHub Issues (integrated, free, sufficient for solo/small team).
- Project board: GitHub Projects (kanban). Columns: Backlog → In Progress → Review → Done.
- Documentation: Read the Docs (public-facing) + inline docstrings (API).

### Label Scheme

```
type:bug        — Something doesn't work
type:feature    — New functionality
type:docs       — Documentation
type:refactor   — Code quality, no behavior change
type:chore      — Maintenance, deps, CI
priority:critical — Blocks development or release
priority:high     — Important for current milestone
priority:low      — Nice to have
area:core       — Core engine (phonology, generator, constraints)
area:ui         — PySide6 interface
area:docs       — Sphinx, RTD, design docs
area:export     — LaTeX, JSON, serialization
area:ci         — GitHub Actions, build pipeline
```

### Commit Message Convention

(See Development Approach → Commit Message Convention above.)

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Sonority rules prove too rigid for diverse languages | Medium | High | Start with English SSP; iterate. The constraint system should be descriptive, not prescriptive — let users override. |
| PySide6 adds complexity beyond coding comfort level | Medium | Medium | GUI is Milestone 3. Core engine works headless first. Learn Qt incrementally. |
| LaTeX tipa package is unavailable on user's system | Low | Medium | Document required packages. Provide a fallback: Unicode IPA in monospace font. |
| Feature creep (allophony,	morphology, historical sim) | High | High | Strict MVP scope. Post-MVP features are documented but not started until MVP ships. |
| panphon or external dependencies introduce maintenance burden | Medium | Low | Core engine has zero deps by design. Any dependencies introduce optional dep is isolated to a utility module. |
| English validation tests are too subjective | Medium | Medium | Define "English-like" precisely: SSP-compliant, correct cluster types, weighted frequencies. Don't require native speaker judgement.

## Open Questions

- Feature representation: Should phoneme features use a fixed enum (e.g., PlaceOfArticulation.VELAR) or free-form strings? Enums are safer but inflexible; strings are flexible but error-prone. [?]

- Constraint DSL: Should phonotactic constraints be Python callables (powerful, requires coding) or a declarative mini-language (accessible, limited)? MVP likely needs only built-in constraints; a DSL is post-MVP. [?]

- panphon integration: Depend on it for feature validation, or maintain our own lightweight feature set? Trade-off: correctness vs. zero-dependency principle. [?]

- GUI state management: Simple MVC, or a proper reactive framework? PySide6 has signals/slots (observer pattern) built in — likely sufficient for MVP. [?]

- Multi-dialect English: Which dialect to model for the test language? Received Pronunciation (RP) is cleaner; General American is more widely recognized. [?] — Suggest GA for recognition, RP for simplicity.

- Syllable boundary detection: Do we need to syllabify generated words (insert . between syllables), or just generate syllable sequences? Syllabification is complex but useful for display. [?]

- Reproducibility: Should generation support a --seed flag for deterministic output? Likely yes — essential for testing. [?]

- MyST dollarmath in docs: Currently disabled in conf.py. Enabling it would allow $...$ LaTeX math in documentation. Should we enable it for IPA notation, or stick with literal Unicode IPA in backticks? [?]




## Decisions Log

| Date | Decision | Context / Rationale |
| --- | --- | --- |
| 2026-04-03 | Switched license from CC-BY-SA-4.0 to GPL-3.0-or-later | Software, not content — GPL is appropriate.
| 2026-04-03 | Adopted src/ layout for package | Standard practice; prevents import shadowing |
| 2026-04-03 | Added [project.optional-dependencies] for RTD | Poetry groups are invisible to pip; RTD needs PEP 621 extras. |
| 2026-04-03 | Pinned sphinx <9.0 in extras	| RTD pulled 9.1.0 which broke extensions. |
| 2026-04-03 | Removed pytest and ruff from .readthedocs.yaml | RTD only needs docs extras, not dev tools. |
| 2026-04-03 | Suppressed E501 in conf.py via ruff config | Sphinx config files routinely exceed 88ch. |
| 2026-04-04 | Chose PySide6 over PyQt6	LGPL licensing | Shared expertise. |
| 2026-04-04 | LaTeX is export-only, not a data format | Avoid parsing complexity; JSON/YAML is canonical. |
| 2026-04-04 | English as validation language | Well-documented phonology; exercises most engine features (clusters, s-appendix, SSP). |
| 2026-04-04 | Core layer is zero-dependency | Testability and headless operation. |
| 2026-04-04 | Live preview is a core differentiator | No competing tool offers this. Competitive advantage. |

---

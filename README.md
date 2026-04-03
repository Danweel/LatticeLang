# LatticeLang - Conglang Toolset

LatticeLang is a libre, open-source tool for constructing natural-sounding languages. Unlike traditional generators, it incorporates **[Sonority Hierarchy](https://en.wikipedia.org/wiki/Sonority_hierarchy)**, and other '[linguistic universals](https://en.wikipedia.org/wiki/Linguistic_universal)' (more precisely, tendencies) by default, while still offering customization for less-ethnocentric rules, and support for experimental/alien languages.

[![Docs Build](https://github.com/Danweel/LatticeLang/actions/workflows/docs-build.yml/badge.svg)](https://github.com/Danweel/LatticeLang/actions/workflows/docs-build.yml)

[![Read the Docs](https://readthedocs.org/projects/latticelang/badge/?version=latest)](https://latticelang.readthedocs.io/)

[![Deploy to Pages](https://github.com/Danweel/LatticeLang/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Danweel/LatticeLang/actions/workflows/deploy-pages.yml)

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.
See [LICENSE](LICENSE) for details.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Features

- **Sonority-aware generation**: Default weights based on cross-linguistic averages. Edit them to your liking.
- **Editable phonotactic distributions**: CVC patterns and weights are editable but also feature preset drag-and-drop clusters for simpler languages.
- **Transliteration engine**: Conversion and simultaenious support of IPA and 'readable' scripts.
- **Project-based workflow**: Manage multiple conlangs and reuse workflows with shared templates.
- **Three tier interface**: Simple, Builder, and Power modes to accommodate different Conlanger needs.
- **Libre & Open**: Built with Python and customtkinter (common GUI), licensed under GPL-3.0.
- **Extensibility**: Conceived with the ground-up to welcome additional functionality from the community in the form of plugins and contributions.
- **Font options**: Comes packaged with v7 SIL fonts (Andika, Charis, Dolous, Gentium), Junicode 2, STIX 2, Liberation 2, Liguistics Pro (from the LinguaFranca>Heuristica>Utopia lineage), Open Sans (from the Noto>Droid Sans lineage), and GNU FreeFont to include a monospace character set, covering a wide variety of style options with near-total character coverage and encodings (Type 1, Open, TrueType, WOFF, etc.).
- **Documentation**: Documentation and guidance from day one as the program develops.
- **Get involved!**: Found an issue? Know how to fix a bug? Have code that could be useful to the project? See CONTRIBUTING.md for guidelines!


## Quick Start

### Ubuntu & Debian **Users**
```bash
pip install latticelang
latticelang
```

### Windows **Users**


### MacOS **Users**

## Documentation
Full documentation is available at [latticelang.readthedocs.io](latticelang.readthedocs.io).

- User Guide: Installation, configuration, and usage tutorials
- Contributing: How to contribute code or documentation
- API Reference: Technical details for developers


## Setting up for Contributors
We welcome contributions!

### Types of Contributions
- Documentation: Improve tutorials, fix typos, add examples (no Python setup required)
- Code: Fix bugs, add features, improve performance, etc.
- Testing: Write unit tests, report bugs

### Guidelines
- CONTRIBUTING.md
- Docs links

### Quickstart for development (Setup Script)
#### For Linux Ubuntu and Debian:
1. Git clone or download the Github zip file
2. Run the bootstrap script to set up your environment:
```bash
./setupenvironment.sh
```

#### For Windows
?

#### For MacOS
?

### Manual Setup (Clone and Install)
**Recommended: Use Poetry for dependency management**
### Setting up for contribution
#### For Linux Ubuntu and Debian:
```
git clone https://github.com/danweel/latticelang.git
cd latticelang

poetry install --with dev
poetry run latticelang
```
#### For Windows
?

#### For MacOS
?

### Quick Start for contributing to the docs

#### For Linux Ubuntu and Debian:
1. Git clone or download the Github zip file
2. Run the bootstrap script to set up your environment:
```bash
./setupthedocs.sh
```

or manually:
```bash
poetry install --with docs
```

I recommend using [VSCodium](https://vscodium.com/) if you are new to contributing. If you do, use the following to obtain recommended extensions for the project:
(put here extensions quick link)

### Prerequisites (these will be checked for and installed by the bootstrap)
- Python 3.9+
- Poetry
- TBD




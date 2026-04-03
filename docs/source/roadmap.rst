Roadmap
=======

LatticeLang is actively developed with a focus on accessibility and modularity.
This roadmap outlines planned features and milestones.

Current Phase: Alpha
--------------------

**Status:** Core architecture established, basic functionality working

Completed
~~~~~~~~~

- [x] Project structure and Poetry setup
- [x] Basic phonology module
- [x] Syllable structure validation
- [x] Word generation engine
- [x] YAML configuration support
- [x] Sphinx documentation framework
- [x] CI/CD pipeline setup

In Progress
~~~~~~~~~~~

- [ ] Complete API documentation
- [ ] CLI interface refinement
- [ ] Font rendering preview tools
- [ ] Example language configurations

Planned Features
----------------

Phase 1: Core Enhancement (Q2-Q3 2026)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- [ ] Morphology module (prefixes, suffixes, infixes)
- [ ] Orthography mapper with Unicode support
- [ ] Phonotactic constraint editor (GUI)
- [ ] Export formats: IPA, ASCII, custom orthographies
- [ ] Language comparison tools

Phase 2: Collaboration (Q4 2026)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- [ ] Multi-user project sharing
- [ ] Version control integration for language designs
- [ ] Community template library
- [ ] Plugin system for custom generators

Phase 3: Advanced Features (2027+)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- [ ] Statistical analysis of phoneme distributions
- [ ] Historical linguistics simulation (sound changes)
- [ ] Integration with conlang communities (Conlang.org, Reddit)
- [ ] Mobile companion app

Out of Scope
------------

LatticeLang intentionally excludes certain features to remain focused and accessible:

- **Full linguistic database** — Unlike SIL FieldWorks, we don't aim to be a complete
  field linguistics suite. We focus on conlang creation, not documentation of endangered
  languages in professional contexts.

- **Enterprise features** — No multi-tenant architecture, enterprise SSO, or commercial
  licensing. This is a community-driven open source project.

- **Heavy GUI dependencies** — While we may add a basic GUI, the core remains CLI-first
  for maximum portability and scriptability.

Positioning
-----------

LatticeLang sits between hobbyist conlang tools and professional linguistics suites:

+------------------+------------------+------------------+------------------+
| Feature          | Hobbyist Tools   | LatticeLang      | SIL FieldWorks   |
+==================+==================+==================+==================+
| Target Audience  | Casual conlangers| Serious conlangers| Professional    |
|                  |                  |                  | linguists        |
+------------------+------------------+------------------+------------------+
| Learning Curve   | Low              | Moderate         | High             |
+------------------+------------------+------------------+------------------+
| Extensibility    | Limited          | High (plugins)   | Very High        |
+------------------+------------------+------------------+------------------+
| Cost             | Free/Paid        | Free (FOSS)      | Free (inst.)     |
+------------------+------------------+------------------+------------------+
| Primary Use Case | Fun/Experiment   | Naturalistic     | Field docs       |
|                  |                  | conlangs         |                  |
+------------------+------------------+------------------+------------------+

We aim to provide enough power for serious conlang projects without the overhead
of professional-grade tooling.

.. note::
   This roadmap is subject to change based on community feedback and contributor availability.
   
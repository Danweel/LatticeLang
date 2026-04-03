Usage Guide
===========

Command Line Interface
----------------------

LatticeLang provides a CLI for generating words and managing phonologies:

.. code-block:: bash

   # Generate random words
   poetry run latticelang generate --count 10

   # Export phonology to YAML
   poetry run latticelang export phonology --format yaml

   # Preview font rendering
   poetry run latticelang preview --font Junicode

Configuration
-------------

LatticeLang uses YAML configuration files for phonology, morphology, and syllable structure.

Example ``phonology.yaml``:

.. code-block:: yaml

   consonants:
     plosives: [p, b, t, d, k, g]
     nasals: [m, n, ŋ]
     fricatives: [f, v, s, z]

   vowels:
     short: [i, e, a, o, u]
     long: [iː, eː, aː, oː, uː]

See the ``examples/`` directory for complete configuration templates.

Modules
-------

LatticeLang is organized into several core modules:

- **phonology** — Phoneme inventory and rules
- **syllable** — Syllable structure and constraints
- **generator** — Word generation algorithms
- **mapper** — Orthography mapping
- **validators** — Constraint validation

Each module is documented in the :doc:`api` section.

.. note::
   This guide will expand with tutorials and examples as the project matures.
   
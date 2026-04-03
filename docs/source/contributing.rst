Contributing
============

We welcome contributions from the conlanging and open source communities!

Getting Started
---------------

1. Fork the repository on GitHub
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/YOUR_USERNAME/LatticeLang.git
      cd LatticeLang

3. Set up your development environment:

   .. code-block:: bash

      poetry install --with dev,docs

4. Create a branch for your changes:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

Coding Standards
----------------

- Follow PEP 8 style guidelines
- Use type hints where possible
- Write docstrings for all public functions and classes
- Include tests for new functionality

Testing
-------

Run the test suite:

.. code-block:: bash

   poetry run pytest

Documentation
-------------

Build the documentation locally:

.. code-block:: bash

   cd docs
   poetry run make html

Submit Changes
--------------

1. Commit your changes with clear, descriptive messages
2. Push to your fork
3. Open a Pull Request on GitHub

Code of Conduct
---------------

This project follows the Contributor Covenant Code of Conduct. Please be respectful
and inclusive in all interactions.

.. note::
   For detailed contribution guidelines, see ``CONTRIBUTING.md`` in the repository root.
   
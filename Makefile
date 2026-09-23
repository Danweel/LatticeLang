SPHINXOPTS ?=

.PHONY: docs docs-live docs-clean help

help:
	@echo "docs       - build HTML docs via Poetry env"
	@echo "docs-live  - rebuild on save, serve at localhost:8000"
	@echo "docs-clean - remove docs/_build"

docs:
	poetry run sphinx-build -b html $(SPHINXOPTS) docs/source docs/_build/html

docs-live:
	poetry run sphinx-autobuild docs/source docs/_build/html

docs-clean:
	rm -rf docs/_build
# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# ----------------------------------------------------------------------------


# -- Project information -----------------------------------------------------

project = 'LatticeLang'
copyright = '2026, Daniil Woodland'
author = 'Danweel'
release = '0.0.1'

# ----------------------------------------------------------------------------


# -- General configuration ---------------------------------------------------

templates_path = ['_templates']
html_static_path = ['_static']

root_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
    'sphinx.ext.autodoc',          # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',         # Google/NumPy docstring support
    'sphinx.ext.viewcode',         # Source code links for documented objects
    'sphinx.ext.intersphinx',      # Cross-reference other Sphinx docs
    'sphinx.ext.todo',             # Inline .. todo:: directives
    'sphinxcontrib.mermaid',       # Text-based diagrams
    'notfound.extension',          # Custom 404 page
    'sphinx_copybutton',           # Copy button on code blocks
    'sphinx_design',               # Cards, tabs, panels
    'sphinx_togglebutton',         # Collapsible content
    'myst_parser',                 # Markdown support
    'sphinxcontrib.bibtex',        # Bibliography citations
]

# ----------------------------------------------------------------------------


# -- Autodoc -----------------------------------------------------------------

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# ----------------------------------------------------------------------------


# -- InterSphinx -------------------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'Sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# ----------------------------------------------------------------------------


# -- Todo extension ----------------------------------------------------------

todo_include_todos = True

# ----------------------------------------------------------------------------


# -- 404 Not Found -----------------------------------------------------------

notfound_template = '404.html'

notfound_context = {
    'title': 'Page Not Found',
    'body': 'The page you are looking for does not exist.',
}

notfound_urls_prefix = '/en/latest/'

# ----------------------------------------------------------------------------


# -- Mermaid -----------------------------------------------------------------

mermaid_version = '11.13.0'

mermaid_init_js = "mermaid.initialize({startOnLoad:true});"

# ----------------------------------------------------------------------------


# -- MyST Configuration -----------------------------------------------------

myst_enable_extensions = [
    'colon_fence',      # Use ::: for directives
    'deflist',          # Definition lists
    'dollarmath',       # LaTeX math syntax (Q30)
    'html_admonition',  # HTML admonitions
    'linkify',          # Auto-link URLs
]

myst_heading_anchors = 4  # Add anchors to headings up to level 4

# ----------------------------------------------------------------------------


# -- BibTeX ------------------------------------------------------------------

bibtex_bibfiles = ["research/refs.bib"]

# ----------------------------------------------------------------------------


# -- HTML output -------------------------------------------------------------

html_theme = 'furo'

# html_logo = "_static/logo.png"

# html_theme_options = {
#    "light_css_variables": {
#        "color-brand-primary": "#6d4aff",
#        "color-brand-content": "#6d4aff",
#    },
#    "dark_css_variables": {
#        "color-brand-primary": "#6d4aff",
#        "color-brand-content": "#6d4aff",
#    },
# }

# ----------------------------------------------------------------------------
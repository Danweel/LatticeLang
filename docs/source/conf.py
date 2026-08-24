# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# ----------------------------------------------------------------------------


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LatticeLang'
copyright = '2026, Daniil Woodland'
author = 'Danweel'
release = '0.0.1'

# ----------------------------------------------------------------------------


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']

root_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_troubleshooting/*.rst']

#

extensions = [
    'sphinx.ext.viewcode',         # Shows source code links for documented Python objects
    'sphinx.ext.intersphinx',      # Cross-reference other Sphinx docs
    'sphinx.ext.todo',             # Inline .. todo:: directives
    'sphinxcontrib.mermaid',       # Text-based diagrams
    'sphinx.ext.autodoc',          # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',         # Google/NumPy docstring support
    'notfound.extension',          # Custom 404 page
    'sphinx_copybutton',           # Copy button on code blocks
    'sphinx_design',               # Cards, tabs, panels — uncomment if needed
    'myst_parser'                  # Markdown support
]                                  # KNOWN ISSUE: myst_parser is in an odd format. This is normal but can throw warnings (that can be safely ignored)

# --------------------------------------------------------------------------


# -- Options for Viewcode --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html

viewcode_line_numbers = True
# viewcode_find_source(app, modname)  # not sure we can use this. check.

# --------------------------------------------------------------------------


# -- Options for AutoDoc --------------------------------------------------
# Auto-generate docs from your module
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Options for InterSphinx -----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'Sphinx': ('https://www.sphinx-doc.org/en/master/', None)
    # ... other mappings
}

# ---------------------------------------------------------------------------


# -- Options for todo extension ---------------------------------------------

todo_include_todos = True

# ---------------------------------------------------------------------------


# -- 404 Not Found customization --------------------------------------------
# https://sphinx-notfound-page.readthedocs.io/en/latest/

notfound_template = '404.html' # Optional: Explicitly set the 404 template if needed (usually automatic)

notfound_context = {
    'title': 'Page Not Found',
    'body': 'The page you are looking for does not exist.',
}
# Optional: add URLs that should always work
notfound_urls_prefix = '/en/latest/'  # For versioned docs

# ---------------------------------------------------------------------------


# -- 'Sphinx Contrib for Mermaid' Template ----------------------------------
# https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/index.html
# Mermaid allows for text-based charts that are more versionable than images

mermaid_version = '11.13.0'  # Pinning Mermaid JS version to ensure build stability.
# Update this version only after testing with the new Mermaid release.

mermaid_init_js = "mermaid.initialize({startOnLoad:true});"
# mermaid_params = ['--theme', 'forest', '--width', '600', '--backgroundColor', 'transparent']

# --------------------------------------------------------------------------


# -- MyST Configuration ----------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

myst_enable_extensions = [
    'colon_fence',      # Use ::: for directives
    'deflist',          # Definition lists
    'dollarmath',       # LaTeX math syntax
    'html_admonition',  # HTML admonitions
    'gfm_autolink',     # Auto-link URLs
]

# Optional: Configure how MyST handles certain syntax
myst_heading_anchors = 4  # Add anchors to headings up to level 3

# --------------------------------------------------------------------------


# -- Options for HTML output ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

# html_logo = "logo.png"

# html_theme_options = {
#    "light_css_variables": {
#        "color-brand-primary": "red",
#        "color-brand-content": "#CC3333",
#        "color-admonition-background": "orange",
#    },
#    "dark_css_variables": {
#        "color-brand-primary": "red",
#        "color-brand-content": "#CC3333",
#        "color-admonition-background": "orange",
#    },
# }

# ---------------------------------------------------------------------------

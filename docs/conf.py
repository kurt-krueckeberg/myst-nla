# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bückeburg Archive Case Files'
copyright = '2025, Kurt Krueckeberg'
author = 'Kurt Krueckeberg'
release = '0.9'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
 "myst_parser",
 "sphinx_design",
 "sphinx_copybutton",
 "sphinxcontrib.bibtex",
]

myst_enable_extensions = [
    "colon_fence", "deflist", "attrs_block", "attrs_inline",
    "substitution", "linkify"
] 

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# -- Theme ------------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = "Krückeberg Archive"          # shown in the header
html_logo = "_static/logo.png"             # optional
html_favicon = "_static/favicon.ico"       # optional

html_theme_options = {
    # Navigation
    "repository_url": "https://example.com/your/repo",  # optional
    "use_repository_button": True,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "use_download_button": True,        # page download dropdown
    "path_to_docs": "docs",             # if your conf.py is in docs/
    "show_navbar_depth": 2,             # how deep the left ToC shows
    # Table of contents pane
    "toc_title": "Contents",
    "use_sidenotes": False,             # footnotes as sidenotes if True
    # Appearance
    "logo_only": False,
    "home_page_in_toc": True,
}

# -- Static assets (for your custom CSS/JS) ---------------------
html_static_path = ["_static"]
html_css_files = ["kurt-customizations.css"]  # optional

# -- LaTeX/PDF (optional) --------------------------------------
latex_engine = "xelatex"
latex_elements = {
    "preamble": r"""
\usepackage{fontspec}
\usepackage{csquotes}
""",
}

# -- Misc -------------------------------------------------------
templates_path = ["_templates"]
exclude_patterns = ["_build"]

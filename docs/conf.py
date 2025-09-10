# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Schaumburg-Lippe Cammer case files'
copyright = '2025, Kurt Krückeberg'
author = 'Kurt Krückeberg'
release = '.9'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']

# -- Extensions ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

myst_enable_extensions = [
    "colon_fence", "deflist", "attrs_block", "attrs_inline",
    "substitution", "linkify",
]

# -- Theme --------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_toc_level": 2,      # right-hand on-page ToC depth
}
html_static_path = ["_static"]       # created by quickstart
html_css_files = ["kurt-customizations.css"]  

# -- General ------------------------------------------------------
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



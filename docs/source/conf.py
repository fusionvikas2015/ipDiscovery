# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'ipDiscovery'
copyright = '2025, Vikas Kumar'
author = 'Vikas Kumar'
release = 'v1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_theme_options = {
#     "collapse_navigation": False,
#     "sticky_navigation": True,
#     "navigation_depth": 2,
# }

html_context = {
    "display_github": True,  # Integrates GitHub link
    "github_user": "fusionvikas2015",
    "github_repo": "ipDiscovery",
    "github_version": "main",  # or the appropriate branch
    "conf_py_path": "/docs/",  # path in the repo to your docs root
}

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

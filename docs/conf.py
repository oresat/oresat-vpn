"""Configuration file for the Sphinx documentation builder."""

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

__VERSION_MAJOR__ = 0
__VERSION_MINOR__ = 0
__VERSION_PATCH__ = 1
__version__ = f"{__VERSION_MAJOR__}.{__VERSION_MINOR__}.{__VERSION_PATCH__}"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OreSat VPN Docs"
copyright = (
    f"{datetime.now().year}, Portland State Aerospace Society"  # pylint: disable=W0622
)
author = "PSAS"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]
templates_path: list = []
exclude_patterns: list = []
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["static"]
html_css_files = ["custom.css"]

# -- Others Options ----------------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# To add links to stand python type definitions.
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# import pathlib
# import sys
# sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example-python-package'
copyright = '2024, Kyle M. Hart'
author = 'Kyle M. Hart'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Automatically builds documentation from docstrings.
    "sphinx.ext.autodoc",
    # Links to other package documentation.
    "sphinx.ext.intersphinx",
    # Converts NumPy-style docstrings to Sphinx.
    "sphinx.ext.napoleon",
    # Enables the ability to view source code.
    "sphinx.ext.viewcode",
]

# Puts types in the signature and details.
autodoc_typehints = "both"
# Show the full module name.
autodoc_typehints_format = "fully-qualified"
# Allow reference to Python documentation.
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
# Change some backend settings so that Return types vs Return descriptions work
# correctly.
napoleon_use_rtype = False
# When showing source code, show line numbers.
viewcode_line_numbers = True

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use a different theme.
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

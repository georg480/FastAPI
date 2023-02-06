# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "FastAPI"
copyright = "2023, Georg Dahmen"
author = "Georg Dahmen"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# import os

# sys.path.insert(0, os.path.abspath("../../"))
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
# extensions = ["sphinx.ext.autodoc",
#             "sphinx.ext.napoleon",
#            ]
# extensions = [
#   'sphinx.ext.duration',
#  'sphinx.ext.doctest',#'sphinxcontrib.napoleon',
# ]

templates_path = ["_templates"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

# language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # "alabaster"
html_static_path = ["_static"]

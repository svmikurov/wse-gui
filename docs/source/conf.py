# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../../src/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WSE-GUI'
copyright = '2025, Sergei Mikurov'
author = 'Sergei Mikurov'
release = '0.3.0'

# -- GitHub information ------------------------------------------------
github_user = 'svmikurov'
github_repo_name = 'wse-gui'
github_version = 'dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Include documentation from docstrings
    # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc
    'sphinx.ext.autodoc',
    # Add copy button from block
    # https://sphinx-copybutton.readthedocs.io/en/latest/#sphinx-copybutton
    'sphinx_copybutton',
    # Allow reference sections using its title
    # https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#module-sphinx.ext.autosectionlabel
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_module_names
add_module_names = False
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
autodoc_default_options = {
    'show-inheritance': True,
}
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
todo_include_todos = True
todo_link_only = True

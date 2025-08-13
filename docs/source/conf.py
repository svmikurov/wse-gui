# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WSE GUI'
copyright = '2025, Sergey Mikurov'
author = 'Sergey Mikurov'
release = '0.4.0'

SRC_PATH = Path(__file__).parents[2] / 'src'
print(f'----------------------------------------------------')
print(f'{SRC_PATH = }')
print(f'----------------------------------------------------')
sys.path.insert(0, SRC_PATH.resolve().as_posix())

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    # Allow reference sections using its title
    # https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#module-sphinx.ext.autosectionlabel
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns: list[str] = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

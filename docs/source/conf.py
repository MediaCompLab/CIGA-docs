# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# 修复路径：添加包含ciga包的父目录
sys.path.insert(0, os.path.abspath('..'))

import ciga.analysis.graph_centrality_analysis
import ciga.analysis.graph_community_analysis
import ciga.analysis.tgraph_centrality_analysis
import ciga.analysis.tgraph_community_analysis
import ciga.analysis.graph_properties
import ciga.analysis.tgraph_properties

import ciga.visualization.graph_plotter

import ciga.utils.data_utils
import ciga.utils.graph_utils

import ciga.ciga

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CIGA'
copyright = '2025, Shu Hu'
author = 'Shu Hu'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 添加必要的sphinx扩展
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # 支持Google和NumPy风格的docstring
    'sphinx_rtd_theme',
]

# autodoc配置
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

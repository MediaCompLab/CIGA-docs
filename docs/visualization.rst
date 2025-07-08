Visualization (:py:mod:`ciga`)
=================================================

This module provides interactive graph visualization capabilities using modern web technologies for both static and temporal graphs.

Functions
--------

.. currentmodule:: ciga
.. autofunction:: iplot

.. currentmodule:: ciga
.. autofunction:: pyviz

Dependencies
------------
**Python**: `pandas <https://pandas.pydata.org/>`_, `numpy <https://numpy.org/>`_, `igraph <https://igraph.org/python/>`_ library

**Web**: `vis.js <https://visjs.org/>`_, `tom-select <https://tom-select.js.org/>`_ for interactive components

Usage
--------
Interactive graph plotting

.. literalinclude:: ../ciga/examples/plot_graph.py
    :language: python

The visualization module generates HTML files with interactive graph displays that can be opened in any modern web browser. Features include:

- Node and edge interaction
- Zoom and pan capabilities  
- Layout algorithms
- Temporal graph animation
- Custom styling options 
Graph (:py:mod:`ciga`)
=================================================

This module provides the core TGraph class for managing and analyzing temporal graphs using the igraph library. It enables efficient handling of time-based social interaction data.

Classes
--------

.. currentmodule:: ciga
.. autoclass:: TGraph
   :members:

Dependencies
------------
**Python**: `igraph <https://igraph.org/python/>`_, `pandas <https://pandas.pydata.org/>`_, `numpy <https://numpy.org/>`_ library

Usage
--------
Create and manipulate a temporal graph

.. literalinclude:: ../ciga/examples/analysis.py
    :language: python
    :lines: 25-40

Plot a graph

.. literalinclude:: ../ciga/examples/plot_graph.py
    :language: python 
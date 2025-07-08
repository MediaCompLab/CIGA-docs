Analysis (:py:mod:`ciga`)
=================================================

This module provides comprehensive graph analysis functions including centrality measures, community detection, and graph properties for both static and temporal graphs.

Centrality Analysis
------------------

Static Graph Centrality
~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: ciga
.. autofunction:: graph_degree

.. currentmodule:: ciga
.. autofunction:: graph_betweenness

.. currentmodule:: ciga
.. autofunction:: graph_closeness

.. currentmodule:: ciga
.. autofunction:: graph_eigenvector_centrality

Temporal Graph Centrality
~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: ciga
.. autofunction:: tgraph_degree

.. currentmodule:: ciga
.. autofunction:: tgraph_betweenness

.. currentmodule:: ciga
.. autofunction:: tgraph_closeness

.. currentmodule:: ciga
.. autofunction:: tgraph_eigenvector_centrality

Community Detection
------------------

.. currentmodule:: ciga
.. autofunction:: graph_community_leiden

.. currentmodule:: ciga
.. autofunction:: tgraph_community_leiden

Graph Properties
---------------

.. currentmodule:: ciga
.. autofunction:: graph_density

.. currentmodule:: ciga
.. autofunction:: graph_transitivity_undirected

.. currentmodule:: ciga
.. autofunction:: tgraph_density

.. currentmodule:: ciga
.. autofunction:: tgraph_transitivity_undirected

Dependencies
------------
**Python**: `igraph <https://igraph.org/python/>`_, `pandas <https://pandas.pydata.org/>`_, `numpy <https://numpy.org/>`_ library

Usage
--------
Centrality analysis

.. literalinclude:: ../ciga/examples/centrality_analysis.py
    :language: python

Community detection

.. literalinclude:: ../ciga/examples/community_detection.py
    :language: python

Non-accumulated centrality analysis

.. literalinclude:: ../ciga/examples/non_acc_centrality_analysis.py
    :language: python 
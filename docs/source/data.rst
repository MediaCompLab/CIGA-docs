Data (:py:mod:`ciga`)
=================================================

This module provides functions for loading and saving data in various formats, including CSV, JSON, and Excel. It is designed to facilitate the import and export of social interaction data for analysis with CIGA.

Functions
--------

.. currentmodule:: ciga
.. autofunction:: prepare_data

.. currentmodule:: ciga
.. autofunction:: segment

.. currentmodule:: ciga
.. autofunction:: calculate_weights

.. currentmodule:: ciga
.. autofunction:: agg_weights

.. currentmodule:: ciga
.. autofunction:: infer_listeners

Dependencies
------------
**Python**: `pandas <https://pandas.pydata.org/>`_, `numpy <https://numpy.org/>`_ library

Usage
--------
Prepare data

.. literalinclude:: ../ciga/examples/analysis.py
    :language: python
    :lines: 1-22

Infer listeners

.. literalinclude:: ../ciga/examples/infer_listeners.py
    :language: python


Tutorials
=========

This section provides step-by-step tutorials for using CIGA to analyze social interaction data.

Getting Started
--------------

Installation
~~~~~~~~~~~~

Install CIGA using pip::

    pip install ciga

Basic Workflow
~~~~~~~~~~~~~

1. **Prepare your data**: Ensure your data contains source, target, and timestamp columns
2. **Load and process**: Use CIGA's data preparation functions
3. **Create TGraph**: Initialize a temporal graph object
4. **Analyze**: Apply centrality measures, community detection, or property analysis
5. **Visualize**: Generate interactive plots of your results

Tutorial 1: Basic Analysis
--------------------------

This tutorial demonstrates how to load data, create a temporal graph, and perform basic analysis.

.. literalinclude:: ../ciga/examples/analysis.py
    :language: python

Tutorial 2: Centrality Analysis
------------------------------

Learn how to compute and analyze centrality measures over time.

.. literalinclude:: ../ciga/examples/centrality_analysis.py
    :language: python

Tutorial 3: Community Detection
------------------------------

Discover communities in your social network data.

.. literalinclude:: ../ciga/examples/community_detection.py
    :language: python

Tutorial 4: Interactive Visualization
------------------------------------

Create interactive plots for exploring your graph data.

.. literalinclude:: ../ciga/examples/plot_graph.py
    :language: python

Tutorial 5: Listener Inference
-----------------------------

Infer listeners from conversation data.

.. literalinclude:: ../ciga/examples/infer_listeners.py
    :language: python

Advanced Topics
--------------

Temporal Graph Analysis
~~~~~~~~~~~~~~~~~~~~~~

CIGA supports sophisticated temporal analysis including:

- Accumulative vs. snapshot analysis
- Weight normalization and inversion
- Fade functions for time-decay effects
- Multi-level temporal segmentation

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~

For large datasets:

- Use appropriate time segmentation
- Enable graph caching for repeated analysis
- Consider memory usage when setting accumulation parameters

Best Practices
--------------

1. **Data Quality**: Ensure your timestamp data is properly formatted
2. **Memory Management**: For large datasets, consider processing in chunks
3. **Validation**: Always validate your results with known patterns in your data
4. **Documentation**: Keep track of your analysis parameters for reproducibility 
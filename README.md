Use Landsat 8 data to test dimensionality reduction, clustering, and eventually clustering algorithms.

Done during Metis:
* Wrangle geospatial data using GDAL and GRASS.
* PCA to reduce channels 1 through 7 to three PCA components.
* Visualize false color maps in a plotly Dash app, including a PCA component map.
* Categorize pixels in GRASS.
* Gridsearch over hyperparameters in DBSCAN and Mean Shift algorithms to categorize pixels & compare results.
* Segment pixels in GRASS.
* Segment pixels in DBSCAN and Mean Shift and compare results.

Future:
* Collect training data on lava flow ages.
* Conduct regression on pixels or segments to estimate ages & compare to test data.
* Expect a major problem to be explaining the difference between windward (wet) and leeward (dry) weathering results.
* Explore whether a neural network with appropriate connection graph can address the windward / leeward problem and improve regression.

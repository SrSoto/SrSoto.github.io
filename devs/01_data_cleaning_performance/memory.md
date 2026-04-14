Acceleration on our transaction monitoring app for our automated Data Cleaning process (or data ingestion).

* **Starting point**: Python classes that caught a Pandas column, called `df[col].apply(...)` and used mostly `object` dtypes.
* **Ending point**: Inheritance on these classes for registering *extended Pandas Dtypes*, overwriting carefully vectorized methods using Cython so as to implement our logic as internally as possible.
* **Results**: 10x acceleration in our ingestion process, with considerable savings as we reduced AWS execution time.
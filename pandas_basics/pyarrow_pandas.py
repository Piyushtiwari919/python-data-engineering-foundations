import pandas as pd
import numpy as np

# Create a list of 1 million repeating strings
data = ["Pending", "Shipped", "Cancelled", "Refunded"] * 250_000

# 1. The Old Way (NumPy Object dtype)
classic_series = pd.Series(data, dtype="object")

# 2. The Modern Way (PyArrow String dtype)
arrow_series = pd.Series(data, dtype="string[pyarrow]")

# Measure memory deep inspection (in Megabytes)
# deep=True forces Pandas to actually weigh the scattered Python objects
classic_mb = classic_series.memory_usage(deep=True) / 1_000_000
arrow_mb = arrow_series.memory_usage(deep=True) / 1_000_000

print(f"NumPy 'object' Memory:  {classic_mb:.2f} MB")
print(f"PyArrow 'string' Memory: {arrow_mb:.2f} MB")
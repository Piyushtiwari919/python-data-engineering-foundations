import sys
import time
import numpy as np


# 1. THE MEMORY DIFFERENCE
# A raw Python integer takes 28 bytes of overhead!
py_num = 5
print(f"Size of one Python int: {sys.getsizeof(py_num)} bytes")

# A NumPy int32 takes exactly 4 bytes (32 bits). Zero overhead.
np_num = np.int32(5)
print(f"Size of one NumPy int32: {np_num.nbytes} bytes\n")


# 2. THE SPEED DIFFERENCE
size = 10_000_000

# Create a Python list and a NumPy array of 10 million numbers
python_list = list(range(size))
numpy_array = np.arange(size, dtype=np.int32)

# --- Python Benchmark ---
start = time.perf_counter()
# We must use a list comprehension to add 5 to every element
python_result = [x + 5 for x in python_list] 
end = time.perf_counter()
print(f"Python List Time:  {end - start:.4f} seconds")

# --- NumPy Benchmark ---
start = time.perf_counter()
# We use vectorization (broadcasting). The CPU rips through the contiguous block.
numpy_result = numpy_array + 5 
end = time.perf_counter()
print(f"NumPy Array Time: {end - start:.4f} seconds")
# 6. Analyze the performance benefits of NumPy arrays over Python lists for large-scale numerical operations.

import numpy as np
import timeit

# Size of the array
N = 10**6

# Create a large NumPy array
np_array = np.arange(N)

# Create a large Python list
py_list = list(range(N))

# Function to perform an operation using NumPy
def numpy_operation():
    return np_array * 2

# Function to perform an operation using Python lists
def list_operation():
    return [x * 2 for x in py_list]

# Timing the operations
numpy_time = timeit.timeit(numpy_operation, number=100)
list_time = timeit.timeit(list_operation, number=100)

print(f"NumPy operation time: {numpy_time:.5f} seconds")
print(f"Python list operation time: {list_time:.5f} seconds")

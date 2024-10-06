# 5. Define ndarrays in NumPy and explain their key features. How do they differ from standard Python lists?

import numpy as np

# Creating a 1D ndarray
ndarray_1d = np.array([1, 2, 3, 4, 5])

# Creating a standard Python list
list_1d = [1, 2, 3, 4, 5]

# Accessing an element
print("ndarray element:", ndarray_1d[2])  # Output: 3
print("list element:", list_1d[2])        # Output: 3

# Vectorized operation on ndarray
ndarray_squared = ndarray_1d ** 2
print("Squared ndarray:", ndarray_squared)  # Output: [ 1  4  9 16 25]

# Attempting the same with a list (requires a loop)
list_squared = [x ** 2 for x in list_1d]
print("Squared list:", list_squared)  # Output: [1, 4, 9, 16, 25]

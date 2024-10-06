# 1. Create a 3x3 NumPy array with random integers between 1 and 100. Then, interchange its rows and columns.

import numpy as np

# Create a 3x3 array with random integers between 1 and 100
array_3x3 = np.random.randint(1, 101, size=(3, 3))

print("Original 3x3 Array:")
print(array_3x3)

# Interchange rows and columns (transpose the array)
transposed_array = array_3x3.T

print("\nTransposed Array:")
print(transposed_array)

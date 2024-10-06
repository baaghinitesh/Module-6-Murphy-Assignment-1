# 7. Compare vstack() and hstack() functions in NumPy. Provide examples demonstrating their usage and output.

import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

# Stack vertically
vstacked = np.vstack((array1, array2))

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nVertically Stacked Array:")
print(vstacked)

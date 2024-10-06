# 2. Generate a ID NumPy array with 10 elements. Reshape it into a 2x5 array, then into a 5x2 array.

import numpy as np

# Generate an array with 10 elements
array_1d = np.arange(10)

print("Original 1D Array:")
print(array_1d)

# Reshape it into a 2x5 array
array_2x5 = array_1d.reshape(2, 5)
print("\nReshaped into 2x5 Array:")
print(array_2x5)

# Reshape it into a 5x2 array
array_5x2 = array_1d.reshape(5, 2)
print("\nReshaped into 5x2 Array:")
print(array_5x2)

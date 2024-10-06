# 3. Create a 4x4 NumPy array with random float values. Add a border of zeros around it, resulting in a 6x6 array.

import numpy as np

# Create a 4x4 array with random float values
array_4x4 = np.random.rand(4, 4)

print("Original 4x4 Array:")
print(array_4x4)

# Add a border of zeros around the array
array_with_border = np.pad(array_4x4, pad_width=1, mode='constant', constant_values=0)

print("\n6x6 Array with Border of Zeros:")
print(array_with_border)

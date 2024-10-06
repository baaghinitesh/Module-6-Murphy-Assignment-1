# 7. Create two 2D NumPy arrays and perform element-wise addition, subtraction, multiplication, and division.

import numpy as np

# Create two 2D NumPy arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

# Perform element-wise addition
addition = array1 + array2

# Perform element-wise subtraction
subtraction = array1 - array2

# Perform element-wise multiplication
multiplication = array1 * array2

# Perform element-wise division
division = array1 / array2

# Display the results
print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

print("\nElement-wise Addition:")
print(addition)

print("\nElement-wise Subtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(multiplication)

print("\nElement-wise Division:")
print(division)

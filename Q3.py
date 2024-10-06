# 3. Describe the methods for reversing a NumPy array along different axes. Provide examples for ID and 2D arrays.

# Reversing a 1D Array
# Method 1: Slicing
import numpy as np

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Reverse the array
reversed_arr_1d = arr_1d[::-1]

print("Original 1D Array:", arr_1d)
print("Reversed 1D Array:", reversed_arr_1d)

# Method 2: np.flip()
# Reverse the 1D array using np.flip
reversed_arr_1d_flip = np.flip(arr_1d)

print("Reversed 1D Array using np.flip:", reversed_arr_1d_flip)

# Reversing a 2D Array
# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Reverse the entire array
reversed_arr_2d = arr_2d[::-1, ::-1]

# Reverse the rows
reversed_rows = arr_2d[::-1]

# Reverse the columns
reversed_cols = arr_2d[:, ::-1]

print("Original 2D Array:\n", arr_2d)
print("Reversed 2D Array (both axes):\n", reversed_arr_2d)
print("Reversed Rows:\n", reversed_rows)
print("Reversed Columns:\n", reversed_cols)

# Method 2: np.flip()
# Reverse the 2D array using np.flip
reversed_arr_2d_flip = np.flip(arr_2d)  # Reverse all axes
reversed_rows_flip = np.flip(arr_2d, axis=0)  # Reverse rows
reversed_cols_flip = np.flip(arr_2d, axis=1)  # Reverse columns

print("Reversed 2D Array using np.flip (both axes):\n", reversed_arr_2d_flip)
print("Reversed Rows using np.flip:\n", reversed_rows_flip)
print("Reversed Columns using np.flip:\n", reversed_cols_flip)

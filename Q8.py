# 8. Explain the differences between fliplr() and flipud() methods in NumPy, including their effects on various array dimensions.

# Example of fliplr()
import numpy as np

# Create a 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Flip left to right
flipped_lr = np.fliplr(array_2d)

print("Original Array (2D):")
print(array_2d)
print("\nFlipped Left to Right:")
print(flipped_lr)

# Example of flipud()
# Create the same 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Flip upside down
flipped_ud = np.flipud(array_2d)

print("\nOriginal Array (2D):")
print(array_2d)
print("\nFlipped Upside Down:")
print(flipped_ud)

# Effects on Higher-Dimensional Arrays
# Example of fliplr()
# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])

# Flip last dimension (columns)
flipped_lr_3d = np.fliplr(array_3d)

print("\nOriginal 3D Array:")
print(array_3d)
print("\nFlipped Left to Right (3D):")
print(flipped_lr_3d)

# Example of flipud()
# Flip first dimension (slices)
flipped_ud_3d = np.flipud(array_3d)

print("\nFlipped Upside Down (3D):")
print(flipped_ud_3d)

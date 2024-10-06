# 9. Discuss the functionality of the array_split() method in NumPy. How does it handle uneven splits?

# Example of array_split()
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7])

# Split into 3 equal parts
split_arrays = np.array_split(array_1d, 3)

print("Original Array:")
print(array_1d)
print("\nSplit Arrays:")
for i, arr in enumerate(split_arrays):
    print(f"Part {i + 1}:", arr)

# Example of Uneven Splits
# Split a 1D array into 4 parts
array_1d = np.array([1, 2, 3, 4, 5, 6, 7])
split_arrays = np.array_split(array_1d, 4)

print("\nSplit Arrays (Uneven):")
for i, arr in enumerate(split_arrays):
    print(f"Part {i + 1}:", arr)

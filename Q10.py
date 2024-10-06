# 10. Explain the concepts of vectorization and broadcasting in NumPy. How do they contribute to efficient array operations?

# Example of Vectorization: 
import numpy as np

# Create two large arrays
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Vectorized addition
c = a + b  

# Example of Broadcasting: 
# Create a 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Create a 1D array (a vector)
vector = np.array([10, 20, 30])

# Broadcasting addition
result = matrix + vector  # The vector is broadcast across the rows of the matrix
print(result)


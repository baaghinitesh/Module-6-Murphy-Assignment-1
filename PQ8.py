# 8. Use NumPy to create a 5x5 identity matrix, then extract its diagonal elements.

import numpy as np

# Create a 5x5 identity matrix
identity_matrix = np.eye(5)

print("5x5 Identity Matrix:")
print(identity_matrix)

# Extract the diagonal elements
diagonal_elements = np.diagonal(identity_matrix)

print("\nDiagonal Elements:")
print(diagonal_elements)

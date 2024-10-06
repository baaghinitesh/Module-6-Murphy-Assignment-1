# 5. Create a NumPy array of strings ['python', 'numpy', 'pandas']. Apply different case transformations (uppercase, lowercase, title case, etc.) to each element.

import numpy as np

# Create a NumPy array of strings
array_strings = np.array(['python', 'numpy', 'pandas'])

# Apply different case transformations
uppercase = np.char.upper(array_strings)
lowercase = np.char.lower(array_strings)
titlecase = np.char.title(array_strings)
capitalize = np.char.capitalize(array_strings)

# Display the results
print("Original Array:")
print(array_strings)
print("\nUppercase:")
print(uppercase)
print("\nLowercase:")
print(lowercase)
print("\nTitle Case:")
print(titlecase)
print("\nCapitalized:")
print(capitalize)

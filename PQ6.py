# 6. Generate a NumPy array of words. Insert a space between each character of every word in the array.

import numpy as np

# Create a NumPy array of words
array_words = np.array(['hello', 'numpy', 'python', 'data'])

# Insert a space between each character of every word
spaced_words = np.char.join(' ', array_words)

# Display the result
print("Original Array of Words:")
print(array_words)
print("\nWords with Spaces Between Characters:")
print(spaced_words)

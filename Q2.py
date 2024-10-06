# 2. Compare and contrast np.mean() and np.average() functions in NumPy. When would you use one over the other?

import numpy as np

# Sample data
data = np.array([1, 2, 3, 4, 5])

# Using np.mean
mean_value = np.mean(data)  # This should give 3.0
print("Mean Value:", mean_value)

# Using np.average without weights
average_value = np.average(data)  # This should also give 3.0
print("Average Value (without weights):", average_value)

# Using np.average with weights
weights = np.array([1, 1, 1, 1, 5])  # Last element is more significant
weighted_average = np.average(data, weights=weights)  # This should give 4.0
print("Weighted Average:", weighted_average)


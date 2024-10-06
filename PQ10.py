# 10. Create a NumPy array representing daily temperatures for a month. Calculate and display the weekly averages.

import numpy as np

# Create a NumPy array representing daily temperatures for 30 days
daily_temperatures = np.random.randint(15, 31, size=30)

# Reshape the array into a 4-week format (4 weeks of 7 days, with 2 extra days)
weekly_temperatures = daily_temperatures[:28].reshape(4, 7)

# Calculate the weekly averages
weekly_averages = weekly_temperatures.mean(axis=1)

# Format the weekly averages to 3 decimal places
weekly_averages = np.round(weekly_averages, 3)

# Display the results
print("Daily Temperatures for 30 Days:")
print(daily_temperatures)
print("\nWeekly Averages (formatted to 3 decimal places):")
print(weekly_averages)

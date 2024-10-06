# 9. Generate a NumPy array of 100 random integers between 0 and 1000. Find and display all prime numbers in this array.

import numpy as np

# Generate a NumPy array of 100 random integers between 0 and 1000
random_integers = np.random.randint(0, 1000, size=100)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all prime numbers in the array and convert to a regular list
prime_numbers = list(map(int, [num for num in random_integers if is_prime(num)]))

# Display the results
print("Random Integers:")
print(random_integers)
print("\nPrime Numbers in the Array:")
print(prime_numbers)

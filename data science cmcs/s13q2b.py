import numpy as np

# Create a flattened array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Flatten the array
flat_arr = arr.flatten()

# Find the maximum and minimum values
max = np.max(flat_arr)
min = np.min(flat_arr)

# Print the results
print(f"Original Array:\n{arr}")
print(f"\nFlattened Array: {flat_arr}")
print(f"\nMaximum Value: {max}")
print(f"Minimum Value: {min}")

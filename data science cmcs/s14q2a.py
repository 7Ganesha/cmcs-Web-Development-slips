import numpy as np

# Create a flattened array
arr = np.array([1, 2, 3, 4, 5])

# Create weights
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# Compute the weighted average along the specified axis
weighted_average = np.average(arr, weights=weights)

# Print the result
print(f"Original Array: {arr}")
print(f"Weights: {weights}")
print(f"Weighted Average: {weighted_average}")

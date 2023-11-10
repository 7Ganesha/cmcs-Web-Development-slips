import pandas as pd

# Load SOCR-HeightWeight dataset (replace with the actual path)
heights_weights_data = pd.read_csv('SOCR-HeightWeight.csv')

# Display column-wise mean
mean_values = heights_weights_data.mean()
print("Column-wise Mean:")
print(mean_values)

# Display column-wise median
median_values = heights_weights_data.median()
print("\nColumn-wise Median:")
print(median_values)

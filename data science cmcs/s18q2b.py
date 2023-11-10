import pandas as pd

# Load heights and weights dataset
heights_weights_data = pd.read_csv('heights_weights.csv')

# Print the first 5 rows
print("First 5 Rows:")
print(heights_weights_data.head())

# Print the last 5 rows
print("\nLast 5 Rows:")
print(heights_weights_data.tail())

# Print 10 random rows
print("\nRandom 10 Rows:")
print(heights_weights_data.sample(10))

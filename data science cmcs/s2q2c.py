import pandas as pd

# Download heights and weights dataset from a given CSV file
# Replace 'heights_weights.csv' with the actual path or URL to your dataset
heights_weights_data = pd.read_csv('heights_weights.csv')

# Display the first 10 rows
print("First 10 rows:")
print(heights_weights_data.head(10))

# Display the last 10 rows
print("\nLast 10 rows:")
print(heights_weights_data.tail(10))

# Display random 20 rows
print("\nRandom 20 rows:")
print(heights_weights_data.sample(20))

# Display the shape of the dataset
print("\nDataset shape:")
print(heights_weights_data.shape)

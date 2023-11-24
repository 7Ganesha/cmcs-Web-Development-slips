import pandas as pd

# Load heights and weights dataset
df = pd.read_csv('heights_weights.csv')

# Print the first 5 rows
print("First 5 Rows:")
print(df.head())

# Print the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Print 10 random rows
print("\nRandom 10 Rows:")
print(df.sample(10))

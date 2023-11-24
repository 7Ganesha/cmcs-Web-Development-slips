import pandas as pd

df = pd.read_csv('heights_weights.csv')

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

print("\nRandom 20 rows:")
print(df.sample(20))

print("\nDataset shape:")
print(df.shape)
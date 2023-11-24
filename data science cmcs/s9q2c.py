import pandas as pd
df = pd.read_csv('winequality-red.csv')

# a) Describing the dataset
print(df.describe())

# b) Shape of the dataset
print(df.shape)

# c) Display first 3 rows from the dataset
print(df.head(3))

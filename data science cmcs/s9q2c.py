import pandas as pd

# Load winequality-red.csv (replace with the actual path)
wine_data = pd.read_csv('winequality-red.csv')

# a) Describing the dataset
print("Describing the dataset:")
print(wine_data.describe())

# b) Shape of the dataset
print("\nShape of the dataset:")
print(wine_data.shape)

# c) Display first 3 rows from the dataset
print("\nDisplaying first 3 rows from the dataset:")
print(wine_data.head(3))

import pandas as pd

# Load User_Data.csv (replace 'User_Data.csv' with the actual path or URL)
df = pd.read_csv('User_Data.csv')

# Print shape
print(f"Shape of the dataset: {df.shape}\n")

# Print number of rows and columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}\n")

# Print data types
print("Data types:")
print(df.dtypes)
print()

# Print feature names
print("Feature names:")
print(df.columns.tolist())
print()

# Print data description
print("Data description:")
print(df.describe())

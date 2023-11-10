import pandas as pd

# Load User_Data.csv (replace 'User_Data.csv' with the actual path or URL)
user_data = pd.read_csv('User_Data.csv')

# Print shape
print(f"Shape of the dataset: {user_data.shape}\n")

# Print number of rows and columns
print(f"Number of rows: {user_data.shape[0]}")
print(f"Number of columns: {user_data.shape[1]}\n")

# Print data types
print("Data types:")
print(user_data.dtypes)
print()

# Print feature names
print("Feature names:")
print(user_data.columns.tolist())
print()

# Print data description
print("Data description:")
print(user_data.describe())

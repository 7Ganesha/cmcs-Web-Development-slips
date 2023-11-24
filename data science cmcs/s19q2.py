import pandas as pd
import numpy as np

# 1. Create a DataFrame with columns name, age, and percentage
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack'],
    'age': [25, 28, 23, 30, 27, 29, 24, 26, 22, 31],
    'percentage': [75, 88, 92, 78, 95, 80, 87, 69, 91, 84]
}

df = pd.DataFrame(data)

# 2. Print shape, number of rows-columns, data types, feature names, and description
print("Data Frame Shape:", df.shape)
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))
print("Data Types:")
print(df.dtypes)
print("Feature Names:")
print(df.columns)
print("Description of the Data:")
print(df.describe())

# 3. Add 5 rows with duplicate values and missing values, and add a 'remarks' column
data_to_add = {
    'name': ['Ivy', 'Eve', 'Alice', 'Bob', 'Charlie'],
    'age': [22, np.nan, 25, 28, 23],
    'percentage': [91, 95, 75, np.nan, 92],
    'remarks': [None, None, None, None, None]
}

df = df.append(pd.DataFrame(data_to_add), ignore_index=True)

# Display the modified data
print("\nModified Data Frame:")
print(df)

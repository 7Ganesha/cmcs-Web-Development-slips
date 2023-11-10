import pandas as pd
import numpy as np

# Create a data frame
data = {
    'column_name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'salary': [50000, 60000, np.nan, 70000, 80000, 90000, 100000, np.nan, 120000, 130000],
    'department': ['HR', 'Finance', 'IT', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)

# Add 10 rows with some missing and duplicate values
additional_data = {
    'column_name': ['K', 'L', 'A', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
    'salary': [140000, 150000, 160000, np.nan, 180000, np.nan, 200000, 210000, np.nan, 230000],
    'department': ['IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR']
}

df = df.append(pd.DataFrame(additional_data), ignore_index=True)

# Print the original data frame
print("Original Data Frame:")
print(df)

# Drop null and empty values
df = df.dropna()

# Print the modified data frame
print("\nModified Data Frame (after dropping null and empty values):")
print(df)

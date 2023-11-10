import pandas as pd

# Load Data.csv
data = pd.read_csv('Data.csv')

# Replace missing values in the 'salary' and 'age' columns with the mean
data['salary'].fillna(data['salary'].mean(), inplace=True)
data['age'].fillna(data['age'].mean(), inplace=True)

# Save the modified data
data.to_csv('Data_no_missing.csv', index=False)

import pandas as pd

# Create a data frame containing columns name, age, salary, and department
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack'],
    'Age': [25, 28, 23, 30, 27, 29, 24, 26, 22, 31],
    'Salary': [60000, 70000, 55000, 75000, 65000, 80000, 60000, 72000, 58000, 78000],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)

# View the data frame
print("Data Frame:")
print(df)

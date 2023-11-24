import pandas as pd

# Create a DataFrame for students' information
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Graduation Percentage': [80.5, 90.0, 78.2, 85.3, 88.9],
    'Age': [22, 24, 23, 21, 25]
}

df = pd.DataFrame(data)

# Display average age of students
average_age = df['Age'].mean()
print(f"Average Age of Students: {average_age} years")

# Display average graduation percentage
average_percentage = df['Graduation Percentage'].mean()
print(f"Average Graduation Percentage: {average_percentage}%")

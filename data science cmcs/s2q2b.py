import pandas as pd
import matplotlib.pyplot as plt

# Load Data.csv
data = pd.read_csv('Data.csv')

# Generate a line plot of name vs salary
plt.plot(data['name'], data['salary'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Name vs Salary')
plt.xticks(rotation=90)
plt.show()
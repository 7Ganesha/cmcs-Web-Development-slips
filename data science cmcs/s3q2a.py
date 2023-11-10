import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load iris.csv dataset
iris_data = pd.read_csv('iris.csv')

# Create box plots for each feature across the three species
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal_length', data=iris_data)
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=iris_data)
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=iris_data)
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=iris_data)

plt.suptitle('Distribution of Iris Features Across Species')
plt.show()

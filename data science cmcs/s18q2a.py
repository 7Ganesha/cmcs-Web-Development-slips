import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load iris dataset
df = pd.read_csv('iris.csv')

# Create box plots to compare features across the three species
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal_length', data=df, palette='Set3')
plt.title('Sepal Length Distribution')
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=df, palette='Set3')
plt.title('Sepal Width Distribution')
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=df, palette='Set3')
plt.title('Petal Length Distribution')
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=df, palette='Set3')
plt.title('Petal Width Distribution')

plt.tight_layout()
plt.show()

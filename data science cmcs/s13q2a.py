import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load iris.csv dataset
df = pd.read_csv('iris.csv')

# Scatter plot to find the relationship between petal length and petal width
plt.figure(figsize=(8, 6))
sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species', palette='viridis', s=70)
plt.title('Relationship between Petal Length and Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.show()

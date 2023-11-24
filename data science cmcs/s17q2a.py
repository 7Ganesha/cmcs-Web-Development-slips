import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load iris dataset
df = pd.read_csv('iris.csv')

# Scatter plot to compare two features of the iris dataset
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species', palette='viridis', s=70)
plt.title('Comparison of Sepal Length and Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

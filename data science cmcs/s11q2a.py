import pandas as pd
import matplotlib.pyplot as plt

# Load Iris data
iris_data = pd.read_csv('iris.csv')

# Get the frequency of the three species
species_counts = iris_data['species'].value_counts()

# Create a pie plot
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Iris Species Distribution')
plt.show()

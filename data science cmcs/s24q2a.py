import pandas as pd
import matplotlib.pyplot as plt

# Load the iris.csv dataset
df = pd.read_csv('iris.csv')

# Get the frequency of the three species
species_counts = df['species'].value_counts()

# Create a bar plot to display the frequency
plt.bar(species_counts.index, species_counts.values, color=['blue', 'green', 'orange'])
plt.title('Frequency of Iris Species')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.show()

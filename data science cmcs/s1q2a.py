import pandas as pd
import matplotlib.pyplot as plt

# Load Iris data
df = pd.read_csv('Iris.csv')

# Get the frequency of the three species
species_counts = df['species'].value_counts()

# Create a pie plot
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Iris Species Distribution')
plt.show()

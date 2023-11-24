import pandas as pd
import matplotlib.pyplot as plt

# Load the iris.csv dataset
df = pd.read_csv('iris.csv')

# Create histograms for each species
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.hist(species_data['petal_length'], bins=20, alpha=0.5, label=species)

plt.title('Histogram of Petal Length for Iris Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load iris.csv dataset
iris_data = pd.read_csv('iris.csv')

# Create histograms for each species
plt.figure(figsize=(10, 6))
for species in iris_data['species'].unique():
    species_data = iris_data[iris_data['species'] == species]
    plt.hist(species_data['petal_length'], bins=20, alpha=0.5, label=species)

plt.title('Histogram of Petal Length for Iris Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

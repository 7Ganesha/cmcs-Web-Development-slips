import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
np.random.seed(42)
random_array = np.random.randint(1, 100, 50)

# Line chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(random_array, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# Scatter plot
plt.subplot(1, 2, 2)
plt.scatter(range(len(random_array)), random_array, color='green', marker='^')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

plt.tight_layout()
plt.show()

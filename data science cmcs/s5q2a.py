import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
np.random.seed(42)
random_array = np.random.randint(1, 100, 50)

# Line chart
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.plot(random_array, color='blue')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# Scatter plot
plt.subplot(1, 4, 2)
plt.scatter(range(len(random_array)), random_array, color='green')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

# Histogram
plt.subplot(1, 4, 3)
plt.hist(random_array, bins=15, color='orange', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Box plot
plt.subplot(1, 4, 4)
plt.boxplot(random_array, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='purple'))
plt.title('Box Plot')
plt.xlabel('Value')

plt.suptitle('Visualization of Random Array')
plt.tight_layout()
plt.show()

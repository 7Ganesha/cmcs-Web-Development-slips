import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
np.random.seed(42)
random_array = np.random.randint(1, 100, 50)

# Line chart
plt.subplot(2, 2, 1)
plt.plot(random_array, color='blue')
plt.title('Line Chart')

# Scatter plot
plt.subplot(2, 2, 2)
plt.scatter(range(len(random_array)), random_array, color='green')
plt.title('Scatter Plot')

# Histogram
plt.subplot(2, 2, 3)
plt.hist(random_array, bins=15, color='orange', edgecolor='black')
plt.title('Histogram')

# Box plot
plt.subplot(2, 2, 4)
plt.boxplot(random_array, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='purple'))
plt.title('Box Plot')

plt.suptitle('Visualization of Random Array')
plt.tight_layout()
plt.show()

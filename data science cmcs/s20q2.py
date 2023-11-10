import numpy as np
import matplotlib.pyplot as plt

# Part A: Generate a random array of 50 integers and display them using a line chart, scatter plot, histogram, and box plot.

# Generate a random array of 50 integers
np.random.seed(42)
random_array = np.random.randint(1, 100, 50)

# Create subplots to display the data in a line chart, scatter plot, histogram, and box plot
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Visualization of Random Array', fontsize=16)

# Line chart
axes[0, 0].plot(random_array, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
axes[0, 0].set_title('Line Chart')
axes[0, 0].set_xlabel('Index')
axes[0, 0].set_ylabel('Value')

# Scatter plot
axes[0, 1].scatter(range(len(random_array)), random_array, color='green', marker='^')
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('Index')
axes[0, 1].set_ylabel('Value')

# Histogram
axes[1, 0].hist(random_array, bins=15, color='orange', edgecolor='black')
axes[1, 0].set_title('Histogram')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

# Box plot
axes[1, 1].boxplot(random_array, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='purple'))
axes[1, 1].set_title('Box Plot')
axes[1, 1].set_xlabel('Value')

# Part B: Add two outliers to the random array and display the box plot with outliers.

# Add two outliers to the random array
random_array = np.append(random_array, [150, 160])

# Display the box plot with outliers
plt.figure(figsize=(6, 4))
plt.boxplot(random_array, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='purple'))
plt.title('Box Plot with Outliers')
plt.xlabel('Value')

plt.tight_layout()
plt.show()

import numpy as np

# Function to compute Manhattan distance between two points
def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

# Function to compute sum of Manhattan distance between all pairs of points
def sum_manhattan_distance(points):
    num_points = len(points)
    total_distance = 0

    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            total_distance += manhattan_distance(points[i], points[j])

    return total_distance

# Example points (replace with your dataset)
points = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Compute and print the sum of Manhattan distance
total_manhattan_distance = sum_manhattan_distance(points)
print(f"Sum of Manhattan Distance between all pairs of points: {total_manhattan_distance}")

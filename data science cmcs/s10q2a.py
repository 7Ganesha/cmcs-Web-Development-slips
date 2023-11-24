import pandas as pd

# Load SOCR-HeightWeight dataset (replace with the actual path)
df = pd.read_csv('SOCR-HeightWeight.csv')

# Display column-wise mean
mean= df.mean()
print("Column-wise Mean:")
print(mean)

# Display column-wise median
median = df.median()
print("\nColumn-wise Median:")
print(median)

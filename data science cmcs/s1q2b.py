import pandas as pd

# Load winequality-red data
df = pd.read_csv('exe.csv')

# View basic statistical details
print(df.describe())


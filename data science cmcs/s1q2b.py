import pandas as pd

# Load winequality-red data
wine_data = pd.read_csv('winequality-red.csv')

# View basic statistical details
basic_stats = wine_data.describe()
print(basic_stats)

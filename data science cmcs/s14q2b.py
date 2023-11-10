import pandas as pd

# Load advertising.csv dataset
advertising_data = pd.read_csv('advertising.csv')

# View basic statistical details of the data
basic_stats = advertising_data.describe()
print(basic_stats)

import pandas as pd

# Load Heights and Weights Dataset (replace 'heights_weights.csv' with the actual path or URL)
heights_weights_data = pd.read_csv('heights_weights.csv')

# View basic statistical details
basic_stats = heights_weights_data.describe()
print(basic_stats)

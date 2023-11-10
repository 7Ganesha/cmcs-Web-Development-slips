import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer

# Load the wine quality dataset
wine_data = pd.read_csv('winequality-red.csv')

# Extract the features (columns other than 'quality')
features = wine_data.drop('quality', axis=1)

# a. Rescaling (Min-Max Scaling)
min_max_scaler = MinMaxScaler()
rescaled_data = min_max_scaler.fit_transform(features)

# b. Standardizing Data (Z-score Standardization)
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(features)

# c. Binarizing Data (Using a binary threshold)
binarizer = Binarizer(threshold=0.5)
binarized_data = binarizer.transform(features)

# Print the first few rows of each transformed dataset
print("Rescaled Data:")
print(pd.DataFrame(rescaled_data, columns=features.columns).head())

print("\nStandardized Data:")
print(pd.DataFrame(standardized_data, columns=features.columns).head())

print("\nBinarized Data:")
print(pd.DataFrame(binarized_data, columns=features.columns).head())

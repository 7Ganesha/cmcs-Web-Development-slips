import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load winequality-red.csv (replace with the actual path)
wine_data = pd.read_csv('winequality-red.csv')

# Extract the features (excluding the target variable 'quality')
features = wine_data.drop('quality', axis=1)

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the features using the StandardScaler
standardized_features = scaler.fit_transform(features)

# Create a new DataFrame with the standardized features
standardized_data = pd.DataFrame(standardized_features, columns=features.columns)

# Add the 'quality' column back to the DataFrame
standardized_data['quality'] = wine_data['quality']

# Save the standardized data to a new CSV file
standardized_data.to_csv('winequality-red-standardized.csv', index=False)

# Display the first few rows of the standardized data
print("Standardized Data:")
print(standardized_data.head())

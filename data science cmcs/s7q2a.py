import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load Data.csv
data = pd.read_csv('Data.csv')

# OneHot encoding on 'Country' column
onehot_encoder = OneHotEncoder(sparse=False, drop='first')  # Drop the first column to avoid multicollinearity
country_encoded = pd.DataFrame(onehot_encoder.fit_transform(data[['Country']]), columns=onehot_encoder.get_feature_names(['Country']))
data = pd.concat([data, country_encoded], axis=1)
data.drop('Country', axis=1, inplace=True)

# Save the modified data
data.to_csv('OneHot_Encoded_Data.csv', index=False)

# Display the modified data
print("Part A: OneHot Encoded Data:")
print(data)

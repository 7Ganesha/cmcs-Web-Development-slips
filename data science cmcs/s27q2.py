import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create a sample DataFrame
data = {
    'Country': ['USA', 'Canada', 'UK', 'Canada', 'USA', 'UK'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# a. Apply One-Hot encoding on the 'Country' column
df = pd.get_dummies(df, columns=['Country'], prefix='Country')

# b. Apply Label encoding on the 'Purchased' column
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

print("DataFrame saved to 'data.csv'")

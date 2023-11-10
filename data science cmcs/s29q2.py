import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create a sample DataFrame with two categorical columns
data = {
    'Country': ['USA', 'Canada', 'UK', 'Canada', 'USA', 'UK'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# 1. Apply One-Hot encoding on the 'Country' column
df = pd.get_dummies(df, columns=['Country'], prefix='Country')

# 2. Apply Label encoding on the 'Purchased' column
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

# 3. Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

print("DataFrame saved to 'data.csv'")

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Data.csv
data = pd.read_csv('Data.csv')

# Label encoding on 'Purchased' column
label_encoder = LabelEncoder()
data['Purchased'] = label_encoder.fit_transform(data['Purchased'])

# Save the modified data
data.to_csv('Label_Encoded_Data.csv', index=False)

# Display the modified data
print("\nPart B: Label Encoded Data:")
print(data)

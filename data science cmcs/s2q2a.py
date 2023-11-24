import pandas as pd

df = pd.read_csv('exe.csv')
df.fillna(df['marks'].mean(), inplace=True)

print(df)
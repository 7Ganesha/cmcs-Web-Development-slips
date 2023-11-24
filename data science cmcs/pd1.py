import pandas as pd
df=pd.read_csv('exe.csv')
print(df)

df.fillna(df['marks'].mean(),inplace=True)
print(df)

print(df.shape)
print(df.info())
print(df.dtypes)
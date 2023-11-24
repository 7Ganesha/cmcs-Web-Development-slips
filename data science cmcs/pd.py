import pandas as pd
df=pd.DataFrame(columns=(['company','model','year']))
df.loc[0]=['Tata','nexon',2017]
df.loc[1]=['bmw','c12',2016]
df.loc[2]=['md','c60',2014]
print(df)

#using numpy
print("using numpy")
import numpy as np
data=np.array([['tata','nexon',2017],['bmw','b12',2016],['md','c60',2014]])
df=pd.DataFrame(data,columns=['comapany','model','year'])
print(df)

#using list
print("using list")
data=[['tata','nexon',2017],['bmw','b12',2016],['md','c60',2014]]
df=pd.DataFrame(data,columns=['comapany','model','year'])
print(df)

#using dictionary with list
print("using dictionary with list")
data={
    'company':['tata','bmw','md'],
    'model':['nexon','b12','c60'],
    'year':[2017,2016,2014]
}
df=pd.DataFrame.from_dict(data)
print(df)

# Display the first 10 rows
print("First 2 rows:")
print(df.head(2))

# Display the last 10 rows
print("\nLast 2 rows:")
print(df.tail(2))

# Display random 20 rows
print("\nRandom 2 rows:")
print(df.sample(2))

# Display the shape of the dataset
print("\nDataset shape:")
print(df.shape)
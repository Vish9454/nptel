import pandas as pd
data=pd.read_csv("F:/nba.csv")
data2=data.copy()
'''
print(data.shape)
print(data.isna().sum())
print(data.isnull().sum())
missing=data2[data2.isnull().any(axis=1)]
print(missing.shape)
print(data.describe())
print(data.isnull().sum())
data2["Salary"].fillna(data2["Salary"].median(),inplace=True)
print(data2.isnull().sum())
print(data2["Position"].value_counts())
print(data2["Position"].value_counts().index[0])
print(data2["Position"].value_counts().mode())
print(data2.isnull().sum())
data2["Position"].fillna(data2["Position"].mode()[0],inplace=True) #or .value_counts().index[0]
print(data2.isnull().sum())
'''
data2=data2.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
print(data2.isnull().sum())
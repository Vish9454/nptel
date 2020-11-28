import numpy as np
import pandas  as pd
data=pd.read_csv("F:\Testwel_new.csv",index_col=0)
print(data.dtypes)
print(np.unique(data['Money']))
data=pd.read_csv("F:\Testwel_new.csv",index_col=0,na_values='???')
print(data.dtypes)
print(data.info())
data['Product']=data['Product'].astype("category")
print(data.dtypes)
print(data['Product'].nbytes)
print(data['Product'].astype("object").nbytes)
#finding missing values
print(data.isnull().sum())
print("######################################################################")
print(data['Money'].dtypes)
print((data.columns))
print(len(data))
print(data.shape)
data.insert(5,"Price_evaluator","")
for i in range(0,len(data['Money']),1):
#    print(data['Money'].iloc[i])
#    data['Price_evaluator'][i]="Hello"
    if (data['Money'].iloc[i]<=1000):
        data['Price_evaluator'].iloc[i]="low"
    elif (data['Money'].iloc[i] >=50000):
        data['Price_evaluator'].iloc[i]="High"
    else:
        data['Price_evaluator'].iloc[i]="Medium"

print(data)

print(data['Price_evaluator'].value_counts())

print(data)
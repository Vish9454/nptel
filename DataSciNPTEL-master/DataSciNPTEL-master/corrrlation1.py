import pandas as pd
data=pd.read_csv("F:/correlation.csv")
num_data=data.select_dtypes(exclude=[object])
print(num_data)
print(num_data.shape)
corr_mat=num_data.corr()
print(corr_mat)

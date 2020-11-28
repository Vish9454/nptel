from pandas import  *
data=read_csv("F:\Testwel_new.csv")
print(data)
print("##########################################################################")
print(data.head())
print("##########################################################################")
print(data.iloc[[3,4,5]])
print("###############################")
print(data.iloc[3:5])

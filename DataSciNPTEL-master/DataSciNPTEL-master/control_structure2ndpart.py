import pandas  as pd
data=pd.read_csv("F:\Testwel_new.csv",index_col=0)
data.insert(5,'km_per_month',"");data.insert(6,'Age_converted',"")
#print(data)
def function_convert(val1,val2):
    Age_year=val1/12
    km_per_month=val2/val1
    return [Age_year,km_per_month]

data["Age_converted"],data["km_per_month"]= \
    function_convert(data["Age"],data["km"])
data["Age_converted"]=round(data["Age_converted"],1)
data["km_per_month"]=round(data["km_per_month"],1)

print(data)
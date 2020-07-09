import os
def exten_count(lst):
    count_ext=[]
    for i in lst:
        if "." in i:
            l=i.rindex(".")  # Finding last index of the occurance of dot(.)
            x=i[l+1:]
            count_ext.append(x) # appending all extensions in the list
#Counting frequency by dictionary
    freq={}
    for items in count_ext:
        if items in freq:
            freq[items]+=1
        else:
            freq[items]=1
    for key,value in freq.items():
        print(f'{key} : {value}')

onlyfiles = next(os.walk("/home/ameyo/Downloads/"))[2]
exten_count(onlyfiles)

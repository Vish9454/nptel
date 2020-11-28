def bubble(list):
    x=len(list)
    for i in range(x):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp
                j+=1
            i+=1
    return True
list=[2,8,6,4,9,567,423,9,754]
bubble(list)3
print("The sorted list is as ",list )
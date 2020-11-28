list=[1,21,3,4,10,5,67,]

try:
    print(list[10])
except IndexError:
    print("The index does not exist")

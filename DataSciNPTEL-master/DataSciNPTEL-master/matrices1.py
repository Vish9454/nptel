from numpy import *
a=matrix('1 2 3 4 ; 4 5 6 7; 7 8 9 10')

print(a)

print(a.shape )
print(a.shape[0])#rows
print(a.shape[1])#columns
print(a.size)#elements
print(insert(a,3,[[10,11,12,13]],axis=0))
print(insert(a,4,[[234,456,678]],axis=1))
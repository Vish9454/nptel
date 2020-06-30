# list vs tuple
import sys
import time as t
from timeit import timeit
import numpy as n
tuple_names = (1, 2, 3)
list_names = ['Nicholas', 'Michelle', 'Alex']
num_names=n.array(['Nicholas', 'Michelle', 'Alex'])

print(sys.getsizeof(tuple_names),"tuple")
print(sys.getsizeof(list_names),"list")
print(sys.getsizeof(num_names),"numpy")
################################################################################
sum1,sum2,sum3=0,0,0
s1=t.time()
for i in range(tuple_names):
    print(i)
e1=t.time()
print((e1-s1)*1000,"for tuple")

s2=t.time()
for i in range(list_names):
    sum2=sum2+i
e2=t.time()
print((e2-s2)*1000,"for list")

s3=t.time()
for i in range(num_names):
    sum3=sum3+i
e3=t.time()
print((e3-s3)*1000,"for numpy")


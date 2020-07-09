x=1
def f():
    x=2
    return x
print(x)
print(f())
print(x)
print("##########################################################################")
a=1
def f1():
    try:
        y=a
        a=2
        return a+y
    except UnboundLocalError as e:
        print("Variable not declared")
print(a)
print(f1())
print(a)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
x1 = 2
def f(a1):
    x1 = a1 * a1
    return x1
y1 = f(3)
print(x1, y1)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
x2=4
h1=lambda x2:x2**3
print(h1)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(2 < 3 or not 3 < 1)  # important concept
print(2 > 3 and not 3 > 1)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
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

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)
print("****************************************************************")
import os
print(os.getcwd())
print(os.name)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##")
t1=(1,2,3,4);t2=(6,7,78,8)
print(t1,id(t1))
t1=t1+t2
print(t1,id(t1))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
tt1=[1,2,3,4];tt2=[6,7,78,8]
print(tt1,id(tt1))
tt1=tt1+tt2
print(tt1,id(tt1))
print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT vvvvv important")
list1=[10,20,30];list2=[10,20,30];print(id(list1),id(list2))
tuple1=(10,20,30);tuple2=(10,20,30);print(id(tuple1),id(tuple2))
integer1=10;integer2=10;print(id(integer1),id(integer2))
print(list1 is list2);print(tuple1 is tuple2)














import time
from threading import *
def fact1(a, b):
    start=time.time()
    if a<=b:
        y=a
    else:
        y=b
    for i in range(1, y+1):
        if (a % i == 0 and b % i == 0):
            x=i
    print("The GCD is as", x,current_thread().getName())
    end=time.time()
    print("Time taken is ",end-start)

fact1(9999999992,9993762)



def gcdrev(a,b):
    start=time.time()
    x=min(a,b);y=0
    for i in range(x,0,-1):
        if a%i==0 and b%i==0:
            y=i
            break
    print("The GCD is ", y,current_thread().getName())
    end=time.time()
    print("Time taken is ", end - start)

gcdrev(9999999992,9993762)

def gcd_euclid(m,n):
    start = time.time()
    if m<n:
        (m,n)=(n,m)
    while(m%n)!=0:
        (m,n)=(n,m%n)
    print("Euclid output is ",n,current_thread().getName())
    end = time.time()
    print("Time taken is ", end - start)
gcd_euclid(9999999992,9993762)


t1=Thread(target=fact1)
t1.start
t2=Thread(target=gcdrev)
t2.start
t3=Thread(target=gcd_euclid)
t3.start
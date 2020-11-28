from numpy import *
x=arange(2,20,2).reshape(3,3);print(x)

y=arange(2,20,2).reshape(3,3);print(y)
z=add(x,y);print(z)
a=multiply(x,y);print(a)
b=divide(x,y);print(b)
c=subtract(x,y);print(c)
d=remainder(x,y);print(d)
print(x[1:3])
print(x[:2,:2])
print(transpose(x))

#print(append(x,[[22,24,26]],axis=0))
#print(append(y,[[22],[24],[26]],axis=1))
print(insert(x,1,[234 ,234, 236],axis=0))
print(delete(x,1,axis=0))


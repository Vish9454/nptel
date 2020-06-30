#print squares of even numbers from 0 to 99
def iseven(x):
    return x%2==0
def square(x):
    return x*x
print(list(map(square,filter(iseven,range(10)))))

#print the same thing in as List comprehension as -
#print([square(x) for i in range(100) if iseven(x)])

#print pythagoros theorm
print([(x,y,z) for x in range(10) for y in range(x,10) for z in range(y,10) if x*x + y*y==z*z])
#     --map--   -------------------------generator--------------------------   ------filter-----
#range(x,100) -- inner generators can be dependent on outer generators

#list can be used to print matrix , ex -4*3 matrix
l=[[0 for col in range(3)] for rows in range(4)]
#-----map is 0--------rest is generator------------------
print(l)
l[1][1]=7;print(l)

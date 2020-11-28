def square():
    num=1;sq=1;n=1
    while n <10:
        sq=num*num
        num+=1
        yield sq
        n+=1

values=square()
print(next(values));print(next(values))
for i in values:
    print(i)

class compa():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def compare_the_age(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=compa("vishal",40)
c2=compa("aman",40)

if c1.compare_the_age(c2):
    print("They Are Same")
else:
    print("They are diff")



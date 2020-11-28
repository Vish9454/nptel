class duck:
    def talk(self):
        print("Duck class quack quack")
class Horse:
    def talk(self):
        print("Horse class huaahhh huaaahh ")
class Dog:
    def talk(self):
        print("Dog class bark bark")

class All:
    def code(self,param):
        param.talk()              # duck typing,do do not care from which class it is, if talk is there then it will execute.

duck_obj=duck()             #class is also an object so assign it to param
Obj=All()                #creating object of class All
Obj.code(duck_obj)          #calling code method, we cannot do it if we do not create the object of All()






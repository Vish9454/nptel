class duck:
    def talk(self):
        print("Duck class quack quack")
class Horse:
    def talk(self):
        print("Horse class huaahhh huaaahh ")
class Dog:
    def taalk(self):
        print("Dog class bark bark")

def function(self):
    self.talk()      #talk method object passing

d=duck()      #creating object as d
function(d)   #calling the function having parameter as d

H=Horse()
function(H)


print(id(d));print(id(H))



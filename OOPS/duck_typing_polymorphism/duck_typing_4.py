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
    try:
        self.talk()
        self.hello()
    except AttributeError as e:
        print(e)
obj=duck()
function(obj)



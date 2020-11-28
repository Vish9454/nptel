class duck:
    def talk(self):
        print("Duck class quack quack")
class Horse:
    def talk(self):
        print("Horse class huaahhh huaaahh ")
class Dog:
    def talk(self):
        print("Dog class bark bark")

for self in duck(),Horse(),Dog():
    self.talk()



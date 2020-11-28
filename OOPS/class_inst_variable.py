class Car:
    wheels=4
    def __init__(self,mil,speed):
        self.mil=mil
        self.speed =speed
        print(self.mil,self.speed,self.wheels)

c1=Car(10,200)
c2=Car(8,150)
c1.mil=250
Car.wheels=5
print(c1.mil,c1.speed,c1.wheels)


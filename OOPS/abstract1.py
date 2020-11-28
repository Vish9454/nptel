from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass

class square(Shape):
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2
    def area(self):
        return self.a1*self.a2
    def perimeter(self):
        return 4*self.a1


sq=square(3,3)
print(sq.area());
print(sq.perimeter())

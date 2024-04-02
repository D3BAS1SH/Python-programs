# Define an abstract class shapes with an abstract method area

from abc import ABC,abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius) -> None:
        self.Radius=radius
    def area(self):
        return pi*(self.Radius**2)
class Rectangle(Shape):
    def __init__(self,L,W) -> None:
        self.Length=L
        self.Width=W
    def area(self):
        return self.Length*self.Width
C=Circle(10)
print(C.area())
print(Circle(100).area())
print(Rectangle(20,30).area())
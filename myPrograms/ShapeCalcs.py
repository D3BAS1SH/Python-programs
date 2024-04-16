from abc import abstractmethod
from math import pi
class ShapeCalcs:
    @abstractmethod
    def Area(self):
        pass
    def Perimeter(self):
        pass
    pass

class circle(ShapeCalcs):
    def __init__(self,r=0.0):
        self._radius=r
    def Area(self):
        return (self._radius**2)*pi
    def Perimeter(self):
        return self._radius*2*pi
    pass

class Triangle(ShapeCalcs):
    def __init__(self,a=0.0,b=0.0,c=0.0):
        self._a=a
        self._b=b
        self._c=c
    def Area(self):
        s=(self._a+self._b+self._c)/2
        return (s*(s-self._a)*(s-self._b)*(s-self._c))**(0.5)
    def Perimeter(self):
        return self._a+self._b+self._c
    pass

class Rectangle(ShapeCalcs):
    def __init__(self,a=0.0,b=0.0):
        self._a=a
        self._b=b
    def Area(self):
        return (self._a*self._b)
    def Perimeter(self):
        return 2*(self._a+self._b)
    pass

C=circle(10)
T=Triangle(1,2,3)
R=Rectangle(5,15)

print(C.Area())
print(C.Perimeter())
print(T.Area())
print(T.Perimeter())
print(R.Area())
print(R.Perimeter())

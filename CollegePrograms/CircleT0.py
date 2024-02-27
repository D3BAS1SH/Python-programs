import math as MATH

class Circle:
    def __init__(self,radius=0) -> None:
        self.__radius=radius
        pass
    
    def setRadius(self,R=0):
        self.__radius=R
        pass

    def getRadius(self):
        return self.__radius
    def getArea(self):
        return (self.getRadius()**2)*MATH.pi
    def __getCircumfarence(self):
        return self.getRadius()*MATH.pi*2
    
    pass

C0 = Circle(10)
print(C0.getArea())
print(C0._Circle__getCircumfarence())
# print(C0.__radius)
print(C0._Circle__radius)
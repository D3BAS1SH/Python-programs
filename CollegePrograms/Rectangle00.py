class Rectangle:
    def __init__(self,length=0,width=0) -> None:
        self.__Length=length
        self.__Width=width
        pass
    def getLength(self):
        return self.__Length
    def getWidth(self):
        return self.__Width
    def getArea(self):
        return self.getLength()*self.getWidth()
    def getPerimeter(self):
        return (self.getLength()+self.getWidth())*2
    def showStats(self):
        print(f"Length : {self.getLength()}, Width : {self.getWidth()}\nArea : {self.getArea()}, Perimeter : {self.getPerimeter()}")
    pass

""" RectList=[Rectangle(10,20),Rectangle(5,4),Rectangle(3,8),Rectangle(1.5,20),Rectangle(70,0.3),Rectangle(10,20)] """
RectList=[]

num=int(input("Number of Rectangles you want to give : "))
print("\nNow Give the values by the following Instruction.\n")

for x in range(num):
    print()
    L = float(input(f"Length of the {x+1} Rectangle : "))
    W = float(input(f"Length of the {x+1} Rectangle : "))
    RectList.append(Rectangle(L,W))

newSortedList=sorted(RectList,key=lambda obj : obj.getArea())


print()
for x in newSortedList:
    x.showStats()
    print()
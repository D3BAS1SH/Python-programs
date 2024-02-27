class Rectangle:
    def __init__(self,length=0,width=0) -> None:
        self.__Length=length
        self.__Width=width
        pass

    def setLength(self,L=0):
        self.__Length=L
        pass
    def setWidth(self,W=0):
        self.__Width=W
        pass

    def getLength(self):
        return self.__Length
    def getWidth(self):
        return self.__Width
    def getArea(self):
        return self.getLength()*self.getWidth()
    
    def showStats(self):
        print()
        print(self.getLength())
        print(self.getWidth())
        print(self.getArea())
        print()
    pass

class BOX(Rectangle):
    def __init__(self,height=0, length=0, width=0) -> None:
        super().__init__(length, width)
        self.__Height=height
        pass
    def showStats(self):
        print("LENGTH : ",self.__Length)
        print("WIDTH : ",self.__Width)
        print("HEIGHT : ",self.__Height)
        pass
    def showParentStats(self):
        super().showStats()
        pass
    pass

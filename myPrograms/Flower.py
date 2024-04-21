class Flower:
    def __init__(self,price=0,color='transparent',smell=None) -> None:
        self.__Price=price
        self.__Color=color
        self.__Smell=smell
        pass
    def getPrice(self):
        return self.__Price
    def getColor(self):
        return self.__Color
    def getSmell(self):
        return self.__Smell
    def Display(self):
        print(f"Price : {self.__Price}")
        print(f"Color : {self.__Color}")
        print(f"Smell : {self.__Smell}")
        print()
        pass
    pass

Lily=Flower(115,"White","sweet")
Rose=Flower(200,"Red","sweet")
Hibiscus=Flower(75,"Pink","sweet")

Lily.Display()
Rose.Display()
Hibiscus.Display()
class ShoppingCart:
    def __init__(self,Items=[]) -> None:
        self.Items=Items
        pass
    def AddItem(self,Item):
        # self.Items=self.Items.append(list(Item))
        self.Items=self.Items +[Item]        
        pass
    def RemoveItem(self,Item):
        I=None
        for index,x in enumerate(self.Items):
            if Item==x[0]:
                I=index
                break
        if(I==None):
            return -1
        self.Items.pop(I)
        pass
    def TotalPrice(self):
        totalM=0
        for x in self.Items:
            totalM+=x[1]
        return totalM
    pass

MyCart=ShoppingCart([("A",100),("B",150),("C",180)])
print(MyCart.TotalPrice())
MyCart.AddItem(Item=("EE",1000))
print(MyCart.TotalPrice())
MyCart.RemoveItem("A")
print(MyCart.TotalPrice())
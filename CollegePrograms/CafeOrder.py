ItemNPrice={'Tea':[5,10],'Coffee':[10,15],'Cookies':[5,10],'Bread':[10,20],'Poison':0}
OrderTaken={}
totalPrice=0
def showItems():
    print("Items Available : \n")
    for x in ItemNPrice.keys():
        print(x)
    print()

def Options():
    print("1) Show Items.")
    print("2) TakeOrder Items.")
    print("3) Bill.")

def TakeOrder():
    itemName=input("Item name : ")
    
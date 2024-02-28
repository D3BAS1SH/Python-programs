from Rectangle00 import Rectangle

def GETCHOICE():
    SHOWINFO()
    x = int(input("YOUR CHOICE : "))
    return x

def SHOWINFO():
    print()
    print("1) Sort rectangles by the Length.")
    print("2) Sort rectangles by the Width.")
    print("3) Sort rectangles by the Area.")
    print("4) Sort rectangles by the Perimeter.")
    print("5) Exit")
    print()

num=int(input("Number of Rectangles You want to give : "))
print("Please provide the required information by the following instructions.")

RectList=[]

for x in range(num):
    print()
    L=float(input(f'Length of {x+1} rectangle : '))
    W=float(input(f'Width of {x+1} rectangle : '))
    RectList.append(Rectangle(L,W))

ShallContinue=True

while(ShallContinue):
    match GETCHOICE():
        case 1:
            LenSort=sorted(RectList,key=lambda obj : obj.getLength())
            for x in LenSort:
                x.showStats()
            #break
        case 2:
            WidSort=sorted(RectList,key=lambda obj : obj.getWidth())
            for x in WidSort:
                x.showStats()
        case 3:
            AreSort=sorted(RectList,key=lambda obj : obj.getArea())
            for x in AreSort:
                x.showStats()
        case 4:
            PerSort=sorted(RectList,key=lambda obj : obj.getPerimeter())
            for x in WidSort:
                x.showStats()
        case 5:
            ShallContinue=False
            print("Thank youuuu.")
class Rectangle:
    def __init__(this,length=0,width=0):
        this.Length=length;this.Width=width
        pass
    def PrintProps(this):
        print(f'LENGTH : {this.Length}, WIDTH : {this.Width}')
        pass
    def Area(this):
        return this.Length*this.Width
    def Get_Area(this,length,width):
        return length*width
    pass

R=Rectangle(2.5,10)
R.PrintProps()

P=Rectangle(15.5,2)

if(R.Area())>(P.Area()):
    print('Rectangle R has larger Area')
elif R.Area()==P.Area():
    print('Area of Rectangle R and P is SAME SAME.')
else:
    print("Area of Rectangle P is larger.")
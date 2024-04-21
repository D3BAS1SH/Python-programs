class myClass:
    def __init__(self,a,b) -> None:
        self.A=a
        self.B=b
        pass
    def __add__(self,Other):
        return myClass(self.A+Other.A,self.B+Other.B)
    pass

A=myClass(5,7)
B=myClass(5,3)
C=A+B
print(C.A,C.B)
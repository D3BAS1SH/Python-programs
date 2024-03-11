class Calculator:
    def Addition(self,a,b):
        return a+b
    def Substraction(self,a,b):
        return a-b
    def Multiply(self,a,b):
        return a*b
    def Division(self,a,b):
        return a/b
    def PowerOF(self,a,b):
        return a**b
    pass

V = Calculator()
print(V.Addition(15,1))
print(V.Substraction(15,51))
print(V.Multiply(15,19))
print(V.Division(1,18))
print(V.PowerOF(15,6))
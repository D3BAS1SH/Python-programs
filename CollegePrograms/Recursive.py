def Fact(n):
    if not isinstance(n,int) or isinstance(n,str) or n<0 :
        #print("Not a valid point")
        return "NADA"
    if n==0:
        return 1
    else:
        return n*Fact(n-1)
print(Fact('a'))
def getEven(L):
    for x in L:
        if isinstance(x,int) and x%2==0:
            return x
    return "No Even Value Found"

print(getEven(['Hello',(1.3,4.10),87,15.8,21,90.1,{20:22},{'name':'ROG'},[1,1,1,1]]))
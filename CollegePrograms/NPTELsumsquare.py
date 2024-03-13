def SUMOFSUQARE(l):
    odd=[x**2 for x in l if(x%2==1)]
    even=[x**2 for x in l if(x%2==0)]
    return [sum(odd),sum(even)]
print(SUMOFSUQARE([1,3,5]))
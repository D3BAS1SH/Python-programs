import math as M

def getGcd(a,b):
    return M.gcd(a,b)

def getLcm(a,b):
    return a*b // getGcd(a,b)

def getGcd3(a,b,c):
    return getGcd(getGcd(a,b),c)

def getLcm3(a,b,c):
    return getLcm(getLcm(a,b),c)

a=int(input("1st Number : "))
b=int(input("2nd Number : "))
c=int(input("3rd Number : "))
print(f'LCM of {a}, {b} and {c} : {getLcm3(a,b,c)}')
print(f'GCD of {a}, {b} and {c} : {getGcd3(a,b,c)}')
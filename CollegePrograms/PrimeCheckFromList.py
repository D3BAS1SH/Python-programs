import math

def isPrime(n):
    for i in range(2,math.floor(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

MAIN_LIST=[1,4,2,9,10,17,23,29]
primeTuple=tuple([X for X in MAIN_LIST if isPrime(X)])

print(primeTuple)
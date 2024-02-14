import math

def isPerfectSquare(n):
    sqtVal=math.sqrt(n)
    if(sqtVal<math.ceil(sqtVal) and sqtVal>math.floor(sqtVal)):
        return False
    else:
        return True
    
def nearestPerfectNum(n):
    n=int(n)
    for v in range(n,0,-1):
        if(isPerfectSquare(v)):
            print("returning",v,'as nearest perfect number')
            return v

def threesquares(n):
    if(isPerfectSquare(n)):
        return True
    elif(n<0):
        return False
    else:
        a=nearestPerfectNum(n)
        b=nearestPerfectNum(int(n-a))
        if((a+b)==n):
            return True
        else:
            c=nearestPerfectNum(n-(a+b))
            if(a+b+c==n):
                return True
            else:
                return False

print(threesquares(1000))
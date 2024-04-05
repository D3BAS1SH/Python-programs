# Make a list if n prime numbers and make another list of n random numbers. Make sure that the both lists have no duplicate numbers. Make a dictionary such that each element from the first list is the key and the element from second list is values.

import random

def isPrime(n):
    for x in range(2,(n//2)+1):
        if(int(n%x)==0):
            return False
    return True

def GetPrimeNumberList(n):
    Array=[];num=1
    while(n!=0):
        if(isPrime(num)):
            Array.append(num)
            n-=1
        num+=1
    return Array

def GetRandomNumber(n):
    Arr=[]
    while(n!=0):
        Val=random.randint(1,100)
        if(Val not in Arr):
            Arr.append(Val)
            n-=1
    return Arr

NLen=int(input("Length of array : "))

_1st=GetPrimeNumberList(NLen)
_2nd=GetRandomNumber(NLen)

# MyColl=dict()

print({_1st[x]:_2nd[x] for x in range(NLen)})

# for x in range(NLen):
#     MyColl[_1st[x]]=_2nd[x]

# print(MyColl)
#define a function any number of integers as arguments and returns the gcd.
import math as M

def getGCDof(V):
    finalGCD=M.gcd(V[0],V[1])
    for x in range(1,len(V)-1):
        finalGCD = M.gcd(finalGCD,V[x],V[x+1])
    return finalGCD

li=[]
for x in range(5):
    li.append(int(input("Input : ")))

print(f'Answer : {getGCDof(li)}')
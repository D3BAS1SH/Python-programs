# Print 10 prime numbers
import math

def isPrime(n):
    for i in range(2,math.floor(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

l=[];i=101
while(len(l)<10):
    if(isPrime(i)):
        l.append(i)
    i+=1

print(l)
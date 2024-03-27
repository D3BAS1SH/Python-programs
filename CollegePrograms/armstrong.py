def lengthOf(n):
    return len(str(n))

def digitsOfN(n):
    n=int(n)
    digis=[]
    while (n!=0):
        digis,n=[int(n%10)]+digis,int(n/10)
    return digis

def isArmstrong(n):
    L=lengthOf(n)
    Digits=digitsOfN(n)
    sum=0
    for x in Digits:
        sum+=x**L
    if(sum==n):
        return True
    return False

print(isArmstrong(153))
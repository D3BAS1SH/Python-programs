CheckL=['Literature','Hello',True,1,2,3,10.15,20.11,18.98,3.131,1.419]

def AverageF(L):
    count=0;sum=0
    for x in L:
        if(isinstance(x,float)):
            count+=1
            sum+=x
    if(count==0):
        return "No float found"
    return sum/count
print(AverageF(CheckL))

CheckL0=[1,(-10.6,-10),"Hello",True,{'Name':'ROG'},['Nvidia','Intel'],{'22'}]

print(AverageF(CheckL0))
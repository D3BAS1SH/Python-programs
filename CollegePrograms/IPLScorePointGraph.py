import matplotlib.pyplot as PL

def SeqSum(L):
    x=[];sum=0
    for v in L:
        sum+=v
        x.append(sum)
    return x

IPL=dict()
IPL["RR"]=(1,1,1,0,1)
IPL["KKR"]=(1,0,1,0,1)
IPL["SRH"]=(1,1,1,1,0)
IPL["CSK"]=(0,1,1,0,0)

myX=list(range(1,6))
print(myX)
myY=[SeqSum(x) for x in IPL.values()]
print(myY)

for n,s in IPL.items():
    PL.plot(myX,SeqSum(s),label=n,marker='o')
    PL.xticks(range(1,7))
    PL.yticks(range(0,7))
    # PL.yticks(range(int(min(myX)), int(max(myX)) + 1))
PL.legend()
PL.show()
# PL.plot(,[SeqSum(x) for x in IPL.values()])
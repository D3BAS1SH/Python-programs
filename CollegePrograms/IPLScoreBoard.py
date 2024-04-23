import matplotlib.pyplot as PL

def SumOfArray(L):
    x = 0
    for V in L:
        x+=V
    return x

IPL=dict()
IPL["RR"]=[1,1,1,0,1]
IPL["KKR"]=[1,0,1,0,1]
IPL["SRH"]=[1,1,1,1,0]
IPL["CSK"]=[0,1,1,0,0]

IPL_Teams=list(IPL.keys())
IPL_Score=[SumOfArray(x) for x in IPL.values()]

PL.bar(IPL_Teams,[len(x) for x in IPL.values()],color="#104010",width=0.4)
PL.bar(IPL_Teams,IPL_Score,color="#0000f3",width=0.4)
# PL.legend()
PL.xlabel("IPL TEAMS")
PL.ylabel("IPL TEAM SCORE")
PL.title("IPL SCORE BOARD")
PL.show()

print(IPL_Teams)
print(IPL_Score)
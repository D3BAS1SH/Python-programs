def addpoly(p1,p2):
    totalP=[[(x,v) for v in p2 if(x[1]==v[1])] for x in p1]
    # print(totalP)
    ClearEMP=[x for x in totalP if x!=[]]
    finalTotalP=[list(v[0]) for v in ClearEMP]
    # print(finalTotalP)
    SumAr=[]
    for x in finalTotalP:
        S=0
        for y in range(len(x)):
        #    print(x[y])
           S+=x[y][0]
        # print("ENDS")
        SumAr.append((S,x[0][1]))
    # print(SumAr)
    # print(p1+p2)
    RestAr=[v for v in p1+p2 if v[1] not in [x[1] for x in SumAr]]
    # print(RestAr)
    # print(RestAr+SumAr)
    finalPoly=RestAr+[x for x in SumAr if x[0]!=0]
    print(finalPoly)

# Mutiplication part
def multiplyTuples(T1,T2):
    return (T1[0]*T2[0],T1[1]+T2[1])

def Simplify(L0):
    totalP=[[(x,v) for v in L0 if(x[1]==v[1])] for x in L0]
    # print(totalP)
    ClearEMP=[x for x in totalP if x!=[]]
    finalTotalP=[list(v[0]) for v in ClearEMP]

def multpoly(p1,p2):
    finalPoly=[]
    for x in p1:
        for v in p2:
            finalPoly.append(multiplyTuples(x,v))
    
    print(finalPoly)
# addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
# addpoly([(5,3),(3,1)],[(-4,3),(-2,1)])
# addpoly([(5,4),(3,2)],[(-4,1),(-2,0)])
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
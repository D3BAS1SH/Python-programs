def remdup(l):
    seen=set()
    result=[]
    for i in l:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even+=i**2
        else:
            odd+=i**2
    return [odd,even]

def transpose(m):
    rows=len(m)
    cols=len(m[0])

    trM=[[m[j][i] for j in range(rows)] for i in range(cols)]
    return trM
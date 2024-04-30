def Add(A,B):
    if len(A)!=len(B):
        return f"Dimension of {len(A)},  and {len(B)} is not same"
    elif (len(A[0]))!=len(B[0]):
        return f"Dimension of {len(A)},  and {len(B)} is not same"
    else:
        return [[A[x][y]+B[x][y] for y in range(len(A[0]))] for x in range(len(A))]
    pass

def Subtract(A,B):
    if len(A)!=len(B):
        return f"Dimension of {len(A)},  and {len(B)} is not same"
    elif (len(A[0]))!=len(B[0]):
        return f"Dimension of {len(A)},  and {len(B)} is not same"
    else:
        return [[A[x][y]-B[x][y] for y in range(len(A[0]))] for x in range(len(A))]
    pass

def isMatrix(A):

    value=set([len(x) for x in A if isinstance(x,list)])

    if(len(value)==1):
        return True
    return False

    """ if(isinstance(A,list)):
        theMats=[True for x in A if isinstance(x,list)]
        if(theMats.count(True)==len(A)):
            if len({len(x) for x in A})==1:
                return True
            return False
        return False
    return False """

print(isMatrix([[123]]))
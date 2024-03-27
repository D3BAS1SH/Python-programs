def binarySearch(L,key):
    L.sort()
    l,m,r=0,int((len(L)-1)/2),len(L)-1
    while(l<=r):
        m=l+(r-l)//2
        if(L[m]==key):
            return m
        elif(L[m]<key):
            l=m+1
        elif(L[m]>key):
            r=m-1
    return -1

def RecursiveBinarySearch(Val,Key):
    # print("#")
    m=len(Val)//2
    # print(m)
    if(Val[m]==Key):
        return m
    elif (Val[m]>Key):
        return RecursiveBinarySearch(Val[:m],Key)
    elif (Val[m]<Key):
        return m+1+RecursiveBinarySearch(Val[m+1:],Key)
    else :
        return -1

print(RecursiveBinarySearch([1,2,3,4,5,6,7,8,9,10,12,13,46,79,89,102,125,149,150],125))
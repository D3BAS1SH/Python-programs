""" def g(m,n):
    res=0
    while m>=n:
        (res,m)=(res+1,m/n)
    return res """

def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return (res)

for i in range(2,10):
    print("i : ",i,g(375,i))
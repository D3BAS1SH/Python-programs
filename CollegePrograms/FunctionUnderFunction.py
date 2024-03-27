def outerFun(a,b):
    def innerFun(c,d):
        return c+d
    return innerFun(a,20)
    return a

result= outerFun(5,10)
print(result)
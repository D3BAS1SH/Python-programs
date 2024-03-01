def Fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    return Fibonacci(x-1)+Fibonacci(x-2)

print(Fibonacci(10))
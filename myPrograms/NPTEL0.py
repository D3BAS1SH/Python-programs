def f(x):
    d=0
    while x>1:
        print(x)
        (x,d)=(x/2,d+1)
    return d
print(f(27182818))
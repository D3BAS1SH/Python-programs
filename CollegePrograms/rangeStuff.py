for i in range(10):
    for j in range(i):
        print("$",end="")
    print()
x=0
while x in range(10):
    y=0
    while y in range(x):
        print("$",end="")
        y+=1
    print()
    x+=1
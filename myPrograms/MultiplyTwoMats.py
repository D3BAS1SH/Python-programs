Mat0=[]
Mat1=[]
Mult=[]

R0=int(input("Number of Rows in the 1st Matrix : "))
C0=int(input("Number of Cols in the 1st Matrix : "))

R1=int(input("Number of Rows in the 2nd Matrix : "))
C1=int(input("Number of Cols in the 2nd Matrix : "))

if(C0!=R1):
    print("Multiplication isn't possible.")
else:

    for i in range(R0):
        Row=[]
        for j in range(C0):
            Row.append(float(input(f"{i},{j} Index Value : ")))
        Mat0.append(Row)
    
    for i in range(R1):
        Row=[]
        for j in range(C1):
            Row.append(float(input(f"{i},{j} Index Value : ")))
        Mat1.append(Row)
    
    for i in range(R0):
        Row=[]
        for j in range(C1):
            Multi=0
            for k in range(C0):
                Multi+=Mat0[i][k]*Mat1[k][j]
            Row.append(Multi)
        Mult.append(Row)
    
    for v in (Mult):
        print(v)
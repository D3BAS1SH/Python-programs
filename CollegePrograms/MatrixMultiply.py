Mat1=[]
Mat2=[]
F_MAT=[]

print("------------------------------------------------")
print("             INPUT FOR 1ST MATRIX               ")
print("------------------------------------------------")
M1=int(input("Number of ROWS : "))
N1=int(input("Number of COLS : "))
print("------------------------------------------------")
print("             INPUT FOR 2nD MATRIX               ")
print("------------------------------------------------")
M2=int(input("Number of ROWS : "))
N2=int(input("Number of COLS : "))

if(N1!=M2):
    print("Matrix Multiplication isn't possible")
else:
    print("------------------------------------------------")
    print("             INPUT FOR 1ST MATRIX               ")
    print("------------------------------------------------")
    for x in range(M1):
        rows=[]
        for y in range(N1):
            rows.append(float(input(f"{x},{y} Index Value : ")))
        Mat1.append(rows)
    print("------------------------------------------------")
    print("             INPUT FOR 2ND MATRIX               ")
    print("------------------------------------------------")
    for x in range(M2):
        rows=[]
        for y in range(N2):
            rows.append(float(input(f"{x},{y} Index Value : ")))
        Mat2.append(rows)
    for x in range(M1):
        rows=[]
        for y in range(N2):
            sum=0
            for z in range(N1):
                sum+=Mat1[x][z]*Mat2[z][y]
            rows.append(sum)
        F_MAT.append(rows)
    for x in F_MAT:
        for y in x:
            print(y,end=" ")
        print()
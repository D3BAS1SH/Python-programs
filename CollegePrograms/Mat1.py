Mat1=[]
Mat2=[]
MatAdd=[]

M=int(input('Number of Rows : '))
N=int(input('Number of Columns : '))

for i in range(M):
    row=[]
    for j in range(N):
        row.append(int(input(f'{i},{j} Index Value : ')))
    Mat1.append(row)

for i in range(M):
    row=[];rowA=[]
    for j in range(N):
        row.append(int(input(f'{i},{j} Index Value : ')))
        rowA.append(row[j]+Mat1[i][j])
    Mat2.append(row)
    MatAdd.append(rowA)

for i in range(M):
    for j in range(N):
        print(MatAdd[i][j],end=' ')
    print()

""" for i in range(M):
    row=[]
    for j in range(N):
        row.append(int(input(f'{i},{j} Index Value : ')))
    Mat1.append(row)

for i in range(M):
    row=[]
    for j in range(N):
        row.append(int(input(f'{i},{j} Index Value : ')))
    Mat2.append(row)

for i in range(M):
    row=[]
    for j in range(N):
        row.append(Mat1[i][j]+Mat2[i][j])
    MatAdd.append(row)

print(MatAdd) """
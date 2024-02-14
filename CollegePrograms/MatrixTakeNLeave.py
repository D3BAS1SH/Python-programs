Mat=[]

M=int(input('NUMBER OF ROWS : '))
N=int(input('NUMBER OF COLUMNS : '))

""" for i in range(M):
    row=list(map(int,(input(f'Give {N} Values seprated by space : ').split(' '))))
    Mat.append(row) """

for i in range(M):
    row=[]
    for j in range(N):
        row.append(int(input(f'{i+1},{j+1} Value : ')))
    Mat.append(row)

print(Mat)


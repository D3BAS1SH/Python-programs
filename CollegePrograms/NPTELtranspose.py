def transpose(v):
    transposed=[]
    for x in range(len(v[0])):
        row=[]
        for y in range(len(v)):
            row.append(v[y][x])
        transposed.append(row)
    print(transposed)
transpose([[1,2,3],[4,5,6]])
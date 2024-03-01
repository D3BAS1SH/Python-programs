Mat=[
    [17,15,4],
    [10,12,9],
    [11,13,18],
]

P="name"
O=input(f"Say my {P}")

TransposedMat=[]

for v in range(len(Mat[0])):
    Row=[]
    for x in range(len(Mat)):
        Row.append(Mat[x][v])
    TransposedMat.append(Row)

for x in TransposedMat:
    print(x)
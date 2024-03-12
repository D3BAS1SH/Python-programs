import numpy as NP

MAT0 = NP.array([[1,2,3],[10,20,30],[11,22,33]])
TRAN = NP.transpose(MAT0)
print(MAT0)
print(TRAN)
# RESHAPE = NP.reshape(MAT0,[9,1])
# print(RESHAPE)

A = NP.random.randint(10,size=(2,2))
B = NP.random.randint(10,size=(2,2))
print(A)
print(B)
print('DOT\n',NP.dot(A,B))
print('MULTIPLY\n',NP.multiply(A,B))
print('MATMUL\n',NP.matmul(A,B))
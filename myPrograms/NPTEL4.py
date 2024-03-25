OOOO="abcd"
OOOO[1]="B"
print(OOOO)
x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
print(x)
y = x[0:6]                     # Statement 2
print(y)
""" print(x[0:7]) """
z = x                          # Statement 3
print(z)
w = y                          # Statement 4
print(w)
x[1] = x[1][0:3] + 'd'         # Statement 5
print(x)
y[2] = 4                       # Statement 6
print(y)
z[1][1:3] = 'yzw'              # Statement 7
print(z)
z[0] = 0                       # Statement 8
print(z)
w[4][0] = 1000                 # Statement 9
print(w)
a = (x[4][1] == 4)
print(a)
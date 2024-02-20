#make a dictionary where the key are the members of the list of integers, values are square of integers if it is even else cube of integers.
KEYVALS=[10,20,1,2,3,11,13]
D=(map(lambda x : {x:x**2} if x%2==0 else {x: x**3} ,KEYVALS))
print(list(D))
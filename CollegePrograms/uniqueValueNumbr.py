L=[10,20,1,2.5,'satya',5+2j, True]
L=list(set([type(x) for x in L]))
print(len(L))
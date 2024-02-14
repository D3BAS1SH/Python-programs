C={'Hitesh','Satya','Anjani','Manoj'}
B={'Dev','Ankit','Satya','syed'}
F={'Sanjeeb','syed','Satya','PAA','Hitesh'}

CPlay=C.pop()
print(CPlay)
C.add(CPlay)
print(C)

semt=set.union(C.difference(B,F),F.difference(C,B))
print(semt)

CF_NB=F.intersection(C).difference(B)
print(CF_NB)

myMNewSemt=set.union(C.intersection(B),C.intersection(F),B.intersection(F))
print(myMNewSemt)

atLeast1=set.union(B,C,F)
print(atLeast1)
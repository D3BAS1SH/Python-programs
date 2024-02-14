T={'Smarak','Adyasha','Dipti','Susmita','Anjani'}
C={'Srinibas','Zeshan','Debasish','Adyasha','Arpita'}

print(T.symmetric_difference(C))

newSet={T.pop(),C.pop()}
print(newSet)

""" C.remove('Srinibas')
print(C) """

T.clear()
print(T)

C.discard('Dipti')
print(C)

T.add('Strix')
print(T)

S=T.union(C)
print(S)

X={1,5,11,23}
T.update(T.union(X,S,C))
print(T)

print(T.issubset(X))
print(T.issubset(S))
print(T.issubset(C))
print()

print(T.issuperset(X))
print(T.issuperset(S))
print(T.issuperset(C))
print()

print(T.isdisjoint(X))
print(T.isdisjoint(S))
print(T.isdisjoint(C))
print()

print(T.difference(C))
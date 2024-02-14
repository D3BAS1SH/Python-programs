NUM0=[1,4,20,63,90,51,14,10]
sq=[]
sq0=[x**2 for x in NUM0 if x%2==0]
sq2=[x**2 if x%2==0 else x for x in NUM0]

for x in NUM0:
    sq.append(x**2)

print(sq)
print(sq0)
print(sq2)
l=['Xaden','Zade','Ankit','Anish','Saddam','Hitesh','Setting','Sawan','Syed']
L1=[x for x in l if x.startswith('S')]
L2=[x for x in l if x not in L1]
L2.sort()
L1=L1+L2
print(L1)
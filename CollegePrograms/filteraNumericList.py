MAINLIST=[True,1,'hello',5+10j,10,'suii',90.11,False,False,'Things',3.131,'Fortune',100,1,-40,-40-7j,True,['Xaden','Violet'],['Tairn','Sygeal']]

Num=[x for x in MAINLIST if isinstance(x,(int,float,complex)) and not isinstance(x,bool)]
noNUm=[x for x in MAINLIST if isinstance(x,(str,bool,object))]
noNum0=[x for x in MAINLIST if x not in noNUm]

print(noNum0)
print(Num)
print(noNUm)
x=[ x for x in [(10,20),"Hello",(50,80),10] if isinstance(x,(tuple,list,set,dict))]
for v in (x):
    print(v)
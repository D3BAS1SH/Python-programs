LIST=[0,1,2,3,4]
TUPLE=(0,10,20,30,40)

print(TUPLE.index(40))

TUPLE=tuple([LIST[X]+TUPLE[X] for X in range(0,len(LIST)) ])

print(TUPLE)
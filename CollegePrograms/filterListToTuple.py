""" MAIN_LIST=[0,-10,30,-11,-19,20,15,3.14,7.11,-0.77]
pTve=()
nTve=()

for x in MAIN_LIST:
    if x <0:
        nTve+=(x,)
    else:
        pTve+=(x,)

print(f"MAIN LIST : {MAIN_LIST}")
print(f"POSTIVE LUPLE : {pTve}")
print(f"NEGATIVE TUPLE : {nTve}") """

MAIN_LIST=[0,-10,30,-11,-19,20,15,3.14,7.11,-0.77]
pTve=tuple([X for X in MAIN_LIST if X>-1])
nTve=tuple([X for X in MAIN_LIST if X<0])

print(f"MAIN LIST : {MAIN_LIST}")
print(f"POSTIVE LUPLE : {pTve}")
print(f"NEGATIVE TUPLE : {nTve}")
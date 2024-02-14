MAIN_TUPLE=[('Hitesh',21,65),('Debasish',20,60),('Ankit',30,60)]
AGes=[x[1] for x in MAIN_TUPLE]
AGes.sort()
print(AGes)
MAIN_TUPLE.sort(key=lambda x : x[1])
print(MAIN_TUPLE)
MAIN_TUPLE.sort(key=lambda x : x[2])
print(MAIN_TUPLE)
MAIN_TUPLE.sort(key=lambda x : x[0])
print(MAIN_TUPLE)
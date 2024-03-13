#Develope a python program to find the range of values present in a given matrix.

import numpy as NP

ROW=int(input('NUMBERS OF ROWS : '))
COL=int(input('NUMBERS OF COLS : '))

MAT=[]

for x in range(ROW):
    ROWAR=[]
    for y in range(COL):
        ROWAR.append(int(input(f"{x},{y} index value : ")))
    MAT.append(ROWAR)

print(f"MINIMUM OF THE RANE : {NP.min(MAT)}")
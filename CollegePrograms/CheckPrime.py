import sympy as SM
import numpy as NP

MAT=[]
start=int(input("Starting Range : "))
end = int(input("Ending Range   : "))

MAT=[x for x in range(start,end+1) if SM.isprime(x)]
print(MAT)
print(sum(MAT))
print(NP.average(MAT))
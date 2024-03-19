import math as M
num=int(input("NUMBER : "))
print([x for x in range(1,int((num/2))+1) if (num%x==0)])
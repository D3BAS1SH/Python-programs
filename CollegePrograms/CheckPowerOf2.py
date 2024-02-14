import math

num=int(input('NUMBER : '))

if num > 0 and num&(num-1)==0:
    print(num,'is a power of 2')
else:
    print(num,'is not a power of 2')
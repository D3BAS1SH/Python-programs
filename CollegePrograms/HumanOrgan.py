n=int(input('Number of Organs you know in human body : '))
OrganFunc=set()
HumanOrgan=set()
OrganWork={}
for x in range(n):
#HumanOrgan.add(input(f'{x+1} Organ : '))
#OrganFunc.add(input('Its function : '))
    keyyyyy=input(f'{x+1} Organ : ')
    valueee=input(f'{keyyyyy} Function : ')
    OrganWork[keyyyyy]=valueee
print(OrganWork)
func=input('Function of a organ ')
#keyvals=[[v for v in OrganWork.keys() if OrganWork[v]==x] for x in OrganWork.values() if x==func]
keyvals=[keyyy for keyyy in OrganWork.keys() if OrganWork[keyyy]==func]
print(keyvals)
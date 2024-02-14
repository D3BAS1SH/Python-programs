MAIN_LIST=[2,4,1,7,6,8,9,11]
EvenList=[]
OddList=[]

for x in MAIN_LIST:
    if(x%2==0):
        EvenList.append(x)
    else:
        OddList.append(x)

print(MAIN_LIST)
print(EvenList)
print(OddList)
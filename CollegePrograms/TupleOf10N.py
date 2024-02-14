list1=[]

i=70
while(len(list1)!=10):
    if(i%70==0):
        list1.append(i)
    i+=70
print(tuple(list1))
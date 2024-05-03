Num=int(input("Number of Student : "))
Student=[]
for x in range(Num):
    print(f"{x+1} Student Info : ")
    name=input("NAME : ")
    gender=input("GENDER : ")
    age=input("AGE : ")
    Student.append((name,gender,age))
M=[x for x in Student if x[1]=="M" or x[1]=='m']
F=[x for x in Student if x[1]=="F" or x[1]=='f']

sortedListM=sorted(M,key=lambda x : x[2])
sortedListF=sorted(F,key=lambda x : x[2])

with open("./StudentSortedFile0.txt",'w+') as F:
    for x in sortedListF:
        F.write(f"{x[0]},{x[1]},{x[2]}\n")
    for x in sortedListM:
        F.write(f"{x[0]},{x[1]},{x[2]}\n")
    F.close()
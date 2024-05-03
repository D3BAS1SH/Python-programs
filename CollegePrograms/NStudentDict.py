def checkEmailId(x):
    mySpecs='`~!#$%^&*()-_=+{}[]|:;\"\',<>/?\\'
    
    if(x.count('@') != 1):
        return False
    
    for e in x:
        if(e in mySpecs):
            return False
        
    if('@gmail.com'in x):
        return True
    
    return False

Num=int(input("Number of input : "))
Student=dict()
x=0
while (x<Num):
    print(f"{x+1} Student info:->")
    name=input("NAME : ")
    phone=int(input("PHONE NUMBER : "))
    email=input("EMAIL : ")
    if(phone<=6000000000):
        print("Entry Rejected Due to invalid Phone number")
        continue
    if not checkEmailId(email):
        print("Entry Rejected Due to invalid Email address")
        continue
    Student[phone]=(name,email)
    x+=1

print(Student)
# 
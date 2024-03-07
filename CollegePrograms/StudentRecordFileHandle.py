FILE_NAME='StudentRecord'

try:
    FileOpen = open(f"{FILE_NAME}.txt",'a+')
except Exception as e:
    print("File Creation Failed Cause :",e)
else:
    print("File Openning Succesful.")
    FileOpen.close()

def Menu():
    print()
    print("1) Add Records.")
    print('2) Delete Student records.')
    print("3) Update Student Records.")
    print("4) Show Student Records.")
    print("5) Exit.")
    print()

def GetChoice():
    Menu()
    v = int(input("Your Choice : "))
    return v

# Adding records to File
def AddRecords():
    with open(f"{FILE_NAME}.txt",'a+') as File:
        AddMore=True
        StudentRec=[]
        while(AddMore):
            Name = input("Student Name : ")
            Roll = input("Student Roll : ")
            Cgpa = input("Student Cgpa : ")
            String=f"{Name},{Roll},{Cgpa}\n"
            print()
            Check = input("Want to add more records (Y/N) : ")
            if(Check == 'Y' or Check == "y"):
                StudentRec.append(String)
            else:
                StudentRec.append(String)
                AddMore=not AddMore
        File.writelines(StudentRec)
        print(f'\n{len(StudentRec)} Record Added...\n')
        File.close()
    return

# Delete Records from a file
def DeleteRecords():
    ShowRecords()
    WhichRecord=(input("Give the Roll Number you want to Delete : "))
    updateRec=[]
    with open(f'{FILE_NAME}.txt','r+') as F:
        AllRecs=F.readlines()
        print(AllRecs)
        for x in AllRecs:
            print("X :",x)
            myObj=x.strip().split(',')
            print("MyObj :",myObj)
            if(myObj[1]==WhichRecord):
                continue
            else:
                updateRec.append(f"{myObj[0]},{myObj[1]},{myObj[2]}\n")
    F.close()
    print(updateRec)
    with open(f"{FILE_NAME}.txt",'w') as V:
        V.writelines(updateRec)
    V.close()
    return

# Update Records from a file
def UpdateRecords():
    return

# Show Records.
def ShowRecords():
    with open(f'{FILE_NAME}.txt','r') as F:
        Array=F.readlines()
        print("\n\nRecord Number :",len(Array),'\n')
        for x in Array:
            Stud=x.strip().split(',')
            print(f"NAME : {Stud[0]}")
            print(f"ROLL : {Stud[1]}")
            print(f"CGPA : {Stud[2]}")
            print()
    F.close()
    return

ExitStatus=False
while(not ExitStatus):
    match GetChoice():
        case 1:
            AddRecords()
        case 2:
            DeleteRecords()
        case 3:
            UpdateRecords()
        case 4:
            ShowRecords()
        case 5:
            ExitStatus = not ExitStatus
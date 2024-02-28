class Student:
    def __init__(self,name="",age=0,cgpa=0,roll=0) -> None:
        self.__Name=name
        self.__Age=age
        self.__Roll=roll
        self.__Cgpa=cgpa
        pass
    def getName(self):
        return self.__Name
    def getAge(self):
        return self.__Age
    def getRoll(self):
        return self.__Roll
    def getCgpa(self):
        return self.__Cgpa
    def showStats(self):
        print()
        print('===========================================')
        print(f'NAME : {self.getName()}')
        print(f'AGE  : {self.getAge()}')
        print(f'ROLL : {self.getRoll()}')
        print(f'CGPA : {self.getCgpa()}')
        print('===========================================')
    pass

def SHOWINFO():
    print()
    print("1) Sort by Name.")
    print("2) Sort by Age .")
    print("3) Sort by Roll.")
    print("4) Sort by Cgpa.")
    print("5) Exit")
    print()

def GETCHOICE():
    SHOWINFO()
    x = int(input("Your CHOICE : "))
    return x
n = int(input("Number of student's info you want : "))

StudentList=[]

for x in range(n):
    print()
    name=str(input("Student Name : ")).capitalize()
    age =int(input("Student Age  : "))
    roll=int(input("Student Roll : "))
    cgpa=float(input("Student Cgpa : "))
    StudentList.append(Student(name,age,cgpa,roll))

ShallContinue = True

while(ShallContinue):
    match GETCHOICE():
        case 1:
            NameSort=sorted(StudentList,key=lambda v : v.getName())
            for x in NameSort:
                x.showStats()
        case 2:
            AgeSort=sorted(StudentList,key=lambda v : v.getAge())
            for x in AgeSort:
                x.showStats()
        case 3:
            RollSort=sorted(StudentList,key=lambda v : v.getRoll())
            for x in RollSort:
                x.showStats()
        case 4:
            CgpaSort=sorted(StudentList,key=lambda v : v.getCgpa())
            for x in CgpaSort:
                x.showStats()
        case 5:
            ShallContinue= not ShallContinue
            print("\nTHANK YA!")
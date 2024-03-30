class Student:
    age=20
    def __init__(self,name):
        self.Name=name
        pass
    def info(self):
        print(f"Name : {self.Name}, Age : {self.age}")
        pass
S=Student("Anjani")
S1=Student("Anshu")
S1.age=19
S.info()
S1.info()
Student.age=1002
S1.info()
S.info()
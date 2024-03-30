class Student:
    age=20
    def __init__(self,name):
        self.Name=name
        pass
    def info(self):
        print(f"Name : {self.Name}, Age : {self.age}")
        pass
S1=Student("Debasish")
S1.info()
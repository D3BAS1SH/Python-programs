class Student:
    age=20
    def __init__(self,name):
        self.Name=name
        pass
    def info(self):
        print(f"Name : {self.Name}, Age : {self.age}")
        pass
    @staticmethod
    def fun(x):
        print(f"Helloooo Studenats...!!{x.Name}")
    def WhoIsOlder(X,Y):
        if(X.age>Y.age):
            return X
        return Y

S=Student("Anjani")
S1=Student("Anshu")
S1.age=19
S.info()
S1.info()
Student.age=1002
S1.info()
S.info()
Cs=Student("Smarak")
Cs.info()
Student.fun(S)
Student.WhoIsOlder(S,S1).info()
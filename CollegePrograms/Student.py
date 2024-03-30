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

class Dog:
    def __init__(self,name,age,color):
        self.Name=name
        self.age=age
        self.Color=color
        pass
    def info(self):
        print(f"Name : {self.Name}, Age : {self.age}, Color : {self.Color}")

D= Dog("Tommy",4,"Black")
D1=Dog("Mickey",6,"Brown")

Student.WhoIsOlder(D,D1).info()

#There are 3 different types of animals one dog, one cat, and mouse.
#Cat having attribute name and private age.
#Dog Having private name and age and color.
#Mouse having attribute color and size in terms of length

#Create two objects from each class and check whether the Dog objects have same name as Cat object and Check whether the dog objects have same color as mouse object. 
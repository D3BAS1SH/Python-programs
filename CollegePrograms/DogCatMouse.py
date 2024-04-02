#There are 3 different types of animals one dog, one cat, and mouse.
#Cat having attribute name and private age.
#Dog Having private name and age and color.
#Mouse having attribute color and size in terms of length

#Create two objects from each class and check whether the Dog objects have same name as Cat object and Check whether the dog objects have same color as mouse object. 

class Cat:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def info(self):
        print(f"Name : {self.name}, Age : {self._age}")
    def getAge(self):
        return self._age
    def getName(self):
        return self.name

class Dog:
    def __init__(self,name,age,color):
        self._name=name
        self.age=age
        self.color=color
    def info(self):
        print(f"Name : {self._name}, Age : {self.age}, Color : {self.color}")
    def getAge(self):
        return self._name
    def getName(self):
        return self.age
    def getColor(self):
        return self.color

class Mouse:
    def __init__(self,color,size):
        self.color=color
        self.size=size
    def info(self):
        print(f"Color : {self.color}, Size : {self.size}")
    def getColor(self):
        return self.color
    def getSize(self):
        return self.size

D=Dog("Bob",20,"Brown")
C=Cat("Tom",17)
M=Mouse("Brown",15)

if D.getName()==C.getName():
    print(f"Dog {D.info()} have same name as Cat {C.info()}")
else:
    print(f"Dog {D.info()} have same name as Cat {C.info()}")

if D.getColor()==M.getColor():
    print(f"Dog {D.info()} have same color as Cat {C.info()}")
else:
    print(f"Dog {D.info()} have same color as Cat {C.info()}")
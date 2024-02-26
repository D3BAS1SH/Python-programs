# <pass> is a statement with no value or method nothing.
# in python .roll can contain a value as roll

class Student:
    def __init__(self,NAME='',ROLL=-1):
        self.name=NAME
        self.roll=ROLL
    pass

s=Student(ROLL=10)
print(s.roll)
print(s.name)

print(s.name,s.roll)

W=Student('Debasish')
print(W.name, W.roll)

# R=Student()
# print(isinstance(R.roll,int)) #TRUE
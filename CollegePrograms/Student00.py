#define a class student with members name ad roll no. kepe name private, inherit another class from student and two other members section & branch, where branch is private

class Student:
    def __init__(self,name='',roll=0):
        self.__name=name
        self.roll=roll
        pass
    def setName(self,name=''):
        self.__name=name
    def showStats(self):
        print()
        print("NAME :",self.__name)
        print("ROLL :",self.roll)
        print()
        pass
    pass

class CR(Student):
    def __init__(self,branch='',section='', name='', roll=0):
        self.__Branch=branch
        self.Section=section
        super().__init__(name, roll)
        pass
    
    def setBranch(self,branch=''):
        self.__Branch=branch
        pass

    def showStats(self):
        super().showStats()
        print("Branch : ",self.__Branch)
        print("Section : ",self.Section)
        print()
        pass
    pass

Me = Student('Debasish Sahu',23)
Him = CR('CSE','Genius','Anjani',10)

Him.showStats()
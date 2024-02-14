Student={}

for i in range(5):
    name=input(f'Studnet {i+1} Name : ')
    roll=input(f'Studnet {i+1} Roll : ')
    Student.update({roll:name})

myKeys=list(Student.keys())
myKeys.sort(reverse=True)

for x in myKeys:
    print(f'{x} Rollno is : {Student[x]} Student.')
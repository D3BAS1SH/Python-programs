""" myString=(str(input('Give a string : '))).split(' ')

myTask=[]

for x in myString:
    myTask.append((len(x),x))

myTask=sorted(myTask)

for x in myTask:
    print(x) """

myString=(str(input('Give a string : '))).split(' ')

myTask={len(x):x for x in myString}

myTaskKey=sorted(myTask)

for i in myTaskKey:
    print(f'{myTask[i]}',end=' ')
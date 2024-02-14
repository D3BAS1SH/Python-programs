import random

MAINLIST=['SUIII',2.5,1,4,3+2j,True,False]

randV= random.randint(0,len(MAINLIST)-1)

if isinstance(MAINLIST[randV],bool):
    print(f'{MAINLIST[randV]} is not a Integer.')
elif(isinstance(MAINLIST[randV],int)):
    print(MAINLIST[randV],"is a Integer.")
else:
    print(MAINLIST[randV],'is not a Integer.')
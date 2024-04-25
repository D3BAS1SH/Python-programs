import matplotlib.pyplot as PL

Data={
    1:['P','F','P'],
    2:['F','P','P'],
    3:['F','P','P'],
    4:['P','P','P'],
    5:['P','F','F'],
    6:['F','F','F'],
    7:['P','F','F'],
    8:['P','F','F'],
    9:['P','P','P'],
    10:['F','P','F']
}

atleastPass1=len([x for x,y in Data.items() if 'P' in y])
atleastPass2=len([x for x,y in Data.items() if y.count('P')>=2])
allPass=len([x for x,y in Data.items() if y.count('P')==3])
allFail=len([x for x,y in Data.items() if y.count('F')==3])

mySubjectData=[
    len([x for x,y in Data.items() if y[0]=='P']),
    len([x for x,y in Data.items() if y[1]=='P']),
    len([x for x,y in Data.items() if y[2]=='P']),
]

mySubjects=[
    "Python",
    "DAA",
    "COA"
]

PL.subplot(2,1,1)
PL.bar(["atleastPass1","atleastPass2","allPass","allFail"],[atleastPass1,atleastPass2,allPass,allFail],width=0.5)
PL.grid(True,axis='y')

PL.subplot(2,1,2)
PL.bar(mySubjects,mySubjectData,width=0.5)
PL.grid(True,axis='y')

PL.show()
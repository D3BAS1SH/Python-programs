myWord=input("The word you are finding : ")

with open("./myPrograms/RandomText.txt","r") as F0:
    print(F0.name)
    myData=F0.readlines()
    for i,lines in enumerate(myData):
        if(myWord in lines.split(" ")):
            print(f"{myWord} Found in the line\n:->{i,lines}")
    F0.close()
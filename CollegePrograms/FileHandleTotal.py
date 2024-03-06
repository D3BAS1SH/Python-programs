File=None
Fname=''
Exit=False
def Options():
    print()
    print("1) Create a file.")
    print("2) Add Friend Info to File.")
    print("3) Read Friend Info from File.")
    print("4) Search Info From File.")
    print("5) Exit.")
    print()

def GeChoice():
    Options()
    x = int(input("Your Choice : "))
    return x

def CreateFile():
    global File,Fname
    Fname = input("File Name (You don't need to add .txt at the end.) : ")
    try:
        File = open(f"./{Fname}.txt",'a+')
    except Exception as E:
        print("File Creation : Failed.\nReason :",E)
    print("File Creation : Success")
    #File.close()

def AddFriendInfo():
    name=input("Friend Name : ")
    nomb=input("Friend Numb : ")
    city=input("Friend City : ")
    try:
        File.write(f"{name},{nomb},{city}\n")
    except Exception as e:
        print("Writing Status : Failed\nReason :",e)
    print("Writing Status : Success.")
    # File.close()

def ReadAllDataFrom():
    global File
    File=open(f'{Fname}.txt','r')
    print(File.read())

def SearchInFile():
    return

while(not Exit):
    match GeChoice():
        case 1:
            CreateFile()
        case 2:
            AddFriendInfo()
        case 3:
            ReadAllDataFrom()
        case 4:
            SearchInFile()
        case 5:
            Exit = not Exit
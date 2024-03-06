FILEPATH='./CollegePrograms/CacheFiles'
File=None

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
    Fname = input("File Name (You don't need to add .txt at the end.) : ")
    File = open(f"{FILEPATH}/{Fname}.txt",'a+')
    print()
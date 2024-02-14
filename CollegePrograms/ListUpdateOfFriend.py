FRIEND_LIST=['Ankit','Hitesh','Syed','Anish','Debasish']

def Add(l):
    l.append(str(input('FRIEND NAME : ')))

def Remove(l,val):
    l.remove(val)

def Update(l,Val):
    newVal=str(input('NEW VALUE : '))
    l[l.index(Val)]=newVal

def Options():
    print()
    print("1 : Add Friend")
    print("2 : Remove Friend")
    print("3 : Update Friend")
    print("4 : Show Friend")
    print("5 : Exit")
    print()

def PrintVals(l):
    for x in l:
        print(x)

while(True):
    Options()
    chV=int(input('OPTION : '))
    if(chV==1):
        Add(FRIEND_LIST)
    elif(chV==2):
        PrintVals(FRIEND_LIST)
        WhichOne=str(input('VALUE YOU WANT TO REMOVE : '))
        Remove(FRIEND_LIST,WhichOne)
    elif(chV==3):
        PrintVals(FRIEND_LIST)
        WhichOne=str(input('WHICH ONE YOU WANT TO UPDATE : '))
        Update(FRIEND_LIST,WhichOne)
    elif(chV==4):
        PrintVals(FRIEND_LIST)
    elif(chV==5):
        break
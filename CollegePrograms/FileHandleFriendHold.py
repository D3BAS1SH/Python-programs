File=None
try:
    File=open('./CollegePrograms/CacheFiles/FriendInfo.txt','a+')
except Exception as e:
    print("Error Occured Because :",e)

ShallAddMore=True
while(ShallAddMore):
    name=input("Name : ")
    mobi=input("Mobile Number : ")
    city=input('City : ')
    try:
        File.write(f"{name},{mobi},{city}\n")
    except Exception as Ex:
        print("File Handle Failed :",Ex)
    Ch = input("Want to add more info of your Friends? (Y/N) : ")
    if Ch=='Y' or Ch.lower()=='y':
        continue
    else:
        ShallAddMore=False
print("Information of your friend is added....")
File.close()
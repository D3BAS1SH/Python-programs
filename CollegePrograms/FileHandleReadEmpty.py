File = None
try:
    File=open('./CollegePrograms/CacheFiles/FriendInfo.txt','r+')
except Exception as E:
    print(E)

print(File.read())

File.write("Say my  name")
#You can read a empty file.
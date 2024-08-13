# with open("./Hello.txt",'w') as F:
#     F.write("Sami")
#     F.close()

with open("./Hello.txt",'r+') as F:
    MyLine=F.readline()
    print(MyLine)
    F.seek(0)
    F.write("Satya Ranjan Pattanaik")
with open('./myPrograms/RandomText.txt',"r+") as F:
    
    print("****************")
    for x in F:
        """ print(F.readline()) """
        for word in x.split(' '):
            print(word)
    print("****************")
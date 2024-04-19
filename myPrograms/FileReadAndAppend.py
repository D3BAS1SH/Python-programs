with open('./myPrograms/RandomText.txt','r+') as File0:
    with open('./myPrograms/MyAppendedText.txt','a+') as File1:
        for x in File0:
            print(x)
            File1.write(x)
        File1.close()
    File0.close()
myV=input("Enter a string : ")
vowels="aeiouAEIOU"
VowelOccs={x:0 for x in vowels}

for x in myV:
    if(x in vowels):
        VowelOccs[x]=VowelOccs[x]+1
        print(VowelOccs[x])

print(VowelOccs)
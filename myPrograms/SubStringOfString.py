MyString=str(input("Give any String : "))
initialIndex=int(input("Initial Index : "))
FinalIndex=int(input("Final Index : "))
subString = MyString[initialIndex:FinalIndex+1]
print(f"Your sub string from {initialIndex} to {FinalIndex} : {subString}")
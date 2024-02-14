myString=list(input('GIVE A STRING : '))
alpha=0;digit=0;specialChar=0
for x in myString:
    if x.isalpha():
        alpha+=1
    elif x.isdigit():
        digit+=1
    else:
        specialChar+=1
print('SPECIAL CHARACTER : ',specialChar)
print('ALPHABET : ',alpha)
print('DIGIT : ',digit)
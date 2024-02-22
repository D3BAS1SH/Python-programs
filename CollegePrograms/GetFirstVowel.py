def getFirstVowel(STRING):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for x in STRING[::-1]:
        if x in vowels:
            return x
    return "NO VOUEELLL FOUNNDDD"
print(getFirstVowel("Debasish"))
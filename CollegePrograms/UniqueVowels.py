def UniqueVowelOnly(S):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    return set([x for x in S if x in vowels])

print(UniqueVowelOnly("The Quick Brown Fox Jump over a lazy  Dog. OOGy"))
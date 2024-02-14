MAIN_STRING='HELLO WORLD'
myCharList=list(set([x for x in MAIN_STRING]))
myCharOccr=[(MAIN_STRING.count(i),i) for i in myCharList]
print(myCharList)
print(myCharOccr)
myCharOccr=sorted(myCharOccr)
print(myCharOccr)
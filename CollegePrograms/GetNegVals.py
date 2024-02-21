#Define a function that returns all the negative integers in a give nlist.

def GetNegVals(L):
    return [x for x in L if isinstance(x,(int,float)) and x<0]

mainList=[1,-20,10,89,26,-15.909,-65,89,-23,100,'Hello',{'ded'},{'Test':10},[40,"no"],(4.56,13.44)]
print(GetNegVals(mainList))
#print( (lambda x : [ v for v in x if v<0])(mainList))
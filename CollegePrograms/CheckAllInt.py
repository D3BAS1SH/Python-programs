MAINLIST=[True,1,3,4,5,'Hello','Bye','Hitesh']
MAINLIST0=[1,2,True,3,4,110,871,1]

def CheckPureInt(L):
    if isinstance(L,(list,set,tuple,dict,str)):
        return "Pagal Hogaya he kya?"

    if len(L)==0:
        return "Nahh you dumb."
    for x in L:
        if isinstance(x,bool) or not isinstance(x,int):
            return False
    return True

print(CheckPureInt(000))


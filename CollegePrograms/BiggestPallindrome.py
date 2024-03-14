def CheckPallindrome(V):
    return V==V[::-1]

def GetBiggestPallindrome(WORD):
    bit=2
    PW=[]
    while(bit!=len(WORD)):
        for x in range(len(WORD)-bit+1):
            if(CheckPallindrome(WORD[x:x+bit])):
                PW.append(WORD[x:x+bit])
        bit+=1
    return PW[-1]
    

print(GetBiggestPallindrome("abcaddacdda"))
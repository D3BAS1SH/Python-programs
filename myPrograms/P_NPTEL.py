def threesquares(m):
    if m <= 0:
    	return False
    for p in range(int(m**0.5) + 1):
        for q in range(p + 1):
            for r in range(q + 1):
                if p**2 + q**2 + r**2 == m:
                    return True
    return False

  
def repfree(s):
    uniquelen = len(set(s))
    strlen = len(s)
    return(uniquelen == strlen)
  
  
def hillvalley(l):
    dect = False
    inc = False
    c = 0
    for i in range(len(l)-1):
        if c > 1:
            return False
        right = l[i+1]
        middle = l[i]
        diff = right - middle
        if diff > 0:
            if dect:
                c += 1
            inc = True
            dect = False
        elif diff < 0:
            if inc:
                c += 1
            dect = True
            inc = False
    if c == 1:
        return True
    return False
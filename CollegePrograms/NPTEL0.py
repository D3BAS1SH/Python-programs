def mystery(l,v):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))

print(mystery([22,14,19,65,82,55],1))
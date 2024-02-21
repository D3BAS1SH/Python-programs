#Define a function which will return list of strings which have the length less than 7 from a given list
def strlist(l):
    return [x for x in l if isinstance(x,str) and len(x)<7]
L=[5,123,44,0.17,"1235151",'Hellooooo','Dev','Himtesh','Hitesh','Messi',True,False,]
print(strlist(L))
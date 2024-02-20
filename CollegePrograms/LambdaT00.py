LOL=[[1,2],['Satya',3.5,1],[True,'Good',5,4.3]]
#Get0=[lambda LOL: [x[0] for x in LOL]]
#print(Get0[0](LOL))
list(map( lambda x:x[0],LOL))
print((lambda LOL: [x[0] for x in LOL])(LOL))
print(list(map( lambda x:x[0],LOL)))
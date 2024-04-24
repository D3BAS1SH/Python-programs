from matplotlib import pyplot as PL

D=dict()
D['Satya']=['Tea','COD',70]
D['Smarak']=['Tea','COD',82]
D['Arita']=['Coffee','Badminton',45]
D['Gayatri']=['Coffee','Ludo',60]

Tea=len(['Tea' for x,y in D.items() if 'Tea' in  y])
Coffee=len(['Coffee' for x,y in D.items() if 'Coffee' in  y])
print(Tea)
print(Coffee)

Games=[D[x][1] for x in D.keys()]
GameCounts=[Games.count(x) for x in set(Games)]
print(Games)
print(GameCounts)

PL.subplot(2,1,1)

PL.pie(GameCounts,labels=list(set(Games)))
PL.subplot(2,1,2)
PL.pie([Tea,Coffee],labels=['TEA','COFFEE'])

PL.show()
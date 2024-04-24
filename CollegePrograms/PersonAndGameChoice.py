from matplotlib import pyplot as PL

D=dict()
D['Satya']=['Tea','Football',70]
D['Smarak']=['Tea','COD',82]
D['Arita']=['Coffee','Badminton',45]
D['Gayatri']=['Coffee','Ludo',60]

Tea=len(['Tea' for x,y in D.items() if 'Tea' in  y])
Coffee=len(['Coffee' for x,y in D.items() if 'Coffee' in  y])
print(Tea)
print(Coffee)

PL.pie([Tea,Coffee],labels=['TEA','COFFEE'])

PL.show()
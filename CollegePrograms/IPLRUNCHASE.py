import matplotlib.pyplot as PL

def SeqSum(Ar):
    return [sum(Ar[:i]) for i in range(1,len(Ar)+1)]

Data={
    'RCB':[0,12,10,12,11,18,20,21,10,20,14],
    'SRH':[0,8,10,11,15,10,12,15,10,11,15]
}

PL.subplot(2,1,1)
PL.plot(list(range(1,len(Data['RCB'])+1)),Data['RCB'],marker='o',label="RCB")
PL.plot(list(range(1,len(Data['SRH'])+1)),Data['SRH'],marker='o',label="SRH")
PL.legend()
PL.grid(True)

PL.subplot(2,1,2)
PL.plot(list(range(1,6)),SeqSum(Data['RCB'][:5]),marker='s',label='RCB')
PL.plot(list(range(1,6)),SeqSum(Data['SRH'][:5]),marker='s',label='SRH')
PL.legend();PL.grid(True)
PL.show()
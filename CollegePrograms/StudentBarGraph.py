import matplotlib.pyplot as PL

Info={
    2:{
        'P10':60.5,
        'P12':70,
        'P16':65
    },
    3:{
        'P10':70.5,
        'P12':60.5,
        'P16':50
    },
    4:{
        'P10':80,
        'P12':75,
        'P16':61
    },
}

PL.figure(figsize=(6,6))
PL.ylim(0,100)
for x,y in Info.items():
    _Keys=list(y.keys())
    _Vals=list(y.values())
    PL.plot(_Keys,_Vals,marker='s',label=x)
    # PL.scatter(_Keys,_Vals,marker='s')
    print(_Keys)
    print(_Vals)
    print()
PL.legend()
PL.xlabel("Exams")
PL.ylabel("Percentage")
PL.grid(True)
PL.show()

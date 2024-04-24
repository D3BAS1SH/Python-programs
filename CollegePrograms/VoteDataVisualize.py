from matplotlib import pyplot as PL

Data={
    1:[20,'M',50,'Football'],
    2:[22,'F',55,'Football'],
    3:[18,'F',58,'Cricket'],
    4:[16,'F',60,'Badminton'],
    5:[15,'M',45,'Chess'],
}

Roll=list(Data.keys())
Age=[Data[x][0] for x in Data]
Gender=[Data[x][1] for x in Data]
Weight=[Data[x][2] for x in Data]
GameLike=[Data[x][3] for x in Data]

VoteEligibility=[len([x for x in Age if x>=18]),len([x for x in Age if x<18])]
PL.subplot(2,3,1)
PL.pie(VoteEligibility,labels=["Eligibel","Not Eligible"],autopct='%1.1f%%')

MassGender=[Gender.count('M'),Gender.count('F')]
PL.subplot(2,3,2)
PL.pie(MassGender,labels=['M','F'],autopct='%1.1f%%')

PL.subplot(2,3,3)
PL.bar(Roll,Weight,width=0.5)

PL.subplot(2,3,5)
GameLikeCount=[GameLike.count(x) for x in set(GameLike)]
PL.pie(GameLikeCount,labels=list(set(GameLike)),autopct='%1.1f%%')

PL.show()
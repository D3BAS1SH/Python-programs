count = 0
myPals=[]
while(count<5):
    V=input("Enter a pallindrome String : ")
    if(V==V[::-1]):
        myPals.append(V)
        count+=1
    else:
        print(f"Given String {V} is not Pallindrome")

for x in myPals:
    print(x)
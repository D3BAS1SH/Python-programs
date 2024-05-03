batsman=dict()

n=int(input("Number of lengthb : "))

print("Now give values as Batsman_name-runs_he_made-balls_he_played-sixes-fours")
for x in range(n):
    myValue=tuple(input(f"{x+1}) Player : ").split('-'))
    batsman[myValue[0]]=(myValue[1],myValue[2],myValue[3],myValue[4])
print(batsman)
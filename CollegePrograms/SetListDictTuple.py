wd={}

weekdays=(
    "Sunday",
    "Monday",
    "Tuesday",
    "Thursday",
    "Friday",
    "Saturday"
)

for x in weekdays:
    wd[x]=input(f"Enter your color for {x} : ")

print(wd)

sColor= input("THe color you want to search : ")

myList=[x for x,y in wd.items() if y==sColor]

print(f"{len(myList) and myList}")

""" for x,y in wd.items():
    if(y==sColor):
        print(x) """


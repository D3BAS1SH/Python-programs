mainStr=input("A String : ")
if mainStr.lower() == mainStr[::-1].lower():
    print(f"{mainStr} is pallindrome sentence.")
else:
    print(f"{mainStr} is not pallindrome sentence.")
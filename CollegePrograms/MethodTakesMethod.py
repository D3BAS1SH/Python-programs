def GreetDay():
    return "Morning"
def GreetNight():
    return 'Night'
def GreetEvening():
    return 'Evening'

def GetName():
    return "JOHN"

def GreetF(GT,GN):
    print("GOOD",GT(),GN())

GreetF(GreetEvening,GetName)
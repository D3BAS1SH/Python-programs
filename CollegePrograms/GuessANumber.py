import random

rand=random.randint(1,100)

while(True):
    num=int(input('Guess a number : '))
    if(num==rand):
        print("\nBravo Bravo kiddo.\n")
        break
    elif(num>rand):
        print("You are going higher than the number.")
    else:
        print('You are going Lower than the number.')
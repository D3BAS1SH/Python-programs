def SumOfDigitOf(x):
    sum = 0
    while(int(x) >0):
        # print(sum)
        sum += x%10
        x=x//10
    return sum

for x in range(100,200):
    if(SumOfDigitOf(x)%2==0):
        print(x)
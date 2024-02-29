def fact(n):
    try:
        if isinstance(n,bool):
            raise Exception("The Value is type of Boolean")
        elif isinstance(n,(str,float,list,tuple,dict,set)):
            raise Exception(f"The Input Contains {type(n)}")
        elif n < 0:
            raise Exception("Can't get factorial of a negative number.")
    except Exception as e:
        print("Error Exception due to : ",e)
    else:
        if(n==1 or n==0):
            return 1
        else:
            return n*fact(n-1)

print(fact(0))
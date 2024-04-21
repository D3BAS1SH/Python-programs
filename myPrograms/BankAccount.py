class BankAccount:
    account_number=10000000000000
    def __init__(self,name,DOO=(0,0,0)):
        BankAccount.account_number+=1
        
        self.__AccountNum=BankAccount.account_number
        self.__Name=name
        self.__DateOfOpen=DOO
        self.__balance=0
        
        pass
    def Deposit(self,Money):
        self.__balance+=Money
        pass
    def Withdraw(self,amount):
        if self.__balance==0:
            return f"Account balance : {self.__balance}. Can't Withdraw"
        self.__balance-=amount
        pass
    def CheckBalance(self):
        return self.__balance
    pass

Dev=BankAccount("Debasish",(19,12,2004))
Dev.Deposit(500000)
print(Dev.CheckBalance())
Dev.Withdraw(100000)
print(Dev.CheckBalance())
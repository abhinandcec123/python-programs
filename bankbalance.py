class bank:
    def __init__(self,amount,balance):
        self.amount=amount
        self.balance=balance

    def deposit(self):
        return self.balance+self.amount

    def withdrawal(self):
        return self.balance-self.amount
balance=0
deposit=int(input("Enter the deposit:"))
print(deposit,"rupees credited to your account")
withdrawal=int(input("Enter the amount to withdraw"))
if(balance!=0):
    print("Insufficient Balance")
if(withdrawal>deposit):
    print("Insufficient Balance")
else:
    print("Collect your cash")
    


class bankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


b1 = bankAccount("rim",1000)

b1.deposit(500)
print("balance after deposit: ",b1.get_balance())

b1.withdraw(300)
print("balance after withdrawal: ",b1.get_balance())

print(b1.get_balance())
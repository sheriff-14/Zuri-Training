class Budget:
    def __init__(self,category):
        self.category = category

    def deposit(self,amount,Category):
        print("you have deposited",amount,"to",Category)

    def withdraw(self,amount,Category):
        print("You have withdrawn",amount,"from",Category)

    def transfer(self,amount,Category):
        print("You have transfered",amount,"to",Category)


    def checkBalances(self,amount,Category):
        print("Your balance in",Category,"is",amount)


mybudget = Budget("Any")
mybudget.deposit(111,"rent")
mybudget.withdraw(102,"clothing")
mybudget.transfer(100,"entertainment")
mybudget.checkBalances(150,"food")
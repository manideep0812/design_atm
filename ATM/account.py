class Account:
    def newAccount(self,accountNumber,ibalance):
        self.accountNumber = accountNumber
        self.balance = ibalance
    def getBalance(self):
        return (self.balance)
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount)
            print("New Balance is",self.balance)
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn",amount)
            print("Upadated balance",self.balance)
        else:
            return "Insufficient balance or invalid amount"
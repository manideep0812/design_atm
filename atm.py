from abc import ABC,abstractmethod
class Account:
    def newAccount(self,name,phone,accountNumber,accountType,cardNumber,cardPin,ibalance):
        self.name = name
        self.phoneNumber = phone
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.cardNumber = cardNumber
        self.cardPin = cardPin
        self.balance = ibalance
    def getBalance(self):
        return (self.balance)
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return self.balance
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance or invalid amount"
        
class IaccountSelection(ABC):
    @abstractmethod
    def run(self):
        pass

class savingAccountStrategy(IaccountSelection):
    def run(self):
        print("you selected savings account")

class currentAccountStrategy(IaccountSelection):
    def run(self):
        print("you selected current account")

class accountSelection(IaccountSelection):
    def __init__(self,account_strategy:IaccountSelection=None):
        self.account_strategy = account_strategy
    def setAccountStrategy(self,strategy:IaccountSelection):
        self.account_strategy = strategy
    def run(self):
        if self.account_strategy is not None:
                self.account_strategy.run()

class Pinverification:
    def __init__(self):
        print("pin verification successfull")


class Itransaction(ABC):
    @abstractmethod
    def doTransaction(self):
        pass
class withDraw(Itransaction,Account):
    def doTransaction(self,account,amount):
        account.withdraw(amount)
class deposit(Itransaction,Account):
    def doTransaction(self,account,amount):
        account.deposit(amount)
class selectTrans(Itransaction,Account):
    def __init__(self,transaction_type:Itransaction=None):
        self.transaction_type = transaction_type
    def setTransactionType(self,transactionType:Itransaction):
        self.transaction_type = transactionType
    def doTransaction(self,account,amount):
        self.transaction_type.doTransaction(account,amount)

class sendNotification():
    def send(self,account):
        print("Your current balance is",account.getBalance())
        print("Notification sent!!")

class Idlestate:
    def __init__(self):
        print("sitting in idle state")
        Pinverification()


class ATM:
    def __init__(self,accounts):
        self.accounts = accounts
    def start(self):
        Idlestate()

accounts = []
account1 = Account()
account1.newAccount("Manideep",9849221570,123456789,"Savings",12345,1234,10000)
account2 = Account()
account2.newAccount("Ramu",9849221571,987654321,"Current",54321,4321,5000)
accounts=[account1,account2]

accountType = accountSelection()
transaction = selectTrans()
notification = sendNotification()
atm = ATM(accountType,transaction,notification)

accountType.setAccountStrategy(currentAccountStrategy())
transaction.setTransactionType(withDraw())

atm.start()
transaction.doTransaction(account1,1000)
accountType.run()

notification.send(account1)



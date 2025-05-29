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
        
class AccountSelection:
    def __init__(self):
        print("please select type of account:")
        print("1.Savings            2.Current")
    def accountSelection(self,selectedOption):
        if selectedOption == 1:
            print("You selected savings account")
        else:
            print("You selected current account")
        pinVerify=Pinverification()
        pinVerify.verify(accounts)

class Pinverification:
    def verify(self, accounts):
        cardNumber = int(input("Please enter you card number: "))
        for account in accounts:
            if account.cardNumber == cardNumber:
                print("Card number accepted...now please pin...")
                pin = int(input("Enter pin: "))
                if account.cardPin == pin:
                    transaction = Transactiontype()
                    transaction.transaction(account)
                else:
                    print("Incorrect PIN")
                    return
        return

class Transactiontype(Account):
    def transaction(self,account):
        print("please select type of transaction type:")
        print("1.withdrawal            2.deposit")
        option = int(input("Enter your option: "))
        amount = int(input("Enter the amount: "))
        if option == 1:
            account.withdraw(amount)
        else:
            account.deposit(amount)
        sendNotification(account)


class sendNotification:
    def __init__(self,account):
        print("Your current balance is",account.getBalance())
        print("Notification sent!!")

class ATM:
    def __init__(self,accounts):
        self.accounts = accounts
    def start(self):
        accSelect = AccountSelection()
        accSelect.accountSelection(int(input()))

accounts = []
account1 = Account()
account1.newAccount("Manideep",984920,123456789,"Savings",12345,1234,10000)
account2 = Account()
account2.newAccount("Ramu",984921,987654321,"Current",54321,4321,5000)
accounts=[account1,account2]
atm = ATM(accounts)
atm.start()
print("------------------new transaction------------------")
atm.start()

## enter card number = 12345 and pin = 1234 to select account1
## enter card number = 54321 and pin = 4321 to select account2
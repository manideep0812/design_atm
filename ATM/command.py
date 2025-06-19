from abc import ABC
from account import Account
class ITransactionCommand(ABC):
    def execute(self):
        pass

class withDrawCommand(ITransactionCommand):
    def __init__(self,account:Account,amount) -> None:
        self.account=account
        self.amount =amount
    def execute(self):
        self.account.withdraw(self.amount)

class depositCommand(ITransactionCommand):
    def __init__(self,account:Account,amount) -> None:
        self.account=account
        self.amount =amount
    def execute(self):
        self.account.deposit(self.amount)

class getBalanceCommand(ITransactionCommand):
    def __init__(self,account:Account) -> None:
        self.account=account
    def execute(self):
        self.account.getBalance()

        
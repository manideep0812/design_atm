from abc import ABC
from command import ITransactionCommand
class IAccountStrategy(ABC):
    def processTransaction(self,command:ITransactionCommand):
        pass

class savingAccountStrategy(IAccountStrategy):
    def processTransaction(self,command:ITransactionCommand):
        print("You selected Savings Account")
        command.execute()
        

class currentAccountStrategy(IAccountStrategy):
    def processTransaction(self,command:ITransactionCommand):
        print("You selected Current Account")
        command.execute()
        
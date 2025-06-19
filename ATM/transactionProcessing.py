from abc import ABC

from accountStrategy import IAccountStrategy
from command import ITransactionCommand
class ITransactionProcessing(ABC):
    def setStrategy(self,strategy:IAccountStrategy) -> None:
        pass
    def setCommand(self,command:ITransactionCommand) -> None:
        pass
    def execute(self) -> None:
        pass

class transactionProcessor(ITransactionProcessing):
    # strategy:IAccountStrategy
    # command:ITransactionCommand
    def setStrategy(self,strategy:IAccountStrategy) -> None:
        self.strategy = strategy
    def setCommand(self, command: ITransactionCommand) -> None:
        self.command=command
    def execute(self) -> None:
        self.strategy.processTransaction(self.command)

        

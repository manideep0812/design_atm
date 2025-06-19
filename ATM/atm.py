from atmstate import IAtmStateManager, atmStateManager
from transactionProcessing import ITransactionProcessing


class ATM:
    def __init__(self,stateManager:IAtmStateManager,transactionProcessor:ITransactionProcessing) -> None:
        self.stateManager = stateManager
        self.transactionProcessor = transactionProcessor

    def start(self)->None:
        self.stateManager.handleState(self)
        
    def performTransaction(self) -> None:
        self.transactionProcessor.execute()


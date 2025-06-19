from abc import ABC
class IAtmState(ABC):
    def handle(self,atm):
        pass

class IAtmStateManager(ABC):
    def setState(self,state:IAtmState):
        pass
    def handleState(self,context):
        pass

class atmStateManager(IAtmStateManager):
    def __init__(self):
        self.state=idleState()
        pass
    def setState(self, state: IAtmState):
        self.state = state
    def handleState(self, context):
        self.state.handle(context)
        
class idleState(IAtmState):
    def handle(self, atm):
        print("card Inserted... moving to pin verification")
        atm.stateManager.setState(pinVerificationStatusState())
        atm.start()

class pinVerificationStatusState(IAtmState):
    def handle(self, atm ):
        print("pin verification successful...Moving to trans selection")
        atm.stateManager.setState(transactionSelectionState())
        atm.start()

class transactionSelectionState(IAtmState):
    def handle(self, atm):
        print("Entered in transaction Selection state")
        atm.stateManager.setState(transactionExecutionState())
        atm.start()

class transactionExecutionState(IAtmState):
    def handle(self, atm):
        print("Entered in transaction execution state")
        atm.stateManager.setState(ejectCardState())
        atm.start()

class ejectCardState(IAtmState):
    def handle(self, atm):
        print("Transaction Completed!!!")
        print("Thanks you")
        atm.stateManager.setState(idleState())
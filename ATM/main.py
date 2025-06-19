from atm import ATM
from account import Account
from atmstate import atmStateManager
from command import withDrawCommand
from transactionProcessing import transactionProcessor
from accountStrategy import savingAccountStrategy


account=Account()
account.newAccount(12345,10000)

stateManager= atmStateManager()

transactionProcess = transactionProcessor()

atm = ATM(stateManager,transactionProcess)

transactionProcess.setStrategy(savingAccountStrategy())
transactionProcess.setCommand(withDrawCommand(account,2000))

atm.start()
transactionProcess.execute()



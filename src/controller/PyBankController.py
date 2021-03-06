from src.model.Account import Account
from src.utility.InputValidatorUtility import InputValidatorUtility
from src.service.PyBankService import PyBankService

import sys


class PyBankController:

    userAccounts = {}
    failedAttempt: int = 0

    service: PyBankService = PyBankService()

    def __init__(self):
        pass

    def startPyBank(self):
        self.displayOptions()
        #acc: Account = Account(1, 'name', 'add1', 'add2', 0, 0)
        #acc.getAccountDetails()

    def performOperation(self, value):
        if not value == 8:
            if value == 1:
                pass
            elif value == 2:
                pass
            elif value == 3:
                pass
            elif value == 4:
                pass
            elif value == 5:
                pass
            elif value == 6:
                self.closeAccount()
            elif value == 7:
                pass
        else:
            print("Thank you for banking with us.")
            sys.exit(0)

    def displayOptions(self):
        print("*************************")
        print("--- Welcome to PyBank ---")
        print("*************************")
        print("1. Add Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Update Details")
        print("5. Display Account Details")
        print("6. Close Account")
        print("7. Chat with Representative")
        print("8. Exit")

        userInput = input("Enter option: ")

        validator = InputValidatorUtility()
        validationResult = validator.mainMenuInputValidator(userInput)

        if validationResult == "valid":
            self.performOperation(int(userInput))
        else:
            self.failedAttempt = self.failedAttempt + 1
            if self.failedAttempt > 3:
                print("You have exceeded attempt limit. Bank will now close.")
            else:
                print(validationResult, "\nPlease try again")
                self.displayOptions()

    def closeAccount(self):
        print(self.service.closeAccount(self.userAccounts, 1234))
        pass

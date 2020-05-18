class PyBankService:

    def closeAccount(self, userAccounts, accNo):
        print(self.anyUserExist(userAccounts))
        pass

    def anyUserExist(self, userAccounts):
        return not len(userAccounts.keys()) == 0

class Account:

    def __init__(self, accNo, name, add1, add2, contact, bal):
        self.accNo = accNo
        self.name = name
        self.add1 = add1
        self.add2 = add2
        self.contact = contact
        self.bal = bal

    def getAccountDetails(self):
        print("Account Number: ", self.accNo)
        print("Account Holder: ", self.name)
        print("Address Line 1: ", self.add1)
        print("Address Line 2: ", self.add2)
        print("Contact Number: ", self.contact)
        print("Avail  Balance: ", self.bal)

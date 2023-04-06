class Bank:
    bank_name = ""
    bank_branch_name = ""
    bank_ifsc_code = ""

    def __init__(self, name, branch_name, ifsc_code):
        self.bank_name = name
        self.bank_branch_name = branch_name
        self.bank_ifsc_code = ifsc_code

    def get_bank_details(self):
        return f"Bank name: {self.bank_name}\nBank Branch: {self.bank_branch_name}\nIFSC Code: {self.bank_ifsc_code}"

# testing
# statebank = Bank("State Bank", "Dildar Nagar", "g5ki1")
# # print(dir(statebank))
# # print(statebank.bank_branch_name)
# print(statebank.get_bank_details())

# unionbank = Bank("Union Bank", "Zamania", "dh6w9")
# print(unionbank.bank_name)

# bank1, bank2, bank3, bank4, bank5
for i in range(5):
    x = "bank" + str(i+1)
    bank_name = input("Enter your bank name")
    bank_branch_name = input("Enter your bank branch")
    bank_ifsc_code = input("Enter your ifsc code")
    x = Bank(bank_name, bank_branch_name, bank_ifsc_code)
    print(x.get_bank_details())
    print('*'*10)




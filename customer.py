class Customer:
    customer_name = "";
    customer_id = "";
    balance = 0;

    def __init__(self, name, id):
        self.customer_name = name
        self.customer_id = id
        self.balance = 1000 #default balance
    
    def deposit(self, amount_deposit):
        self.balance = self.balance + amount_deposit
        print(self.balance)

    def withdrawl(self, amount_withdrawl):
        if self.balance >= amount_withdrawl:
            self.balance = self.balance - amount_withdrawl
            print("Amount Withdrawl is Successful\nYour Current Balance is: ")
            print(self.balance)
        else:
            print("Insufficient Balance\nYour Balance is: " + str(self.balance))
    

rohit = Customer("Rohit Sharma", 9839990849)

while True:
    print("Enter the no:\n1. for withdrawl\n2. for deposit\n3. for balance check\n4. 0 for quit")
    number = int(input())
    if number == 1:
        print("Enter the Amount you want to withdraw: ")
        amount_withdrawl = int(input())
        rohit.withdrawl(amount_withdrawl)

    elif number == 2:
        print("Enter the Amount you want to deposit: ")
        amount_deposit = int(input())
        print("Money Deposited\nYour amount is: ")
        rohit.deposit(amount_deposit)

    elif number == 3:
        print("Your Balance is: ")    
        print(rohit.balance)
    elif number == 0:
        break
    else:
        print("Invalid Key");   






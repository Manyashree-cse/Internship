class BankAccount:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount},balance is {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"withdraw {amount},balance is {self.balance}")
        else:
            print("insufficient balance")

    def display_balance(self):
        print(f"current balance: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self,interest_rate,account_holder):
        self.interest_rate=interest_rate
        super().__init__(account_holder)
    
    def add_interest(self):
        interest=(self.balance*self.interest_rate)/100
        self.balance+=interest
        print(f"the interest is {interest}, the balance is {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit,account_holder):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_holder)

    def withdraw_with_overdraft(self,amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn using overdraft: ₹{amount},balance is {self.balance}")
        else:
            print("Overdraft limit exceeded")

bank3=CurrentAccount(200,"manya")
bank3.deposit(1000)
bank3.withdraw_with_overdraft(1200)

# bank1=BankAccount("manya")
# bank1.deposit(1000)
# bank1.withdraw(1000)
# bank1.display_balance()

# bank2=BankAccount("manya")
# bank2.deposit(1000)
# bank2.withdraw(500)

# bank2=SavingAccount(10,"manya")
# bank2.deposit(1000)
# bank2.withdraw(500)
# bank2.add_interest()
# bank2.deposit(1000)
# bank2.display_balance()
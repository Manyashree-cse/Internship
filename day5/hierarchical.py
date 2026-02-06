class BankAccount:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"withdraw {amount}")
        else:
            print("insufficient balance")

    def display_balance(self,amount):
        print("current balance {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self,interest_rate,account_holder,balance):
        self.interest_rate=interest_rate
        super().__init__(account_holder,balance)
    
    def add_interest(self):
        interest=(sself.balance*interest_rate)/100
        self.balance+=interest
        print("the interest is:",interest)

class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit,account_holder,balance):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_holder,balance)

    def withdraw_with_overdraft(self,amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn using overdraft: ₹{amount}")
        else:
            print("Overdraft limit exceeded")

s = SavingsAccount("Anita", 5000, 5)
s.deposit(1000)
s.add_interest()
s.withdraw(2000)
s.display_balance()
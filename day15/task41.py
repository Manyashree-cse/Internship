class BankAccount:
    def __init__(self):
        self.account_holder=""

acc = BankAccount()
acc.account_holder = "Alice"
print(acc.account_holder)
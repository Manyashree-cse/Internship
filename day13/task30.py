class BankAccount:
    def __init__(self, initial_balance):
        self.__balance=initial_balance

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print(f"Withdrawal successful. Remaining balance: {self.__balance}")
        else:
            print(f"Insufficient funds. Balance remains: {self.__balance}")

acc = BankAccount(1000)
acc.withdraw(200)
acc.withdraw(900)
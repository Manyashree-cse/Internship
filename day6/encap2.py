class BankAccount:
    account_holder_name="unknown"
    __account_type="savings"

    def __init__(self,pin):
        self.__pin=pin
        self.__balance=0
    def set_pin(self,new_pin):
        self.__pin=new_pin
        print('pin is set')
    def get_pin(self):
        return self.__pin
    def verify_pin(self,new_pin):
        return new_pin==self.__pin
        # if new_pin==self.__pin:
        #     return "correct pin"
        # else:
        #     return "incorrect pin"
    def get_balance(self,new_pin):
        if self.verify_pin(new_pin):
            return self.__balance
        else:
            return "incorrect pin"
    def set_balance(self,amount,pin):
        if self.verify_pin(pin):
            self.__balance+=amount
            print("updated balance:",self.__balance)
        else:
            print("enter valid pin")

BA=BankAccount(1234)
BA.account_holder_name="manya"
print(BA.account_holder_name)
BA.set_pin(2244)
print(BA.get_pin())
print(BA.get_balance(2244))
BA.set_balance(200,2248)

#print(BA.verify_pin(224))

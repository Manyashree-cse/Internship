from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self,amount):
        return f"Paid {amount} using Credit Card"

class UPI(PaymentMethod):
    def pay(self,amount):
        return f"Paid {amount} using UPI"

cc = CreditCard()
upi = UPI()
print(cc.pay(1500))
print(upi.pay(500))
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class StripePayment(PaymentGateway):
    def pay(self, amount):
        return f"Paid ₹{amount} using Stripe"

class PaytmPayment(PaymentGateway):
    def pay(self, amount):
        return f"Paid ₹{amount} using Paytm"

stripe = StripePayment()
print( stripe.pay(100))
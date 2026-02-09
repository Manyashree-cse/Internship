class Payment:
    def pay(self):
        print("payment system")
class GooglePay(Payment):
    def pay(self):
        print("googlpay")
class PhonePay(Payment):
    def pay(self):
        print("phonepay")
class CreditCard(Payment):
    def pay(self):
        print("creditcard")

obj1=GooglePay();
obj1.pay()
obj2=PhonePay();
obj2.pay()
obj3=CreditCard();
obj3.pay()

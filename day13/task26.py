class DeliveryBot:
    def status(self):
        return "Package en route." 

class FastDeliveryBot(DeliveryBot):
    def status(self):
        return "Package arriving in 5 minutes!"

basic = DeliveryBot()
fast = FastDeliveryBot()
print(basic.status())
print(fast.status())
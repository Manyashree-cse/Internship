class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        self.discount_percent = discount_percent
        if discount_percent == 0:
            discounted_price = price
        else:
            discounted_price = price - (price * discount_percent / 100)
        super().__init__(name, discounted_price)

    def get_discounted_price(self):
        return self.price

p1 = DiscountedProduct("Phone", 100, 5)
print(p1.get_discounted_price())
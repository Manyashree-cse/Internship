class Product:
    def __init__(self, name, stock):
        self.name=name
        self._stock=stock

    def sell(self, quantity):
        if quantity<=self._stock:
            self._stock-=quantity
            return f"Sold {quantity} units of {self.name}"
        else:
            return "Insufficient stock"

    def get_stock(self):
        return self._stock

p = Product("Laptop", 10)    
p.sell(3)   
p.sell(8)   
print(p.get_stock())
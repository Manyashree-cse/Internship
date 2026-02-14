class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        self.doors=doors
        super().__init__(brand,model)

    def description(self):
            return f"{self.brand} {self.model} with {self.doors} doors."

class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        self.engine=engine
        super().__init__(brand,model)

    def description(self):
        return f"{self.brand} {self.model} with {self.engine} engine."

c1 = Car("Toyota", "Camry", 4)
print( c1.description())
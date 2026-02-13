class Product:
    def __init__(self, name, **kwargs):
        self.name=name
        super().__init__(**kwargs)

class DigitalProduct(Product):
    def __init__(self, name, size, **kwargs):
        self.size=size
        Product.__init__(self,name)

class PhysicalProduct(Product):
    def __init__(self, name, weight, **kwargs):
        self.weight=weight
        Product.__init__(self,name)

class HybridProduct(DigitalProduct, PhysicalProduct):
    def __init__(self, name, size, weight):
        DigitalProduct.__init__(self,name,size)
        PhysicalProduct.__init__(self,name,weight)

    def details(self):
        return f"{self.name} includes {self.size} digital files and weighs {self.weight}."

hp1 = HybridProduct("Python Mastery", "2GB", "1kg")
print( hp1.details())

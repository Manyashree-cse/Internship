class Animal:
    def __init__(self, category):
        self.category=category

class Mammal(Animal):
    def __init__(self, category, temperature):
        self.temperature=temperature
        super().__init__(category)

class Dog(Mammal):
    def __init__(self, category, temperature, breed):
        self.breed=breed
        super().__init__(category,temperature)

    def describe(self):
        return f"This is a {self.breed}. It is a {self.temperature} {self.category}."

d1 = Dog("Animal", "Warm-blooded", "Husky")
print( d1.describe())
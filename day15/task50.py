from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Movable):
    def move(self):
        return "Car is driving"

class Bike(Movable):
    def move(self):
        return "Bike is riding"

c = Car()
print( c.move())

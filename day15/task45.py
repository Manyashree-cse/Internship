from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_speed(self):
        pass

class Car(Vehicle):
    def __init__(self, speed):
        self.speed = speed
    def get_speed(self):
        return f"Car is moving at {self.speed} km/h"

class Bike(Vehicle):
    def __init__(self, speed):
        self.speed = speed
    def get_speed(self):
        return f"Bike is moving at {self.speed} km/h"

c = Car(80)
b = Bike(40)
print(c.get_speed())
print(b.get_speed())
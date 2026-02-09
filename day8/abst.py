from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("car engine started")
    def conc1(self):
       print("hi")
class Bike(Vehicle):
    def start_engine(self):
        print("bike engine started")
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")
c=Car()
c.start_engine()
# c=Car()
# c.conc1()
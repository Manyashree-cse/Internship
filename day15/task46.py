from abc import ABC, abstractmethod

class Robot(ABC):
    @abstractmethod
    def perform_task(self):
        pass

class CleaningRobot(Robot):
    def perform_task(self):
        return "Cleaning in progress"   

class DeliveryRobot(Robot):
    def perform_task(self):
        return "Delivering items"

# Test
r1 = CleaningRobot()
r2 = DeliveryRobot()
print(r1.perform_task())
print(r2.perform_task())

r1 = CleaningRobot()
assert r1.perform_task()
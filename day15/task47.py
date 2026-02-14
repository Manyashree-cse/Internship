from abc import ABC, abstractmethod

class ControllableDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(ControllableDevice):
    def turn_on(self):
        return f"Smart Light is now ON"

class SmartFan(ControllableDevice):
    def turn_on(self):
        return f"Smart Fan is now ON"

light = SmartLight()
print( light.turn_on())
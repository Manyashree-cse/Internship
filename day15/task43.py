from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side*self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return self.radius*self.radius*math.pi

s = Square(4)
r = Rectangle(3, 5)
c = Circle(7)
print(s.calculate_area())
print(r.calculate_area())
print(c.calculate_area())
from abc import ABC, abstractmethod

class Window(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def calculate_area(self):
        pass

class SquareWindow(Window):
    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side
    def calculate_area(self):
        return self.side*self.side

class RectangleWindow(Window):
    def __init__(self, length, width, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width

sq = SquareWindow(6)
rc = RectangleWindow(3, 9)
print(sq.calculate_area())
print(rc.calculate_area())
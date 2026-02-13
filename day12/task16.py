class Developer:
    def code(self):
        return f"{self.name} is coding"

class Designer:
    def design(self):
        return f"{self.name} is designing"

class HybridWorker(Developer, Designer):
    def __init__(self, name):
        self.name=name
        super().__init__()

h1 = HybridWorker("Ava")
print( h1.code())
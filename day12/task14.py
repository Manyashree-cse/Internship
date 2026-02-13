class Platform:
    def __init__(self, name):
        self.name=name

class Course(Platform):
    def __init__(self, name, title):
        self.title=title
        super().__init__(name)

class Module(Course):
    def __init__(self, name, title, module_name):
        self.module_name=module_name
        super().__init__(name, title)

    def full_title(self):
        return f"'{self.module_name}' is a module in '{self.title}' course on {self.name}"

m1 = Module("Udemy", "Python Bootcamp", "Functions")
print( m1.full_title())
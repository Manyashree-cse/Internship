class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email

class Instructor(User):
    def __init__(self, name, email, course):
        self.course=course
        super().__init__(name, email)

    def role(self):
        return f"{self.name} ({self.email}) teaches {self.course}."

class Learner(User):
    def __init__(self, name, email, course):
        self.course=course
        super().__init__(name, email)

    def role(self):
        return f"{self.name} ({self.email}) is enrolled in {self.course}."

i1 = Instructor("Arjun", "arjun@edu.com", "Python")
print( i1.role())
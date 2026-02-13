class Person:
    def __init__(self, name, **kwargs):
        self.name=name
        super().__init__(**kwargs)

class Faculty(Person):
    def __init__(self, name, subject, **kwargs):
        self.subject=subject
        Person.__init__(self,name)

    def teach(self):
        return "Faculty Teach"

class Staff(Person):
    def __init__(self, name, department, **kwargs):
        self.department=department
        Person.__init__(self,name)

    def work(self):
        return "Staff work"

class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        Faculty.__init__(self,name, subject)
        Staff.__init__(self,name, department)

    def profile_data(self):
        return f"{self.name} teaches {self.subject} and works in {self.department} department."

a1 = Administrator("Rakesh", "Math", "Operations")
print( a1.profile_data())

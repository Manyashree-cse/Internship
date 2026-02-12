class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age, grade):
        self.grade=grade
        super().__init__(name,age)

    def get_details(self):
        return f"{self.name} is {self.age} years old and studies in {self.grade} grade."

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject=subject
        super().__init__(name,age)

    def get_details(self):
        return f"{self.name} is {self.age} years old and teaches {self.subject}."

s1 = Student("Asha", 15, "10th")
print( s1.get_details())
s2=Teacher("Mr. Roy",40,"Mathematics")
print( s2.get_details())
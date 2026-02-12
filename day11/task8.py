class Person:
    def __init__(self, name, emp_id):
        self.name=name
        self.emp_id=emp_id

class Manager(Person):
    def __init__(self, name, emp_id, department):
        self.department=department
        super().__init__(name,emp_id)

    def get_profile_data(self):
        return f"{self.name} (ID: {self.emp_id}) is a manager of {self.department} department."

class Engineer(Person):
    def __init__(self, name, emp_id, specialization):
        self.specialization=specialization
        super().__init__(name,emp_id)

    def get_profile_data(self):
        return f"{self.name} (ID: {self.emp_id}) is a {self.specialization.lower()} engineer."

m1 = Manager("Kavita", 101, "HR")
print( m1.get_profile_data())

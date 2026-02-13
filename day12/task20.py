class Employee:
    def __init__(self, name, base_salary):
        self.name=name
        self.base_salary=base_salary

class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        self.bonus=bonus
        super().__init__(name,base_salary)

    def calculate_salary(self):
        return f"{self.base_salary+self.bonus}"

d1 = Developer("A", 40000, 5000)
print( d1.calculate_salary())
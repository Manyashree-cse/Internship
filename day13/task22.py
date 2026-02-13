class Student:
    def __init__(self, name, student_id):
        self.name=name
        self.student_id=student_id

class Graduate(Student):
    def __init__(self, name, student_id, degree):
        self.degree=degree
        super().__init__(name,student_id)
    def get_graduate_info(self):
        return f"{self.name} ({self.student_id}) - {self.degree}"

g1 = Graduate("Bob", "G001", "MBA")
print( g1.get_graduate_info())
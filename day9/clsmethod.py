class Student:
    college_name="ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new_college):
        cls.college_name=new_college
    @staticmethod
    def is_pass(marks):
        if marks>=35:
            return "pass"
        else:
            return "fail"
    def display(self):
        print("Name:",self.name)
        print("roll_no:",self.roll_no)
        print("college:",Student.college_name)
# std1=Student("manya",20)
# std1.display()

# std1=Student("manya",20)
# Student.change_college("jnv")
# std1.display()

# print(std1.is_pass(38))

print(Student.is_pass(38))
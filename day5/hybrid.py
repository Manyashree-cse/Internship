class Person:
    def __init__(self,name):
        self.name=name
    def display_person(self):
        print("the name is:",self.name)
class Student(Person):
    def __init__(self,student_id,name):
        self.student_id=student_id
        Person.__init__(self,name)
    def display_student(self):
        print("student id:",self.student_id)

class SportsPlayer(Person):
    def __init__(self,sport_name,name):
        self.sport_name=sport_name
        Person.__init__(self,name)
    def display_sports_player(self):
        print("sports is",self.sport_name)

class CollegeStudent(Student,SportsPlayer):
    def __init__(self,college_name,student_id,sport_name,name):
        self.college_name=college_name
        Student.__init__(self,student_id,name)
        SportsPlayer.__init__(self,sport_name,name)
    def diplay_college_student(self):
        print("college name:",self.college_name)

obj1=CollegeStudent("mitt","cs005","chess","manya")
obj1.diplay_college_student()
obj1.display_sports_player()
obj1.display_student()
obj1.display_person()

obj2=SportsPlayer("chess","manya")
obj2.display_sports_player()
obj2.display_person()

obj3=Student("chess","manya")
obj3.display_student()
obj3.display_person()


"""
#works in cs,sp but error in s
class Person:
    def __init__(self,name):
        self.name=name
    def display_person(self):
        print("the name is:",self.name)
class Student(Person):
    def __init__(self,student_id,name):
        self.student_id=student_id
        #Person.__init__(self,name)
        super().__init__(self,name)
    def display_student(self):
        print("student id:",self.student_id)

class SportsPlayer(Person):
    def __init__(self,sport_name,name):
        self.sport_name=sport_name
        # Person.__init__(self,name)
        super().__init__(name)
    def display_sports_player(self):
        print("sports is",self.sport_name)

class CollegeStudent(Student,SportsPlayer):
    def __init__(self,college_name,student_id,sport_name,name):
        self.college_name=college_name
        Student.__init__(self,student_id,name)
        SportsPlayer.__init__(self,sport_name,name)
    def diplay_college_student(self):
        print("college name:",self.college_name)

obj1=CollegeStudent("mitt","cs005","chess","manya")
obj1.diplay_college_student()
obj1.display_sports_player()
obj1.display_student()
obj1.display_person()

obj2=SportsPlayer("chess","manya")
obj2.display_sports_player()
obj2.display_person()

obj3=Student`("chess","manya")
obj3.display_person()
"""
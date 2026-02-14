class Student:
    def __init__(self, name):
        self.name=name
        self._grade=0

    def update_grade(self, new_grade):
        if new_grade>self._grade:
            self._grade=new_grade
            return self._grade
        else:
            return self._grade
        
s1 = Student("Bob")
print( s1.update_grade(20))
print( s1.update_grade(40))
class Employee:
    def __init__(self, name):
        self.name=name
        self._access_count=0

    def log_access(self):
        self._access_count+=1
        return self._access_count

e1 = Employee("A")
print( e1.log_access())
print( e1.log_access())
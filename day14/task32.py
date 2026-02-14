class UserAccount:
    def __init__(self):
        self.__points=0

    def add_points(self, amount):
        if amount>0:
            self.__points+=amount

    def get_points(self):
        return self.__point
u1 = UserAccount()
u1.add_points(10)
print( u1.get_points())
class Robot:
    def communicate(self):
        return "Beep beep."

class ExplorerRobot(Robot):
    def communicate(self):
        return "Exploring new planets!"

r = Robot()
e = ExplorerRobot()
print(r.communicate())
print(e.communicate())

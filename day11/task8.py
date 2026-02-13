class User:
    def __init__(self, name, **kwargs):
        self.name=name
        super().__init__(**kwargs)
class Driver(User):
    def __init__(self, name, car, **kwargs):
        self.car=car
        User.__init__(self,name)
class Rider(User):
    def __init__(self, name, pickup_location, **kwargs):
        self.pickup_location=pickup_location
        User.__init__(self,name)
class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        Driver.__init__(self,name,car)
        Rider.__init__(self,name,pickup_location)

    def summary(self):
        return f"{self.name} will pick up the rider from {self.pickup_location} using {self.car}."

t1 = Trip("Amit", "Honda City", "Sector 21")
print( t1.summary())

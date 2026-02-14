class Vehicle:
    def __init__(self, vehicle_type, speed):
        self.speed=speed
        self.vehicle_type=vehicle_type

class Flight(Vehicle):
    def __init__(self, vehicle_type, speed, flight_number, duration):
        self.flight_number=flight_number
        self.duration=duration
        super().__init__(vehicle_type, speed)

    def flight_summary(self):
        return f"Flight {self.flight_number} ({self.vehicle_type}) travels at {self.speed} km/h for {self.duration} hours"

f1 = Flight("Airbus", 700, "A123", 3)
print( f1.flight_summary())

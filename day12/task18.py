class Flyer:
    def fly(self, height):
        return f"Flying at {height} meters"

class Camera:
    def take_photo(self, location):
        return f"Photo taken at {location}"

class Drone(Flyer, Camera):
    pass

d1 = Drone()
print( d1.fly(50))
class Appliance:
    def status(self):
        return "Appliance is off."

class SmartAppliance(Appliance):
    def status(self):
        return "Appliance is on and connected."

a = Appliance()
s = SmartAppliance()
print(a.status())
print(s.status())

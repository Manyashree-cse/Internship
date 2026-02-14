class Creature:
    def battle_cry(self):
        return "For glory!"

class Dragon(Creature):
    def battle_cry(self):
        return "Feel my fiery breath!"

c = Creature()
d = Dragon()
print(c.battle_cry())
print(d.battle_cry())

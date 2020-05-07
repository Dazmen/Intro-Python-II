from random import randint

class Weapon():
    def __init__(self, name, description, min_dmg, max_dmg, hit_mod=0):
        self.name = name
        self.description = description
        self.damage = randint(min_dmg, max_dmg)
        self.hit_mod = hit_mod
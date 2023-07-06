import random
from abc import ABC

class Inhabitant(ABC):
    
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.strength = random.randint(1,10)
        self.agility = random.randint(1,10)
        self.armour = random.randint(1,10)
        self.alive = True
    
    def increase_health(self):
        if self.health < 10 and self.alive:
            self.health += 1
    
    def increase_strength(self):
        if self.strength < 10 and self.alive:
            self.strength += 1

    def increase_agility(self):
        if self.agility < 10 and self.alive:
            self.agility += 1
    
    def increase_armour(self):
        if self.armour < 10 and self.alive:
            self.armour += 1

    def decrease_health(self):
            self.health -= 1
            if self.health == 0:
                self.alive = False
    
    def decrease_strength(self):
        if self.strength > 0 and self.alive:
            self.strength += 1

    def decrease_agility(self):
        if self.agility < 10 and self.alive:
            self.agility += 1
    
    def decrease_armour(self):
        if self.armour < 10 and self.alive:
            self.armour += 1


class Werewolf(Inhabitant):
    pass

class Fairy(Inhabitant):
    pass

class Human(Inhabitant):
    pass
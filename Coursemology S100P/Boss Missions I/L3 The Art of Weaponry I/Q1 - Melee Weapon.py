import random

class Weapon:
    def __init__(self, name, value_min_damage, value_max_damage):
        self.name = name
        self.value_min_damage = value_min_damage
        self.value_max_damage = value_max_damage

    def min_damage(self):
        return self.value_min_damage

    def max_damage(self):
        return self.value_max_damage

    def damage(self):
        return random.randint(self.value_min_damage, self.value_max_damage)
    
sword = Weapon("Sword", 10, 20)
print(f"{sword.name} - Min Damage: {sword.min_damage()}, Max Damage: {sword.max_damage()}")
inflicted_damage = sword.damage()
print(f"{sword.name} inflicted {inflicted_damage} damage.")
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

class Ammo:
    def __init__(self, name, weapon, qty):
        self.name = name
        self.weapon = weapon
        self.qty = qty

    def get_quantity(self):
        return self.qty

    def weapon_type(self):
        return self.weapon

    def remove_all(self):
        self.qty = 0
    
class RangedWeapon(Weapon):
    def __init__(self, name, min_damage, max_damage):
        super().__init__(name, min_damage, max_damage)
        self.shots = 0

    def shots_left(self):
        return self.shots

    def load(self, ammo):
        if ammo.weapon_type() == self.name:
            self.shots += ammo.get_quantity()
            ammo.remove_all()
            print(f"Loaded {self.shots} shots into {self.name}.")
        else:
            print(f"Cannot load {ammo.weapon_type()} into {self.name}. Wrong ammo type.")

    def damage(self):
        if self.shots > 0:
            self.shots -= 1
            return super().damage()
        else:
            print(f"{self.name} has no shots left. Unable to inflict damage.")
            return 0
        
pistol = RangedWeapon("Pistol", 5, 15)
# Display initial ammo
print(f"Initial Shots Left in {pistol.name}: {pistol.shots_left()}")
# Create an ammo instance
bullets = Ammo("Bullets", "Pistol", 20)
# Load ammo into the ranged weapon
pistol.load(bullets)
# Display updated ammo after loading
print(f"Shots Left in {pistol.name} after loading: {pistol.shots_left()}")
# Inflict damage with the ranged weapon
inflicted_damage = pistol.damage()
print(f"{pistol.name} inflicted {inflicted_damage} damage. Shots Left: {pistol.shots_left()}")
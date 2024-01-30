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

bullets = Ammo("Bullets", "Gun", 50)
print(f"{bullets.name} - Quantity: {bullets.get_quantity()}, Weapon Type: {bullets.weapon_type()}")
bullets.remove_all()
print(f"All {bullets.name} removed. New Quantity: {bullets.get_quantity()}")
import random
import pickle
import os

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

    def info(self):
        return "Melee Weapon"

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
    
    def info(self):
        return "Ammunition"
    
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
    
    def info(self):
        return "Ranged Weapon"

    def damage(self):
        if self.shots > 0:
            self.shots -= 1
            return super().damage()
        else:
            print(f"{self.name} has no shots left. Unable to inflict damage.")
            return 0

def create_weapon(inventory, weapons):
    name = input("Enter melee weapon name (Case Sensitive!): ")
    min_damage = int(input("Enter minimum damage: "))
    max_damage = int(input("Enter maximum damage: "))
    weapons[name] = Weapon(name, min_damage, max_damage)
    inventory[name] = weapons[name]
    print(f"Weapon '{name}' created successfully!")

def create_ammo(inventory, weapons):
    name = input("Enter ammunition name (Case Sensitive!): ")
    weapon_type = input("Enter compatible weapon type: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = Ammo(name, weapon_type, qty)
    print(f"Ammo '{name}' created successfully!")

def create_ranged_weapon(inventory, weapons):
    name = input("Enter ranged weapon name (Case Sensitive!): ")
    min_damage = int(input("Enter minimum damage: "))
    max_damage = int(input("Enter maximum damage: "))
    weapons[name] = RangedWeapon(name, min_damage, max_damage)
    inventory[name] = weapons[name]
    print(f"Ranged Weapon '{name}' created successfully!")

def load_inventory():
    try:
        with open('inventory.pkl', 'rb') as file:
            inventory = pickle.load(file)
    except FileNotFoundError:
        inventory = {}
    return inventory

def save_inventory(inventory):
    with open('inventory.pkl', 'wb') as file:
        pickle.dump(inventory, file)

def create_item(inventory, weapons):
    print("Choose the type of item to create:")
    print("1. Melee Weapon")
    print("2. Ammunition")
    print("3. Ranged Weapon")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        create_weapon(inventory, weapons)
    elif choice == 2:
        create_ammo(inventory, weapons)
    elif choice == 3:
        create_ranged_weapon(inventory, weapons)

def load_ammo(inventory, weapons):
    weapon_name = input("Enter weapon name (Case Sensitive!): ")
    ammo_name = input("Enter ammo name (Case Sensitive!): ")

    if weapon_name in inventory and ammo_name in inventory:
        weapon = inventory.get(weapon_name)
        ammo = inventory.get(ammo_name)

        if isinstance(weapon, RangedWeapon) and isinstance(ammo, Ammo):
            if ammo.weapon_type() == weapon.name:
                weapon.load(ammo)
                print(f"Ammo '{ammo_name}' has been successfully loaded into '{weapon_name}'!")
                del inventory[ammo_name]
            else:
                print(f"Error: Incompatible ammo type. Expected '{weapon.name}' ammo.")
        else:
            print(isinstance(weapon, RangedWeapon))
            print(isinstance(ammo, Ammo))
            print("Error: Incompatible weapon or ammo type.")
    else:
        print("Error: Weapon or ammo not found in the inventory.")

def remove_item(inventory):
    item = input("Enter item name to remove (Case Sensitive!): ")
    if item in inventory:
        del inventory[item]
        print(f"Item '{item}' removed from inventory.")
    else:
        print("Error: Item not found in the inventory.")

def display_inventory(inventory):
    if inventory:
        print("Current Inventory:")
        for item_name, item_obj in inventory.items():
            if isinstance(item_obj, Weapon):
                if isinstance(item_obj, RangedWeapon):
                    print(f"{item_name} - Ranged Weapon")
                else:
                    print(f"{item_name} - Melee Weapon")
            elif isinstance(item_obj, Ammo):
                print(f"{item_name} - Ammunition")
    else:
        print("Inventory is empty.")

def main():
    inventory = load_inventory()
    weapons = {}

    while True:
        print("\nChoose an option:")
        print("1. Create an item")
        print("2. Load ammo")
        print("3. Remove an item")
        print("4. Display all items")
        print("5. Exit Program")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nInvalid input. Please enter a number.")
            continue

        if choice == 1:
            os.system('cls')
            create_item(inventory, weapons)
        elif choice == 2:
            os.system('cls')
            load_ammo(inventory, weapons)
        elif choice == 3:
            os.system('cls')
            remove_item(inventory)
        elif choice == 4:
            os.system('cls')
            display_inventory(inventory)
        elif choice == 5:
            save_inventory(inventory)
            print("\nExiting program. Inventory saved.")
            break
        else:
            os.system('cls')
            print("\nInvalid choice. Please try again.")

main()
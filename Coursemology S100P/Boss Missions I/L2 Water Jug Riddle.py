class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.water = 0

    def fill(self):
        self.water = self.capacity

    def empty(self):
        self.water = 0

    def pour_into(self, other_jug):
        space_available = other_jug.capacity - other_jug.water
        amount_poured = min(space_available, self.water)
        other_jug.water += amount_poured
        self.water -= amount_poured

jug_3l = Jug(3)
jug_5l = Jug(5)

""" Fill the 5-litre jug, then pour it into the 3-litre jug so the 5-litre jug have 2 liters.
Empty the 3-litre jug and transfer the 2 liters from the 5-litre jug into it so the 3-litre jug have 2 liters.
Now fill the 5-litre jug to full and pour it into the 3-litre jug until the 3-litre jug is full.
Now you have the 5-litre jug with exactly 4 liters in it """


jug_5l.fill()  # Fill the 5-litre jug
jug_5l.pour_into(jug_3l)  # Pour water into the 3-litre jug

jug_3l.empty()  # Empty the 3-litre jug
jug_5l.pour_into(jug_3l)  # Pour remaining water from 5-litre jug to 3-litre jug

jug_5l.fill()  # Fill the 5-litre jug again
jug_5l.pour_into(jug_3l)

print("Jug 3:", jug_3l.water, "litres")
print("Jug 5:", jug_5l.water, "litres") # Exactly 4 litres
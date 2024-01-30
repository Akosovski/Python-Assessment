class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def speedUp(self):
        if (self.speed + 10) >= 100:
            print("Your car is at maximum speed.")
        elif (self.speed + 10) < 100:
            self.speed += 10

    def slowDown(self):
        if (self.speed - 10) <= 0:
            print("Your car is not moving.")
        elif (self.speed - 10) > 0:
            self.speed -= 10
        
    def stop(self):
        if self.speed <= 0:
            print("Your car has already stopped.")
        elif self.speed > 0:
            self.speed = 0

Racecar = Car("Racecar")
Freed = Car("Honda Freed")
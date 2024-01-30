class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculate_area()
        self.circumference = self.calculate_circumference()

    def calculate_area(self):
        return 3.14159 * self.radius**2

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius
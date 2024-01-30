class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
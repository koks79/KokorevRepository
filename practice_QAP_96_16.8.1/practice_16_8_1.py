
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def get_area(self):
        return self.height * self.width

class Square:
    def __init__(self, hw):
        self.hw = hw
    def get_area_square(self):
        return self.hw ** 2

class Round:
    def __init__(self, radius):
        self.radius = radius
    def get_round_squre(self):
        return (self.radius*3.14)**2





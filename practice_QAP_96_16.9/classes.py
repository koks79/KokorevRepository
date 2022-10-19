
class Rectangle:
    def __init__(self, x_coord, y_coord, height, width):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = height
        self.width = width
    def get_area(self):
        return self.height * self.width
    def __str__(self):
        return f'Параметры прямоугольника\n x: {self.x_coord}, y: {self.y_coord}, ширина: {self.width}, высота: {self.height}'

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'\n"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'
    def get_client_info(self):
        return f'{self.name} {self.surname}, {self.city}'

from practice_16_8_1 import Rectangle, Square, Round

# далее создаем два прямоугольника

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
# вывод площади двух наших прямроугольников
print(rect1.get_area())
print(rect2.get_area())
# создаем два квадрата
square1 = Square(5)
square2 = Square(10)
# находим площадь квадратов
print(square1.get_area())
print(square2.get_area())
# создаем пару кругов
round1 = Round(8)
round2 = Round(100)
# находим площадь кругов
print(round1.get_area())
print(round2.get_area())

print(type(rect1), type(square1), type(round1))

# теперб перебираем все объекты циклом и считаем площади
figures = [rect1, rect2, square1, square2, round1, round2]
for figure in figures:
    if isinstance(figure, Square):
        print((figure.get_area()))
    elif isinstance(figure, Round):
        print(figure.get_area())
    else:
        print(figure.get_area())




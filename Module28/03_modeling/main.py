import math

class Square:
    def __init__(self, length: int) -> None:
        self.length = length

    def find_square(self):
        self.square = self.length ** 2
        print(f'Площадь квадрата: {self.sqare}')

    def find_perimeter(self):
        self.perimeter = 2 * (math.sqrt(self.basis ** 2 + self.height ** 2) + self.basis + self.height)
        print(f'Периметр квадрата: {self.perimeter}')

class Triangle:
    def __init__(self, basis: int, height: int) -> None:
        self.basis = basis
        self.height = height

    @property
    def height(self):
        return f'Высота {self.height}'

    @height.setter
    def height(self, height):
        self.height = height

    def find_perimeter(self):
        self.perimeter = 2 * (math.sqrt(self.basis ** 2 + self.height ** 2) + self.basis + self.height)
        print(f'Периметр треугольника: {self.perimeter}')

    def find_square(self):
        self.sqare = self.basis * self.height / 2
        print(f'Площадь треугольника: {self.sqare}')


a = Triangle(basis = 10, height = 70)
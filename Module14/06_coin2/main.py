import math


def rad_cool(x, y, r):
    r_cool = x ** 0.5 + y ** 0.5
    if r > r_cool:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

rad_cool(x, y, r)

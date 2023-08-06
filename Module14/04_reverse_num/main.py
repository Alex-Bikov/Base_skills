import math


def int_number(number):
    rev_int_number = ''
    int_number = math.trunc(number)
    while int_number != 0:
        x = int_number % 10
        rev_int_number = rev_int_number + str(x)
        int_number //= 10
    return rev_int_number


def float_number(number):
    rev_float_number = ''
    float_number = number - math.trunc(number)
    float_number = int(round(float_number, 2) * 100)
    while float_number != 0:
        x = float_number % 10
        rev_float_number = rev_float_number + str(x)
        float_number //= 10
    return rev_float_number


number = float(input('Введите число: '))
second_number = float(input('Введите число: '))

a = int_number(number)
b = float_number(number)
c = int_number(second_number)
d = float_number(second_number)
new_number = float(a + '.' + b)
new_second_number = float(c + '.' + d)
print('Первое число наоборот: ', new_number)
print('Второе число наоборот: ', new_second_number)
print('Сумма: ', new_number + new_second_number)



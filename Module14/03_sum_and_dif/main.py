def total_number(number):
    chek = 0
    while number != 0:
        chek += 1
        number //= 10
    return chek


def total_summ(number):
    summ = 0
    while number != 0:
        x = number % 10
        summ += x
        number //= 10
    return summ


number = int(input('Введите часло: '))

a = total_number(number)
b = total_summ(number)
print('Сумма цифр: ', b)
print('Кол-во цифр в числе: ', a)
print('Разность суммы и кол-ва цифр: ', b - a)

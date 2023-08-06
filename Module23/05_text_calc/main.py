def summa(num1, num2):
    return num1 + num2


def difference(num1, num2):
    return num1 - num2


def debasement(num1, num2):
    return num1 * num2


def debasement2(num1, num2):
    return num1 ** num2


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return 0


def division1(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return 0


def division2(num1, num2):
    try:
        return num1 // num2
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return 0


with open('calc.txt', 'r') as file:
    total_sum_oper = 0
    for i_line in file:
        i_line = i_line.split()
        print(i_line)
        if i_line[1] == '+':
            answer = summa(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '-':
            answer = difference(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '*':
            answer = debasement(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '/':
            answer = division(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '%':
            answer = division1(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '//':
            answer = division2(int(i_line[0]), int(i_line[2]))
        elif i_line[1] == '**':
            answer = debasement2(int(i_line[0]), int(i_line[2]))
        total_sum_oper += answer
print('Сумма операций', total_sum_oper)

import random


def f(x, y):
    # try:  Функция просто выполняет расчёты, при делении на ноль выбросит исключение, а ловить и обрабатывать это будет
    #  основной код программы (как это сейчас уже и происходит), поэтому тут перехватывать исключения не надо
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y
    # except ZeroDivisionError:
    #     return None


def f2(x, y):
    # try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x
    # except ZeroDivisionError:
    #     return None


file = open('coordinates.txt', 'r')
try:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print("Что-то пошло не так с первой функцией")
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print("Что-то пошло не так со второй функцией")
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'w')
        my_list = sorted([res1, res2, number])
        file_2.write(' '.join(str(my_list)))
except Exception:
    print("Что-то пошло не так")
finally:
    file.close()
    file_2.close()

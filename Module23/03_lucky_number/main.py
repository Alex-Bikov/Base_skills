import random


with open('out_file.txt', 'w') as all_numbers:
    count = 0
    while count < 777:
        number = int(input('Введите число: '))
        number_error = random.randint(0, 13)
        if number_error == 1:
            raise ValueError('Вас постигла неудача!')  #  просто выбрасываем исключение, согласно заданию
            # break
        count += number
        all_numbers.write('{0}\n'.format(str(number)))
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

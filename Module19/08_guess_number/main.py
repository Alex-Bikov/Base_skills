import random

max_number = int(input('Введите максимальное число: '))
number_secret = str(random.randint(0, max_number + 1))
number_set = {i for i in range(1, max_number + 1)}
answer = ' '
answer_set = set()
while (answer != 'то') or (answer[0] != 'Помогите!'):
    answer_set.clear()
    answer = input('Нужное число есть среди вот этих чисел: ', )
    answer.split()
    for i in answer:
        if i.isdigit():
            answer_set.add(int(i))
        else:
            print('неверный ввод данных')
            break
    if number_secret in answer_set:
        print('Ответ Артёма: Да')
        number_set.intersection_update(answer_set)
    elif number_secret not in answer_set:
        print('Ответ Артёма: Нет')
        number_set.difference_update(answer_set)
    elif number_secret == number_set:
        print('То число')
        break
    print()
if answer == 'Помогите!':
    print('Артём мог загадать следующие числа:', new_text.join(' '))

max_number = int(input('Введите максимальное число: '))
all_nums = set(range(1, max_number + 1))
possible_nums = all_nums

while True:
    guess = input('Нужное число есть среди вот этих чисел:')
    if guess == 'Помогите!':
        break
    guess = {int(i_num) for i_num in guess.split()}
    answer = input('Ответ Артёма: ').lower()
    if answer == 'да':
        possible_nums &= guess
    else:
        possible_nums -= guess

print('Артём мог загадать следующие числа:', sorted(possible_nums))

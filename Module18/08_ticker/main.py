# abcd
# cdba
first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
for i in range(len(second_text)):
    new_text = first_text[i:] + first_text[:i]
    if new_text == second_text:
        print('Первая строка получается из второй со сдвигом', i)
        break
    if i == len(second_text) - 1:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

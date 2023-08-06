# text = input('Строка: ')
# Строка: abcd
# (10, 20, 30, 40)
# numbers = input('Кортеж чисел: ')
text = 'abcd'
numbers = '(10, 20, 30, 40)'
new_tuple = list()
numbers = numbers[1:-1].split(', ')
for i in range(len(text)):
    numbers[i] = int(numbers[i])
    data_tuple = (text[i], numbers[i])
    new_tuple.append(data_tuple)
print(new_tuple)
for i_ in new_tuple:
    print(i_)

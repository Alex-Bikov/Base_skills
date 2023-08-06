number_list = []
number = int(input('Введите число: '))
for i in range(number + 1):
    if i % 2 != 0:
        number_list.append(i)
print(number_list)

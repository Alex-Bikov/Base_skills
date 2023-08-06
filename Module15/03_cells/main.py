efficiency_list = []
number_cell = int(input('Кол-во клеток: '))
for i in range(1, number_cell + 1):
    print('Эффективность ', i, ' клетки: ', end='')
    efficiency = int(input(''))
    efficiency_list.append(efficiency)
print('Неподходящие значения: ', end=' ')
for index in range(number_cell):
    if efficiency_list[index] < index:
        print(efficiency_list[index], end=' ')

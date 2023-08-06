numbers = int(input('Кол-во чисел: '))
list_num = []
all_num = []
print()
for i_num in range(1, numbers + 1):
    num = int(input('Число: '))
    list_num.append(num)
print()
print('Последовательность: ', end='')
chek = 0
len_num = len(list_num)
for _ in list_num:
    print(_, end=' ')
if list_num[len(list_num) - 1] == list_num[len(list_num) - 2]:
    b = len(list_num) - 2
else:
    b = list_num[len(list_num) - 2]
for i in range(b, 0, -1):
    chek += 1
    all_num.append(list_num[i - 1])
print('\nНужно приписать чисел: ', chek)
print('Сами числа:', end=' ')
for _ in all_num:
    print(_, end=' ')

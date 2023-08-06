first_list = [1, 2, 2, 3]
second_list = [2, 4, 6, 3, 3, 2, 1]
print('Первый список:', first_list)
print('Второй список:', second_list)
first_list += second_list
for i in first_list:
    x = first_list.count(i)
    for i_index in range(x - 1):
        first_list.remove(i)
print('Новый первый список с уникальными элементами:', first_list)


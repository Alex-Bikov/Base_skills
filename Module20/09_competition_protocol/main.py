# 1 запись: 69485 Jack
# 2 запись: 95715 qwerty
# 3 запись: 95715 Alex
# 4 запись: 83647 M
# 5 запись: 197128 qwerty
# 6 запись: 95715 Jack
# 7 запись: 93289 Alex
# 8 запись: 95715 Alex
# 9 запись: 95715 M

# Итоги соревнований:
# 1 место. qwerty (197128)  5
# 2 место. Alex (95715)  3
# 3 место. Jack (95715)   6


record = int(input('Сколько записей вносится в протокол? '))
data = dict()
print('Записи (результат и имя):')
for i in range(1, record + 1):
    data_record = input('{} запись: '.format(i)).split()
    data_record[0] = int(data_record[0])
    if data_record[1] not in data:
        data[data_record[1]] = [data_record[0], i]
    else:
        if data[data_record[1]][0] < data_record[0]:
            data[data_record[1]] = [data_record[0], i]
print(data)
data_list = list()
for i_data in data:
    data_list += [data[i_data]]
data_list = sorted(data_list, key =lambda x: (-x[0], x[1]))
print(data_list)
data_list = data_list[:3]
print(data_list)
print('Итоги соревнований:')
num_count = 0
for i_value in data_list:
    num_count += 1
    for i_key, ival_data in enumerate(data):
        if data[ival_data] == i_value:
            print('{0} место. {1} ({2})'.format(num_count, ival_data, i_value[0]))

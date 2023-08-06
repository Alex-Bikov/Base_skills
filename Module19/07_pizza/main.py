order = int(input('Введите кол-во заказов: '))
info_clients = dict()
for i in range(1, order + 1):
    info_order = input('{} заказ: '.format(i)).split()
    if info_order[0] not in info_clients:
        info_clients[info_order[0]] = [dict()]
        info_clients[info_order[0]][0][info_order[1]] = int(info_order[2])
    else:
        if info_order[1] in info_clients[info_order[0]][0]:
            info_clients[info_order[0]][0][info_order[1]] += int(info_order[2])
        else:
            info_clients[info_order[0]][0][info_order[1]] = int(info_order[2])
print()
for i_info in info_clients:
    print('{}:'.format(i_info))
    list_keys = list(info_clients[i_info][0].keys())
    list_keys.sort()
    for i_list_keys in list_keys:
        print('    {0}: {1}'.format(i_list_keys, info_clients[i_info][0][i_list_keys]))

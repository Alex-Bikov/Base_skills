all_containers = int(input('Кол-во контейнеров: '))
containers_list = []
for i in range(all_containers):
    container = int(input('Введите вес контейнера: '))
    if (container % 1 == 0) and (0 < container < 200):
        containers_list.append(container)
    else:
        print('Неверно введены данные, напишите еще раз! ')
        container = int(input('Введите вес контейнера: '))
        containers_list.append(container)
print(containers_list)
new_container = int(input('Введите вес нового контейнера: '))
for index in range(0, len(containers_list)):
    if containers_list[index] > new_container:
        x = index
    elif containers_list[index] == new_container:
        x = index + 1
print('Номер, куда встанет новый контейнер: ', x + 1)

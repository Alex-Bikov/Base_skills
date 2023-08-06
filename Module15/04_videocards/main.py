number = int(input('Кол-во видеокарт: '))
videocard_list = []
videocard_list_new = []
for i in range(1, number + 1):
    print(i, 'Видеокарта: ', end='')
    videocard = int(input())
    videocard_list.append(videocard)
print('Старый список видеокарт: ', videocard_list)
max_list = videocard_list[0]
for index in videocard_list:
    if index > max_list:
        max_list = index  #  опечатка

print('Самая большая', max_list)
for index_max in range(number):
    if videocard_list[index_max] == max_list:
        continue
    else:
        videocard_list_new.append(videocard_list[index_max])
print('Новый список видеокарт: ', videocard_list_new)


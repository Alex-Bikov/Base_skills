number = int(input('Кол-во коньков: '))
skates_list = []
foot_size = []
for i_list in range(number):
    print('Размер', i_list + 1, ' пары: ', end='')
    skates = int(input(''))
    skates_list.append(skates)
people_num = int(input('Кол-во людей: '))
for i_list in range(people_num):
    print('Размер ноги', i_list + 1, ' человека: ', end='')
    foot_size_num = (int(input('')))
    foot_size.append(foot_size_num)
chek = 0
for index_s in foot_size:
    for index_f in skates_list:
        if (index_s == index_f) or (index_s < index_f):
            chek += 1
            skates_list.remove(index_s)
print('Наибольшее кол-во людей, которые могут взять ролики: ', chek)

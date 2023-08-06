shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название детали: ')
chek_name = 0
chek_num = 0
for i_shop in shop:
    if i_shop[0] == name:
        chek_name += 1
        chek_num += i_shop[1]
print('Кол-во деталей - ', chek_name)
print('Общая стоимость - ', chek_num)


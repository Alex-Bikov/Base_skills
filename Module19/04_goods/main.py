goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
all_keys = list(goods.keys())
chek = 0
for i in store:
    total_sum = 0
    total_quantity = 0
    for i_ in store[i]:
        quantity = i_['quantity']
        price = i_['price']
        total_quantity += quantity
        total_sum += quantity * price
    print('{0} - {1} шт, стоимость {2} руб'.format(all_keys[chek], total_quantity, total_sum))
    chek += 1

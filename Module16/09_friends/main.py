friends = int(input('Кол-во друзей: '))
list_friends = []
cash_friends = []
for _ in range(1, friends + 1):
    list_friends.append(_)
    cash_friends.append(0)
print(cash_friends, list_friends)
vouchers = int(input('Долговых расписок: '))
print()
for i_num in range(vouchers):
    print(i_num + 1, 'расписка')
    whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    cash = int(input('Сколько: '))
    cash_friends[whom - 1] += cash
    cash_friends[from_whom - 1] -= cash
    print()
print('Баланс друзей:')
for i_list in list_friends:
    cash_friends[i_list - 1] = -cash_friends[i_list - 1]
    print(i_list, ':', cash_friends[i_list - 1])

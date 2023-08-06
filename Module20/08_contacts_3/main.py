phone_book = {('паша', 'волков'): 123, ('паша', 'кириллов'): 415, ('паша', 'сомов'): 415, ('леша', 'кириллов'): 107}
while True:
    action = input('добавить контакт или найти человека? ')
    if action == 'добавить контакт':
        data_man = tuple(input('имя и фамилию контакта: ').lower().split())
        if data_man not in phone_book:
            number_phone = int(input('номер телефона: '))
            phone_book[data_man] = number_phone
        else:
            print('Данный человек уже есть в книге.')
    elif action == 'найти человека':
        data_man = input('фамилия контакта: ').lower()
        for i_date in phone_book:
            if i_date[1] == data_man:
                print(i_date, ':', phone_book[i_date])
    print(phone_book)


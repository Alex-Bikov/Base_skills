guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке ', len(guests), 'человек: ', guests)
    command = input('Гость пришел или ушел? ')
    if command == 'пришел':
        name_guests = input('Имя гостя: ')
        if len(guests) == 6:
            print('Прости,', name_guests, ', но мест нет.')
        else:
            print('Привет,', name_guests, '!')
            guests.append(name_guests)
    elif command == 'ушел':
        name_guests = input('Имя гостя: ')
        guests.remove(name_guests)
        print('Пока,', name_guests, '!')
    elif command == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    print()
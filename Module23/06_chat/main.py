with open('history.txt', 'r+', encoding='utf-8') as data_file:
    while True:
        user_name = input('Введите имя пользователя: ')
        search = input('Что будем делать?\n1. Посмотреть текущий текст чата\n2.Отправить сообщение\n')
        if search == '1':
            for i_line in data_file:
                print(i_line)
        elif search == '2':
            text = input('Введите текст: ')
            data_file.write(f'{user_name}: {text}\n')
        else:
            print('Неправильная команда')

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
films_list = []
loves_films = input('Введите фильм(Для остановки программы наберите end): ')
chek = 0
while loves_films != 'end':
    for i in films:
        if loves_films == i:
            films_list.append(loves_films)
            print('Фильм добавлен в ваш список!')
            chek += 1
            break
    if chek == 0:
        print('Ошибка, данного фильма нет!')
    loves_films = input('Введите фильм(Для остановки программы наберите end): ')
print('Ваш список фильмов :', films_list)

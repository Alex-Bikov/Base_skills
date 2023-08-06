pair = int(input('Введите количество пар слов: '))
pair_dict = dict()
for i in range(1, pair + 1):
    text = input('{} пара: '.format(i)).split(' - ')
    pair_dict[text[0].lower()] = text[1].lower()
    pair_dict[text[1].lower()] = text[0].lower()
while True:
    word = input('Введите слово: ').lower()
    if word not in pair_dict:
        print('Такого слова в словаре нет.')
    else:
        print('Синоним:', pair_dict[word].title())

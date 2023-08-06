text = input('Введите текст: ')
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# text_vowels = [x for x in vowels for i in text if i == x]
#  Чуть проще так:
text_vowels = [x for x in text if x in vowels]
print('Список гласных букв: ', text_vowels)
print('Длина списка: ', len(text_vowels))

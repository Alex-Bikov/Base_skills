alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
text = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))
a = [alphabet[alphabet.index(i) + 3
     if alphabet.index(i) + 3 < len(alphabet) else alphabet.index(i) + step - len(alphabet)]
     for i in text if i != ' ']
print(a)

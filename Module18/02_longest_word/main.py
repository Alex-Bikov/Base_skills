# Lore ipsum dolor sit amet
text = input('Введите текст: ').split()
chek = 0
max_text = 0

for i in range(len(text)):
    if len(text[i]) > max_text:
        max_text = len(text[i])
        chek = i
    else:
        continue
print('Самое длинное слово: ', text[chek], 'Длина:', max_text)


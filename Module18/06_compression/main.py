# aaAAbbсaaaA

text = input('Введите строку: ')
len_text = len(text)
chek = 1
symbol = text[0]
text_new = ''
for i in range(len_text):
    if i == len_text - 1:
        if symbol == text[i - 1]:
            text_new += symbol + str(chek)
        else:
            text_new += symbol + str(chek)
    elif symbol == text[i + 1]:
        chek += 1
    else:
        text_new += symbol + str(chek)
        symbol = text[i + 1]
        chek = 1
print(text_new)

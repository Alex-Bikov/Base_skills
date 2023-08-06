symbols = '!,.-?:'
# Хотя ,. возм:ожно и нет.
new_text = []
text = input('Сообщение: ').split(' ')
for i in text:
    if i.isalpha():
        new_text.append(i[::-1])
    elif not i.isalpha():
        new_text.append(i)
    else:
        for i_symbols in i:
            if i_symbols in symbols:
                x = i.index(i_symbols)
                break
        new_slovo = i[x - 1::-1] + i_symbols + i[-1:x:-1]
        new_text.append(new_slovo)
print(' '.join(new_text))

word = input('Введите слово: ')
new_word_list = []
word_list = list(word)
x = len(word_list)
for i in range(x, 0, -1):
    new_word_list.append(word_list[i - 1])
print(new_word_list)
if word_list == new_word_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

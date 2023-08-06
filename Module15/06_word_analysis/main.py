word = input('Введите слово: ')
word_list = []
new_list = []
chek = 0
all_chek = 0
word_list = list(word)
for index in range(chek):
    chek_list = 0
    for i in range(chek):
        if word_list[index] == word_list[i]:
            chek_list += 1
    if chek_list == 1:
        new_list.append(word_list[index])
for _ in new_list:
    all_chek += 1
print('Кол-во уникальных букв: ', all_chek)
print(new_list)

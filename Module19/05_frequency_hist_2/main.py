text = input('Введите текст: ')
print('Оригинальный словарь частот:')
text_dict = dict()
new_text_dict = dict()
new_text_dict[1] = list()
new_text_dict[2] = list()
new_text_dict[3] = list()

for i in text:
    if i in text_dict:
        text_dict[i] += 1
    else:
        text_dict[i] = 1
keys_text = sorted(text_dict)
for i_keys in keys_text:
    print(i_keys, ':', text_dict[i_keys])
    if text_dict[i_keys] == 1:
        new_text_dict[1].append(i_keys)
    elif text_dict[i_keys] == 2:
        new_text_dict[2].append(i_keys)
    elif text_dict[i_keys] == 3:
        new_text_dict[3].append(i_keys)
print()
print('Инвертированный словарь частот:')
for i_dict in new_text_dict:
    print(i_dict, ':', new_text_dict[i_dict])

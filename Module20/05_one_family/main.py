data_family = {('Сидоров', 'Никита'): 35,
               ('Сидорова', 'Алина'): 34,
               ('Сидоров', 'Павел'): 10,
               ('Быков', 'Алекс'): 26,
               }
surname = input('Введите фамилию: ')
for i_sur in data_family:
    if (i_sur[0].lower() in surname.lower()) or surname.lower() in i_sur[0].lower():
        surname_tuple, name_tuple = i_sur
        print(surname_tuple, name_tuple, data_family[i_sur])

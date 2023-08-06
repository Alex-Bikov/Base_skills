def rabota(data_line):  # TODO транслит не допускается, все названия должны быть по-английски
    if len(data_line) < 3:  # TODO добавил проверку достаточного количества элементов в списке
        raise ValueError('Мало данных!')
    if not data_line[0].isalpha():
        raise NameError('поле имени содержит НЕ только буквы')
    if '@' and '.' not in data_line[1]:
        raise SyntaxError('поле емейл НЕ содержит @ и .(точку)')
    if (int(data_line[2]) < 10) or (int(data_line[2]) > 99):
        raise ValueError('поле возраст НЕ является числом от 10 до 99')


with open('registrations.txt', 'r', encoding='utf-8') as file, \
        open('registrations_good.log', 'a', encoding='utf-8') as good_data, \
        open('registrations_bad.log', 'a', encoding='utf-8') as bad_data:
    for line in file:
        try:
            data_line = line.split()
            name = data_line[0]
            email = data_line[1]
            age = data_line[2]
            rabota(data_line)
        except(IndexError, NameError, SyntaxError, ValueError) as exc:
            bad_data.write(f'{name} {email} {age}     {exc}\n')
        else:
            good_data.write(f'{name} {email} {age}\n')

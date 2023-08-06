first_year = int(input('Введите первый год: '))
second_years = int(input('Введите второй год: '))
print('Года от', first_year, 'до',second_years, 'с тремя одинаковыми цифрами:')
for date in range(first_year, second_years + 1):
    number = date % 10
    dozens = date % 100 // 10
    hundreds = date // 100 % 10
    thousand = date // 1000
    if (dozens == hundreds) and (dozens == thousand) and (number == dozens):
        continue
    if number == dozens:
        if (number == hundreds) or (number == thousand):
            print(date)
    elif (dozens == hundreds) and (dozens == thousand):
        print(date)
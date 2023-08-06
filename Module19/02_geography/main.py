country_check = int(input('Кол-во стран: '))
data_country = dict()
for i in range(country_check):
    country = input('{} страна: '.format(i + 1)).split()
    data_country[country[0]] = country[1:]
print(data_country)
chek_city = 1
while True:
    check = 1
    city = input('{} город: '.format(chek_city))
    for i_country in data_country:
        for i_city in data_country[i_country]:
            if city == i_city:
                print('Город {} расположен в стране {}.'.format(city, i_country))
                check += 1
                break
    if check == 1:
        print('По городу {} данных нет.'.format(city))
        break
    chek_city += 1

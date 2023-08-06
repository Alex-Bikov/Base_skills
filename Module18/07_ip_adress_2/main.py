a = True
while a:
    address = input('Введите IP: ').split('.')
    for i in address:
        if i.isdigit():
            print(i, 'не целое число')
            break
        elif int(i) < 0:
            print(i, 'Меньше 0')
            break
        elif int(i) > 255:
            print(i, 'превышает 255')
            break
        elif len(address) < 4:
            print('Адрес - это четыре числа, разделенные точками')
            break
    else:
        a = False
print('IP-адрес корректен')

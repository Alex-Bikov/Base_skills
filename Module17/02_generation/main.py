number = int(input('Введите длину списка: '))
num_list = [x % 5 if x % 2 != 0 else 1 for x in range(number)]
print(num_list)

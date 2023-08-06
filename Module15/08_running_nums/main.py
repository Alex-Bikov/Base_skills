lst = [1, 4, -3, 0, 10]
steps = int(input('Сдвиг: '))
lst = lst[-steps:] + lst[:-steps]
print(lst)

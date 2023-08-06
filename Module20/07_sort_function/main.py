import random

number_tuple = tuple(random.randint(0, 100) for i in range(15))
while True:
    for i in number_tuple:
        if isinstance(i, float):
            print(number_tuple)
            break
    number_tuple = tuple(sorted(list(number_tuple)))
    print(number_tuple)
    break

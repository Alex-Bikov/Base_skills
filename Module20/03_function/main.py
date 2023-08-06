def new_tuple(text_tuple, number_rand):
    new_tuple = tuple()
    if number_rand not in text_tuple:
        return new_tuple
    elif text_tuple.count(number_rand) == 1:
        num_ind = text_tuple.index(number_rand)
        new_tuple = text_tuple[num_ind:]
        return new_tuple
    else:
        num_ind = [i for i, x in enumerate(text_tuple) if x == number_rand]
        new_tuple = text_tuple[num_ind[0]:num_ind[1] + 1]
        return new_tuple


text_tuple = input('Введите кортеж: ').split(', ')
text_tuple = tuple(text_tuple)
print(text_tuple)
number_rand = input('Введите число любое: ')

print(new_tuple(text_tuple, number_rand))

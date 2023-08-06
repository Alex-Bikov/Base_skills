# x = [i for i in range(15)]
# x = (1,2,3,4,5,6,7,8,9)
# x = '123456789'
x = {
    1: 'sd',
    2: 'sd',
    3: 'sd',
    4: 'sd',
    5: 'sd',
    6: 'sd',
    7: 'sd',
    8: 'sd',
    9: 'sd',
    10: 'sd',
    11: 'sd',
    12: 'sd'
}


def is_prime(i_ind):
    for i in range(2, i_ind):
        if (i_ind % i == 0) and (i != i_ind):
            return False
    return True


new_list = list()
if isinstance(x, list) or isinstance(x, tuple) or isinstance(x, str):
    for i_ind, i_value in enumerate(x):
        if is_prime(i_ind) and (i_ind > 1):
            new_list.append(i_value)
elif isinstance(x, dict):
    for i_ind, i_value in enumerate(x):
        if is_prime(i_ind) and (i_ind > 1):
            new_list.append([i_ind, i_value])
print(new_list)
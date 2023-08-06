def chek(number, password):
    x = 0
    for i in range(len(password)):
        for i_ in number:
            if password[i] == str(i_):
                x += 1
    return x


def symbols_up(password):
    for i in password:
        if i.isupper():
            return True
    return False


while True:
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    password = input('Придумайте пароль: ')
    all_numbers = chek(number, password)
    if (len(password) < 8) or (all_numbers < 3) or not symbols_up(password):  # поправил
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        break
print('Это надёжный пароль!')

def len_name(i_line, num_line):
    if len(i_line) < 3:
        raise ValueError
    else:
        return len(i_line)


with open('people.txt', 'r') as file_name:
    num_line = 0
    total_sum_symbol = 0
    data_file = file_name.read()
    try:
        for i_line in data_file.split('\n'):
            print(i_line)
            num_line += 1
            try:
                total_sum_symbol += len_name(i_line, num_line)
            except ValueError:
                print('Строка {0}:\nValueError: Кол-во символов в строке менее 3ех'.format(num_line))
    finally:
        print('Кол-во символов: {sum_symbol}'.format(sum_symbol=total_sum_symbol))

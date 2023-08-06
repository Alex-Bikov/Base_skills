line = input('Введите строку: ')
#head_hunter
boundaries = [x for x in range(len(line)) if line[x] == 'h']
print(boundaries)
line = line[:boundaries[0] + 1] + line[boundaries[1] - 1:boundaries[0]:-1] + line[boundaries[1]:]
print(line)


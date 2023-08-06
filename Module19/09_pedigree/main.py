numbers_people = int(input('Введите количество человек: '))
wood = dict()
for i in range(1, numbers_people):
    pair = input('{} пара: '.format(i)).split()
    if pair[0] in wood:
        wood[pair[0]] += 1
        for i_dict in wood:
            if wood[i_dict] == wood[pair[0]] and i_dict != pair[0]:
                wood[i_dict] += 1
        wood[pair[1]] = wood[pair[0]] - 1
    if pair[1] not in wood:
        wood[pair[1]] = 0
    if pair[0] not in wood:
        wood[pair[0]] = wood[pair[1]] + 1

keys = sorted(list(wood.keys()))
print('\n“Высота” каждого члена семьи:')
for i in keys:
    print(i, ':', wood[i])

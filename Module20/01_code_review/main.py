students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f_sur_inter(number):
    lst = list()
    string = 0
    for i in number:
        for i_int in number[i]['interests']:
            lst.append(i_int)
        string += len(number[i]['surname'])
    return lst, string


for i in students:
    print('id: {0}, возраст: {1}'.format(i, students[i]['age']))


lst_interests = f_sur_inter(students)[0]
len_sur = f_sur_inter(students)[1]

print(lst_interests, len_sur)


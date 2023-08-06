list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list()
new_list1 = list()
for i_ind, i_value in enumerate(list1):
    if i_ind % 2 == 0:
        new_list.append(i_value)
    else:
        new_list1.append(i_value)
new_list = list(zip(new_list, new_list1))
print(new_list)

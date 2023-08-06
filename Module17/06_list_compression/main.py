list_number = [1, 0, 0, 3, 5, 6, 0, 7, 3, 0, 0]
new_list = [i for i in list_number if i != 0]
x = list_number.count(0)
for i in range(x):
    new_list.append(0)
new_list = [i for i in list_number if i != 0]
print(list_number)
print(new_list)

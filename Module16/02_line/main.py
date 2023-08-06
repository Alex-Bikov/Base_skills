first_class = []
second_class = []
for i_first in range(160, 177, 2):
    first_class.append(i_first)
for i_second in range(162, 181, 3):
    second_class.append(i_second)
all_class = first_class + second_class
all_class.sort()
print(all_class)

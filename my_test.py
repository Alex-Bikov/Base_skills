# x = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
#      {"key2": "value2"}]
#
#
# def y(x):
#     new_dict = dict()
#     for i in x:
#         for j in i:
#             if j in new_dict:
#                 break
#             else:
#                 new_dict[j] = i[j]
#     return new_dict
#
# x = y(x)
# print(x)


def test(lst):
    tmp = set()
    result = []
    for i in lst:
        tmp_i = tuple(i.items())

        if tmp_i not in tmp:
            result.append(i)
            tmp.add(tmp_i)
    return result


x = [
    {"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
    {"key2": "value2"}
]

x = test(x)
print(x)

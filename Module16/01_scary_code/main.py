a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a += b
t = a.count(5)
print(t)
for i in range(t):
    a.remove(5)
a += c
t = a.count(3)
print(t)
print(a)

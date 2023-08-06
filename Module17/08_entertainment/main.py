import random

n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
a = ['I'] * n
for i in range(k):
    x = random.randint(1, n)
    y = random.randint(1, x)
    print('Бросок', i + 1, 'Сбиты палки с номера', y, 'по номер', x)
    if x-y == 0:
        a[x - 1] = '.'
    else:
        a[y - 1:x] = ['.' for i in range(x-y + 1)]
print(len(a), 'Длина а')
print('Результат: ', end='')
for i_ in a:
    print(i_, end='')

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number = int(input('Сколько песен выбрать? '))
time = 0
for i in range(number):
    single = input('Название {} песни: '.format(i + 1))
    time += violator_songs[single]
print('Общее время звучания песен: {} минут'.format(round(time, 2)))

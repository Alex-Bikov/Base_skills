import random

first_team = [round(random.uniform(5, 10), 2) for x in range(20)]
print('Первая команда:', first_team)
second_team = [round(random.uniform(5, 10), 2) for x in range(20)]
print('Вторая команда:', second_team)
wins_team = [first_team[i] if first_team[i] - second_team[i] > 0 else second_team[i] for i in
             range(20)]
print('Победители тура:', wins_team)
